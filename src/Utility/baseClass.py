from selenium import webdriver
import time
from Test_Cases.TC_1_VerifyInstantDemoRequestFormDataSubmitted import SignUpFormTest
from Test_Cases.TC_2_emailValidation import EmailFieldValidationTest
from Test_Cases.TC_3_registerAuser import RegisterUserTest




chromePath= "./Driver/chromedriver.exe"    
driver =webdriver.Chrome(executable_path=chromePath)
driver.maximize_window()
time.sleep(2)
base_url= "https://phptravels.com/demo/"

def set_up():
    driver.get(base_url)
    time.sleep(5)
    
def test_Tc_1():
    tcOne= SignUpFormTest(driver) 
    tcOne.test_fillUpFormValid()
    
def test_Tc_2():
    tcTwo= EmailFieldValidationTest(driver)
    tcTwo.test_emailFieldValidation()

def test_Tc_3():
    tcThree= RegisterUserTest(driver)
    tcThree.test_registerAValidUser()
    
    
set_up()
test_Tc_1()
test_Tc_2()
test_Tc_3()