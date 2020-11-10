from selenium import webdriver
from base import AuthorizationHelper, BooksHelper, CartHelper


driver = webdriver.Firefox()

auth  = AuthorizationHelper(driver)
books = BooksHelper(driver)
cart  = CartHelper(driver)


def test_successful_signup():
    # Basic registration by following rules.
    auth.signup("Test", "testuser", "Pass1", "Pass1")
    assert auth.signup_seccess()

def test_successful_signup_username_with_numbers():
    auth.signup("Test", "Test2", "Pass1", "Pass1")
    assert auth.signup_seccess()

def test_successful_signup_without_name():
    # Name is not required.
    auth.signup("", "Test3", "Pass1", "Pass1")
    assert auth.signup_seccess()

def test_failed_signup_username_check():
    # username must be at least 5 characters.
    auth.signup("Test", "test", "Pass1", "Pass1")
    assert not auth.signup_seccess()

def test_failed_signup_password_check():
    # password must be at least 5 characters and contain at least one number and letter.
    auth.signup("Test", "Test4", "test", "test")
    assert not auth.signup_seccess()

def test_failed_signup_different_confirm_pass():
    # password must be the same as confirmation password.
    auth.signup("Test", "Test5", "Password1337", "test")
    assert not auth.signup_seccess()

def test_failed_signup_existing_user():
    # trying to create account with existing user data.
    auth.signup("Test", "testuser", "Pass1", "Pass1")
    assert not auth.signup_seccess()


# login tests
def test_successful_login():
    auth.login("testuser", "Pass1")
    assert auth.login_success()

def test_successful_login_username_with_numbers():
    auth.login("Test2", "Pass1")
    assert auth.login_success()

def test_failed_login_wrong_username():
    auth.login("wrongusername", "Password1337")
    assert not auth.login_success()

def test_failed_login_wrong_password():
    auth.login("testuser", "wrongpassword")
    assert not auth.login_success()


# Collecting books data for tests.
books.get_books_data()

def test_valid_info_about_books():
    # checks if book has title, description, author and so on.
    # P.S. I didn't notice that "The Way of the Web Tester.." hasn't description before this test.. 
    insufficient_data = list(filter(lambda book_info: len(book_info) < 9, books.books_data))
    assert not insufficient_data

def test_all_prices_more_than_zero():
    incorrect_current_price = list(filter(lambda price: price == '0.00', books.current_prices))
    incorrect_previous_price = list(filter(lambda price: price == '0.00', books.previous_prices))
    assert not incorrect_current_price and not incorrect_previous_price

def test_valid_ISBN13():
    # this test checks if all ISBN-13 codes has 13 numbers.
    wrong_codes = list(filter(lambda code: len(code) != 13, books.ISBN13_codes))
    assert not wrong_codes

def test_valid_ISBN10():
    # checks if all ISBN-10 codes has 10 numbers in it.
    wrong_codes = list(filter(lambda code: len(code) != 10, books.ISBN10_codes))
    assert not wrong_codes

def test_check_add_to_cart_buttons():
    books_without_add_to_cart_button = [book for book in books.books_data if book[-1] != 'Добавить в корзину']
    assert not books_without_add_to_cart_button


# cart page tests
def test_cart():
    auth.login("testuser", "Pass1")
    success_all_books_added = cart.add_all_books_to_cart()
    assert success_all_books_added
