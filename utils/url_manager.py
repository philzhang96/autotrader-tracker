import pandas as pd

def remove_sold_urls(input_file="urls.xlsx", output_file="urls.xlsx", sold_urls=None):
    """
    Removes URLs marked as 'SOLD' from the input Excel file.
    
    Args:
        input_file (str): The path to the input Excel file containing URLs.
        output_file (str): The path where the updated Excel file will be saved.
        sold_urls (list of str): The list of URLs to remove from the Excel file.
    """
    if not sold_urls:
        print("No sold URLs provided to remove.")
        return
    
    try:
        # Load the existing URLs from the Excel file
        df = pd.read_excel(input_file)
        
        # Check if the expected column exists
        if "URL" not in df.columns:
            print(f"Column 'URL' not found in {input_file}.")
            return
        
        # Filter out sold URLs
        original_count = len(df)
        df = df[~df["URL"].isin(sold_urls)]
        removed_count = original_count - len(df)
        
        # Save the updated DataFrame back to the Excel file
        df.to_excel(output_file, index=False)
        print(f"Removed {removed_count} sold URLs from {input_file}.")
    
    except Exception as e:
        print(f"Error updating {input_file}: {e}")
