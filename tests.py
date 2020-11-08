from selenium import webdriver
from base import AuthorizationHelper


driver = webdriver.Firefox()
auth = AuthorizationHelper(driver)


def test_registration():
    auth.register("Jouny", "procoder1337", "Hesoyam1337", "Hesoyam1337")
    assert auth.registration_seccess()

def test_registration_without_name():
    auth.register("", "Test2", "Test2", "Test2")
    assert auth.registration_seccess()

def test_registration_username_check():
    auth.register("Georgii", "Test", "Hesoyam1337", "Hesoyam1337")
    assert not auth.registration_seccess()

def test_registration_without_name():
    auth.register("", "Test2", "Test2", "Test2")
    assert auth.registration_seccess()

def test_registration_pass_check():
    pass

def test_registration_confirm_pass_check():
    pass

def test_registration_existing_user():
    pass


# login tests
def test_login():
    pass

def test_login_wrong_pass():
    pass

"""
Just some local tests
"""
