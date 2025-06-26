import logging

from Tenzor_task.conftest import driver
from Tenzor_task.pages.task_1.page_site import StartPage
from Tenzor_task.pages.task_1.page_tenzor import TenzorPage


class TestSbis:
    logging.getLogger().info("Test logging")

    def test_open_contacts(self, driver):
        start_page = StartPage(driver)
        start_page.open()
        start_page.click()

    def test_power_people(self, driver):
        tenzor_page = TenzorPage(driver)
        tenzor_page.open_tenzor()
        tenzor_page.check_title_people()

    def test_more_details(self, driver, ):
        tenzor_page = TenzorPage(driver)
        tenzor_page.open_tenzor()
        tenzor_page.check_title_people()

    def test_comparison_blogs(self, driver):
        tenzor_page = TenzorPage(driver)
        tenzor_page.open_tenzor_about()
        tenzor_page.check_comparison_blogs()
