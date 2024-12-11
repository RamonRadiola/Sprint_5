from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators


def maen_logic(driver): #функция авторизации
    driver.get(Constants.URL)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_ASSEMBLE_BURGER))
    driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_IN))
    driver.find_element(*Locators.LOGIN_PLACE).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD_PLACE).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON_LAST).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_ASSEMBLE_BURGER))

class TestTransition:
    def test_transition_in_profile(self, driver):
        maen_logic(driver)
        driver.find_element(*Locators.BUTTON_PROFILE).click()
        assert driver.current_url == Constants.URL_PROFIlE

    def test_transition_in_constructor(self, driver):
        maen_logic(driver)
        driver.get(Constants.URL_PROFIlE)
        driver.find_element(*Locators.BUTTON_CONSTRUCT).click()
        assert driver.current_url == Constants.URL

    def test_transition_in_logo(self, driver):
        maen_logic(driver)
        driver.get(Constants.URL_PROFIlE)
        driver.find_element(*Locators.BUTTON_LOGO).click()
        assert driver.current_url == Constants.URL

    def test_transition_logout(self, driver):
        maen_logic(driver)
        driver.get(Constants.URL_PROFIlE)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGOUT))
        driver.find_element(*Locators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TRIGGER_IN))
        assert driver.current_url == Constants.URL_LOGIN

    def test_transition_burger_filling(self, driver):
        maen_logic(driver)
        driver.find_element(*Locators.BUTTON_FILLING).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TRIGGER_FILLING))

    def test_transition_burger_sous(self, driver):
        maen_logic(driver)
        driver.find_element(*Locators.BUTTON_SOUS).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TRIGGER_SOUS))

    def test_transition_bun(self, driver):
        maen_logic(driver)
        driver.find_element(*Locators.BUTTON_FILLING).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TRIGGER_FILLING))
        driver.find_element(*Locators.BUTTON_BUN).click()
        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TRIGGER_BUN))

