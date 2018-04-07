"""Sign Up user DAO."""
import os
import boto3
from sign_up_exceptions import UsernameExistsException, InvalidPasswordException
from util.logger_utility import LoggerUtility


class SignUpDao():
    """Sign Up user DAO."""

    def sign_up(self, username, password):
        """Sign Up user DAO."""
        try:
            cognito_client = boto3.client('cognito-idp')
            response = cognito_client.sign_up(
                ClientId=os.getenv('CLIENT_ID'),
                Username=username,
                Password=password
            )
            self.confirm_sign_up(username)
        except cognito_client.exceptions.UsernameExistsException as username_exists_exception:
            LoggerUtility.log_error(username_exists_exception)
            raise UsernameExistsException('User already exists')
        except cognito_client.exceptions.InvalidPasswordException as invalid_password_exception:
            LoggerUtility.log_error(invalid_password_exception)
            raise InvalidPasswordException('Password did not conform with policy')

        except Exception as exception:
            LoggerUtility.log_error(exception)
            raise Exception(exception)
        return response

    def confirm_sign_up(self, username):
        """Sign Confirm Up user."""
        cognito_client = boto3.client('cognito-idp')
        response = cognito_client.admin_confirm_sign_up(
            UserPoolId=os.getenv('USER_POOL_ID'),
            Username=username
        )
        return response
