from selenium.webdriver.common.by import By

from Tenzor_task.locators.selectors import TenzorLocators


class TenzorPage:
    def __init__(self, driver):
        self.driver = driver

    def open_tenzor(self):
        self.driver.get('https://tensor.ru/')

    def check_title_people(self):
        title = self.driver.find_element(By.XPATH, TenzorLocators.TENZOR_POWERPEOPLE_FIND)

        assert title.text == 'Сила в людях'

    def check_link(self):
        link = "https://tensor.ru/about/"
        self.driver.find_element(By.XPATH, '(//a[contains(text(), "Подробнее")])[3]').click()

        assert link == "https://tensor.ru/about/"

    def open_tenzor_about(self):
        self.driver.get('https://tensor.ru/about')

    def check_comparison_blogs(self):
        photos = self.driver.find_elements(By.CSS_SELECTOR, TenzorLocators.TENZOR_WORK_IMAGE)
        height_list = [photo.get_attribute("height") for photo in photos]
        width_list = [photo.get_attribute("width") for photo in photos]

        isHeight = True if len(set(height_list)) == 1 else False
        isWidth = True if len(set(width_list)) == 1 else False

        assert isWidth and isHeight