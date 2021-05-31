from browser import Browser
from selenium.webdriver.common.by import By


class HomePageLocator(object):
    # Home Page Locators

    SEARCH_FIELD = (By.ID, "search")
    SUBMIT_BUTTON = (By.XPATH, "//form[1]/button[1]")


class HomePage(Browser):
    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.click_element(*HomePageLocator.SUBMIT_BUTTON)
