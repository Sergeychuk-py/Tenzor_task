import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tenzor_task.conftest import driver

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
        driver.get('https://sbis.ru/contacts/')

        WebDriverWait(driver, 30).until(
            EC.visibility_of(driver.find_element(By.XPATH, '// span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]'))
        ).click()
        input_el = driver.find_element(By.XPATH, '// input[@name="ws-input_2025-07-15"]')
        input_el.send_keys('Камчатский край')
        driver.find_element(By.XPATH, '// span[contains(text(), "Камчатский край")]').click()

        time.sleep(3)
        assert driver.title == 'Saby Контакты — Камчатский край'
        assert driver.current_url == 'https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients'


