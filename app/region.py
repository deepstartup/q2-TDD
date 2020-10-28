"""region.py: region data load and manage 
in TDD approach"""

import pandas as pd
import SourceConnection
import DestinationConnection
from config import configparam
from dq_rules import DQ
from dt_rules import DT

class region():
    def __init__(self):
        self.region=region
    def connection_region_src(self):
        pass
    def connection_region_tgt(self):
        pass
    def dq_region(self):
        pass
    def dt_region(self):
        pass
    def load_region(self):
        """
        load region data using pandas
        """
        pass
    def save_region(self):
        """
        save the region into destinaiton
        """
        pass