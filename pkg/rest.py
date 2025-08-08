from rest_framework.response import Response

def BaseResponse(data=None, status=200, message=None, error=None):
    response = {
        'success': status < 400,
        'data': data,
        'status': status,
        'message': message
    }
    if error:
        response['error'] = error
    return Response(response, status=status)