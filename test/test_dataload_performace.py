"""test_dataload_performace.py: unit test python package to execute the unit testing 
in TDD approach"""

import unittest
import time
from app.region import Region
from app.customer import Customer
from app.sales import Sales
from app.config import configparam
from .test_sales import TestSales
from .test_region import TestRegion
from .test_customer import TestCustomer


start_time = time.time()
class TestPerformance():
    def setup(self):
        self.region=Region("virginia","north carolina")
        self.customer=Customer("XXXX","XXXXX")
        self.config=configparam(Sales)
        self.Sales=Sales(Region,Customer)
        self.test_sales=TestSales()
        self.test_resion=TestRegion()
        self.test_customer=TestCustomer()
    def test_performace_sales(self,test_sales):
        """Basic operation performance test and load test on sales
        """
        start_time = time.time()
        test_sales(self.test_resion,self.test_customer)
        return time.time()-start_time
        pass
    def test_performace_customer(self,test_customer):
        """Basic operation performance test and load test on customer
        """
        start_time = time.time()
        test_customer(self.test_customer)
        return time.time()-start_time
        pass
    