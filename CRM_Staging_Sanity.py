import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://staging-crm.buyani.com/crm")

#Variables
username = "seoaperina"
password = "Cumbria2021!"
newcustomer_lastname = "Sanity Test"
newcustomer_firstname = "010524"
newcustomer_contactnumber = "09123456789"
newcustomer_middlename = "CRI"
newcustomer_emailaddress = (f"{newcustomer_firstname}{newcustomer_middlename}@cumbriaridge.com")
editcustomer_BAMIDate = (f"{newcustomer_firstname}")
ticketclassification = "Sanity Test"

#Login


uname = driver.find_element("xpath", '/html/body/div/div/div/form/div[1]/input')
uname.send_keys(username)
pw = driver.find_element("xpath", '/html/body/div/div/div/form/div[2]/input')
pw.send_keys(password)
login = driver.find_element("xpath", '/html/body/div/div/div/form/button')
login.click()
time.sleep(3)

#Team Selection
team = driver.find_element("xpath", '//*[@id="navbarSupportedContent"]/div/div/div/div[2]/button')
team.click()
Saricasa_team = driver.find_element("xpath", '//*[@id="bs-select-1-13"]/span')
Saricasa_team.click()
time.sleep(3)

#Customer Module - Creation of New Customer
customer = driver.find_element("xpath", '/html/body/div[1]/nav/div/div/div[2]/div/ul/li[6]/a/span')
customer.click()
new_customer = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/a')
new_customer.click()
new_lastname = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[1]/div[1]/div/div[1]/div[1]/div/input')
new_lastname.send_keys(newcustomer_lastname)
new_firstname = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[1]/div[1]/div/div[1]/div[3]/div/input')
new_firstname.send_keys(newcustomer_firstname)
new_middlename = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[1]/div[1]/div/div[1]/div[4]/div/input')
new_middlename.send_keys(newcustomer_middlename)
new_contact = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[1]/div[1]/div/div[3]/div[2]/div/input')
new_contact.send_keys(newcustomer_contactnumber)
new_email = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[1]/div[1]/div/div[3]/div[1]/div/input')
new_email.send_keys(newcustomer_emailaddress)
submit_newcustomer = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[3]/div[2]/button')
submit_newcustomer.click()
time.sleep(5)

#Customer Module - Edit Existing Customer
edit_existingcustomer = driver.find_element("xpath", '//*[@id="TableRecord"]/div[1]/table/tbody/tr[3]/td[1]/a')
edit_existingcustomer.click()
edit_existingcustomer_BAMIDate = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[1]/div[1]/div/div[4]/div[12]/div/input')
edit_existingcustomer_BAMIDate.send_keys(editcustomer_BAMIDate)
edit_existingcustomer_update = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[3]/div[2]/button')
edit_existingcustomer_update.click()

#Customer Module - Create New Ticket via Ticket History Tab
create_ticket_TicketHistoryTab = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/nav/div/a[6]')
create_ticket_TicketHistoryTab.click()
time.sleep(2)
create_ticket_Button = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/form/div[1]/div[6]/div/div[1]/a')
create_ticket_Button.click()
create_ticket_Classification = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/form/div/div[2]/nav/div/a[3]')
create_ticket_Classification.click()
time.sleep(2)
create_ticket_TicketClassification = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/form/div/div[2]/div[3]/div[3]/div/div[1]/input')
create_ticket_TicketClassification.send_keys(ticketclassification)
pyautogui.press('enter')
create_ticket_Save = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/form/div/div[2]/div[5]/div[2]/button')
create_ticket_Save.click()

#Ticket Module - Create New Ticket
ticket = driver.find_element("xpath", '//*[@id="sidenav-collapse-main"]/ul/li[7]/a/span')
ticket.click()
new_ticket = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div[1]/a')
new_ticket.click()
time.sleep(1)
new_ticket_customername = driver.find_element("xpath", '/html/body/div[1]/div/div[2]/div[1]/div[1]/form/div/div[1]/input')
new_ticket_customername.send_keys(newcustomer_lastname)
time.sleep(5)
new_ticket_customername_select = driver.find_element("xpath", '/html/body/ul[1]/li[1]/div')
new_ticket_customername_select.click()






