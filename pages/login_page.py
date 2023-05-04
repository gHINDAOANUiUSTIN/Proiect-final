from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
	USERNAME = (By.XPATH, '//input[@name="ShopLoginForm_Login"]')
	PASSWORD = (By.XPATH, '//input[@name="ShopLoginForm_Password"]')
	LOGIN_BUTTON = (By.XPATH, '//div[@class="col-sm-12"]/button[@type="submit"]')
	ERROR_MESSAGE = (By.XPATH, '//div[@class="alert alert-danger"]')

	def check_login_page_redirection(self):
		current_url = self.chrome.current_url
		expected_content = "login"
		assert expected_content in current_url, "Error, URL was not loaded properly."

	def insert_username(self, username):
		self.chrome.find_element(*self.USERNAME).send_keys(username)

	def insert_password(self, password):
		self.chrome.find_element(*self.PASSWORD).send_keys(password)

	def click_login_button(self):
		self.chrome.find_element(*self.LOGIN_BUTTON).click()

	def check_error_message(self):
		self.chrome.find_element(*self.ERROR_MESSAGE)

