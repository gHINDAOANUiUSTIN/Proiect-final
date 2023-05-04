from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    ADD_PRODUCT_BUTTON = (By.XPATH, '//div[@class="plus"]')
    REMOVE_PRODUCT_BUTTON = (By.XPATH, '//a[@class="btn-tool btn-delete"]/i[@class="material-icons"]')
    EMPTY_CART = (By.XPATH, '//div[@class="empty-cart"]/h2')
    LOGO = (By.XPATH, '//div[@id="HeaderRow"]/div[1]/a/img[@alt="Logo"]')

    def click_add_product_button(self):
        self.chrome.find_element(*self.ADD_PRODUCT_BUTTON).click()

    def click_remove_product(self):
        self.chrome.find_element(*self.REMOVE_PRODUCT_BUTTON).click()

    def check_number_of_products(self):
        total_price = float(
            self.chrome.find_element(By.XPATH, '//div[@class="total-price"]').text.replace(',', '.').split()[0]) + \
            0.1 * float(
            self.chrome.find_element(By.XPATH, '//div[@class="total-price"]/sup').text.replace(',', '.').split()[0])
        unit_price = float(
            self.chrome.find_element(By.XPATH, '//div[@class="unit-price"]').text.replace(',', '.').split()[0]) + \
            0.1 * float(
            self.chrome.find_element(By.XPATH, '//div[@class="unit-price"]/sup').text.replace(',', '.').split()[0])
        assert total_price != 2 * unit_price, "ERROR, check if the ADD_PRODUCT_BUTTON is working"

    def cart_is_empty(self):
        self.chrome.find_element(*self.EMPTY_CART)

    def click_logo(self):
        self.chrome.find_element(*self.LOGO).click()
