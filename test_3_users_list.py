import pytest
import requests
import allure



@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User API Tests')
@allure.title('Test List Users')
@allure.description('This test verifies that the user list can be retrieved successfully.')
@allure.severity(allure.severity_level.NORMAL)
def test_all_users_list():
    with allure.step('Send request to get user list'):
        response = requests.get('https://reqres.in/api/users?page=2')
        response_data = response.json()

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step('Verify the list is not empty'):
        assert len(response_data['data']) > 0, 'The list should not be empty'

    print(response_data)


@pytest.mark.xxx
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User API Tests')
@allure.title('Test Single User Retrieval')
@allure.description('This test verifies that a single user can be retrieved successfully.')
@allure.severity(allure.severity_level.NORMAL)
def test_single_user():
    with allure.step('Send request to get a single user'):
        response = requests.get('https://reqres.in/api/users/2')
        response_data = response.json()

    with allure.step('Verify response status code'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step('Verify the user ID is 2'):
        assert response_data['data']['id'] == 2, 'User ID should be 2'

    with allure.step('Verify the user email is correct'):
        assert response_data['data']['email'] == "janet.weaver@reqres.in", "Email should be janet.weaver@reqres.in"

    with allure.step('Verify the first name is Janet'):
        assert response_data['data']['first_name'] == 'Janet', "First name should be Janet"

    with allure.step('Verify the last name is Weaver'):
        assert response_data['data']['last_name'] == 'Weaver', "Last name should be Weaver"

    with allure.step('Verify the avatar URL is correct'):
        assert response_data['data']['avatar'] == 'https://reqres.in/img/faces/2-image.jpg', 'Avatar URL should be https://reqres.in/img/faces/2-image.jpg'

    with allure.step('Verify the support URL is correct'):
        assert response_data['support']['url'] == 'https://reqres.in/#support-heading', 'Support URL should be https://reqres.in/#support-heading'

    with allure.step('Verify the support text is correct'):
        assert response_data['support']['text'] == 'To keep ReqRes free, contributions towards server costs are appreciated!', 'Support text should match'

    print(response_data)


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User API Tests')
@allure.title('Test Single User Not Found')
@allure.description('This test verifies that the API returns a 404 status code when a user is not found.')
@allure.severity(allure.severity_level.NORMAL)
def test_single_user_not_found():
    with allure.step('Send request to get a non-existent user'):
        response = requests.get('https://reqres.in/api/users/23')
        response_data = response.json()

    with allure.step('Verify response status code'):
        assert response.status_code == 404, f'Expected Status Code 404, but got {response.status_code}'

    with allure.step('Verify the response body is empty'):
        assert response_data == {}, 'Expected response data to be empty, but it was not'

    print(response_data)
