### Boolean Field Validation and Defect Detection

The framework includes a parameterized API test that validates Boolean product fields using both `True` and `False` variations.

The test covers:

* `is_location_offer`
* `is_rental`
* `in_stock`
* `is_eco_friendly`

For each field, the test:

1. Generates a product payload.
2. Sets the selected Boolean field to the parameterized value.
3. Creates the product through `POST /products`.
4. Retrieves the corresponding value from the response dynamically.
5. Compares the response value with the value sent in the request.

The test uses `pytest.mark.parametrize` to cover multiple field/value combinations with a single reusable test:

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

The response field is accessed dynamically using Python's `getattr()`:

```python
assert getattr(response, field) == value
```

This allows the same test logic to validate different response fields without duplicating test code.

#### Observed API Behavior

The test currently identifies inconsistent API behavior for some Boolean fields.

For example:

```text
Request:  is_location_offer = True
Response: is_location_offer = False
Result:   FAIL
```

and:

```text
Request:  is_location_offer = False
Response: is_location_offer = True
Result:   FAIL
```

The same behavior has been observed for `is_eco_friendly`:

```text
Request:  is_eco_friendly = True
Response: is_eco_friendly = False
Result:   FAIL
```

and:

```text
Request:  is_eco_friendly = False
Response: is_eco_friendly = True
Result:   FAIL
```

Other Boolean fields currently pass the same validation.

This demonstrates that the test is detecting an actual mismatch between the request payload and the API response rather than simply validating that the endpoint returns a successful HTTP status.

The test therefore serves as both an automated regression check and a tool for identifying potential API defects.

The failure message includes the field name and both values, making the problem immediately visible:

```text
is_location_offer mismatch: response=False, payload=True
```

#### Why This Test Is Useful

This test demonstrates several practical QA automation techniques:

* parameterized testing with `pytest`
* positive and negative Boolean variations
* dynamic field access with `getattr()`
* request/response data comparison
* reusable test data generation
* detection of data transformation issues
* identification of potential API defects
* concise test coverage without duplicated test methods

The test is intentionally kept as a normal failing test rather than being marked as `xfail`, because the observed behavior represents a request/response mismatch that requires investigation.

Once the API behavior is confirmed against the expected API contract, the test can serve as a regression test to ensure that the defect does not reappear.
