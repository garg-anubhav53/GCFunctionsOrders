
# [START functions_helloworld_http]
# [START functions_http_content]

# [START functions_http_method]
# [START functions_helloworld_get]
import functions_framework

# [END functions_http_method]
# [END functions_helloworld_get]

from markupsafe import escape

import bq

# [END functions_helloworld_http]
# [END functions_http_content]


# [START functions_helloworld_get]

@functions_framework.http

def receive_request(request):
    if request.type == 'GET': 
        return get_recent_order(request)
    elif request.type == 'POST':
        return order_insert(request)

def get_recent_order(request):
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
    
    recentrowDict = bq.get_most_recent_order()
    return f"Hello {name} from OMfirsttest, without the other GCP files! See the dict of db records {recentrowDict}"



def order_insert(request):
    request_json = request.get_json(silent=True)
    order_Dicts = get_dict_of_order_from_json(request_json)
    anyInsertionFailures = False

    for order_Dict in order_Dicts:
        bq.insert_order_details(order_Dict['order_id'], order_Dict['order_date'], order_Dict['order_details'], order_Dict['order_status'])
        insert_confirmation_message = bq.insert_order_details('1', '2024-05-01T10:00:00Z', 'Item A,Item B', 'Shipped')
        if insert_confirmation_message == 'failure':
            anyInsertionFailures = True
    
    if anyInsertionFailures:
        return "Great, {order_Dict.size} orders were inserted successfully!"
    else:
        return "Apologies, one or more of the orders did not get inserted. Please check your database."
def get_dict_of_order_from_json(json):
    order_dicts = []
    for order in json:
        order_id = order['order_id']
        order_date = order['order_date']
        order_details = order['order_details']
        order_status = order['order_status']
        
        order_dict = {
            'order_id': order_id,
            'order_date': order_date,
            'order_details': order_details,
            'order_status': order_status
        }
        order_dicts.append(order_dict)
    return order_dicts

# [END functions_helloworld_get]