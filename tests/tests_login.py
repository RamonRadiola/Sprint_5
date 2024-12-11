from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators

class TestLogin:
    def test_login_main(self, driver):
        driver.get(Constants.URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_ASSEMBLE_BURGER))
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_IN))
        driver.find_element(*Locators.LOGIN_PLACE).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_PLACE).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LAST).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_ASSEMBLE_BURGER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_login_profile(self, driver):
        driver.get(Constants.URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_ASSEMBLE_BURGER))
        driver.find_element(*Locators.BUTTON_PROFILE).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_IN))
        driver.find_element(*Locators.LOGIN_PLACE).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_PLACE).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LAST).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_ASSEMBLE_BURGER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_form_reg(self, driver):
        driver.get(Constants.URL_REG)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_REG))
        driver.find_element(*Locators.BUTTON_LOGIN_FORM_REG).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_IN))
        driver.find_element(*Locators.LOGIN_PLACE).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_PLACE).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LAST).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_ASSEMBLE_BURGER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_reset_password(self, driver):
        driver.get(Constants.URL_LOGIN)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_IN))
        driver.find_element(*Locators.BUTTON_RESET_PASSWORD).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_RES_PASSWORD))
        driver.find_element(*Locators.BUTTON_LOGIN_RESET_PASSWORD).click()
        driver.find_element(*Locators.LOGIN_PLACE).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_PLACE).send_keys(Constants.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LAST).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_ASSEMBLE_BURGER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

