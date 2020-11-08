from selenium.webdriver.common.by import By


MAIN_PAGE_REG_BUTTON      = '//*[@id="app"]/nav/div[2]/div[2]/div/div/a[2]/strong'
REGISTRATION_NAME         = (By.ID, "name")
REGISTRATION_USERNAME     = (By.ID, "username")
REGISTRATION_PASS         = (By.ID, "password")
REGISTRATION_CONFIRM_PASS = (By.ID, "password-confirm")
REGISTRATION_BUTTON       = (By.XPATH, '//*[@id="app"]/section/div/div[2]/div/div/div[2]/form/div[5]/div[2]/div/div/button')

MAIN_PAGE_LOGIN_BUTTON    = '/html/body/div/nav/div[2]/div[2]/div/div/a[1]/span[2]'
LOGIN_USERNAME            = (By.ID, "username")
LOGIN_PASSWORD            = (By.ID, "password")
LOGIN_BUTTON              = (By.ID, "submit")

SESSION_COOKIE            = 'LNcPkvrr9HwM09Z8PJ5KuYYQSP7YIagML99a2SVb'
