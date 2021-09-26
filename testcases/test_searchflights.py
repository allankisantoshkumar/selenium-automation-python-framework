import time

import pytest
import softest

from pages.yatra_launch_page import LaunchPage
from utilities.Utils import Utils
from ddt import ddt,data,file_data,unpack


@pytest.mark.usefixtures("setup")
@ddt()
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp=LaunchPage(self.driver)
        self.ut=Utils()
    #@data(("New Delhi","JFK","06/10/2021","1 Stop"),("BOM","JFK","28/10/2021","2 Stop"))
    #@unpack
   # @file_data("../testdata/testdate.json")
    #@file_data("../testdata/testyml.ymal")
    #@data(*Utils.read_data_from_excel("C://Users//Santosh Allanki//PycharmProjects//TestFrameWorkDemo//testdata//tdataexcel.xlsx","Sheet1"))
    @data(*Utils.read_data_from_csv("C:\\Users\\Santosh Allanki\\PycharmProjects\\TestFrameWorkDemo\\testdata\\tdatacsv.csv"))
    @unpack
    def test_search_flights_1_stop(self,goingFrom,goingTo,date,stops):
        search_flight_result=self.lp.searchFlights(goingFrom,goingTo,date)
        self.lp.page_scroll()
        search_flight_result.filter_flights_by_stop(stops)
        allstops=search_flight_result.get_search_flight_results()
        self.log.info(len(allstops))
        self.ut.assertListItemText(allstops,stops)




