import pandas as pd

def export_to_excel(data, output_file="car_info.xlsx"):
    """
    Exports the scraped data to an Excel file.
    
    Args:
        data (list of dict): The data to export, where each dict is a row.
        output_file (str): The path of the output Excel file.
    """
    if not data:
        print("No data to export.")
        return
    
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"Data exported to {output_file}")
