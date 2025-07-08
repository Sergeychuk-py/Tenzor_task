import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tenzor_task.conftest import driver
from Tenzor_task.locators.selectors import TenzorLocators2

from selenium.webdriver.common.by import By

from Tenzor_task.pages.task_2.page_saby import PageSaby


class Test_Saby():

    def test_check_region(self, driver):
        page_saby = PageSaby(driver)
        page_saby.open_saby_contact()
        page_saby.check_region('Челябинская обл.')

    def test_check_city(self, driver):
        """Проверяет город"""
        page_saby = PageSaby(driver)
        page_saby.open_saby_contact()
        page_saby.check_city('Челябинск')

    def test_list_partners(self, driver):
        page_saby = PageSaby(driver)
        page_saby.open_saby_contact()
        page_saby.list_partners()

    def test_change_region(self, driver):
        driver.get('https://saby.ru/')
        driver.find_element(By.XPATH, '//div[contains(text(), "Контакты")]').click()
        driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon').click()

        driver.find_element(By.XPATH, '// span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]').click()

        driver.find_element(By.XPATH, '// span[contains(text(), "41 Камчатский край")]').click()
        driver.find_element(By.XPATH, '(//span[@class="controls-DecoratorHighlight"])[43]').click()
        assert driver.current_url == 'https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients'
        assert driver.title == 'Saby Контакты — Камчатский край'
