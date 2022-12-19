from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import js2py

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:8989")
options.add_argument("--user-data-dir=C:\\Users\\SUMUKH\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.add_argument("--profile-directory=Profile 1")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Login Part
# driver.get(url='https://www.chess.com/home')

# Running Scripts
def run_scripts():
    driver.execute_script(js2py.get_file_contents('scripts/clear_highlights.js'))
