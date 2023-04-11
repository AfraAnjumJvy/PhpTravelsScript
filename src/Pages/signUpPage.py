from selenium.webdriver.common.by import By



class signUpPage():
    
    def __init__(self, driver):
        self.driver = driver
        
        self.signUp_button_name = '//*[@id="loginSignup"]/li[2]/a'
        self.firstName_textbox_name = "firstname"
        self.lastName_textbox_name = "lastname"
        self.email_textbox_name = "email"
        self.phonenumber_textbox_name = "phonenumber"
        self.address1_textbox_name = "address1"
        self.address2_textbox_name = "address2"
        self.city_textbox_name = "city"
        self.state_textbox_name = "state" 
        self.postcode_textbox_name = "postcode"
        self.password_textbox_name = "password"
        self.password2_textbox_name = "password2"
        self.capchaTick_tickBox_id = "#recaptcha-anchor > div.recaptcha-checkbox-checkmark"
        self.register_button_css = '#frmCheckout > p > input'
        
        
    def click_signUp(self):
        self.driver.find_element(By.XPATH, self.signUp_button_name ).click() 
                
    def enter_firstName(self, firstname):
        self.driver.find_element(By.NAME, self.firstName_textbox_name).clear()
        self.driver.find_element(By.NAME, self.firstName_textbox_name).send_keys(firstname)
        
    def enter_lastName(self, lastname):
        self.driver.find_element(By.NAME, self.lastName_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.lastName_textbox_name ).send_keys(lastname)
        
    def enter_email(self, email):
        self.driver.find_element(By.NAME, self.email_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.email_textbox_name ).send_keys(email)
        
    def enter_phoneNumber(self, phnNumber):
        self.driver.find_element(By.NAME, self.phonenumber_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.phonenumber_textbox_name ).send_keys(phnNumber)
        
    def enter_address1(self, address1):
        self.driver.find_element(By.NAME, self.address1_textbox_name).clear()
        self.driver.find_element(By.NAME, self.address1_textbox_name).send_keys(address1)
      
        
    def enter_address2(self, address2):
        self.driver.find_element(By.NAME, self.address2_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.address2_textbox_name).send_keys(address2)
      
    def enter_city(self, city):
        self.driver.find_element(By.NAME, self.city_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.city_textbox_name).send_keys(city)
     
    def enter_state(self, state):
        self.driver.find_element(By.NAME, self.state_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.state_textbox_name).send_keys(state)   
    
    def enter_postCode(self, postCode):
        self.driver.find_element(By.NAME, self.postcode_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.postcode_textbox_name ).send_keys(postCode)   
        
    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name ).send_keys(password)  
        
    def enter_password2(self, password2):
        self.driver.find_element(By.NAME, self.password2_textbox_name ).clear()
        self.driver.find_element(By.NAME, self.password2_textbox_name ).send_keys(password2)  
          
    def click_capchaTick(self):
        
        self.driver.find_element(By.CSS_SELECTOR, self.capchaTick_tickBox_id ).click()
        
    def click_register(self):
        
        self.driver.find_element(By.CSS_SELECTOR, self.register_button_css ).click()
        