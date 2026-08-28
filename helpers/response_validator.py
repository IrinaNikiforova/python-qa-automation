from pydantic import BaseModel

class ResponseValidator:

    @staticmethod
    def parse_response(response, model):
        return model.model_validate(response.json())

    @staticmethod
    def assert_models_lists_equal(expected, actual):
   
        assert len(expected) == len(actual), (
            f"Different number of models: "
            f"expected={len(expected)}, actual={len(actual)}"
        )

        for index, (expected_model, actual_model) in enumerate(
            zip(expected, actual)
        ):
            try:
                ResponseValidator.assert_models_equal(
                    expected_model,
                    actual_model
                )

            except AssertionError as error:
                raise AssertionError(
                    f"Models at index {index} are different:\n{error}"
                ) from error

    
    @staticmethod
    def assert_models_equal(model_1, model_2):
        common_fields = set(type(model_1).model_fields) & set(type(model_2).model_fields)
    
        for elm in common_fields:
            attribute_1 = getattr(model_1, elm)
            attribute_2 = getattr(model_2, elm)

            if isinstance(attribute_1, (str, int, float, bool, type(None))) and isinstance(attribute_2, (str, int, float, bool, type(None))):
                assert attribute_1 == attribute_2, (f"Field '{elm}' differs: "f"{attribute_1!r} != {attribute_2!r}")
            elif isinstance(attribute_1, BaseModel) and isinstance(attribute_2, BaseModel):
                ResponseValidator.assert_models_equal(attribute_1, attribute_2)
            elif isinstance(attribute_1, list) and isinstance(attribute_2, list):
                ResponseValidator.assert_models_lists_equal(attribute_1, attribute_2)
            else: 
                raise AssertionError(
                    f"Unsupported or mismatched types for field '{elm}': "
                    f"{type(attribute_1).__name__} vs "
                    f"{type(attribute_2).__name__}"
                )



