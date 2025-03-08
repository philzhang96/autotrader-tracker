import pandas as pd
from datetime import datetime
import os

def export_price_to_excel(data, output_file="car_info.xlsx"):
    if not data:
        print("No data to export.")
        return
    
    date_str = datetime.now().strftime('%d/%m/%Y')
    price_column = f"{date_str}"
    
    new_data = pd.DataFrame(data)
    
    # Ensure the column is correctly named as Mileage
    new_data = new_data.rename(columns={"Miles": "Mileage"})

    if os.path.exists(output_file):
        existing_data = pd.read_excel(output_file)

        # Extract only the static columns from new data
        static_columns = ["URL", "Make", "Mileage", "Registration Year"]
        static_data = new_data[static_columns]

        # Prepare price data with the date as the column name
        price_data = new_data[["URL", "Price"]].rename(columns={"Price": price_column})

        # Keep only URLs that are not already in the existing data
        new_static_data = static_data[~static_data["URL"].isin(existing_data["URL"])]

        # Concatenate the new static data only if it's not already present
        combined_data = pd.concat([existing_data, new_static_data], ignore_index=True)

        # Merge the new price data without duplicating static columns
        combined_data = pd.merge(combined_data, price_data, on="URL", how="left")
    else:
        # First run: keep all columns and initialize the price column
        columns = ["URL", "Make", "Mileage", "Registration Year", "Price"]
        new_data = new_data[columns].rename(columns={"Price": price_column})
        combined_data = new_data

    combined_data.to_excel(output_file, index=False)
    print(f"Data exported to {output_file}")
