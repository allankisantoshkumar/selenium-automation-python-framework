import time
import logging

from selenium.webdriver.common.by import By

from utilities.Utils import Utils

from base.base_driver import BaseDriver


class SearchFlightResult(BaseDriver):
    log=Utils.custom_logger(loglevel=logging.WARNING)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        #self.wait=wait

    #Locators
    FILTER_BY_1_STOP_ICON="//p[@class='font-lightgrey bold' and text()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold' and text()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold' and text()='0']"
    SEARCH_FLIGHT_RESULT="//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"

    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH,self.FILTER_BY_1_STOP_ICON)
    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH,self.FILTER_BY_2_STOP_ICON)
    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH,self.FILTER_BY_NON_STOP_ICON)
    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.SEARCH_FLIGHT_RESULT)


    def filter_flights_by_stop(self,by_stop):
        if by_stop =="1 Stop":
            self.get_filter_by_one_stop_icon().click()
            self.log.warning("selected flight with  one  stop")
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            self.log.warning("selected flight with  two  stop")
            time.sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click()
            self.log.warning("selected flight with  non  stop")
            time.sleep(2)
        else:
            self.log.warning("please provide valid opitions")
















