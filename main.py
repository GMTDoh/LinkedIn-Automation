import time
from csv import reader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# We need to import a CSV with the names, profile, URL, or something else that can distinguish who we are trying to find
    # We could use the LinkedIn URL as it's the easiest to find, then use the class element of the name on the LinkedIn profile to personalize the message
    # The month used in the personalized message could be difficul, but could also be taken from the CSV file
# Finding a way to iterate through the entire CSV file might be a challenge as currently this only iterates a single time
    # This is something that wil be decently easy to solve and should be done towards the end

class LinkedinBot:
    def __init__(self, username, password):
        """ Initialized Chromedriver, sets common urls, username and password for user """

        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        
        # this can add specific text into the search bar if we want to look something up
            # we can save this for later
            # could be used for companies
        self.feed_url = self.base_url + '/feed'
        
        # this is the specific link that we will use to get to certain profiles
        self.profile_url = link
        
        # username & password is defined below and will be inputted when the code is run - this could be personalized with whoever is using it 
            # This means that anyone could use the program
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
        
        # Looks for button that contains the text "Sign in" and clicks it
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

        # This code could be used to make a post (I found it from an open source code on GitHub)
            # This isn't something we need right now, but commenting it out instead of deleting it seemed more appropriate
    # def post(self, text):
        # """ Make a text post """
        # self.driver.find_element_by_class_name('share-box__open').click()
        # self.driver.find_element_by_class_name('mentions-texteditor__content').send_keys(text)
        # self.driver.find_element_by_class_name('share-actions__primary-action').click()
    
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
        # this is for the previous search method - might not be used
        """ Called after search method to send connections to all on page """

        connect = self.driver.find_element_by_class_name('search-result__action-button')
        connect.click()
        
        time.sleep(2)
        
        self.driver.find_element_by_class_name('ml1').click()
        
    def profile_connect(self, connect=False):
        # searches for specific profiles to connect with them
        self._nav(self.profile_url)
        
        # Waiting for search results to load
        time.sleep(3)
        
        if connect:
            self._search_connect_message
            
     def _search_connect_message(self):
        # this is for when we want to send a personal message intvitation
        """ Called after search method to send connections to all on page """

        connect = self.driver.find_element_by_id('ember587')
        connect.click()
        # here is where the pop-up comes up asking if we want to add a personal message
        
        time.sleep(2)
        
        # mr1 is the class name for the "Add a note" button
        self.driver.find_element_by_class_name('mr1').click()
        
        time.sleep(2)
        
        # custom-message is the ID name for the message-text box
        # message is the variable we are assigning to our personalized note
        # not entirely sure if this is the correct method for adding text, but I am searching for different to find elements
        self.driver.find_element_by_id('custom-message').send_keys(message)
        
        time.sleep(4)
        
        # ml1 is the class name for the "Send" button after we have written a message
        self.driver.find_element_by_class_name('ml1').click()
        
if __name__ == '__main__':    
    
    username = ''
    password = ''
    message = ''
    
    bot = LinkedinBot(username, password)
    
    # iterate over each line as a ordered dictionary and use certain columns as needed
    # this is the main iteration that we go through for the linked in profiles
    with open('LIA.csv', 'r') as linkedin_csv:
        linkedin_profiles_csv = DictReader(linkedin_csv)
        for row in linkedin_profiles_csv:
            link = row['Link']
            
            bot.login(username, password)
            bot.profile_search(connect=True)
            
    
    #The methods used to call certain objects and to run certain codes will need to be looked over to make sure it is all running smoothly
    
    # post_text = ''
    # search_text is used to distinguish the text parameter from the "post" function and the "search" function
    # search_text = ''
    
    # bot.search(search_text, connect=True)
    
    # bot.post(post_text)
    
    
    # General Notes
        # the connect button on a specific LinkedIn:
            # profile ID: "ember587"
            # class: ml2
            
    
