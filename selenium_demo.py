from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

opts = Options()
chromium_path = "C:\\Users\\domin\\chrome-win\\chrome.exe"
opts.binary_location = chromium_path
chromedriver_path = Service("C:\\Users\\domin\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opts)
driver = webdriver.Chrome(service=chromedriver_path, options=opts)

driver.get("https://unstats.un.org/bigdata/regional-hubs.cshtml#rwanda")

time.sleep(5)

driver.quit()

# C:\Users\domin\AppData\Local\Temp\ipykernel_21716\3316448015.py:5: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
#  driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opts)
# C:\Users\domin\AppData\Local\Temp\ipykernel_21716\3316448015.py:5: DeprecationWarning: use options instead of chrome_options
#  driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opts)
