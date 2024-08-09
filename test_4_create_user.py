import pytest
import requests
import allure

my_bookingid = 0

@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User API Tests')
@allure.title('Test Create User')
@allure.description('This test verifies that a new user can be created successfully.')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user():
    body = {
        "name": "Marina",
        "job": "leader"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send request to create a new user'):
        response = requests.post(
            'https://reqres.in/api/users',
            json=body,
            headers=headers
        )
        response_body = response.json()

    with allure.step('Verify response status code'):
        assert response.status_code == 201, f'Expected status code 201, but got {response.status_code}'

    with allure.step('Verify response body contains correct fields'):
        assert 'name' in response_body, "Response JSON should contain 'name' field"
        assert 'job' in response_body, "Response JSON should contain 'job' field"
        assert 'id' in response_body, "Response JSON should contain 'id' field"
        assert 'createdAt' in response_body, "Response JSON should contain 'createdAt' field"

    with allure.step('Verify response body contains correct values'):
        assert response_body['name'] == body['name'], "The 'name' field in the response does not match the input"
        assert response_body['job'] == body['job'], "The 'job' field in the response does not match the input"

    global my_bookingid
    my_bookingid = response_body['id']
    print(my_bookingid)
    print(response_body)


# @pytest.mark.xxx
# def test_my_booking():
#     response = requests.get(f'https://reqres.in/api/users/{my_bookingid}')
#     response_data = response.json()
#     assert response.status_code == 200, ' '
#     print(response_data)






