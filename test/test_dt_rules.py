"""test_dt_rules.py: unit test python package to execute the unit testing 
in TDD approach"""
import unittest
from app.dt_rules import DT
from app.config import configparam

class Test_DT():
    def setup(self):
        self.config=configparam()
        self.DT=DT(configparam)
    def test_dt_rules(self,DT):
        """Testing the Set of rules from configparam module"""
        pass
