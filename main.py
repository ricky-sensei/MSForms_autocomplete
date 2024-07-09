from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=ds18TgAtOUqL_UbB9Idi-7ehO5ec8fJBq-V1xyNPYZdUNFlEMlNMOUZXMVg0T04zTDNWT1kyU1VISi4u&origin=QRCode")
time.sleep(3)

element = driver.find_element(by=By.XPATH, value=r'//*[@id="question-list"]/div[1]/div[2]/div/div/div')
element.click()
time.sleep(3)
