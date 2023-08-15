from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from pom.VacationsPage import VacationsPage
import time


@when('usuario ingresa a la seccion de vacaciones')
def step_impl(self):
    self.VacationsPage.clickSecctionVacations()
    time.sleep(2)


@then('revisar vacaciones')
def step_impl(self):
    self.VacationsPage.pageVacations()
    time.sleep(5)