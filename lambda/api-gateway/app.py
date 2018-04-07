"""Rest API for data."""
from chalice import Chalice
from chalice import Response
from endpoint1_dao import EndPoint1Dao
from endpoint2_dao import Endpoint2Dao
from endpoint3_dao import Endpoint3Dao
from endpoint4_dao import Endpoint4Dao
from util.logger_utility import LoggerUtility

# API Gateway Name
APP = Chalice(app_name='API-Gateway-Name')


@APP.route('/endpoint1', methods=['POST'])
def endpoint1():
    """Rest API for endpoint1."""
    try:
        request = APP.current_request
        endpoint1_dao = Endpoint1Dao()
        response = endpoint1_dao.save_data(request.json_body)
        LoggerUtility.log_info(response)
        if response:
            return Response(body=request.json_body, status_code=200)
        return Response(body=request.json_body, status_code=500)
    except AttributeError as exception:
        LoggerUtility.log_error(exception)
        return Response(request.json_body, 400)


@APP.route('/endpoint2', methods=['POST'])
def endpoint2():
    """Rest API for endpoint2."""
    try:
        request = APP.current_request
        endpoint2_dao = Endpoint2Dao()
        response = endpoint2_dao.save_data(request.json_body)
        LoggerUtility.log_info(response)
        if response:
            return Response(body=request.json_body, status_code=200)
        return Response(body=request.json_body, status_code=500)
    except AttributeError as exception:
        LoggerUtility.log_error(exception)
        return Response(request.json_body, 400)


@APP.route('/endpoint3', methods=['POST'])
def endpoint3():
    """Rest API for endpoint3."""
    try:
        request = APP.current_request
        endpoint3_dao = Endpoint3Dao()
        response = endpoint3_dao.save_data(request.json_body)
        LoggerUtility.log_info(response)
        if response:
            return Response(body=request.json_body, status_code=200)
        return Response(body=request.json_body, status_code=500)
    except AttributeError as exception:
        LoggerUtility.log_error(exception)
        return Response(request.json_body, 400)


@APP.route('/endpoint4', methods=['POST'])
def endpoint4():
    """Rest API for Endpoint4."""
    try:
        request = APP.current_request
        endpoint4_dao = Endpoint4Dao()
        response = endpoint4_dao.save_data(request.json_body)
        LoggerUtility.log_info(response)
        if response:
            return Response(body=request.json_body, status_code=200)
        return Response(body=request.json_body, status_code=500)
    except AttributeError as exception:
        LoggerUtility.log_error(exception)
        return Response(request.json_body, 400)
        
