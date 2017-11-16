from selenium.webdriver.common.by import By

__OPEN_MULTIPLE_WINDOWS_MENU = (By.XPATH, '//a[@href="#example-1-tab-4"]')
__LINK = (By.TAG_NAME, 'a')
__OPEN_MULTIPLE_WINDOWS_FRAME = (By.XPATH, '//div[@id = "example-1-tab-4"]//iframe')


def get_open_multiple_windows_menu(driver):
    return driver.find_element(*__OPEN_MULTIPLE_WINDOWS_MENU)


def get_link(driver):
    return driver.find_element(*__LINK)


def get_open_multiple_windows_frame(driver):
    return driver.find_element(*__OPEN_MULTIPLE_WINDOWS_FRAME)