#Question 2: Amazon - https://www.amazon.com/
# Wait for search results to load after performing a search query,
# or wait for product recommendations to appear on the home page.(Both Implicit and explicit wait)

from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# 1. Implicit Wait to search amazon on google.com
driver=webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
st=driver.find_element(By.XPATH,'//*[@class="gLFyf"]')
st.send_keys("amazon")
st.submit()
driver.find_element(By.XPATH,"//h3[contains(text(),'Amazon.in')]").click()
driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]') # in order to move cursor into amazon site
actual=driver.current_url
expected="https://www.amazon.in/"
if(actual==expected):     # to validate the webpage
    print("We are on Amazon site")
else:
    print("Error site")
driver.close()

# 2. Explicit wait on search product in amazon
driver=webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://www.amazon.in/")
    ewait1=WebDriverWait(driver,10)
    driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys("Watch")
    search=ewait1.until(EC.presence_of_element_located((By.XPATH,'//*[@class="nav-right"]')))
    search.click()
except TimeoutException:
    print("Time out")
except ElementNotVisibleException:
    print("element not found")
except ElementNotSelectableException:
    print("element not selected")
finally:
    print("Its working")
#To validate the page
actual1=driver.title
expected1="Amazon.in : Watch"
print(actual1)
if(actual1==expected1):
    print("We are in Watches session")
else:
    print("Error")