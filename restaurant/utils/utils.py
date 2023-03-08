def errorResponse(code, message, status):

    return {
        "code": code,
        "status": status,
        "message": message
    }