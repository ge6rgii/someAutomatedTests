import locators_config as locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://localhost:8080'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator,time=2):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def find_elements(self, locator,time=2):
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
    
    def signup(self, name, username, password, password_confirm):
        self.driver.get(f'{self.base_url}/signup')
        self.enter_text(name, locators.REGISTRATION_NAME)
        self.enter_text(username, locators.REGISTRATION_USERNAME)
        self.enter_text(password, locators.REGISTRATION_PASS)
        self.enter_text(password_confirm, locators.REGISTRATION_CONFIRM_PASS)
        self.click_on_element(locators.REGISTRATION_BUTTON)

    def login(self, username, password):
        self.driver.get(f'{self.base_url}/login')
        self.enter_text(username, locators.LOGIN_USERNAME)
        self.enter_text(password, locators.LOGIN_PASSWORD)
        self.click_on_element(locators.LOGIN_BUTTON)

    def login_success(self):
        try:
            self.click_on_element(locators.SIGNOUT_BUTTON)
            return 'Success'
        except TimeoutException:
            return None        

    def signup_seccess(self):
        try:
            return self.find_element(locators.REGISTRATION_SUCCESS).text
        except TimeoutException:
            return None    

    def get_session_cookie(self):
        return self.driver.get_cookie("sessionup")['value']


class BooksHelper(Base):

    def __init__(self, driver):      
        super().__init__(driver)
        #self.session_cookie = session_cookie
        #self.driver.add_cookie({'sessionup': self.session_cookie})

    def get_books_data(self):
        self.driver.get(f'{self.base_url}/books')
        all_books = self.find_elements(locators.BOOKS)
        self.books_data = [book.text.split('\n') for book in all_books if len(book.text) > 0]
        self.books_titles = [book.text.split('\n') for book in all_books if len(book.text) > 0]
        self.current_prices = [book[-3].split()[0] for book in self.books_data]
        self.previous_prices = [book[-2].split()[2] for book in self.books_data]
        self.ISBN13_codes = [book[0].split()[1].replace('-', '') for book in self.books_data]
        self.ISBN10_codes = [book[1].split()[1] for book in self.books_data]
        return self.books_data


class CartHelper(BooksHelper):
    
    def add_all_books_to_cart(self):
        books_data = self.get_books_data()
        self.books_titles = [book[2] for book in books_data]
        add_to_cart_buttons = self.find_elements(locators.ADD_TO_CART_BUTTONS)

        for button in add_to_cart_buttons:
            button.click()
        
        return self.books_titles
    
    def check_added_to_cart_books(self):
        self.driver.get(f'{self.base_url}/cart')
        added_books = self.find_elements(locators.BOOKS)
        added_books_titles = [book.text.split('\n')[2] for book in added_books if len(book.text) > 0]

        return all(book in self.books_titles for book in added_books_titles)


class OrderHelper(Base):
    
    def get_added_to_cart_books(self):
        self.driver.get(f'{self.base_url}/orders/1')
        added_books = self.find_elements(locators.ADDED_TO_CART_BOOKS)
        added_books_data = [book.text.split('\n') for book in added_books if len(book.text) > 0]
        added_books_prices = [book.split()[-1] for book in added_books_data[0]]
        return added_books_prices

    def get_cart_total_price(self):
        cart_info = self.find_elements(locators.CART_TOTAL_PRICE)
        cart_total_price = [data.text.split('\n') for data in cart_info]
        cart_total_price = cart_total_price[1][0].split()[2]
        return cart_total_price
