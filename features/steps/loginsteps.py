from behave import *
from selenium import webdriver
from pom.LoginPage import LoginPage
from pom.RegisterPage import RegisterPage
from pom.FlightPage import FlightPage
from pom.VacationsPage import VacationsPage
@given('usuario ingresa a la pagina demogru')
def irDemoGuru(self):
    #Instanciar driver
    self.driver = webdriver.Chrome()
    #Inicializar el navegador
    self.driver.get('https://demo.guru99.com/test/newtours/')
    self.LoginPage = LoginPage(self.driver)
    self.RegisterPage = RegisterPage(self.driver)
    self.FlightPage = FlightPage(self.driver)
    self.VacationsPage = VacationsPage(self.driver)

@when('usuario ingresa sus credenciales')
def ingresoCredenciales(self):
    self.LoginPage.writeName("user1")
    self.LoginPage.writePass("pass1")
@when('click en submit')
def clickBtnSubmit(self):
    #Localizar el btnSubmit
    self.LoginPage.clickBtnSubmit()
    #btnSubmit = context.driver.find_element(By.NAME,'submit')
    #btnSubmit.click()

@then('logeo exitoso')
def logeoExitoso(context):
    #Obtener el titulo de la pagina
    tituloPagina = context.driver.title
    #Validacion
    assert tituloPagina == "Login: Mercury Tours"
