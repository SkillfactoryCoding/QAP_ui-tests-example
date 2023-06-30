from pages.auth_page import AuthPage


def test_authorisation(web_browser):

    page = AuthPage(web_browser)
    page.email.send_keys('delich@gmail.com')
    page.password.send_keys("12345")
    page.btn.click()

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'
