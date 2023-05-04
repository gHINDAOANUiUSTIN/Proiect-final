from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    PRODUCT_LINK = (By.XPATH, '//div[@class="product-list main-list row"]'
                              '//div[1]//div[@class="lazy inventory-item"]')
    SIMPLE_SEARCH_RESULTS = (By.XPATH, '//div[1]/h1[@class="current-category-name"]')
    FIRST_PRODUCT_RETURNED = (By.XPATH, '//div[@class="product-list main-list row"]'
                                        '//div[1]//div[@class="lazy inventory-item"]//h2')

    def simple_search_results(self):
        ssr = self.chrome.find_element(*self.SIMPLE_SEARCH_RESULTS)
        ssr = ssr.get_attribute("textContent")
        fpr = self.chrome.find_element(*self.FIRST_PRODUCT_RETURNED)
        fpr = fpr.get_attribute("textContent")
        assert any(word in fpr for word in ssr.split()) or any(word in ssr for word in fpr.split()), \
            "ERROR, the searched product doesn't appear first in the search results"

    def click_on_product(self):
        self.wait_and_click_element_by_selector(*self.PRODUCT_LINK)
