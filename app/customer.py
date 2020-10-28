"""customer.py: customer data load and manage 
in TDD approach"""

import pandas as pd
import SourceConnection
import DestinationConnection
from config import configparam
from region import Region
from dq_rules import DQ
from dt_rules import DT

class Customer():
    def __init__(self,Region):
        self.customer=Customer
        self.region=Region
    def connection_customer_src(self):
        pass
    def connection_customer_tgt(self):
        pass
    def dq_customer(self):
        pass
    def dt_customer(self):
        pass
    def load_customer(self):
        """
        load customer data using pandas
        """
        pass
    def save_customer(self):
        """
        save the customer into destinaiton
        """
        pass