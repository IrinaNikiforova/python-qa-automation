# Python API Test Automation Framework

A Python-based API test automation framework built with **Python**, **pytest**, **Requests**, **Pydantic**, and **Faker**.

The project demonstrates practical QA automation skills including API testing, request/response validation, test data generation, authentication, parameterized testing, custom error handling, logging, test reporting, fixture-based test data management, and defect detection.

---

## Tech Stack

* **Python 3.12+**
* **pytest**
* **Requests**
* **Pydantic v2**
* **Faker**
* **Allure Report**
* **Python logging**
* **REST API**
* **Git / GitHub**

---

## Project Structure

```text
python-qa-automation/

├── api/
│   ├── api_client.py
│   ├── auth_api.py
│   ├── product_api.py
│   └── user_api.py
│
├── config/
│   └── users.examples.py
│
├── exceptions/
│   └── api_error.py
│
├── helpers/
│   ├── list_helpers.py
│   ├── product_payload_generator.py
│   ├── product_payload_generator_2.py
│   └── response_validator.py
│
├── models/
│   ├── create_product_request.py
│   ├── login_response.py
│   ├── product_by_id_response.py
│   ├── product_create_response.py
│   ├── product.py
│   ├── products_response.py
│   ├── user_adress.py
│   ├── users_me_response.py
│   └── users_response.py
│
├── tests/
│   └── test_product_api.py
│
├── utils/
│   └── logger.py
│
├── lessons/
│   ├── lesson_10.py
│   ├── lesson_11.py
│   └── lesson_12.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## Framework Architecture

The framework separates HTTP communication, endpoint logic, data models, test data generation, reusable helpers, fixtures, and tests.

```text
Tests
  │
  ▼
API Layer
  │
  ▼
ApiClient
  │
  ▼
REST API
  │
  ▼
Response
  │
  ▼
Pydantic Models
  │
  ▼
Validation / Assertions
```

Supporting components such as fixtures, helpers, logging, and custom exceptions are used across the framework.

### Main Components

### ApiClient

Responsible for low-level HTTP communication.

It provides common methods for:

* GET
* POST
* PUT
* PATCH
* DELETE

The client also manages authentication tokens.

Endpoint-specific logic is kept outside the HTTP client.

---

### API Layer

Endpoint classes provide business-level API methods.

Examples:

```text
ProductApi
AuthApi
UserApi
```

For example, tests interact with methods such as:

```python
product_api.products()

product_api.product_by_id(product_id)

product_api.create_product(payload)

product_api.delete_product(product_id)
```

This keeps tests readable and avoids placing raw HTTP requests directly inside test cases.

---

## Pydantic Models

Pydantic models are used to validate and structure API data.

Response models include:

```text
Product
ProductsResponse
ProductCreateResponse
ProductByIdResponse
LoginResponse
UsersResponse
UsersMeResponse
```

Nested API objects are represented as typed models.

For example:

```python
response.brand.id
response.category.id
response.product_image.id
```

This provides structured access to API response data and allows validation of response schemas and data types.

---

## Request Models

Request data can also be represented using Pydantic models.

The project includes:

```text
CreateProductRequest
```

This separates request data from response models.

The framework therefore distinguishes between:

```text
Request Model
      ↓
API Request
      ↓
API Response
      ↓
Response Model
```

---

## API Test Coverage

The current test suite covers the following areas:

| Area                    | Coverage                                       |
| ----------------------- | ---------------------------------------------- |
| Product creation        | Request/response field validation              |
| Product retrieval       | GET product by ID                              |
| Product consistency     | Collection vs. individual product comparison   |
| Product data validation | Required fields, types and values              |
| Brand filtering         | Filter result validation                       |
| Pagination              | Page numbers, totals and response sizes        |
| Authentication          | Authenticated product requests                 |
| Search                  | Case-insensitive and negative search scenarios |
| Boolean fields          | True/False parameterized scenarios             |
| Defect detection        | Known API behavior documented with `xfail`     |
| Test data               | Dynamic product data generation                |
| Cleanup                 | Automatic deletion of created products         |

---

## Product Creation Testing

The framework tests product creation through the API using dynamically generated test data.

The test validates that important fields returned by the API match the original request payload.

Examples include:

```python
assert response.price == payload["price"]

assert response.brand.id == payload["brand_id"]

assert response.category.id == payload["category_id"]

assert response.co2_rating == payload["co2_rating"]

assert response.name == payload["name"]
```

This verifies the relationship between request data and response data instead of only checking the HTTP status code.

---

## Dynamic Test Data Generation

The framework includes reusable helpers for generating test data.

### ProductPayloadGenerator

`ProductPayloadGenerator` generates product data using Faker, random values, and valid reference data obtained from the API.

Generated data can include:

* product name
* description
* price
* stock
* Boolean fields
* brand
* category
* product image

Valid IDs are obtained from API data instead of relying only on hard-coded values.

---

### Model-Driven Payload Generation

The project also contains an experimental `ProductPayloadGenerator2`.

This generator uses a Pydantic model as the source of information about the fields that need to be generated.

For example:

```python
ProductPayloadGenerator2.collect_products_data_2(
    CreateProductRequest
)
```

The generator inspects:

```python
model.model_fields
```

and determines how to generate data based on the field type.

It currently supports:

* `str`
* `float`
* `bool`
* optional types such as `str | None`
* nested Pydantic models

Nested models are handled recursively.

Conceptually:

```text
Pydantic Model
      ↓
Inspect fields
      ↓
Determine field type
      ↓
Generate value
      ↓
Nested Model?
      ↓
Generate nested data recursively
```

The generator is intentionally being developed incrementally as additional API endpoints become available.

Reference fields such as `brand_id`, `category_id`, and `product_image_id` will be progressively connected to their corresponding API sources as the framework expands.

---

## Parameterized Testing

Pytest parameterization is used to execute the same test with different input values.

For example, Boolean fields are tested with both `True` and `False` values:

```python
@pytest.mark.parametrize(
    "field, value",
    [
        ("is_location_offer", True),
        ("is_location_offer", False),
        ("is_rental", True),
        ("is_rental", False),
        ("in_stock", True),
        ("in_stock", False),
        ("is_eco_friendly", True),
        ("is_eco_friendly", False),
    ]
)
```

This allows multiple scenarios to be covered without duplicating test code.

---

## Boolean Field Validation and Defect Detection

The product creation tests revealed inconsistent API behavior for some Boolean fields.

The framework checks whether the value sent in the request is correctly reflected in the API response.

For example:

```text
Request

is_rental = True

Expected response

is_rental = True
```

If the API returns a different value, the test reports the mismatch.

Some Boolean scenarios also result in HTTP 500 responses from the API.

The tests therefore help identify both:

* response value mismatches
* unexpected server errors

This demonstrates how automated tests can be used for both regression testing and defect detection.

---

## Known API Defect

The project contains a test marked with `pytest.mark.xfail` for a known API behavior.

The scenario is:

```text
POST /products
       ↓
Product created successfully
       ↓
GET /products/{id}
       ↓
Product is available
```

However, the same product does not reliably appear in the paginated:

```text
GET /products
```

The test documents this known behavior:

```python
@pytest.mark.xfail(
    reason=(
        "BUG: Product created through POST /products is available "
        "through GET /products/{id}, but does not reliably appear "
        "in the paginated GET /products response."
    ),
    strict=False
)
```

This keeps the known defect visible in the test suite without treating the expected failure as an unknown regression.

---

## Response Validation

The framework includes a reusable `ResponseValidator`.

It provides functionality for:

* parsing API responses into Pydantic models
* comparing Pydantic models
* comparing lists of models
* reporting detailed field-level differences

For example:

```python
ResponseValidator.assert_models_equal(
    response,
    product_by_id
)
```

This is used to verify that the same product contains consistent data when retrieved through different API endpoints.

The comparison helps identify inconsistencies between:

```text
GET /products
```

and:

```text
GET /products/{id}
```

---

## Product Validation

The test suite validates product data returned by the API.

Examples include:

```python
assert isinstance(product.id, str)
assert product.id
assert product.name
assert product.price >= 0
```

Nested objects are also checked:

```python
assert product.category.id
assert product.category.name
assert product.category.slug

assert product.brand.id
assert product.brand.name
```

Optional fields are handled explicitly.

For example:

```python
if product.description is not None:
    assert product.description
```

This allows the test to distinguish between an optional `None` value and an invalid empty value.

---

## Filtering

Brand filtering is tested by first collecting available brands and then requesting products using each brand ID.

The response is validated to ensure that returned products belong to the requested brand.

Example:

```python
products = product_api.products(brand=brand_id)

for product in products.data:
    assert product.brand.id == brand_id
    assert product.brand.name == brand_name
```

This validates both filtering behavior and the consistency of brand information.

---

## Pagination Testing

Pagination behavior is validated using multiple pages.

The tests verify:

* current page number
* total products
* total pages
* page size
* different results between pages

Example:

```python
assert products_page_1.current_page == 1
assert products_page_2.current_page == 2

assert len(products_page_1.data) <= products_page_1.per_page
assert len(products_page_2.data) <= products_page_2.per_page
```

---

## Authentication Testing

The framework supports authenticated API requests using tokens obtained through the login endpoint.

Authentication is implemented through pytest fixtures.

Example:

```python
product_api.client.set_token(auth_token)

products = product_api.products()
```

Separate authentication fixtures are used for different user roles when required by the test scenario.

---

## Fixtures and Test Data Management

Pytest fixtures are used to manage:

* API clients
* authentication
* test data
* test setup
* cleanup

A `created_product` fixture:

1. Generates product data.
2. Authenticates as an administrator.
3. Creates a product through the API.
4. Provides the payload and response to the test.
5. Deletes the created product after the test.

The cleanup is performed using `try/finally`, which ensures that the created product is removed even if the test fails.

Conceptually:

```text
Setup
  ↓
Create product
  ↓
Run test
  ↓
Cleanup
  ↓
Delete product
```

This keeps the test environment cleaner and reduces dependency between test runs.

---

## Retry Handling

The product creation fixture includes limited retry handling for transient API failures.

The retry mechanism does not retry expected client or authorization errors such as:

```text
400
401
403
404
```

This prevents unnecessary retries for failures that are unlikely to be resolved by simply repeating the request.

---

## Custom API Errors

The framework uses a custom `ApiError` exception.

```text
ApiError
├── status_code
└── response_body
```

Unexpected API responses can therefore be represented as a framework-level exception instead of being handled separately in every test.

This keeps error handling centralized and makes failures easier to understand.

---

## Search Testing

Product search is tested with both positive and negative scenarios.

Positive examples include different letter cases:

```text
Hammer
hammer
dRill
ThOr
```

A negative search scenario is also included:

```text
sdfvsdfv
```

The test verifies case-insensitive search behavior and validates returned product names against the requested search term.

---

## Logging

Python's built-in `logging` module is used for framework logging.

The project provides a reusable logger:

```text
utils/logger.py
```

The framework logs important API operations such as:

```text
GET /products
GET /products -> 200

POST /products
POST /products -> 201
```

Logging is focused on useful execution information rather than sensitive request data such as:

* authentication tokens
* passwords
* authorization headers
* API keys

---

## Allure Reporting

The project uses **Allure Report** for test reporting.

Run the tests with:

```bash
pytest --alluredir=allure-results
```

Generate the report:

```bash
allure generate allure-results -o allure-report --clean
```

Open the report:

```bash
allure open allure-report
```

Allure results and generated reports are excluded from Git using `.gitignore`.

---

## Running the Tests

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test
```