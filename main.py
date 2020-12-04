import time
import csv
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Above are Python libraries. These are give Python extra functions we can work with - these are something we will need to download

#Instructions
# Download Python
	# Will probably already have Python installed so skip this for now
	# Go to: https://www.python.org/downloads/release/python-390/
	# If you have a relatively new computer, click where it says "Windows x86-64 web-based installer"
	# If your computer is older, "Windows x86 web-based installer"
# Download chromedriver
	# Go to: https://chromedriver.chromium.org
	# Click where is says "Latest stable release"
	# Unzip the file and you should be ready to go
# Download parsel
	# Go to: https://pypi.org/project/parsel/
	# Click where it says "Download"
	# Open Terminal/Command Propt and type in: pip3 install parsel --user
	# Wait until it's all done
# Download selenium
	# Go to: https://selenium-python.readthedocs.io/installation.html
	# Open Terminal/Command Prompt and type in: C:\Python35\Scripts\pip.exe install selenium

class LinkedinBot:
	def __init__(self, username, password, month, profile_url):
		""" Initialized Chromedriver, sets common urls, username and password for user """


		# This locates the chromedriver on the computer to be used by the automation
		# THIS is something that will have to be changed given its location
		self.driver = webdriver.Chrome('/Users/georgedoherty/Desktop/chromedriver')
		
		# These are URL's that we use to log in
		self.base_url = 'https://www.linkedin.com'
		self.login_url = self.base_url + '/login'
		
		# These are the initialized variables that are used to find specific profiles, log in, and for personalizing the note
		self.profile_url = profile_url
		self.username = username
		self.password = password
		self.month = month


	def _nav(self, url):
		""" Allows us to navigate to a url """
		
		
		self.driver.get(url)
		time.sleep(2)


	def login(self, username, password):
		""" Login to LinkedIn account """
		
		
		# Navigates to the login URL and inputs the given username and password
		self._nav(self.login_url)
		self.driver.find_element_by_id('username').send_keys(self.username)
		self.driver.find_element_by_id('password').send_keys(self.password)
		
		# Looks for button that contains the text "Sign in" and clicks it
		self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()
		

	def profile_connect(self, month, connect=False):
		""" Navigates to the given profile """
		
		
		# Navigates to the profile URL and waits for it to load
		self._nav(self.profile_url)
		
		# When connect=True true under 'if __name__' then the following function will proceed
				# NEVER set the above connect=False to True
		if connect:
			self._search_connect_message()
			
			
	def _search_connect_message(self):
		""" Extracts profile name, clicks 'Connect', adds personal message, then sends the invite"""
		
		
		# This grabs the name of the profile and creates the note using the name and the inputted month
		sel = Selector(text = self.driver.page_source)
		entire_name = sel.xpath('//*[starts-with(@class, "inline t-24 t-black t-normal break-words")]/text()').extract_first()
		if entire_name:
			entire_name.strip()
			l_entire_name = entire_name.split()
			first_name = l_entire_name[0]
			time.sleep(1)
		note = "Hi " + first_name + ", I'm a Venture Partner at Beni VC (www.benivc.com) an NYC fund writing $50K - $250K follow-on checks. Noticed you raised in " + self.month + ". Could the round be re-opened for us since we can write $1M per round for future rounds? If not, when should I reach out for next round?"
		
		# This clicks the 'Connect' button on the website
		connect = self.driver.find_element_by_class_name('ml2')
		connect.click()
		time.sleep(1)
		# here is where the pop-up comes up asking if we want to add a personal note
		
		# This clicks the 'Add a note' button on the pop-up
		add_note_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]/span")
		add_note_button.click()
		time.sleep(1)
		
		# This clicks the text box and inputs the note
		self.driver.find_element_by_id('custom-message').click()
		self.driver.find_element_by_id('custom-message').send_keys(note)
		time.sleep(1)
		
		# This clicks the 'Send' button after the note has been written
				# This will be commented out as the code is worked on in order to not send out the invitations
		#send_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]/span")
		#send_button.click()

		
if __name__ == '__main__':
	""" Where we employ the given functions we created above"""
	
	
	# This asks the user to provide their name - this means we can have multiple different users - I had a little fun with this
	print("Who requests passage of this automation?")
	person = input()
	if person == "George" or person == "george":
		print("Hello, Master - we are at your service")
		username = 'george.doherty20@gmail.com'
		password = '577Raygl'
		time.sleep(2)
		
	if person == "Charles" or person == "charles":
		print("Welcome, Charles! - we are at your service"
		username = 'Solomon.charles@gmail.com'
		password = 'Intern!u20 '
		time.sleep(2)
		
	# This allows us to input the month for the note
	print("What month are we doing today boys:")
	month = input()
	print("Alright alright alright let's get 'er done")
	
	# This reads and opens the CSV file 
	f = open('LIA.csv', mode='r', encoding='utf-8-sig')
	csv_f = csv.reader(f)
	
	# This iterates through the CSV putting the URL's into a list
	profiles = []
	for row in csv_f:
		profiles.append(str(row[0]))
	
	# Iterates through the list and calls the functions needed for the automation	
	for profile in profiles:
		profile_url = profile
		
		bot = LinkedinBot(username, password, month, profile_url)
		bot.login(username, password)
		bot.profile_connect(month, connect=True)
