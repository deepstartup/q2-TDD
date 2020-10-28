"""test_region.py: unit test python package to execute the unit testing 
in TDD approach"""

import unittest
from app.region import Region
from app.config import configparam
from app.dq_rules import DQ
from app.dt_rules import DT

class TestRegion():
    def setup(self):
        self.region=Region("virginia","north carolina")
        self.config=configparam(Region)
    def test_region_init(self):
        self.assertEqual(self.region.name,"virginia")
        self.assertEqual(self.region.name,"north carolina")
        self.assertRaises(self.region.name, "XXXXX")
    def test_region_validaiton(self):
        self.assertEqual(self.region.dataval1,config.dataval1)
    def test_region_data_load(self):
        self.assertEqual(self.region.loadtestingvals,config.loadtestingvals)
    def test_region_dq(self,Sales):
        """DQ rules test rules if any""" 
        pass
    def test_region_dt(self,Sales):
        """DT rules test rules if any"""
        pass