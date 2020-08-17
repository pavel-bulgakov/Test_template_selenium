from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()
driver.implicitly_wait(6)
driver.find_element(By.XPATH, "//input[@placeholder='First']").send_keys("Pavel")
driver.find_element(By.XPATH, "//input[@placeholder='Last']").send_keys("Bulgakov")
driver.find_element(By.XPATH, "//div//div//div[2]//div[1]//div[1]//input[1]").send_keys("test@gmail.com")
driver.find_element(By.XPATH, "//input[contains(@placeholder,'### ### ####')]").send_keys("5621117722")
driver.find_element(By.XPATH, "//span[contains(text(),'# Product 1')]").click()
driver.find_element(By.XPATH, "//label[@id='radio-0000000e1']//label").click()
driver.find_element(By.XPATH, "//span[contains(text(),'# Product 3')]").click()
driver.find_element(By.XPATH, "//label[@id='radio-0000000e3']//label").click()
driver.find_element(By.XPATH, "//label[@id='radio-0000000e4']//label").click()
driver.find_element(By.XPATH, "//label[@id='radio-0000000e5']//label").click()
driver.find_element(By.XPATH, "//body/form[@id='form']/div/div/div/div/div[1]/div[1]/input[1]").send_keys("2")
driver.find_element(By.XPATH, "//body/form[@id='form']/div/div/div/div/div/div/div[2]").click()
driver.implicitly_wait(4)
driver.find_element(By.XPATH, "//div[contains(@class,'today')]").click()
driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys("7722 reseda blv")
driver.find_element(By.XPATH, "//input[@placeholder='Street Address Line 2']").send_keys("apt 1")
driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys("Los Angeles")
driver.find_element(By.XPATH, "//input[@placeholder='Region']").send_keys("CA")
driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys("94444")
driver.find_element(By.XPATH, "//input[@placeholder='Street Address Line 2']").send_keys("apt 1")
driver.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys("United States")
driver.find_element(By.XPATH, "//form[@id='form']//div//div//div//div//div//div//select")

driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//option[contains(text(),'Choice2')]").click()
driver.find_element(By.XPATH, "//label[@id='checkbox-00000018-0']//label").click()
driver.find_element(By.XPATH, "//label[@id='checkbox-00000018-1']//label").click()
driver.find_element(By.XPATH, "//label[@id='checkbox-00000018-2']//label").click()
driver.find_element(By.XPATH, "//label[@id='checkbox-00000018-3']//label").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//body/form[@id='form']/div/div/div[9]/div[1]/div[4]/div[1]/input[1]").send_keys(" Choice 1 and Choice 3 ")
driver.find_element(By.XPATH, "//body/form[@id='form']/div/div/div[9]/div[1]/div[4]/div[1]/input[1]").click()

frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
driver.switch_to.frame(frame)
driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click()
#https://www.youtube.com/watch?v=fsF7enQY8uI
# driver.quit()



