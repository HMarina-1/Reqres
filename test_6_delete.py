import pytest
import requests
import allure
# import test_4_create_user


@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('User API Tests')
@allure.title('Test Delete User')
@allure.description('This test verifies the successful deletion of a user.')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete():
    with allure.step('Send request to delete user'):
        response = requests.delete(f'https://reqres.in/api/users/2')

    with allure.step('Check response status code'):
        assert response.status_code == 204, f'Expected status code 204, but got {response.status_code}'

    print('User deleted successfully')
