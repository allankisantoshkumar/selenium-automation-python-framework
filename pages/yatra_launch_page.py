import time

from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By



from base.base_driver import BaseDriver
from pages.search_flights_result_page import SearchFlightResult
from utilities.Utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
       # self.wait=wait

    #Locators
    DEPART_FROM_FIELD="//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD="//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST="//div[@class='viewport']//div[1]//li"
    SELECT_DATE_FIELD="//input[@id='BE_flight_origin_date']"
    ALL_DATES="//*[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON="//input[@value='Search Flights']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResult(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.GOING_TO_RESULT_LIST)

    def getDepatureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def  getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH,self.SEARCH_BUTTON)

    def  enterDepartFromLocation(self,departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enterGoingToLocation(self,goingToLocation):
        self.getGoingToField().click()
        self.log.info("Clicked on going to")
        time.sleep(2)
        self.getGoingToField().send_keys(goingToLocation)
        self.log.info("Typed text into going to filed successfully")
        time.sleep(2)
        search_results=self.getGoingToResult()
        for results in search_results:
            if goingToLocation in results.text:
                results.click()
                break

    def enterDepatureDate(self,departureDate):
        self.getDepatureDateField().click()
        alldates=self.getAllDatesField().find_elements(By.XPATH,self.ALL_DATES)
        for date in alldates:
            if date.get_attribute("data-date") == departureDate:
                date.click()
                break

    def clickSearchFlightsButton(self):
        self.getSearchButton().click()
        time.sleep(4)

    def searchFlights(self,departlocation,goingtolocation,depaturedate):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepatureDate(depaturedate)
        self.clickSearchFlightsButton()
        search_flight_result = SearchFlightResult(self.driver)
        return search_flight_result

