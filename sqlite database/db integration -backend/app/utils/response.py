# Success Response
def success_response(
    message: str,
    data=None
):

    return {
        "success": True,
        "message": message,
        "data": data
    }


# Error Response
def error_response(
    message: str
):

    return {
        "success": False,
        "message": message
    }