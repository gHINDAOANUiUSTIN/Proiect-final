from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from browser import Browser


class BasePage(Browser):
    COOKIES_BUTTON = (By.XPATH, '//div[@id="CybotCookiebotDialogBodyButtonsWrapper"]/button[4]')

    def accept_cookies(self):
        try:
            self.chrome.find_element(*self.COOKIES_BUTTON).click()
        except:
            pass

    def skip_current_step(self):
        pass

    def wait_and_click_element_by_selector(self, by, selector):
        WebDriverWait(self.chrome, 7).until(ec.presence_of_element_located((by, selector)))
        self.chrome.find_element(by, selector).click()
