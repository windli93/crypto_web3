import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-blink-features')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--single-process')
        # chrome_options.add_argument('--origin=https://us.shein.com')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                    '(KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37')
        self.driver = webdriver.Remote(command_executor='http://192.168.47.158:4444/wd/hub',
                                       options=webdriver.ChromeOptions())

    def test_search_in_python_org(self):
        driver = self.driver
        driver.implicitly_wait(120)
        driver.set_script_timeout(120)
        driver.set_page_load_timeout(120)
        driver.get('http://www.python.org')
        self.assertIn('Python', driver.title)
        assert 'No results found.' not in driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
