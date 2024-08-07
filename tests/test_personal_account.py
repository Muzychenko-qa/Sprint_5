from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestPersonalAccount:

    def test_go_to_personal_account_not_authorized_user(self, driver):
        driver.find_element(*StellarBurgersLocators.PERSONAL_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))
        element = driver.find_element(*StellarBurgersLocators.TEXT_SING_IN)
        assert element.is_displayed()

    def test_go_to_personal_account_authorized_user(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.SIGN_IN_EMAIL).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.SIGN_IN_PASSWORD).send_keys(Data.AUTH_PASSWORD)

        driver.find_element(*StellarBurgersLocators.SIGN_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

        driver.find_element(*StellarBurgersLocators.PERSONAL_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located((
            By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")))

        account = driver.find_element(By.CSS_SELECTOR, '.input__textfield')
        assert account.get_property('value') == Data.AUTH_NAME

    def test_go_from_personal_account_to_constructor_clicking_by_link(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.SIGN_IN_EMAIL).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.SIGN_IN_PASSWORD).send_keys(Data.AUTH_PASSWORD)

        driver.find_element(*StellarBurgersLocators.SIGN_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

        driver.find_element(*StellarBurgersLocators.PERSONAL_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located((
            By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")))

        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.CONSTRUCTOR_H1_TEXT))

        element = driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_H1_TEXT)
        assert element.text == "Соберите бургер"

    def test_go_from_personal_account_to_stella_burger_link(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.SIGN_IN_EMAIL).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.SIGN_IN_PASSWORD).send_keys(Data.AUTH_PASSWORD)

        driver.find_element(*StellarBurgersLocators.SIGN_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

        driver.find_element(*StellarBurgersLocators.PERSONAL_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located((
            By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")))

        driver.find_element(*StellarBurgersLocators.STELLA_BURGER_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.CONSTRUCTOR_H1_TEXT))

        element = driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_H1_TEXT)
        assert element.text == "Соберите бургер"

    def test_sing_out(self, driver):
        driver.find_element(*StellarBurgersLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        driver.find_element(*StellarBurgersLocators.SIGN_IN_EMAIL).send_keys(Data.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.SIGN_IN_PASSWORD).send_keys(Data.AUTH_PASSWORD)

        driver.find_element(*StellarBurgersLocators.SIGN_BUTTON).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

        driver.find_element(*StellarBurgersLocators.PERSONAL_LINK).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(ec.visibility_of_element_located((
            By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")))

        driver.find_element(*StellarBurgersLocators.SIGN_OUT).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.presence_of_element_located(StellarBurgersLocators.TEXT_SING_IN))

        element = driver.find_element(*StellarBurgersLocators.TEXT_SING_IN)
        assert element.text == "Вход"
