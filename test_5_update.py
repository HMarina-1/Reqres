import allure
import pytest
import requests
# import test_4_create_user


@pytest.mark.xxx
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User API Tests')
@allure.title('Test Update User')
@allure.description('This test verifies the successful update of an existing user.')
@allure.severity(allure.severity_level.CRITICAL)
def test_update():
    body = {
        "name": "Marina",
        "job": "zion resident"
    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send request to update user'):
        response = requests.put(
            f'https://reqres.in/api/users/2',
            json=body,
            headers=headers
        )
        response_body = response.json()

    with allure.step('Check response status code'):
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    with allure.step('Check presence and value of "name" field'):
        assert 'name' in response_body, 'Response JSON does not contain "name"'
        assert response_body['name'] == body[
            'name'], f'Expected name to be {body["name"]}, but got {response_body["name"]}'

    with allure.step('Check presence and value of "job" field'):
        assert 'job' in response_body, 'Response JSON does not contain "job"'
        assert response_body['job'] == body['job'], f'Expected job to be {body["job"]}, but got {response_body["job"]}'

    with allure.step('Check presence of "updatedAt" field'):
        assert 'updatedAt' in response_body, 'Response JSON does not contain "updatedAt"'

    print(response_body)


@pytest.mark.xxx
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User API Tests')
@allure.title('Test Partial Update User')
@allure.description('This test verifies the successful partial update of an existing user.')
@allure.severity(allure.severity_level.CRITICAL)
def test_partial_update():
    body = {
        "name": "morpheus",
        "job": "zion resident"

    }

    headers = {'Content-Type': 'application/json'}

    with allure.step('Send request to partially update user'):
        response = requests.patch(
            f'https://reqres.in/api/users/2',
            json=body,
            headers=headers
        )
        response_body = response.json()

    with allure.step('Check response status code'):
        assert response.status_code == 200, f'Expected status code 200, but got {response.status_code}'

    with allure.step('Check presence and value of "name" field'):
        assert 'name' in response_body, 'Response JSON does not contain "name"'
        assert response_body['name'] == body[
            'name'], f'Expected name to be {body["name"]}, but got {response_body["name"]}'

    with allure.step('Check presence and value of "job" field'):
        assert 'job' in response_body, 'Response JSON does not contain "job"'
        assert response_body['job'] == body['job'], f'Expected job to be {body["job"]}, but got {response_body["job"]}'

    with allure.step('Check presence of "updatedAt" field'):
        assert 'updatedAt' in response_body, 'Response JSON does not contain "updatedAt"'

    print(response_body)
