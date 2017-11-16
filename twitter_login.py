from selenium import webdriver
from getpass import getpass

usr = input('Ingresa el nombre de usuario o el email: ')
pwd = getpass('Ingresa la contrasena: ')

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

usr_box = driver.find_element_by_id('signin-email')
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_id('signin-password')
pwd_box.send_keys(pwd)

login_button = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--medium.EdgeButton--secondary.flex-table-btn.js-submit')
login_button.submit()
