import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LinkedinBot:
    def __init__(self, username, password, note, profile_url):
        """ Initialized Chromedriver, sets common urls, username and password for user """

        self.driver = webdriver.Chrome('/Users/georgedoherty/Desktop/chromedriver')

        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        
        self.feed_url = self.base_url + '/feed'
        
        
        
        self.profile_url = profile_url
        
        
        self.username = username
        self.password = password
        self.note = note

    def _nav(self, url):
        self.driver.get(url)
        time.sleep(3)

    def login(self, username, password):
        """ Login to LinkedIn account """
        self._nav(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        
        # Looks for button that contains the text "Sign in" and clicks it
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

    def post(self, text):
        """ Make a text post """
        self.driver.find_element_by_class_name('share-box__open').click()
        self.driver.find_element_by_class_name('mentions-texteditor__content').send_keys(text)
        self.driver.find_element_by_class_name('share-actions__primary-action').click()
    
    def search(self, text, connect=False):
        # If connect=True, the code will connect with the first person it finds from that search
        """ Search execeuted from home screen """
        self._nav(self.feed_url)

        search = self.driver.find_element_by_class_name('search-global-typeahead__input')
        search.send_keys(text)
        search.send_keys(Keys.ENTER)
        
        # Waiting for search results to load
        time.sleep(3)

        if connect:
            self._search_connect()

    def _search_connect(self):
        # An underscore in the beginning declares this to be a private method - doesn't run unless it is called
        """ Called after search method to send connections to all on page """

        connect = self.driver.find_element_by_class_name('search-result__action-button')
        connect.click()
        
        time.sleep(2)
        
        self.driver.find_element_by_class_name('ml1').click()
        
    def profile_connect(self, note, connect=False):
        self._nav(self.profile_url)
        
        # Waiting for search results to load
        time.sleep(3)
        
        if connect:
        	self._search_connect_message()
            
    def _search_connect_message(self):
        # this is for when we want to send a personal message invitation

        connect = self.driver.find_element_by_class_name('ml2')
        connect.click()
        # here is where the pop-up comes up asking if we want to add a personal message
        
        time.sleep(2)
        
        # mr1 is the class name for the "Add a note" button
        # "Add a note" xpath: /html/body/div[4]/div/div/div[3]/button[1]/span
        
       	add_note_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]/span")
       	add_note_button.click()
        
        time.sleep(2)
        
        # This adds the note in the personal invitation
        self.driver.find_element_by_id('custom-message').click()
        self.driver.find_element_by_id('custom-message').send_keys(self.note)
        
        
        time.sleep(4)
        
        # ml1 is the class name for the "Send" button after we have written a message
        send_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]/span")
        send_button.click()

        
if __name__ == '__main__':    
    # the iteration loop would go here, cannot go up at the top
    username = 'george.doherty20@gmail.com'
    password = '577Raygl'
    note = 'Hey Charles, this was sent to you through my automation!'
    profile_url = "https://www.linkedin.com/in/solomoncharles/"
    bot = LinkedinBot(username, password, note, profile_url)
    bot.login(username, password)
    bot.profile_connect(note, connect=True)
    
    
    #profiles = []
    #f = open('LIA.csv')
    #csv_f = csv.reader(f)
    #for row in csv_f:
    	#profiles.append(str(row[0]))
    
	
    
    
    
    
    
    
    # "https://www.linkedin.com/in/xavier-kelley/"
            
