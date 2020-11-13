import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
### We need to import a CSV with the names, profile, URL, or something else that can distinguish who we are trying to find
    ### We could use the LinkedIn URL as it's the easiest to find, then use the class element of the name on the LinkedIn profile to personalize the message
    ### The month used in the personalized message could be difficul, but could also be taken from the CSV file
### Finding a way to iterate through the entire CSV file might be a challenge as currently this only iterates a single time
    ### This is something that wil be decently easy to solve and should be done towards the end

class LinkedinBot:
    def __init__(self, username, password):
        """ Initialized Chromedriver, sets common urls, username and password for user """

        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        
        ### feed.url is what we will have to mess with in order to get the desired LinkedIn profiles
        self.feed_url = self.base_url + '/feed'

        ### username & password is defined below and will be inputted when the code is run - this could be personalized with whoever is using it 
            ### This means that anyone could use the program
        self.username = username
        self.password = password

    def _nav(self, url):
        self.driver.get(url)
        time.sleep(3)

    def login(self, username, password):
        """ Login to LinkedIn account """
        self._nav(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        
        ### Looks for button that contains the text "Sign in" and clicks it
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

        ### This code could be used to make a post (I found it from an open source code on GitHub)
            ### This isn't something we need right now, but commenting it out instead of deleting it seemed more appropriate
    ###def post(self, text):
        ###""" Make a text post """
        ###self.driver.find_element_by_class_name('share-box__open').click()
        ###self.driver.find_element_by_class_name('mentions-texteditor__content').send_keys(text)
        ###self.driver.find_element_by_class_name('share-actions__primary-action').click()
    
    def search(self, text, connect=False):
        ### If connect=True, the code will connect with the first person it finds from that search
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
        ### An underscore in the beginning declares this to be a private method - doesn't run unless it is called
        """ Called after search method to send connections to all on page """

        connect = self.driver.find_element_by_class_name('search-result__action-button')
        connect.click()
        
        time.sleep(2)
        
        ### Here is where we need to put in the code to add the message
            ### We would use the "send_key" function in order to do this
        self.driver.find_element_by_class_name('ml1').click()


if __name__ == '__main__':

    username = ''
    password = ''
    ###post_text = ''
    
    ### search_text is used to distinguish the text parameter from the "post" function and the "search" function
    search_text = ''

    bot = LinkedinBot(username, password)
    bot.login(username, password)
    ###bot.post(post_text)
    bot.search(search_text, connect=True)
