import pytest
import requests
import allure


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User Authentication Suite')
@allure.title('Test Successful Login')
@allure.description('This test verifies that a user can successfully log in with valid credentials.')
@allure.severity(allure.severity_level.CRITICAL)
def test_login():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://reqres.in/api/login',
        json=body,
        headers=headers
    )

    with allure.step('Verify response status and check for token'):
        response_data = response.json()
    with allure.step('Check that the status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step('Check if token is present in response'):
        assert 'token' in response_data, 'Token not found in response'

    print(response_data['token'])


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User Authentication Suite')
@allure.title('Test Login with Missing Password')
@allure.description('This test verifies that login fails when the password is missing.')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_negative():
    body = {
        "email": "peter@klaven"
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(
        'https://reqres.in/api/login',
        json=body,
        headers=headers
    )

    with allure.step('Verify response status and check for error message'):
        assert response.status_code == 400, f'Expected Status Code 400, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Check if error is present in response'):
        assert 'error' in response_data, "Response JSON should contain 'error'"

    expected_error_message = "Missing password"

    with allure.step('Verify the error message'):
        assert response_data['error'] == expected_error_message, f"Expected error message '{expected_error_message}', but got '{response_body['error']}'"
