from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tenzor_task.locators.selectors import TenzorLocators2


class PageSaby:

    def __init__(self, driver):
        self.driver = driver

    def open_saby_contact(self):
        self.driver.get('https://saby.ru/')
        self.driver.find_element(By.XPATH, '//div[contains(text(), "Контакты")]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon').click()

    def check_region(self, region):
        region_block = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            TenzorLocators2.LOCATOR_TENZOR_CHECK_REGION)).text
        assert region_block == region

    def check_city(self, city):
        city_block = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            TenzorLocators2.LOCATOR_TENZOR_CHECK_PARTNERS_UPDATE)).text
        assert city_block == city

    def list_partners(self):
        list_partners = []
        block_partners = WebDriverWait(self.driver, timeout=30).until(
            EC.presence_of_all_elements_located(TenzorLocators2.LOCATOR_TENZOR_CHECK_PARTNERS))
        for partner in block_partners:
            partners = partner.text.split("\n")
            if len(partners) > 1:
                for elem in partners:
                    list_partners.append(elem)
        assert len(list_partners) > 0