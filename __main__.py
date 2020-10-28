"""
main.py code for the program entrypoint
"""
from app import *
from app.region import Region
from app.customer import Customer
from app.sales import Sales
from app.config import configparam

def main():
    try:
        region=Region()
        customer=Customer(region)
        sales=Sales(region,customer)
        pass
    except Exception as e:
        raise e

if __name__ == '__main__':
      main()