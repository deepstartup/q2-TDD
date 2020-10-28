"""test_dq_rules.py: unit test python package to execute the unit testing 
in TDD approach"""
import unittest
from app.dq_rules import DQ
from app.config import configparam

class Test_DQ():
    def setup(self):
        self.config=configparam()
        self.DQ=DQ(configparam)
    def test_dq_rules(self,DQ):
        """Testing the Set of rules from configparam module for data quality check"""
        pass
