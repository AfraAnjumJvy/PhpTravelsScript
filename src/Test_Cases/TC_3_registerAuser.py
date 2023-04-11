import time
from Pages.signUpPage import signUpPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random


class RegisterUserTest():
   
    @classmethod
    def __init__(self, driver):
        self.driver = driver
    
    def test_registerAValidUser(self):
            
        self.driver.get("https://phptravels.com/demo/")
        time.sleep(3)
        signUp = signUpPage(self.driver)
        signUp.click_signUp()
        time.sleep(3)
        #self.driver.execute_script("https://phptravels.org/register.php")
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        
        time.sleep(2)
        
        signUp.enter_firstName("afra")
        signUp.enter_lastName("jvy")
        time.sleep(2)
        
        #creating random mail so that can perform multiple signup
        addText = random.randint(1000,9999)
        signUp.enter_email("qa1.ssdtest" + str(addText) + "@gmail.com")  
        signUp.enter_phoneNumber("test" + str(addText))
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,50)")
        signUp.enter_address1("test street1")
        signUp.enter_address2("test street")
        signUp.enter_city("test city")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,50)")
        signUp.enter_state("state test")
        signUp.enter_postCode("123")
        signUp.enter_password("123456")
        signUp.enter_password2("123456")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
        time.sleep(7)
       
        #here switch to iframe for clicking on capcha checkbox
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']/div[@class='recaptcha-checkbox-checkmark']"))))
        #again switch to parent frame
        self.driver.switch_to.parent_frame()
        time.sleep(6)
        try:
            signUp.click_register()  
            time.sleep(8)
        except:
            print("failed tc-3: can not submit form with valid data for capcha validation ")