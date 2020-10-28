"""test_customer.py: unit test python package to execute the unit testing 
in TDD approach"""

import unittest
from app.customer import Customer
from app.region import Region
from app.config import configparam
from app.dq_rules import DQ
from app.dt_rules import DT

class TestCustomer():
    def setup(self,Region):
        self.customer=Customer("XXXX","XXXXX")
        self.config=configparam(Customer)
        self.region=Region("fffff")
    def test_customer_init(self):
        self.assertEqual(self.customer.name,"XXXX")
        self.assertEqual(self.customer.name,"XXXXX")
        self.assertRaises(self.customer.name, "KKKKKKK")
    def test_customer_validaiton(self):
        self.assertEqual(self.customer.dataval1,config.dataval1)
    def test_customer_data_load(self):
        self.assertEqual(self.customer.loadtestingvals,config.loadtestingvals)
    def test_customer_dq(self,Sales):
        """DQ rules test rules if any""" 
        pass
    def test_customer_dt(self,Sales):
        """DT rules test rules if any"""
        pass