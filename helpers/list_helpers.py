from collections import Counter


class ListHelpers:

    @staticmethod
    def compare_lists(expected_list, actual_list):

        result = []

        if len(expected_list) != len(actual_list):
            return {
                "status": "FAIL",
                "error": "Different number of categories",
                "expected_count": len(expected_list),
                "actual_count": len(actual_list)
            }

        for index, (actual_names, expected_names) in enumerate(
            zip(actual_list, expected_list)
        ):
            missing_names = Counter(expected_names) - Counter(actual_names)
            unexpected_names = Counter(actual_names) - Counter(expected_names)

            if not missing_names and not unexpected_names:
                status = {
                    "category": index + 1,
                    "status": "PASS"
                }
            else:
                status = {
                    "category": index + 1,
                    "status": "FAIL",
                    "missing": list(missing_names.elements()),
                    "unexpected": list(unexpected_names.elements())
                }

            result.append(status)

        return result