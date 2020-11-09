from selenium import webdriver
from base import AuthorizationHelper, BooksHelper


driver = webdriver.Firefox()

auth = AuthorizationHelper(driver)
books = BooksHelper(driver)


def test_successful_signup():
    # Basic registration by following rules.
    auth.signup("Test", "testuser", "Pass1", "Pass1")
    assert auth.signup_seccess()

def test_successful_signup_username_with_numbers():
    # Basic registration by following rules.
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
    assert auth.login_seccess()

def test_successful_login_username_with_numbers():
    auth.login("Test2", "Pass1")
    assert auth.login_seccess()

def test_failed_login_wrong_username():
    auth.login("wrongusername", "Password1337")
    assert not auth.login_seccess()

def test_failed_login_wrong_password():
    auth.login("testuser", "wrongpassword")
    assert not auth.login_seccess()


# Remove it in prod pleasseeeee.
auth.signup("Test", "testuser", "Pass1", "Pass1")
auth.login("testuser", "Pass1")
# collecting books data for tests. I'm about to rewrite it
books = BooksHelper(driver)
books_data = books.get_books_data()


def test_valid_info_about_books():
    pass

def test_all_prices_more_than_zero():
    pass

def test_valid_ISBN13():
    # this test checks if all ISBN-13 codes has 13 numbers.
    wrong_codes = list(filter(lambda x: len(x) != 13, books.ISBN13_codes))
    assert not wrong_codes

def test_valid_ISBN10():
    # checks if all ISBN-10 codes has 10 numbers in it.
    wrong_codes = list(filter(lambda x: len(x) != 10, books.ISBN10_codes))
    assert not wrong_codes

def test_check_add_to_cart_buttons():
    pass

"""
just some basic tests
"""
