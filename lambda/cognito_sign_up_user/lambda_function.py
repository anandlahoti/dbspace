"""Sign Up user."""
from sign_up_dao import SignUpDao
from sign_up_exceptions import UsernameExistsException, InvalidPasswordException


def lambda_handler(event, context):
    """Sign Up user."""
    try:
        username = event['username']
        password = event['password']
        sign_up_dao = SignUpDao()
        signed_up = sign_up_dao.sign_up(username, password)
        return signed_up
    except UsernameExistsException as username_exists_exception:
        return username_exists_exception
    except InvalidPasswordException as invalid_password_exception:
        return invalid_password_exception
    except Exception as exception:
        return exception
