from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):
    LOGOUT_BUTTON = (By.XPATH, '//a[@data-testing-id="link-logout"]')
    DELETE_ACCOUNT_BUTTON = (By.XPATH, '//a[@class="btn btn-deactivate top-buffer"]')
    CONFIRM_DELETE_ACCOUNT_BUTTON = (By.XPATH, '//input[@class="btn btn-primary"]')
    ACCOUNT_SETTINGS_BUTTON = (By.XPATH, '//div[@class="collapse in"]/ul/li[1]/a')

    def check_user_is_logged(self):
        current_url_my_account = self.chrome.current_url
        expected_content_my_account = "my-account"
        assert expected_content_my_account in current_url_my_account, \
            "Error, URL was not loaded properly. Check if login was successful"

    def click_logout_button(self):
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()

    def click_delete_account(self):
        self.chrome.find_element(*self.DELETE_ACCOUNT_BUTTON).click()

    def click_confirm_delete_account(self):
        self.chrome.find_element(*self.CONFIRM_DELETE_ACCOUNT_BUTTON).click()
