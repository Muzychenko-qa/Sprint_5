from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestAccountAccess:

    def test_access_to_account_click_sign_in_button(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.SIGN_IN_EMAIL).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.SIGN_IN_PASSWORD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.SIGN_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(ec.presence_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        element = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
        assert element.is_displayed()

    def test_access_to_account_click_personal_account_link(self, driver):
        driver.find_element(*StellarBurgersLocators.PERSONAL_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.SIGN_IN_EMAIL).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.SIGN_IN_PASSWORD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.SIGN_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        element = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
        assert element.is_displayed()

    def test_access_to_account_using_registration_link(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.REGISTRATION_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_REGISTRATION))

        driver.find_element(*StellarBurgersLocators.SIGN_IN_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.SIGN_IN_EMAIL).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.SIGN_IN_PASSWORD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.SIGN_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        element = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
        assert element.is_displayed()

    def test_access_to_account_using_restore_password_link(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.RESTORE_PASSWORD_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.RESTORE_PASSWORD_H2_TEXT))

        driver.find_element(*StellarBurgersLocators.SIGN_IN_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.SIGN_IN_EMAIL).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.SIGN_IN_PASSWORD).send_keys(Data.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.SIGN_BUTTON).click()

        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        element = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
        assert element.is_displayed()
