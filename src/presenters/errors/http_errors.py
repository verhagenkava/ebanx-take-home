class HttpErrors:
    """Class to define errors in http"""

    @staticmethod
    def error_400():
        """HTTP 400"""

        return {"status_code": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_404():
        """HTTP 404"""

        return {"status_code": 404, "body": {"error": "Not Found"}}

    @staticmethod
    def error_500():
        """HTTP 500"""

        return {"status_code": 500, "body": {"error": "Internal Server Error"}}