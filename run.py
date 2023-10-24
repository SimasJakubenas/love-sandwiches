# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

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
    print('Enter sales data from the last market.')
    print('Data should be 6 numbers separated by commas.')
    print('Example: 11,22,33,44,55,66\n')

    data_str = input('Enter data here: ')
    
    sales_data = data_str.split(',')
    validate_data(sales_data)

def validate_data(values):
    """
    Checks if all values can be converted to integers and 
    that theres 6 values
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values required. You provided {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}. Please try again.\n')

get_sales_data()