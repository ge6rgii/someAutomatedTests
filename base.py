from xpath_config import SafeBoardXPaths


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://localhost:8080'

    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    def enter_word(self, word, xpath):
        search_field = self.driver.find_element_by_xpath(xpath)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_element(self, xpath):
        element_to_click = self.driver.find_element_by_xpath(xpath)
        element_to_click.click()
        return element_to_click

    def register(self, username, password, password_confirm):
        self.driver.get(f'{self.base_url}/signup')
        self.enter_word(username, SafeBoardXPaths.REGISTRATION_USERNAME)
        self.enter_word(password, SafeBoardXPaths.REGISTRATION_PASS)
        self.enter_word(password_confirm, SafeBoardXPaths.REGISTRATION_CONFIRM_PASS)
        self.click_on_element(SafeBoardXPaths.REGISTRATION_BUTTON)

    def login(self, username, password):
        self.driver.get(f'{self.base_url}/login')
        self.enter_word(username, SafeBoardXPaths.LOGIN_USERNAME)
        self.enter_word(username, SafeBoardXPaths.LOGIN_PASSWORD)
        self.click_on_element(SafeBoardXPaths.LOGIN_BUTTON)


class HelperBooks(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.add_cookie({'sessionup': SafeBoardXPaths.SESSION_COOKIE})
