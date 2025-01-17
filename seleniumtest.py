from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Provide the path to ChromeDriver if not added to PATH
service = Service(r"C:\Windows\chromedriver-win64\chromedriver.exe")

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.google.com")

# Print the page title
print(driver.title)

# Close the browser
driver.quit()