import time
from Pages.instantDemoRequestFormPage import InstantDemoRequestFormPage


class EmailFieldValidationTest():
   
    @classmethod
    def __init__(self, driver):
        self.driver = driver
        
    def test_emailFieldValidation(self):
        self.driver.get("https://phptravels.com/demo/")
        instantDemoRequestFrom = InstantDemoRequestFormPage(self.driver)
        
        #here test email field with invalid mail address where @ missing 
        instantDemoRequestFrom.enter_firstName("afra ")
        instantDemoRequestFrom.enter_lastName("anjum")
        instantDemoRequestFrom.enter_businessName("jvy")
        
        #changing data type 
        numOne=int(instantDemoRequestFrom.get_numberOne())
        numTwo=int(instantDemoRequestFrom.get_numberTwo())
        #adding result data
        result= numOne+numTwo
        instantDemoRequestFrom.enter_result(result)
        instantDemoRequestFrom.enter_email("qassdtest.com")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,100)")
        time.sleep(3)
        instantDemoRequestFrom.click_submit()
        time.sleep(3)
        try:
            self.assertNotEqual("Thank you!", instantDemoRequestFrom.get_thankYouword(), "passed did not redirect to thankyou page with invalid mail")
        except:
            print("failed tc-2 : can not submit form with invalid mail but did not show alert")
            
    

        time.sleep(7)
            
        