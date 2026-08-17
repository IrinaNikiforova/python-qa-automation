import pytest

@pytest.mark.parametrize(
    "payment_method",
    [
        "Credit Card",
        "Cash",
        "Bank Transfer",
    ]
)
def test_payment_method(payment_method):

    assert payment_method in [
        "Credit Card",
        "Cash",
        "Bank Transfer",
    ]