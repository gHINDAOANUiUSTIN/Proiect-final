from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
	LOGIN_PAGE_BUTTON = (By.XPATH, '//a[@class="my-account-login btn btn-primary btn-block"]')
	SELECT_BOOKS = (By.XPATH, '//*[@id="mobileCat-Carte"]/a[1]')
	SELECT_FICTION = (By.XPATH, '//*[@id="discount_id"]/li[1]/a/span')
	SEARCH_BAR = (By.XPATH, '//div[@class="col-md-9 header-search-container-wrapper"]//input[1]')
	SEARCH_BUTTON = (By.XPATH, '//div[@id="HeaderRow"]//div[4]//form/button')
	ACCOUNT_BUTTON = (By.XPATH, '//a[@href="#account-layer"]//div//i')

	def home_page(self):
		self.chrome.get("https://www.elefant.ro/")

	def click_account_button(self):
		self.chrome.find_element(*self.ACCOUNT_BUTTON).click()

	def click_login_page_button(self):
		self.chrome.find_element(*self.LOGIN_PAGE_BUTTON).click()

	def check_logout_page_redirection(self):
		home = self.chrome.get("https://www.elefant.ro/")
		url = self.chrome.current_url
		assert home != url, "Error, URL was not loaded properly. Check if login was successful"

	def select_category(self):
		category = self.chrome.find_elements(*self.SELECT_BOOKS)
		category[1].click()

	def select_genre(self):
		self.chrome.find_element(*self.SELECT_FICTION).click()

	def type_search_product(self, product_name):
		self.chrome.find_element(*self.SEARCH_BAR).send_keys(product_name)

	def click_search_button(self):
		self.chrome.find_element(*self.SEARCH_BUTTON).click()

	def delete_confirmation(self):
		current_url_deletion = self.chrome.current_url
		expected_content_deletion = "ViewCustomerAccountDeactivatedPage"
		assert expected_content_deletion in current_url_deletion, \
			"Error, The account has not been deleted"
