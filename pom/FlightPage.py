from selenium.webdriver.common.by import By
class FlightPage:
    def __init__(self,driver):
        self.driver = driver
        self.btnFlight =(By.XPATH,"//a[@href='reservation.php' and text()='Flights']")

        self.selectOnMonth = (By.XPATH, "//option[@value='5' ][1]")
        self.selectOnDayReturn = (By.XPATH, "//select[@name='fromDay']/option[@value=31]")

        self.selectMonthReturn = (By.XPATH, "//select[@name='toMonth']/option[@value=6]")
        self.selectDayReturn = (By.XPATH, "//select[@name='toDay']/option[@value=10]")

        self.selectBusness = (By.XPATH,"//input[@name='servClass' and @value='Business']")


        self.btnContinue = (By.XPATH,"//input[@name='findFlights']")

        self.btnSubmit = (By.NAME, 'submit')
        self.title = (By.XPATH,"//b[contains(text(),'Dear  ,')]")

        self.txtFlight = (By.XPATH, "//tbody/tr[1]/td[1]/p[1]/font[1]/b[1]/font[1]")
    #Definimos las acciones con los elementos - metodos para mi page
    def clickBtnFlight(self):
        self.driver.find_element(*self.btnFlight).click()
    def selectOnDay(self):
        #self.driver.find_element(*self.txtPass).send_keys(password)
        self.driver.find_element(*self.selectOnMonth).click()
        self.driver.find_element(*self.selectOnDayReturn).click()
    def selectOnDayReturns(self):
        self.driver.find_element(*self.selectMonthReturn).click()
        self.driver.find_element(*self.selectDayReturn).click()

    def selectBusneyss(self):
        self.driver.find_element(*self.selectBusness).click()
    def selectContinue(self):
        self.driver.find_element(*self.btnContinue).click()
    def selectTxtFlight(self):
        txtFlight = self.driver.find_element(*self.txtFlight).text
        print("Texto-----_"+txtFlight+"___")
        assert txtFlight == "After flight finder - No Seats Avaialble  "