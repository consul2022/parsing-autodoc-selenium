from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.autodoc.ru/orders")
lk = driver.find_element(By.XPATH, '//a[@href="javascript:void(0);"]')
lk.click()
auth = driver.find_element(By.XPATH,'//atd-popup[@class="ng-untouched ng-valid ng-dirty"]')
driver.implicitly_wait(2)
Lg = auth.find_element(By.XPATH,'//input[@id="Login"]')
Lg.send_keys("iola-566")
Ps = auth.find_element(By.XPATH,'//input[@id="Password"]')
Ps.send_keys("Qwerty99")
Enter = driver.find_element(By.XPATH,'//button[@id="submit_logon_page"]')
Enter.click()
driver.implicitly_wait(3)
Sl = driver.find_element(By.XPATH,'//p-dropdown[@class="p-element p-inputwrapper p-inputwrapper-filled"]')
Sl.click()
driver.implicitly_wait(10)
Re = driver.find_element(By.XPATH,'//li[@aria-label="Готово к выдаче"]')
Re.click()

time.sleep(600)
driver.quit()






