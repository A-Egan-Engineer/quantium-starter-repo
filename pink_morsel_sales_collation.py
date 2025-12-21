import pandas as pd # Imports Pandas Library for Data Manipulation
import glob # Imports Glob Library for File Pattern Matching

csv_files = glob.glob('data/daily_sales_data_*.csv')  # Accesses All CSV Files in data Folder with daily_sales_data_ Prefix

all_data = pd.DataFrame()  # Initialises Empty DataFrame for Future Data Storage

# pd.set_option('display.max_rows', None)  # Allows Max Rows to be Displayed in Output (Optional)

for file in csv_files:
    data = pd.read_csv(file, index_col='Product', parse_dates=['Date'], delimiter=',')  #Loops Thorugh All CSV Files and Reads into all_data DataFrame
    pink_morsel_data = data.loc[['pink morsel']]  # Filters Data for Pink Morsel Product
    all_data = pd.concat([all_data, pink_morsel_data])  # Appends All Pink Morsel Data to DataFrame

all_data['Date'] = all_data['Date'].dt.strftime('%d-%b-%Y')  # Format Date Column to DD-MMM-YYYY (Australaian Localisation)
all_data['Sales'] = all_data['Price'].str.replace('$', '').astype(float) * all_data['Quantity']  # Sales = Price * Quantity (Float)
all_data['Sales'] = '$' + all_data['Sales'].astype(str)  # Format Sales Column with Dollar Sign and Converts to String

print(all_data[['Sales', 'Date', 'Region']])  # Prints Sales, Date, and Region Columns Only (Terminal Output)

all_data['Sales'] = all_data['Sales'].str.replace('$', '').astype(float)  # Converts Sales Column to Float for .Sum Calculation
total_sales = all_data['Sales'].sum()  # Total Sum of Sales Column
print(f'Total Sales: ${total_sales:,.2f}' + '\n')  # Prints Total Sales Value with Correct Formatting (Terminal Output)

all_data[['Sales', 'Date', 'Region']].to_csv('data\pink_morsel_sales_data.csv', index=False)  # Creates Pink Morsel Sales Summary Single CSV File (Deliverable of Task Two)