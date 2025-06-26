from selenium.webdriver.common.by import By


class TenzorLocators:
    CONTACTS_BUTTON = '//div[@class="sbisru-Header-ContactsMenu js-ContactsMenu"]'
    MORE_DETAILS = '.sbisru-Header-ContactsMenu__arrow-icon'
    TENZOR_BANNER = 'a[href="https://tensor.ru/"]'
    TENZOR_POWERPEOPLE_FIND = '//p[contains(text(), "Сила в людях")]'
    TENZOR_POWERPEOPLE_LINK = '(//a[contains(text(), "Подробнее")])[3]'
    TENZOR_WORK_IMAGE = '.tensor_ru-About__block3-image-wrapper img'


class TenzorLocators2:

    LOCATOR_TENZOR_CHECK_REGION = (By.CSS_SELECTOR, "span[class='sbis_ru-Region-Chooser ml-16 ml-xm-0'] "
                                                    "span[class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    LOCATOR_TENZOR_CHECK_PARTNERS = (By.XPATH, "(//div[@class='controls-BaseControl "
                                               "controls_list_theme-sbisru controls_toggle_theme-sbisru'])[1]")
    LOCATOR_TENZOR_FIND_REGION = (By.XPATH, "//span[contains(@title,'Камчатский край')]")
    LOCATOR_TENZOR_CHECK_PARTNERS_UPDATE = (By.CSS_SELECTOR, "#city-id-2")