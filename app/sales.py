"""Sales.py: Sales data load and manage 
in TDD approach"""

import pandas as pd
import SourceConnection
import DestinationConnection
from cusotmer import Customer
from region import Region
from config import configparam
from dq_rules import DQ
from dt_rules import DT
import numpy as np

class Sales(Region,Customer):
    def __init__(self,Customer,Region):
        self.sales=Sales
        self.customer=Customer
        self.region=Region
    def connection_Sales_src(self):
        pass
    def connection_Sales_tgt(self):
        pass
    def dq_Sales(self):
        pass
    def dt_Sales(self):
        pass
    def load_Sales(self):
        """
        load Sales data using pandas
        """
        pass
    def multiple_hist_load(self):
        """
        Data Performace using parallel dataframe partition by month
        """
        permuted_indices = np.random.permutation(len(df))
        for i in range(configparam.N_PARTITIONS):
            dataFrameSales=pd.DataFrame(src,permuted_indices[::i])
            dataFrameCustomer=pd.merge(self.Region.dfform(),self.Customer.dfform(),on="regionID")
            dataFrameFinal=pd.merge(dataFrameSales,dataFrameCustomer,on="customerID")
        pass
        
    def save_Sales(self):
        """
        save the Sales into destinaiton
        """
        pass