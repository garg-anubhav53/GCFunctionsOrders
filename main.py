
# [START functions_helloworld_http]
# [START functions_http_content]

# [START functions_http_method]
# [START functions_helloworld_get]
import functions_framework

# [END functions_http_method]
# [END functions_helloworld_get]

from markupsafe import escape

# [END functions_helloworld_http]
# [END functions_http_content]


# [START functions_helloworld_get]
@functions_framework.http
def order_get2(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    Note:
        For more information on how Flask integrates with Cloud
        Functions, see the `Writing HTTP functions` page.
        <https://cloud.google.com/functions/docs/writing/http#http_frameworks>
    """
    
    request_json = request.get_json(silent=True)
    name = 'null'
    if request_json and "name" in request_json:
        name = request_json["name"]
    
    return f"Hello {name} from OMfirsttest, without the other GCP files!"


# [END functions_helloworld_get]