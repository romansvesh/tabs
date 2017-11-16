from selenium.webdriver.common.by import By

__LINK = (By.TAG_NAME, 'a')


def get_link(driver):
    return driver.find_element(*__LINK)
