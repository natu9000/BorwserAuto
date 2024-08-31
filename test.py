from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# driver = webdriver.Chrome(chrome_options=options)

options = Options()
options.add_argument('--ignore-certificate-errors')  
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True

driver = webdriver.Chrome(options=options,desired_capabilities=capabilities)
driver.get('https://www.bing.com/?cc=jp')

search_box = driver.find_element(By.NAME,'q')
search_box.send_keys(1)
search_box.submit()
#time.sleep(3)
search_box.send_keys(1000)
search_box.submit()
#time.sleep(3)

# for i in range(5):
#     search_box.send_keys(i)
#     search_box.submit()
#     #time.sleep(3)

driver.quit()