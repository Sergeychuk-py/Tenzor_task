# def test_currected_region(self, driver):
#     driver.get('https://saby.ru/contacts/')
#     driver.find_element(By.XPATH, '//span[contains(text(), "Челябинская обл.")]').click()
#     driver.find_element(By.XPATH, '//span[contains(text(), "41 Камчатский край")]').click()
#     url = driver.current_url
#     print(url)

# def test_open_saby(self, driver):
#     driver.get('https://saby.ru/')
#     driver.find_element(By.XPATH, '//div[contains(text(), "Контакты")]').click()
#     driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon').click()
#     current_regions = WebDriverWait(driver, timeout=10).until(
#         EC.text_to_be_present_in_element(TenzorTask_2.REGION_TEXT_LOCATOR))
#     region = driver.find_element(TenzorTask_2.REGION_TEXT_LOCATOR).text
#     assert region == current_regions
#     pass
# def test_check_region_user(self, driver):
#     """Сверяет регион на сайте с регионом пользователя (current_region)"""
#     driver.get('https://saby.ru/')
#     driver.find_element(By.XPATH, '//div[contains(text(), "Контакты")]').click()
#     driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon').click()
#     region = WebDriverWait(driver, timeout=10).until(EC.text_to_be_present_in_element(
#         TenzorTask_2.REGION_TEXT_LOCATOR, ''))
#     currect_region = driver.find_element(TenzorTask_2.REGION_TEXT_LOCATOR)
#     assert currect_region.text == region
#
#
# def test_region(self, driver):
#     driver.get('https://saby.ru/')
#     driver.find_element(By.XPATH, '//div[contains(text(), "Контакты")]').click()
#     driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon').click()
#     partners_tym = driver.find_element(By.XPATH, '(//div[@id="city-id-2"])[1][contains(text(), "Челябинск")]')
#     assert partners_tym.text == "Челябинск"


# def rental_car_cost(days):
#     if days >= 7:
#         summa_ = days * 40 - 50
#     elif days <= 3:
#         summa_ = days * 40 - 20
#     return summa_
#
# print(rental_car_cost(7))
#
#
# def car_cost(days):
#     cost = 40*days
#     if days>=7:
#         cost = cost-50
#     elif days>=3:
#         cost = cost-20
#     return cost
# print(car_cost(7))
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
#
# def simple_multiplication(number) :
#     if number % 2 == 0:
#         return number * 8
#     else:
#         return number * 9
#
# def task(number):
#     return number * 8 if number % 2 == 0 else number * 9
#
# print(simple_multiplication(8))
# print(task(7))



# def rever_seq(n):
#     return list(range(n, 0, -1))
#
# print(rever_seq(5))

# def test_pilop(self, driver):
#     driver.get('https://saby.ru/')
#     driver.find_element(By.XPATH, '//div[contains(text(), "Контакты")]').click()
#     driver.find_element(By.CSS_SELECTOR, '.sbisru-Header-ContactsMenu__arrow-icon').click()
#     check_partners = WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located(TenzorLocators2.LOCATOR_TENZOR_CHECK_PARTNERS))
#     partners = []
#     for partner in check_partners:
#         if len(partner) > 0:
#             partners.append(partner.text)
#             assert len(partners) > 0
#     check_city = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located(TenzorLocators2.LOCATOR_TENZOR_CHECK_PARTNERS_UPDATE))
#     assert check_city.text == 'Екатеринбург'

# string = "БОЛЬШАЯ ЧАСТЬ ОШИБОК СОСРЕДОТОЧЕНА В НЕБОЛЬШОМ КОЛИЧЕСТВ МОДУЛЕЙ СИСТЕМЫ"
# print(string.lower())

# assert driver.current_url == 'https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients'
#
# input_el = driver.find_element(By.XPATH, '// input[@name="ws-input_2025-07-15"]')
#         input_el.send_keys('Камчатский край')