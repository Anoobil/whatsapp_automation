from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import os
os.system("C:\eclipse_workspace\phoneapp\phone_calls.py 1")
exit(0)


'''
Tested this script in selenium version 3.141.0 and chromedriver version 2.45
If you will get any exception like Message: unknown error: call function result missing 'value' then it must be driver incompatibility issue, please update your
chromedriver and selenium to latest releases
'''


message_text='Hey, RAKI is busy in work, He will get back to you in next 30mins. Thanks' # message you want to send
no_of_message=1 # no. of time you want the message to be send
moblie_no_list=[917799399904] # list of phone number can be of any length

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\Users\dasarr\AppData\Local\Google\Chrome\User Data") #Path to your chrome profile

driver = webdriver.Chrome(executable_path="C:/Users/dasarr/Downloads/chromedriver_win321/chromedriver.exe", chrome_options=options) #path to Chrome driver installed
#driver = webdriver.Chrome('C:/Users/dasarr/Downloads/chromedriver_win321/chromedriver.exe')
driver.get("https://web.whatsapp.com")
sleep(10) #wait time to scan the code in second

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        print "Finding contact to send message"        
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')        
        global no_of_message        
        for x in range(no_of_message):    
            txt_box.send_keys(text + Keys.ENTER)
            txt_box.send_keys("\n")
            print "Message Sent Successfully"

    except Exception as e:        
        print("invailid phone no :"+str(phone_no))
for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,message_text)
        print "Chrome Browser is closing in 20 secs"
        sleep(20)
        driver.close();

    except Exception as e:
        sleep(10)
        is_connected()