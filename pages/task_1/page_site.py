import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Tenzor_task.locators.selectors import TenzorLocators


class StartPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Отрывается saby.ru ")
    def open(self):
        """
        The method opens the website saby.ru
        Метод открывает веб сайт saby.ru
        """
        self.driver.get('https://saby.ru/')

    @allure.step('Переходим на сайт tenzor.ru')
    def click(self):
        self.driver.find_element(By.XPATH, TenzorLocators.CONTACTS_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, TenzorLocators.MORE_DETAILS).click()
        WebDriverWait(self.driver, timeout=10).until(
            lambda d: d.find_element(By.CSS_SELECTOR, TenzorLocators.TENZOR_BANNER)
        )
        self.driver.find_element(By.CSS_SELECTOR, TenzorLocators.TENZOR_BANNER).click()
