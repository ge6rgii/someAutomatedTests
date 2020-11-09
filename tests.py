from selenium import webdriver
from base import AuthorizationHelper


driver = webdriver.Firefox()
auth = AuthorizationHelper(driver)


def test_successful_signup():
    # Basic registration by following rules.
    auth.register("Test", "Test1", "Hesoyam1337", "Hesoyam1337")
    assert auth.registration_seccess()

def test_successful_signup_without_name():
    # Name is not required.
    auth.register("", "Test2", "Hesoyam1337", "Hesoyam1337")
    assert auth.registration_seccess()

def test_failed_signup_username_check():
    # username must be at least 5 characters.
    auth.register("Test", "test", "Hesoyam1337", "Hesoyam1337")
    assert not auth.registration_seccess()

def test_failed_signup_password_check():
    # password must be at least 5 characters and contain at least one number and letter.
    auth.register("Test", "Test3", "test", "test")
    assert not auth.registration_seccess()

def test_failed_signup_different_confirm_pass():
    # password must be the same as confirmation password.
    auth.register("Test", "Test4", "Hesoyam1337", "test")
    assert not auth.registration_seccess()

def test_failed_signup_existing_user():
    # trying to create account with existing user data.
    auth.register("Test", "Test1", "Hesoyam1337", "Hesoyam1337")
    assert not auth.registration_seccess()


# login tests
def test_successful_login():
    auth.login("Test1", "Hesoyam1337")
    assert auth.authentification_seccess()

def test_failed_login_wrong_username():
    auth.login("wrongusername", "Hesoyam1337")
    assert not auth.authentification_seccess()

def test_failed_login_wrong_password():
    auth.login("Test1", "wrongpassword")
    assert not auth.authentification_seccess()
