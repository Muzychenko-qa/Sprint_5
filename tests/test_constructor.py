from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestConstructor:

    def test_click_buns_switch_to_sauces_switch_to_buns(self, driver):
        driver.find_element(*StellarBurgersLocators.SAUCES_SECTION).click()
        driver.find_element(*StellarBurgersLocators.BREAD_SECTION).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.BURGER_BUN_H2))
        element = driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_ACTIVE_TAB)
        assert element.text == "Булки"

    def test_click_sauces_switch_to_sauces(self, driver):
        driver.find_element(*StellarBurgersLocators.SAUCES_SECTION).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.BURGER_BUN_H2))
        element = driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_ACTIVE_TAB)
        assert element.text == "Соусы"

    def test_click_dips_switch_to_dips(self, driver):
        driver.find_element(*StellarBurgersLocators.DIPS_SECTION).click()
        WebDriverWait(driver, Data.WAIT_TIME).until(
            ec.visibility_of_element_located(StellarBurgersLocators.BURGER_BUN_H2))
        element = driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_ACTIVE_TAB)
        assert element.text == "Начинки"
