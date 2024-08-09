import pytest
import requests
import allure

@pytest.mark.xxx
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User API Tests')
@allure.title('Test delayed response for user API')
@allure.description('This test verifies the delayed response from the user API and checks for required fields.')
@allure.severity(allure.severity_level.NORMAL)
def test_delayed_response():
    with allure.step('Send a GET request to the delayed user API'):
        response = requests.get('https://reqres.in/api/users?delay=3')
        response_data = response.json()

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, 'Expected Status Code 200, but got a different one'

    with allure.step('Verify the presence of required top-level fields'):
        assert 'page' in response_data, 'Response is missing "page"'
        assert 'per_page' in response_data, 'Response is missing "per_page"'
        assert 'total' in response_data, 'Response is missing "total"'
        assert 'total_pages' in response_data, 'Response is missing "total_pages"'
        assert 'data' in response_data, 'Response is missing "data"'
        assert len(response_data['data']) > 0, '"data" should contain at least one user'
        assert 'support' in response_data, 'Response is missing "support"'

    with allure.step('Verify the presence of required fields in the first user object'):
        user = response_data['data'][0]
        assert 'id' in user, 'User data is missing "id"'
        assert 'email' in user, 'User data is missing "email"'
        assert 'first_name' in user, 'User data is missing "first_name"'
        assert 'last_name' in user, 'User data is missing "last_name"'
        assert 'avatar' in user, 'User data is missing "avatar"'

    print(response_data)
