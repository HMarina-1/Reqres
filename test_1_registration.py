import pytest
import requests
import allure


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User Registration Suite')
@allure.title('Test Successful Registration')
@allure.description('This test verifies that a user can successfully register with valid credentials.')
@allure.severity(allure.severity_level.BLOCKER)
def test_registration():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://reqres.in/api/register',
        json=body,
        headers=headers
    )

    with allure.step('Verify the response status and extract the token'):
        response_data = response.json()
    with allure.step('Check that the status code is 200 and extract the token'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

        my_token = response_data.get('token')
        print(my_token)
        print(response_data)


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User Registration Suite')
@allure.title('Test Registration with Missing Password')
@allure.description('This test verifies that the registration fails when the password is missing.')
@allure.severity(allure.severity_level.CRITICAL)
def test_registration_negative():
    body = {
        "email": "peter@klaven"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://reqres.in/api/login',
        json=body,
        headers=headers
    )

    with allure.step('Verify the response status and error message'):
        response_data = response.json()

        assert response.status_code == 400, f'Expected Status Code 400, but got {response.status_code}'

        expected_error = "Missing password"
        assert response_data.get("error") == expected_error, f'Expected error message "{expected_error}", but got "{response_body.get("error")}"'
