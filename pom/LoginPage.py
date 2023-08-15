from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.txtUserName = (By.NAME,'userName')
        self.txtPass = (By.NAME,'password')
        self.btnSubmit =(By.NAME,'submit')

    #Definimos las acciones con los elementos - metodos para mi page
    def writeName(self,username):
        self.driver.find_element(*self.txtUserName).send_keys(username)
    def writePass(self,password):
        self.driver.find_element(*self.txtPass).send_keys(password)

    def clickBtnSubmit(self):
        self.driver.find_element(*self.btnSubmit).click()

