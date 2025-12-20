import pandas # Imports Pandas Library for Data Analysis

data = pandas.read_csv('data/daily_sales_data_0.csv', index_col='Product', parse_dates=['Date'], delimiter=',') # Reads the CSV file, Sets Product as Index, Parses Date Col as DateTime & Specifies Delimiter

data = data.loc[['pink morsel']] # Filters Data to Display 'Pink Morsel' Product Only

data['Date'] = data['Date'].dt.strftime('%d-%b-%Y') # Formats Date Col to 'DD-MMM-YYYY' Format (Localisation for Australia)

data['Sales'] = data['Price'].str.replace('$', '').astype(float) * data['Quantity'] # Operation to Multiply Price & Quantity = Sales
data['Sales'] = '$' + data['Sales'].astype(str) # Formats Sales Col to Include $, Converts Sales to Type String for Data Display

pandas.set_option('display.max_rows', None) # Allows Max Rows to be Displayed in Output

print(data[['Sales', 'Date', 'Region']]) # Displays Sales, Date & Region Columns Only in Output

data['Sales'] = data['Sales'].str.replace('$', '').astype(float) # Converts Sales Col to Float for Calculation of Total Sales
total_sales = data['Sales'].sum() # Sum of Sales Col = Total Sales
print(f'Total Sales: ${total_sales:,.2f}' + '\n') # Prints Total Sales with $, Commas & 2 Decimal Places Format (Readability)