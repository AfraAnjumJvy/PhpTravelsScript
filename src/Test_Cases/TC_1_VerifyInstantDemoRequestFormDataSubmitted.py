import time
from Pages.instantDemoRequestFormPage import InstantDemoRequestFormPage



class SignUpFormTest():   
    @classmethod
    def __init__(self, driver):
        self.driver = driver
        
    
    def test_fillUpFormValid(self):
       
        # send all data to the form
        instantDemoRequestFrom = InstantDemoRequestFormPage(self.driver)
        instantDemoRequestFrom.enter_firstName("afra ")
        instantDemoRequestFrom.enter_lastName("anjum")
        instantDemoRequestFrom.enter_businessName("jvy")
        instantDemoRequestFrom.enter_email("qa.ssdtest@gmail.com")
   
        #changing data type of validation number
        numOne=int(instantDemoRequestFrom.get_numberOne())
        numTwo=int(instantDemoRequestFrom.get_numberTwo())
        #adding result data
        result= numOne+numTwo
        # sending result data
        instantDemoRequestFrom.enter_result(result)
        time.sleep(9)
        try:
            instantDemoRequestFrom.click_submit()
            time.sleep(9)
        
            assert "Thank you!" in instantDemoRequestFrom.get_thankYouword()
            print("passed Tc-1 : can successfully submitted the form")
        except:
            print("failed Tc-1 : can not successfully submitted the form")
            time.sleep(7)


