# Pytest Test Suite

## Overview

This suite validates the JSONPlaceholder API (`https://jsonplaceholder.typicode.com`).

**The suite covers:**
1.  **Parameterized Endpoint Validation:** Checks that `/posts`, `/comments`, and `/users` all return a 200 OK status.
2.  **Response Time:** Ensures the response time for `/posts` is under the 2.0-second threshold.
3.  **Schema Validation:** Confirms the data structure of `/posts` using `jsonschema`.

## How to Execute the Suite

1.  **Setup Environment:**
    Navigate to the project root directory in your terminal.
    ```bash
    # Install dependencies
    pip install -r requirements.txt
    ```
2.  **Run Tests:**
    Execute the entire suite using the required verbose flag:
    ```bash
    pytest -v
    ```
    *Expected Result: 5 tests should run and pass.*



## Postman Collection

You can test the APIs using Postman.

- Import the collection from: `postman/Postman Automation.postman_collection.json`
- Import the environment: `postman/Development.postman_environment.json`

Steps:
1. Open Postman
2. Click "Import"
3. Select the JSON files
4. Go to collection and run

---
