from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
#driver = webdriver.Chrome(PATH)

class hackernewsUpvoter():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(PATH) 
        self.username = username
        self.password = password
    
    def sign_in(self):
        self.driver.get("https://news.ycombinator.com/login")
        time.sleep(2)
        account = self.driver.find_element_by_name('acct')
        account.send_keys("burgerrito")
        password = self.driver.find_element_by_name('pw')
        password.send_keys("oboe*unexpired*footprint")
        time.sleep(1)
        password.send_keys(Keys.RETURN)
    
    def upvoter(self):
        self.driver.get("https://news.ycombinator.com/")
        upvoteButtons = self.driver.find_elements_by_class_name("votearrow")
        for button in upvoteButtons:
            button.click()
            time.sleep(1)
        
    def next_page(self):
        self.driver.get("https://news.ycombinator.com/")
        more = self.driver.find_elements_by_class_name("morelink")
        more.click()

bot = hackernewsUpvoter("burgerrito", "oboe*unexpired*footprint")
for i in range(3):
    bot.sign_in()
    bot.upvoter() 
    bot.next_page()



'''
driver.get("https://news.ycombinator.com/login")
print(driver.title)

account = driver.find_element_by_name('acct')
account.send_keys("burgerrito")
password = driver.find_element_by_name('pw')
password.send_keys("oboe*unexpired*footprint")
password.send_keys(Keys.RETURN)

print(driver.page_source)

driver.quit()

'''
