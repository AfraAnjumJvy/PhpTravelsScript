from selenium.webdriver.common.by import By

class InstantDemoRequestFormPage():
    
    def __init__(self, driver):
        self.driver = driver
        
        
        self.firstName_textbox_name = "first_name"
        self.lastName_textbox_name = "last_name"
        self.businessName_textbox_name = "business_name"
        self.email_textbox_name = "email"
        self.numberOne_textbox_id = "numb1"
        self.numberTwo_textbox_id = "numb2"
        self.result_textbox_id = "number"
        self.submit_button_id = "demo"
        self.thankYou_word_css = "#content > section.grey-box.mt1 > div > div > div:nth-child(2) > div > div > div > div > div > div > div > div.completed > h2 > strong"
        
        
    def enter_firstName(self, firstname):
        self.driver.find_element(By.NAME, self.firstName_textbox_name).clear()
        self.driver.find_element(By.NAME, self.firstName_textbox_name).send_keys(firstname)
        
    def enter_lastName(self, lastname):
        self.driver.find_element(By.NAME, self.lastName_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.lastName_textbox_name ).send_keys(lastname)
            
    def enter_businessName(self, businessname):
        self.driver.find_element(By.NAME, self.businessName_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.businessName_textbox_name ).send_keys(businessname)
        
    def enter_email(self, email):
        self.driver.find_element(By.NAME, self.email_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.email_textbox_name ).send_keys(email)
        
    def get_numberOne(self):
        self.driver.find_element(By.ID, self.numberOne_textbox_id )
        numOne = self.driver.find_element(By.ID, self.numberOne_textbox_id ).get_attribute("innerHTML")
        return numOne
     
       
        
    def get_numberTwo(self):
        
        numberTwo = self.driver.find_element(By.ID, self.numberTwo_textbox_id ).get_attribute("innerHTML")
        return numberTwo
         
        
    def enter_result(self, result):
        self.driver.find_element(By.ID, self.result_textbox_id ).clear()
        self.driver.find_element(By.ID, self.result_textbox_id ).send_keys(result)
    
    def click_submit(self):
        self.driver.find_element(By.ID, self.submit_button_id ).click() 
            
    
    def get_thankYouword(self):
       
        thankYouWord = self.driver.find_element(By.CSS_SELECTOR, self.thankYou_word_css ).get_attribute("innerHTML")
        return thankYouWord
     
   


