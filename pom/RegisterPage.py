from selenium.webdriver.common.by import By
class RegisterPage:
    def __init__(self,driver):
        self.driver = driver
        self.btnRegister =(By.XPATH,"//a[text()='REGISTER']")
        self.txtName = (By.NAME, 'email')
        self.txtPassword = (By.NAME, 'password')
        self.textConfirmPassWord = (By.NAME, 'confirmPassword')
        self.btnSubmit = (By.NAME, 'submit')
        self.title = (By.XPATH,"//b[contains(text(),'Dear  ,')]")


    #Definimos las acciones con los elementos - metodos para mi page
    def clickSecctionRegister(self):
        self.driver.find_element(*self.btnRegister).click()
    def writeInfo(self,name,password,confirPass):
        #self.driver.find_element(*self.txtPass).send_keys(password)
        self.driver.find_element(*self.txtName).send_keys(name)
        self.driver.find_element(*self.txtPassword).send_keys(password)
        self.driver.find_element(*self.textConfirmPassWord).send_keys(confirPass)
    def clickBtnSubmit(self):
        self.driver.find_element(*self.btnSubmit).click()
    def registroExitoso(self):
        #self.driver.find_element(*self.btnSubmit).click()
        #tituloExit = context.driver.title
        # Validacion
        titleSuccess = self.driver.find_element(*self.title).text
        assert titleSuccess  == 'Dear  ,'