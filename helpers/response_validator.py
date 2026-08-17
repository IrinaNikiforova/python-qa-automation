class ResponseValidator():
   
    @staticmethod
    def parse_response(response, model):
        body = response.json()
        return model.model_validate(body)

