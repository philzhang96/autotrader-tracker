import pandas as pd
from datetime import datetime
import os

def export_price_to_excel(data, output_file="car_info.xlsx"):
    """
    Exports only the price data to an Excel file, appending the data to an existing file if it exists.
    If the advert is sold, the price column will display "SOLD".
    
    Args:
        data (list of dict): The data to export, where each dict contains 'URL', 'Price', and other details.
        output_file (str): The path of the output Excel file.
    """
    if not data:
        print("No data to export.")
        return
    
    # Generate the column name for the price using the current date
    date_str = datetime.now().strftime('%d/%m/%Y')
    price_column = f"{date_str}"
    
    # Create a DataFrame with all data, including the price column
    new_data = pd.DataFrame(data)
    
    # If the file exists, merge new price data with existing data
    if os.path.exists(output_file):
        existing_data = pd.read_excel(output_file)
        
        # Prepare a DataFrame with only the URL and the new price column
        price_data = new_data[["URL", "Price"]].rename(columns={"Price": price_column})
        
        # Merge the new price data into the existing data
        combined_data = pd.merge(existing_data, price_data, on="URL", how="left")
    else:
        # If creating a new file, reorder columns to place the price at the rightmost position
        columns = [col for col in new_data.columns if col != "Price"] + ["Price"]
        new_data = new_data[columns].rename(columns={"Price": price_column})
        combined_data = new_data

    # Export the combined data to the Excel file
    combined_data.to_excel(output_file, index=False)
    print(f"Data exported to {output_file}")
