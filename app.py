from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from keyboard import press
import time

class TwitterBot:
     def __init__(self,username,password):
         self.username = username
         self.password = password
         self.bot = webdriver.Firefox()

     def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(10)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        press('enter')
        #pasword.send_keys(Keys.ENTER)
        time.sleep(3)

     def like_tweet(self,hastag):
         bot = self.bot
         bot.get('https://twitter.com/search?q='+hastag+'&src=typed_query')
         time.sleep(10)
         links = []
         for i in range(0,10):
             bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
             time.sleep(1)
             #tweets = bot.find_element_by_class_name('tweet')
             tweets = bot.find_elements_by_xpath("//*[contains(@class,'css-1dbjc4n r-18u37iz r-thb0q2')]")
             for tweets in tweets:
                 elements = tweets.find_elements_by_tag_name("a")
                 for elem in elements:
                     links.append(elem.get_attribute("href"))
                     print(links)
                     bot.find_element_by_xpath("//div[@data-testid='like']").click()

             #links = [elem.get_attribute('href') forrrrrg elegm ing tweets]
"""
             for link in links:
                 print(links)
                 bot.get(link)g
                 try:
                     bot.find_element_by_class_name('HeartAnimation').click()
                     time.sleep(10)
                 except Exception as ex:
                     time.sleep(60)
                     """



ak = TwitterBot("Provide your email here","Provide your password here")
ak.login()
ak.like_tweet("Provide the hashtag to be followed")
