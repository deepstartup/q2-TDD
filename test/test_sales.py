"""test_sales.py: unit test python package to execute the unit testing 
in TDD approach"""

import unittest
from app.region import Region
from app.customer import Customer
from app.sales import Sales
from app.config import configparam
from app.dq_rules import DQ
from app.dt_rules import DT

class TestSales():
    def setup(self):
        self.region=Region("virginia","north carolina")
        self.customer=Customer("XXXX","XXXXX")
        self.config=configparam(Sales)
        self.Sales=Sales(Region,Customer)
    def test_region_init(self,Sales,Region):
        self.assertEqual(self.sales.region.name,"virginia")
        self.assertEqual(self.sales.region.name,"north carolina")
        self.assertRaises(self.sales.region.name, "XXXXX")
    def test_customer_init(self,Sales,Customer):
        self.assertEqual(self.sales.customer.name,"XXXX")
        self.assertEqual(self.sales.customer.name,"XXXXX")
        self.assertRaises(self.sales.customer.name, "KKKKKKK")
    def test_sales_validaiton(self,Sales):
        self.assertEqual(self.sales.dataval1,config.dataval1)
        pass
    def test_sales_data_load(self):
        self.assertEqual(self.sales.loadtestingvals,config.loadtestingvals)
        pass
    def test_sales_dq(self,Sales):
        """DQ rules test rules if any""" 
        pass
    def test_sales_dt(self,Sales):
        """DT rules test rules if any"""
        pass