import unittest
from selenium import webdriver

from helpers import helper


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('lib\chromedriver.exe')
        self.driver.get(
            "http://way2automation.com/way2auto_jquery/frames-and-windows.php")
        self.driver.maximize_window()
        helper.login(self.driver)

    def test_clipboard_copy_by_button(self):
        self.driver.get(
            "http://way2automation.com/way2auto_jquery/frames-and-windows.php")
        helper.open_menu_and_click_link(self.driver)
        helper.go_to_new_window(self.driver)
        number_of_windows_before = len(
            helper.get_number_of_windows(self.driver))
        helper.click_link_on_new_page(self.driver)
        number_of_windows_after = len(
            helper.get_number_of_windows(self.driver))
        self.assertEqual(number_of_windows_after, number_of_windows_before + 1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
