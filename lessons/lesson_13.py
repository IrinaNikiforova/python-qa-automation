test_results = {
    "login": {
        "passed": 18,
        "failed": 2,
        "skipped": 1
    },
    "checkout": {
        "passed": 12,
        "failed": 5,
        "skipped": 3
    },
    "search": {
        "passed": 20,
        "failed": 0,
        "skipped": 2
    }
}

def get_failed_tests(test_results):
    dict_of_dailed_tests = {}
    for key in test_results:
        if test_results[key]["failed"] > 0:
            dict_of_dailed_tests.update({
                key : test_results[key]["failed"]
            })
    return dict_of_dailed_tests


print(get_failed_tests(test_results))