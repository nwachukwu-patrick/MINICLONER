# from pywebcopy.configs import get_config
#
# config = get_config('https://digitalstreamfx.com/?a=login')
# wp = config.create_page()
# # wp.get(config['?a=login'])
# wp.get('https://digitalstreamfx.com/?a=login');
# form = wp.get_forms()[0]
# form.inputs['username'].value = 'admin@digitalstreamfx.com' # etc
# form.inputs['password'].value = '9jXG7l0COMC1' # etc
# wp.submit_form(form)
# print(wp.crawl)


# Used to import the webdriver from selenium
# from selenium import webdriver
# import os
#
#
# # Get the path of chromedriver which you have install
#
# def startBot(username, password, url):
#     path = "C:\\Users\\hp\\Downloads\\chromedriver"
#
#     # giving the path of chromedriver to selenium webdriver
#     driver = webdriver.Chrome(path)
#
#     # opening the website in chrome.
#     driver.get(url)
#
#     # find the id or name or class of
#     # username by inspecting on username input
#     driver.find_element_by_name(
#         "id/class/name of username").send_keys(username)
#
#     # find the password by inspecting on password input
#     driver.find_element_by_name(
#         "id/class/name of password").send_keys(password)
#
#     # click on submit
#     driver.find_element_by_css_selector(
#         "id/class/name/css selector of login button").click()
#
#
# # Driver Code
# # Enter below your login credentials
# username = "admin@digitalstreamfx.com"
# password = "9jXG7l0COMC1"
#
# # URL of the login page of site
# # which you want to automate login.
# url = "Enter the URL of login page of website"
#
# # Call the function
# startBot(username, password, url)


# import requests
#
# login_url = "https://digitalstreamfx.com/?a=login"
# username = "admin@digitalstreamfx.com"
# password = "9jXG7l0COMC1"


from selenium import webdriver

login_url = "https://digitalstreamfx.com/?a=login"
username = "admin@digitalstreamfx.com"
password = "9jXG7l0COMC1"

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get(login_url)

# Find the username and password input fields and enter the login data
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")
username_field.send_keys(username)
password_field.send_keys(password)

# Submit the login form
login_button = driver.find_element_by_xpath("//button[contains(text(), 'Log In')]")
login_button.click()

# Check if the login was successful
if "logged_in" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed.")

# Close the browser
driver.quit()