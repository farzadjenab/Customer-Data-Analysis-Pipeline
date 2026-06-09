import pyodbc
import pandas as pd
import os

def export_customer_table():
    """
    Connects to SQL Server and exports the SalesLT.Customer table to a CSV file.
    """
    
    # 1. Connection settings derived from your SSMS screenshot
    # Server: 88387-T3G
    # Database: AdventureWorksLT2019
    server = '88387-T3G'
    database = 'AdventureWorksLT2019'
    
    # Connection string using Windows Authentication (Trusted_Connection)
    # Using the standard 'SQL Server' driver
    connection_string = (
        f'DRIVER={{SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )

    # 2. SQL Query and File naming
    query = "SELECT * FROM SalesLT.Customer"
    output_filename = 'customers_export.csv'

    try:
        # Step 1: Connecting to the database
        print(f"Initiating connection to {server}...")
        connection = pyodbc.connect(connection_string)
        
        # Step 2: Extracting data using Pandas
        # This is more efficient for SEO data analysis and large tables
        print("Executing query and fetching data...")
        df = pd.read_sql(query, connection)
        
        # Step 3: Saving data to CSV
        # 'utf-8-sig' ensures compatibility with Excel for special characters
        print(f"Exporting {len(df)} records to {output_filename}...")
        df.to_csv(output_filename, index=False, encoding='utf-8-sig')
        
        # Step 4: Verification
        absolute_path = os.path.abspath(output_filename)
        if os.path.exists(absolute_path):
            print("-" * 30)
            print("EXPORT SUCCESSFUL")
            print(f"File Location: {absolute_path}")
            print("-" * 30)
        
        # Step 5: Resource cleanup
        connection.close()

    except pyodbc.Error as db_error:
        print(f"Database Error: {db_error}")
    except PermissionError:
        print(f"Permission Error: Ensure '{output_filename}' is not open in Excel.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    export_customer_table()
