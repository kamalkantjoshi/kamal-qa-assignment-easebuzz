import pytest
from jsonschema import validate, ValidationError
from schemas.post_schema import post_schema
from config.config import BASE_URL, MAX_RESPONSE_TIME_SECONDS


@pytest.mark.parametrize("endpoint, expected_status", [
    ("/posts", 200),
    ("/comments", 200),
    ("/users", 200),
])
def test_endpoint_accessibility_and_status(api_client, endpoint, expected_status):
    # Validate that multiple endpoints are accessible and return the expected HTTP status code.
    full_url = f"{BASE_URL}{endpoint}"
    response = api_client.get(full_url)

    assert response.status_code == expected_status, \
        f"Endpoint {endpoint} failed: Expected {expected_status}, got {response.status_code}"


def test_posts_response_time(api_client):
    # Validate that response time of api is within expected time
    full_url = f"{BASE_URL}/posts"
    response = api_client.get(full_url)
    response_time = response.elapsed.total_seconds()

    assert response.status_code == 200, "API did not return status 200"
    assert response_time < MAX_RESPONSE_TIME_SECONDS, \
        f"Response time was {response_time}s, which exceeds {MAX_RESPONSE_TIME_SECONDS}s"


def test_posts_schema_validation(api_client):
    # Validate the structure of json response
    full_url = f"{BASE_URL}/posts"
    response = api_client.get(full_url)

    assert response.status_code == 200, "API did not return status 200"

    try:
        validate(instance=response.json(), schema=post_schema)
    except ValidationError as e:
        pytest.fail(f"Schema validation failed for posts: {e.message}")
    except Exception as e:
        pytest.fail(f"An unexpected error occurred during schema validation: {e}")