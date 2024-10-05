from flask import jsonify


class HandlerException:
    def STATUS200(message):
        response = jsonify(
            {"statusResponse": {"statusCode": 200, "message": "Success"}}
        )
        response.status_code = 200
        return response

    def STATUS400_DATA_NOT_FOUND(message):
        response = jsonify({"statusResponse": {"statusCode": 400, "message": message}})
        response.status_code = 400
        return response

        response = jsonify(
            {"statusResponse": {"statusCode": "VMAPI404", "status": message}}
        )
        response.status_code = 404
        return response
