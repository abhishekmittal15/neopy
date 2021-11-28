from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import time 
import datetime
import os 
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains
load_dotenv()

email_id=os.getenv("email_id")
password=os.getenv("password")

class broker():
    def __init__(self):
        """
        Parameters : 
        1. Data dictionary that stores minute data for each of the options, indexed by its name 
        2. Instruments dictionary stores the position of the option ID and the position of the option in the list of options, indexed by option name
        3. index is a variable that starts from 0 and increments after every minute, allows easy access to data
        """
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver=webdriver.Chrome("C:\chromedriver\chromedriver.exe",options=options)
        self.driver.maximize_window()
        self.driver.get("https://neostox.com")
        self.data={}
        self.instruments={}
        self.index=0
        self.make_connection()

    def make_connection(self):
        driver=self.driver
        sign_in=driver.find_element_by_id("ctl00_li_signin")
        sign_in.click()

        time.sleep(1)
        email_id_element=driver.find_element_by_id("txt_emailaddress")
        email_id_element.send_keys(email_id)

        passwd_element=driver.find_element_by_id("txt_password")
        passwd_element.send_keys(password)

        input("Press Enter when you have verified the reCaptcha")

        current_url=driver.current_url
        print(current_url)
        print("Connection Established")
        self.get_options_list()

    def get_options_list(self):
        driver=self.driver
        tab_content=driver.find_element_by_class_name("tab-content")
        tab_home=tab_content.find_element_by_id("home")
        self.list_options=tab_home.find_elements_by_tag_name("a")
        for index,element in enumerate(self.list_options):
            name,value=(element.text).split("\n")
            option_id=((element.get_attribute('id')).split("_"))[1]
            self.instruments[name]=[index,option_id]
            print(name,value,option_id)

    def get_data(self):
        for element in self.list_options:
            name,value=(element.text).split("\n")
            pct_change,price=value.split("%")
            price=float(price)
            option_id=((element.get_attribute('id')).split("_"))[1]
            if name not in self.data.keys():
                self.data[name]=[]
            self.data[name].append(price)
    
    def buy_order(self,instrument_name,qty):
        option_id=self.instruments[instrument_name][1]
        index=self.instruments[instrument_name][0]
        element=self.list_options[index]
        buy_button_id=f"sb_bbtn{option_id}"
        buy_button=element.find_element_by_id(buy_button_id)
        ActionChains(self.driver).move_to_element(element).perform()
        buy_button.click()
        list_links=self.driver.find_elements_by_tag_name('a')
        for link in list_links:
            if(link.get_attribute('class')=="placeorderbutton placeorderbutton_buy"):
                link.click()
                break

    def sell_order(self,instrument_name,qty):
        option_id=self.instruments[instrument_name][1]
        index=self.instruments[instrument_name][0]
        element=self.list_options[index]
        sell_button_id=f"sb_sbtn{option_id}"
        sell_button=element.find_element_by_id(sell_button_id)
        ActionChains(self.driver).move_to_element(element).perform()
        sell_button.click()
        list_links=self.driver.find_elements_by_tag_name('a')
        for link in list_links:
            if(link.get_attribute('class')=="placeorderbutton placeorderbutton_sell"):
                link.click()
                break

    def run(self):
        while True:
            print(f"Before data fetching : {datetime.datetime.now()}")
            self.get_data()
            self.strategy()
            print(f"After strategy calling : {datetime.datetime.now()}")
            print(self.data)
            current_time=datetime.datetime.now()
            while(current_time.second%60<58):
                current_time=datetime.datetime.now()
                time.sleep(1)
            self.index+=1
    

        
                