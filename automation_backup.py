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
        
        entire_name = self.driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]").split()
        first_name = entire_name[0]
        
        
        
        time.sleep(4)
        
        # ml1 is the class name for the "Send" button after we have written a message
#        send_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]/span")
#        send_button.click()

        
if __name__ == '__main__':

	profiles = []
	
	f = open('LIA.csv', mode='r', encoding='utf-8-sig')
	csv_f = csv.reader(f)
	
	for row in csv_f:
		profiles.append(str(row[0]))
    	

	for profile in profiles:
		profile_url = profile
		
		
		username = 'george.doherty20@gmail.com'
		password = '577Raygl'
		note = 'Hello' + first_name + ', nice to connect with you.'
		bot = LinkedinBot(username, password, note, profile_url)
		bot.login(username, password)
		bot.profile_connect(note, connect=True)
    
    
    
    
    
    
    # "https://www.linkedin.com/in/xavier-kelley/"
            
