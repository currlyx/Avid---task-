from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(r'./chromedriver_win32/chromedriver.exe')
driver.get("https://avid-recruitment.azurewebsites.net/")
username = driver.find_element(By.ID, 'formUsername')
username.send_keys('admin')
password = driver.find_element(By.ID, 'formPassword')
password.send_keys('testPassword')
submit_btn = driver.find_element(By.ID, 'sign-in-button')
submit_btn.click()
driver.implicitly_wait(15)

expectedLimit=1

limit = driver.find_element(By.ID, 'formLimit')
limit.clear()
limit.send_keys(expectedLimit)
query = driver.find_element(By.ID, 'formQuery')
query.send_keys('copyTest')
put_options_btn = driver.find_element(By.ID, 'buttonOptions')
put_options_btn.click()
try:
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, 'table table-striped table-bordered table-hover')))
except TimeoutException:
    print('Waiting takes a lot of time')
table_xpath = '//table[@class="table table-striped table-bordered table-hover"]//tbody//tr'
table = driver.find_elements(By.XPATH, table_xpath)
print('test limit', len(table))

if len(table) == expectedLimit:
    print('PASS - table length is equal - passed limit') 
else:
    raise ValueError('tabel length is not equal limit')
for row in table:
    cell = row.find_element(By.CLASS_NAME, 'folder-id')
    if cell.text == '10':
        print('PASS - ID is equal 10')
        row.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p#folder-id')))
        folder_header = driver.find_element(By.CSS_SELECTOR, 'p#folder-id')
        if folder_header.text == '10':
            print('PASS - displayed Folder ID is equal 10')
        else: 
            raise ValueError('displayed Folder ID is not equal 10')
    else:
        raise ValueError('search ID = 10 - not found')