import requests
import json
from config.config import BASE_URL


def test_fetch_posts_and_save_first_five(api_client, tmp_path):
    # fetch all posts
    full_url = f"{BASE_URL}/posts"
    response = api_client.get(full_url)

    # validate status code
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    print("Status code is 200")

    # verify keys
    posts = response.json()
    required_keys = {"userId", "id", "title", "body"}

    post_number = 1
    for post in posts:
        for key in required_keys:
            assert key in post, f"{key} not found in post {post_number}"
        post_number += 1
    print("All posts contain required keys")

    # save first 5 posts into json file
    first_five_posts = posts[:5]
    output_file = tmp_path / "first_5_posts.json"
    with open(output_file, "w") as f:
        json.dump(first_five_posts, f, indent=4)
    print("First 5 posts saved to first_5_posts.json")
