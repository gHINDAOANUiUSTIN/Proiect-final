from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@name = "addProduct"]')
    ADD_TO_CART_CONFIRMATION = (By.XPATH, '//div[@class="bg-success"]/span')
    VIEW_CART_BUTTON = (By.XPATH, '//a[@class=" btn btn-primary btn-lg btn-block"]')

    def add_to_cart(self):
        self.chrome.find_element(*self.ADD_TO_CART_BUTTON).click()

    def add_to_cart_confirmation(self):
        self.chrome.find_element(*self.ADD_TO_CART_CONFIRMATION)

    def click_view_cart_button(self):
        self.chrome.find_element(*self.VIEW_CART_BUTTON).click()
