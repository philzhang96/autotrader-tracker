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
    
    # Ensure consistency in column naming
    new_data = new_data.rename(columns={"Miles": "Mileage"})

    static_columns = ["URL", "Make", "Mileage", "Registration Year"]
    
    # Extract only relevant static data
    static_data = new_data[static_columns].drop_duplicates()

    # Extract only price data
    price_data = new_data[["URL", "Price"]].rename(columns={"Price": price_column})

    if os.path.exists(output_file):
        try:
            existing_data = pd.read_excel(output_file)

            # Drop fully empty rows to avoid pandas warning
            existing_data = existing_data.dropna(how="all")

            # Ensure "URL" column exists for merging
            if "URL" not in existing_data.columns:
                existing_data["URL"] = None  # Ensures proper merge

            # Merge price updates with existing data
            combined_data = pd.merge(existing_data, price_data, on="URL", how="left")

            # Identify new URLs not in existing data
            new_static_data = static_data[~static_data["URL"].isin(existing_data["URL"])]

            if not new_static_data.empty:
                combined_data = pd.concat([combined_data, new_static_data], ignore_index=True)

        except Exception as e:
            print(f"Error reading {output_file}: {e}")
            combined_data = static_data  # Fallback: start fresh if file is corrupt

    else:
        # If file does not exist, create from scratch
        new_data = new_data[static_columns + ["Price"]].rename(columns={"Price": price_column})
        combined_data = new_data

    try:
        # Save the final DataFrame to Excel
        combined_data.to_excel(output_file, index=False)
        print(f"Data successfully exported to {output_file}")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")
