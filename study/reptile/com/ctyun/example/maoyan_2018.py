from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)

get = driver.get('https://maoyan.com/films?showType=3&yearId=13&offset=0')

