from selenium.webdriver.common.by import By
class VacationsPage:
    def __init__(self,driver):
        self.driver = driver
        self.btnSectionVacations =(By.XPATH,"//a[contains(text(),'Vacations')]")
        self.txtName = (By.NAME, 'email')
        self.txtPassword = (By.NAME, 'password')
        self.textConfirmPassWord = (By.NAME, 'confirmPassword')
        self.btnSubmit = (By.NAME, 'submit')
        self.titlePage = (By.XPATH,"//tbody/tr[3]/td[1]/p[1]/font[1]/b[1]/font[1]")


    #Definimos las acciones con los elementos - metodos para mi page
    def clickSecctionVacations(self):
        self.driver.find_element(*self.btnSectionVacations).click()

    def pageVacations(self):
        #self.driver.find_element(*self.btnSubmit).click()
        #tituloExit = context.driver.title
        # Validacion
        titleSuccess = self.driver.find_element(*self.titlePage).text
        print("titleSuccess:_"+titleSuccess+"__")
        assert titleSuccess  == 'This section of our web site is currently under construction.  '
    def registroExitoso(self):
        #self.driver.find_element(*self.btnSubmit).click()
        #tituloExit = context.driver.title
        # Validacion
        titleSuccess = self.driver.find_element(*self.title).text
        assert titleSuccess  == 'Dear  ,'