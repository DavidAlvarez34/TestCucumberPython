from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pom.FlightPage import FlightPage
@when('usuario ingresa al apartado de vuelos')
def step_impl(self):
    self.FlightPage.clickBtnFlight()
    self.driver.implicitly_wait(5)


@when('selecciona la fecha de ida')
def step_impl(self):
    self.FlightPage.selectOnDay()
    time.sleep(2)
@when('selecciona la fecha de vuelta')
def step_impl(self):
    self.FlightPage.selectOnDayReturns()
    time.sleep(2)



@when('selecciona la Business Class')
def step_impl(self):
    self.FlightPage.selectBusneyss()
    time.sleep(2)

@when('click en continuar')
def step_impl(self):
    self.FlightPage.selectContinue()
    time.sleep(5)


@then('compra exitosa')
def step_impl(self):
    self.FlightPage.selectTxtFlight()
    time.sleep(5)
