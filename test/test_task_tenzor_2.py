from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tenzor_task.conftest import driver
from Tenzor_task.locators.selectors import TenzorLocators2

from selenium.webdriver.common.by import By




class TestSaby():
    def test_check_region(self, driver):
        driver.get('https://saby.ru/')
        driver.find_element(By.XPATH, '//div[contains(text(), "Контакты")]').click()
        driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon').click()
        pagination_block = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            TenzorLocators2.LOCATOR_TENZOR_CHECK_REGION)).text
        assert pagination_block == 'Челябинская обл.'

    def test_check_city(self, driver):
        """Проверяет что список партнеров не является пустым"""
        driver.get('https://saby.ru/')
        driver.find_element(By.XPATH, '//div[contains(text(), "Контакты")]').click()
        driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon').click()
        check_city = driver.find_element(By.XPATH, '//div[@id="city-id-2"]')
        assert check_city.text == 'Челябинск'

    def test_list_partners(self, driver):
        driver.get('https://saby.ru/')
        driver.find_element(By.XPATH, '//div[contains(text(), "Контакты")]').click()
        driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon').click()
        list_partners = []
        block_partners = WebDriverWait(driver, timeout=30).until(EC.presence_of_all_elements_located(TenzorLocators2.LOCATOR_TENZOR_CHECK_PARTNERS))
        for partner in block_partners:
            partners = partner.text.split("\n")
            if len(partners) > 1:
                for elem in partners:
                    list_partners.append(elem)
        assert len(list_partners) > 0

    def test_change_region(self, driver):
        driver.get('https://saby.ru/')
        driver.find_element(By.XPATH, '//div[contains(text(), "Контакты")]').click()
        driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon').click()
        driver.find_element(By.XPATH, '// span[contains(text(), "Челябинская обл.")]').click()
        driver.find_element(By.XPATH, '// span[contains(text(), "41 Камчатский край")]').click()
        region = driver.find_element(By.XPATH, '// span[contains(text(), "41 Камчатский край")]')
        assert region == "41 Камчатский край"
