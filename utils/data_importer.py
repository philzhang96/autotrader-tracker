import pandas as pd

def read_urls_from_excel(input_file="urls.xlsx", column_name="URL"):
    """
    Reads a list of URLs from an Excel file.
    
    Args:
        input_file (str): The path to the Excel file containing URLs.
        column_name (str): The name of the column with URLs.
        
    Returns:
        list: A list of URLs from the specified column.
    """
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(input_file)
        
        # Check if the expected column exists
        if column_name not in df.columns:
            print(f"Column '{column_name}' not found in the Excel file.")
            return []
        
        # Extract the column as a list and drop any empty values
        urls = df[column_name].dropna().tolist()
        print(f"Loaded {len(urls)} URLs from {input_file}.")
        return urls
    
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return []
