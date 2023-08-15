from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from pom.RegisterPage import RegisterPage


@when('usuario ingresa a la seccion de registro')
def step_impl(self):
    # Localizar el register
    #btnRegister = self.driver.find_element(By.XPATH, "//a[text()='REGISTER']")
    #btnRegister.click()
    self.RegisterPage.clickSecctionRegister()



@when('usuario se registra en userInformation')
def step_impl(self):
    self.RegisterPage.writeInfo("jualian","12345","12345")

@when('click en enviar')
def step_impl(self):
    self.RegisterPage.clickBtnSubmit()
    self.driver.implicitly_wait(30)
@Then('registro exitoso')
def step_impl(self):
    self.RegisterPage.registroExitoso()