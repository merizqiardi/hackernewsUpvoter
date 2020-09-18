from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
destination = "https://news.ycombinator.com/"

class hackernewsUpvoter():
    def __init__(self, username, password, website):
        self.driver = webdriver.Chrome(PATH) 
        self.username = username
        self.password = password
        self.website = website

    def sign_in(self, login_page="https://news.ycombinator.com/login"):
         # Go to hackernews's website
        self.driver.get(login_page)
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
        upvoteButtons = self.driver.find_elements_by_class_name("votearrow")

        # Click every upvote buttons in the page 
        for button in upvoteButtons:
            try: 
                button.click()
                time.sleep(1)
            except: 
                print("The upvote button wasn't clickable")
                pass
        
    def goto_page(self, page):
        self.driver.get("https://news.ycombinator.com/news?p={}".format(page))

    def next_page(self):
        more = self.driver.find_elements_by_class_name("morelink")
        more[0].click()

bot = hackernewsUpvoter(input(), input(), destination)
bot.sign_in()

for i in range(3,5):
    bot.upvoter() 
    bot.goto_page(i)
    time.sleep(random.randrange(300,500)/100)



