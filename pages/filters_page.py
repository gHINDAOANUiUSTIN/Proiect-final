from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FiltersPage(BasePage):
    SELECT_DISCOUNT = (By.XPATH, '//ul[@id="DiscountLevel"]/li[2]/a')
    SEARCH_RESULTS = (By.XPATH, '//div[@class="hidden-sm element-count text-nowrap"]')

    def select_discount(self):
        self.wait_and_click_element_by_selector(*self.SELECT_DISCOUNT)

    def filter_search_results(self):
        search_results = self.chrome.find_element(*self.SEARCH_RESULTS)
        number_of_products_text = search_results.text.strip().split()[0]
        number_of_products = float(number_of_products_text.replace('.', ''))
        assert number_of_products > 1000, \
            "Error, the number of search results does not meet expectations."
