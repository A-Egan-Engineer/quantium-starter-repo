# Imports Pandas Library for Data Manipulation
import pandas as pd 
# Imports Glob Library for File Pattern Matching
import glob as gl

# Accesses All CSV Files in data Folder with daily_sales_data_ Prefix
csv_files = gl.glob('data/daily_sales_data_*.csv')  

# Initialises Empty DataFrame for Future Data Storage
all_data = pd.DataFrame()

# Allows Max Rows to be Displayed in Terminal Output (Optional)
# pd.set_option('display.max_rows', None)  

for file in csv_files:
    #Loops Thorugh All CSV Files and Reads into all_data DataFrame
    data = pd.read_csv(file, index_col='Product', parse_dates=['Date'], delimiter=',')  
    # Filters Data for Pink Morsel Product
    pink_morsel_data = data.loc[['pink morsel']]  
    # Appends All Pink Morsel Data to DataFrame
    all_data = pd.concat([all_data, pink_morsel_data])  

# Format Date Column to DD-MMM-YYYY (Australaian Localisation)
all_data['Date'] = all_data['Date'].dt.strftime('%d-%b-%Y')  
# Sales = Price * Quantity (Float)
all_data['Sales'] = all_data['Price'].str.replace('$', '').astype(float) * all_data['Quantity']  
# Format Sales Column with Dollar Sign and Converts to String
all_data['Sales'] = '$' + all_data['Sales'].astype(str)  

# Prints Sales, Date, and Region Columns Only (Terminal Output)
print(all_data[['Sales', 'Date', 'Region']])  

# Converts Sales Column to Float for .Sum Calculation
all_data['Sales'] = all_data['Sales'].str.replace('$', '').astype(float)  
# Total Sum of Sales Column
total_sales = all_data['Sales'].sum()  
# Prints Total Sales Value with Correct Formatting (Terminal Output)
print(f'Total Sales: ${total_sales:,.2f}' + '\n')  

# Creates Pink Morsel Sales Summary Single CSV File (Deliverable of Task Two)
all_data[['Sales', 'Date', 'Region']].to_csv('data\pink_morsel_sales_data.csv', index=False)  