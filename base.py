import locators_config as locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://localhost:8080'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def enter_text(self, word, locator):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_element(self, locator):
        element_to_click = self.find_element(locator)
        element_to_click.click()
        return element_to_click


class AuthorizationHelper(Base):
    
    def register(self, name, username, password, password_confirm):
        self.driver.get(f'{self.base_url}/signup')
        self.enter_text(name, locators.REGISTRATION_NAME)
        self.enter_text(username, locators.REGISTRATION_USERNAME)
        self.enter_text(password, locators.REGISTRATION_PASS)
        self.enter_text(password_confirm, locators.REGISTRATION_CONFIRM_PASS)
        self.click_on_element(locators.REGISTRATION_BUTTON)

    def login(self, username, password):
        self.driver.get(f'{self.base_url}/login')
        self.enter_text(username, locators.LOGIN_USERNAME)
        self.enter_text(username, locators.LOGIN_PASSWORD)
        self.click_on_element(locators.LOGIN_BUTTON)

    def authentification_checker(self):
        pass
        #self.driver.find_element_by_id("signout")


class HelperBooks(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.add_cookie({'sessionup': SafeBoardXPaths.SESSION_COOKIE})
