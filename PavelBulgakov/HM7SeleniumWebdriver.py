import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#импортирую все используемые модули


class ChromeTest(unittest.TestCase):  #создаю класс для теста Хрома

    def setUp(self):
        self.driver = webdriver.Chrome(). #указываю используемый далее драйвер 

    def test_chrome(self):  #создаю тест для хрома внутри класса(обязательно название должно начинаться со слова test и маленькими буквами.
        #также они будут запускаться в алфавитном порядке,то есть если называть следующий тест,то по алфавиту дальше. 1-9 в селениуме сначала,потом буквы
        driver_chrome = self.driver
        driver_chrome.get("https://qasvus.wordpress.com")
        driver_chrome.maximize_window()
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)

        assert "California Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

        search_name = driver_chrome.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_name.send_keys("Pavel Bulgakov")
        search_email = driver_chrome.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_email.send_keys("pavelpavelb@gmail.com")
        search_message = driver_chrome.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_message.clear()
        search_message.send_keys(
            "This my first CrossBrowser test")
        driver_chrome.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_chrome.implicitly_wait(4)

        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2)

        driver_chrome.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
        driver_chrome.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        driver_chrome.implicitly_wait(4)

        assert "California Real Estate" in driver_chrome.title
        print("After clicking 'Go back' button we're back to the right page:", driver_chrome.title)
        time.sleep(1)

    def test_chrome_1120x550(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 550)
        driver_chrome.get("https://qasvus.wordpress.com")
        wait = WebDriverWait(driver_chrome, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)

        assert "California Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

        search_name = driver_chrome.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_email = driver_chrome.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_message = driver_chrome.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_message.clear()
        driver_chrome.find_element(By.XPATH, "//input[@id='g2-name']").send_keys("Pavel Bulgakov")
        driver_chrome.find_element(By.XPATH, "//input[@id='g2-email']").send_keys("pavelpavelb@gmail.com")
        driver_chrome.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys(
            "This my first CrossBrowser test")
        driver_chrome.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_chrome.implicitly_wait(4)
        
        html = driver_chrome.find_element_by_tag_name('html') #созадаю переменную html которая приравнивается ,странице html как целый элемент

        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        # у меня маленький экран на ноутбуке и для того чтобы элемент был в окошке,надо пролистать его вверх

        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2)

        html.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))
        driver_chrome.implicitly_wait(4)

        assert "California Real Estate" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)
        time.sleep(1)

        assert "California Real Estate" in driver_chrome.title
        print("After clicking 'Go back' button we're back to the right page:", driver_chrome.title)
        time.sleep(1)

    def tearDown(self):         #обязательно закрыть за собой браузер этим методом,так делается закрытие class через def tearDown(self)
        self.driver.quit()


class FireFoxTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_fire_fox(self):
        driver_firefox = self.driver
        driver_firefox.get("https://qasvus.wordpress.com")
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)

        assert "California Real Estate" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)
        time.sleep(1)

        search_name = driver_firefox.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_name.send_keys("Pavel Bulgakov")
        search_email = driver_firefox.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_email.send_keys("pavelpavelb@gmail.com")
        search_message = driver_firefox.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_message.clear()
        search_message.send_keys(
            "This my first CrossBrowser test")
        driver_firefox.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_firefox.implicitly_wait(4)

        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2)

        driver_firefox.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
        driver_firefox.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        assert "California Real Estate" in driver_firefox.title
        print("After clicking 'Go back' button we're back to the right page:", driver_firefox.title)
        time.sleep(1)

    def test_fire_fox_default_1250x850_window(self):
        driver_firefox = self.driver
        driver_firefox.get("https://qasvus.wordpress.com")
        driver_firefox.set_window_size(1250, 850)
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)

        assert "California Real Estate" in driver_firefox.title
        print("Page title in Chrome is:", driver_firefox.title)
        time.sleep(1)

        search_name = driver_firefox.find_element_by_xpath("//input[@id='g2-name']")
        search_name.clear()
        search_name.send_keys("Pavel Bulgakov")
        search_email = driver_firefox.find_element_by_xpath("//input[@id='g2-email']")
        search_email.clear()
        search_email.send_keys("pavelpavelb@gmail.com")
        search_message = driver_firefox.find_element_by_xpath("//textarea[@id='contact-form-comment-g2-message']")
        search_message.clear()
        search_message.send_keys(
            "This my first CrossBrowser test")
        driver_firefox.find_element(By.ID, "contact-form-comment-g2-message").submit()
        driver_firefox.implicitly_wait(4)

        html = driver_firefox.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        html.send_keys(Keys.PAGE_UP)
        try:
            wait.until(
                (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]"))))
            print("'Go back' button is visible ")
        except ElementNotVisibleException:
            print("'Go back' button is invisible ")
            time.sleep(2)

        driver_firefox.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
        driver_firefox.implicitly_wait(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        assert "California Real Estate" in driver_firefox.title
        print("After clicking 'Go back' button we're back to the right page:", driver_firefox.title)
        time.sleep(1)

    def tearDown(self):  #обязательно закрыть за собой браузер этим методом,так делается закрытие class через def tearDown(self)
        self.driver.quit()
