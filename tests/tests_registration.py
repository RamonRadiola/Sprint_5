from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators
from helpers import GenenateData

genenate_data = GenenateData()

class TestReg:
    def test_right_registration(self, driver):
        email = genenate_data.generate_email()
        password = genenate_data.generate_right_password()
        driver.get(Constants.URL_REG)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_REG))
        driver.find_element(By.NAME, "name").send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_IN))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_wrong_password(self, driver):
        email = genenate_data.generate_email()
        password = genenate_data.generate_error_password()
        driver.get(Constants.URL_REG)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_REG))
        driver.find_element(By.NAME, "name").send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        text_error = WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locators.TRIGGER_ERR_PASSWORD)).text
        assert text_error == 'Некорректный пароль'