from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

class hackernewsUpvoter():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(PATH) 
        self.username = username
        self.password = password
    
    def sign_in(self):

        # Go to hackernews's website
        self.driver.get("https://news.ycombinator.com/login")
        time.sleep(2)

        # Enter username  
        account = self.driver.find_element_by_name('acct')
        account.send_keys(self.username)

        # Enter password
        password = self.driver.find_element_by_name('pw')
        password.send_keys(self.password)
        time.sleep(random.randrange(11,35)/10)

        # Click enter key
        password.send_keys(Keys.RETURN)
    
    def upvoter(self):
        self.driver.get("https://news.ycombinator.com/")
        upvoteButtons = self.driver.find_elements_by_class_name("votearrow")

        # Click every upvote buttons in the page 
        for button in upvoteButtons:
            button.click()
            time.sleep(1)
        
    def next_page(self):
        self.driver.get("https://news.ycombinator.com/")
        more = self.driver.find_elements_by_class_name("morelink")
        more.click()

bot = hackernewsUpvoter("username here", "password here")

for i in range(3):
    bot.sign_in()
    bot.upvoter() 
    bot.next_page()



