template = {
    "swagger": "2.0",
    "info": {
        "title": "API",
        "description": "API for my data",
        "contact": {
            "responsibleOrganization": "ME",
            "responsibleDeveloper": "Me",
            "email": "eromeroc@banesco.com",
            "url": "linkedin.com/in/banesco/",
        },
        "termsOfService": "http://me.com/terms",
        "version": "0.0.1",
    },
    "schemes": ["http", "https"],
    "operationId": "getmyData",
    "definitions": {
        "SimpleResponseSchema": {
            "type": "object",
            "properties": {
                "statusResponse": {
                    "type": "object",
                    "properties": {
                        "statusCode": {
                            "type": "string",
                            "description": "Response code",
                            "default": "200",
                        },
                        "status": {"type": "string", "description": "Response message"},
                    },
                }
            },
        },
        "ErrorResponseSchema": {
            "type": "object",
            "properties": {
                "statusResponse": {
                    "type": "object",
                    "properties": {
                        "statusCode": {
                            "type": "string",
                            "description": "Response code",
                            "default": "EAPI400",
                        },
                        "status": {
                            "type": "string",
                            "description": "Response message",
                            "default": "Services is not allowed",
                        },
                    },
                }
            },
        },
    },
}
