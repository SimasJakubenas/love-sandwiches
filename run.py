# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures inut by the user
    """
    while True:
        print('Enter sales data from the last market.')
        print('Data should be 6 numbers separated by commas.')
        print('Example: 11,22,33,44,55,66\n')

        data_str = input('Enter data here: ')
        
        sales_data = data_str.split(',')
        if validate_data(sales_data):
            print('Data is valid!')
            break

    return sales_data

def validate_data(values):
    """
    Checks if all values can be converted to integers and 
    that theres 6 values
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values required. You provided {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}. Please try again.\n')

        return False
    return True

def update_sales_worksheet(data):
  
    """
    Udate sales worksheet , ad new row with list data provided.
    """
    print('Updating sales worksheet...\n')
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('Sales worksheet updated successfully.\n')

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate surplus for each input.

    Surplus isdefined by subracting sales figure from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made once stock sold through
    """
    print('Calculating surplus data...\n')
    stock = SHEET.worksheet('stock').get_all_values()
    pprint(stock)
    stock_row = stock[-1]
    print[stock_row]

def main():
    """
    Run all program function
    """

    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    calculate_surplus_data(sales_data)

print('Welcome to Love Sandwiches dataautomation')
main()