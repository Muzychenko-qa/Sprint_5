from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestRegistration:

    def test_success_registration(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.REGISTRATION_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_REGISTRATION))

        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_INPUT).send_keys(Data.AUTH_NAME)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_INPUT).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_INPUT).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.REGISTRATION_H2_TEXT))
        element = driver.find_element(*StellarBurgersLocators.REGISTRATION_H2_TEXT)
        assert element.is_displayed()

    def test_registration_with_incorrect_password(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.REGISTRATION_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_REGISTRATION))

        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_INPUT).send_keys(Data.AUTH_NAME)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_INPUT).send_keys(Data.INCORRECT_PASSWORD)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.INCORRECT_PASSWORD_H2_TEXT))
        element = driver.find_element(*StellarBurgersLocators.INCORRECT_PASSWORD_H2_TEXT)
        assert element.text == 'Некорректный пароль'
