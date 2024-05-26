import unittest
import cfscrape
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def test_something(self):
        name = '小明'
        age = '9岁'
        print('合并字符串:', name + age)

    def test_cloudFlare(self):
        # 实例化一个create_scraper对象
        scraper = cfscrape.create_scraper()
        # 请求报错，可以加上时延
        # scraper = cfscrape.create_scraper(delay = 10)
        # 获取网页源代码
        web_data = scraper.get('https://us.shein.com/').content
        print(web_data)

    def test_hello(self):
        # 打印Hello World
        hello = 'hello world'
        print(hello)

    def test_number(self):
        number = 23
        guess = int(input('Enter an integer : '))

        if guess == number:
            print('Congratulations, you guessed it.')
        elif guess < number:
            print('No, it is a little higher than that')
        else:
            print('No, it is a little lower than that')


if __name__ == '__main__':
    unittest.main()
