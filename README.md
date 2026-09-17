Python QA Automation Framework

A Python-based API automation framework built with pytest, Requests, and Pydantic.

The project is designed to demonstrate practical QA automation skills: API testing, request/response validation, reusable fixtures, authentication, test data generation, custom error handling, retry logic, cleanup, and investigation of unexpected API behavior.

Tech Stack

Python 3.12+

pytest

Requests

Pydantic v2

Faker

REST API

Framework Structure

python-qa-automation/
├── api/
│   ├── api_client.py
│   ├── auth_api.py
│   ├── product_api.py
│   └── user_api.py
├── config/
│   └── users.examples.py
├── exceptions/
│   └── api_error.py
├── helpers/
│   ├── product_payload_generator.py
│   └── response_validator.py
├── models/
│   ├── products_response.py
│   ├── product_by_id_response.py
│   ├── product_create_response.py
│   └── ...
├── tests/
│   └── test_product_api.py
├── conftest.py
├── requirements.txt
└── README.md

Architecture

The framework separates responsibilities between HTTP communication, API endpoint logic, validation, test data, and pytest fixtures.

ApiClient

ApiClient is the low-level HTTP layer. It provides reusable methods for:

GET

POST

PUT

PATCH

DELETE

authorization headers and token management

The client returns the original requests.Response and does not contain endpoint-specific business logic or retry decisions.

API Classes

Endpoint classes such as ProductApi, AuthApi, and UserApi provide higher-level API operations.

For example, ProductApi currently covers:

product listing and filters

product search

product retrieval by ID

product creation

product deletion

Successful responses are validated with Pydantic models. Unexpected HTTP responses are converted into the framework's custom ApiError exception.

Pydantic Models

Pydantic is used to validate API responses and convert JSON responses into typed Python objects.

This provides structured access to nested response data, for example:

response.brand.id
response.category.id
response.product_image.id

The framework also contains recursive model comparison helpers for validating complex nested API responses.

Authentication

Authentication is implemented through reusable pytest fixtures.

Session-scoped authentication fixtures obtain tokens once and provide them to tests that require authorization. Function-scoped API clients are kept isolated because the client stores a mutable authentication token.

Pytest Fixtures

The framework uses fixtures for dependency injection and resource management.

Examples include:

API client creation

authenticated API clients

user and admin authentication tokens

product API objects

created test products

The created_product fixture demonstrates setup, test execution, and teardown with yield and try/finally.

Conceptually:

setup
  ↓
create product
  ↓
yield product to test
  ↓
test runs
  ↓
finally → delete product

Cleanup is attempted even when the test itself fails after the yield statement.

Error Handling

The framework uses a custom ApiError exception that keeps the HTTP status code and response body available to the calling test or fixture.

Example error flow:

HTTP response
    ↓
ProductApi
    ↓
ApiError(status_code, response_body)
    ↓
pytest fixture
    ↓
retry or raise

This keeps API-specific error interpretation inside the API layer while allowing fixtures to make retry decisions.

Retry Logic

Transient API failures can be retried by the created_product fixture.

Permanent client-side or authorization errors such as 400, 401, 403, and 404 are not retried. The request is retried only while retry attempts remain.

The retry behavior has been manually verified by temporarily using an invalid base URL and confirming that the fixture performs the expected number of attempts before raising the error.

Test Data Generation

ProductPayloadGenerator creates product payloads using dynamic test data and valid IDs retrieved from the API.

This helps reduce hard-coded test data and supports broader data coverage across test runs.

At the same time, the project distinguishes between randomized data and deterministic defect-reproduction data when a specific behavior needs to be reproduced consistently.

API Validation Example

The product creation test validates that important request values are reflected correctly in the API response.

Examples include:

price

brand

category

CO2 rating

location offer

rental flag

product name

product image

stock

eco-friendly flag

The assertions compare nested response objects with the corresponding request values rather than relying only on HTTP status codes.

Known API Behavior: is_eco_friendly

One useful finding from the automated tests is data-dependent behavior around the is_eco_friendly field.

The test data generator can create both True and False values. During testing, the following behavior was observed:

Request:  is_eco_friendly = True
Response: is_eco_friendly = False
Result:   assertion failure

When the generated value is False, the same assertion may pass because the API also returns False.

This means the observed failure depends on the generated test data and can appear intermittently across runs.

The test framework is useful here because it exposes the inconsistency instead of masking it. The failure points directly to a mismatch between the generated request data and the API response.

This behavior should be treated as unexpected API behavior / a potential API defect until it is confirmed against the API contract.

For reliable defect reproduction, a dedicated deterministic test can use a fixed value such as is_eco_friendly = True rather than relying on random data.

Known API Behavior: POST /products vs GET /products

The framework also contains an xfail test that investigates read-after-write consistency for newly created products.

The test creates a product through POST /products and then checks the paginated GET /products collection to find the same product by ID. The product can be retrieved successfully through GET /products/{id}, but it does not reliably appear in the paginated product list immediately after creation.

The test performs more than one collection lookup attempt and waits briefly before retrying the search. If the created product is still not found, the test fails with a message containing the product ID and the observed API response.

The scenario is currently marked with pytest.mark.xfail because the behavior is known and is treated as an expected failure while the API behavior remains unresolved. strict=False allows the test to remain informative if the API behavior changes and the test unexpectedly passes.

Example observed behavior:

POST /products              → product created (201)
GET /products/{id}          → product available
GET /products?page=...     → product may be missing from collection

This test demonstrates that the framework can validate not only individual endpoint responses, but also consistency between related API operations and data visibility across endpoints. It helps identify potential synchronization, indexing, caching, or collection-consistency issues without hiding the behavior behind a hard-coded expected result.

Why This Framework

The goal is not only to automate happy-path API checks, but also to demonstrate a practical QA approach:

reusable API abstraction

typed response validation

reusable pytest fixtures

authentication and authorization handling

test data generation

custom exception handling

retry logic for transient failures

automatic test data cleanup

nested request/response comparison

investigation and documentation of unexpected API behavior

The framework is intentionally organized so that tests remain focused on test intent, while API communication, validation, data generation, and cleanup are handled by reusable components.

Running the Tests

Create and activate a virtual environment, install dependencies, and run pytest from the project root.

pytest

Useful commands:

pytest -v
pytest tests/test_product_api.py -v
pytest -k create_product -v

Test Data and Secrets

Real credentials should not be committed to the repository. Example configuration is kept separately from real local credentials, and sensitive files are excluded through .gitignore.

Current Focus

The framework is being extended incrementally with a focus on practical Python and pytest skills, maintainable API automation, and CI-ready test architecture.