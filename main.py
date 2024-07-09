from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

xpath_dict = {
    "１問目": r'//*[@id="question-list"]/div[1]/div[2]/div/div/div',
    "八幡平市": r"/html/body/div[2]/div/div[2]",
    "2問目": r'//*[@id="question-list"]/div[2]/div[2]/div/div/div',
    "大更小学校": r"/html/body/div[2]/div/div[1]",
    "三問目": r'//*[@id="question-list"]/div[3]/div[2]/div/div/div',
    "一年生": r"/html/body/div[2]/div/div[1]",
    "二年生": r"/html/body/div[2]/div/div[2]",
    "４問目": r'//*[@id="question-list"]/div[4]/div[2]/div/div/div',
    "1組": r"/html/body/div[2]/div/div[1]",
    "２組": r"/html/body/div[2]/div/div[2]",
    "5問目": r'//*[@id="question-list"]/div[5]/div[2]/div/div/div',
    "出席番号": '//*[text()=\"1\"]',
    "６問目": r'//*[@id="question-list"]/div[6]/div[2]/div/div/div',
    "男": r"/html/body/div[2]/div/div[1]",
    "女": r"/html/body/div[2]/div/div[2]",
    "７問目": r'//*[@id="question-list"]/div[7]/div[2]/div/div/div',
    "すき": r"/html/body/div[2]/div/div[1]",
    "８－１": '//*[@id="question-list"]/div[8]/div[2]/div/table/tbody/tr[1]/td[1]/div/label/span/input',    "８－２": '//*[@id="question-list"]/div[8]/div[2]/div/table/tbody/tr[2]/td[1]/div/label/span/input',
    "９－１": '//*[@id="question-list"]/div[9]/div[2]/div/table/tbody/tr[1]/td[1]/div/label/span/input',
    "９－２": '//*[@id="question-list"]/div[9]/div[2]/div/table/tbody/tr[2]/td[1]/div/label/span/input',
    "１０－１": '//*[@id="question-list"]/div[10]/div[2]/div/table/tbody/tr[1]/td[1]/div/label/span/input',
    "１０－２": '//*[@id="question-list"]/div[10]/div[2]/div/table/tbody/tr[2]/td[1]/div/label/span/input',
    "１０－３": '//*[@id="question-list"]/div[10]/div[2]/div/table/tbody/tr[3]/td[1]/div/label/span/input',
    "１１問目": '//*[@id="question-list"]/div[11]/div[2]/div/div/div',
    "運動": "/html/body/div[2]/div/div[1]/span[2]/span",
    "送信": '//*[@id="form-main-content1"]/div/div/div[2]/div[3]/div/button',
}


def set_element_and_click(xpath):
    # try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()
    time.sleep(0.5)
    # except Exception as e:
    #     print(f"exception{e}")


def select_radio_button_and_sleep(xpath):
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(0.5)


def main():
    for i in range(1, 30):
        xpath_dict["出席番号"] = f'//*[text()=\"{i}\"]'
        driver.get(
            "https://forms.office.com/Pages/ResponsePage.aspx?id=ds18TgAtOUqL_UbB9Idi-7ehO5ec8fJBq-V1xyNPYZdUNFlEMlNMOUZXMVg0T04zTDNWT1kyU1VISi4u&origin=QRCode"
        )
        time.sleep(3)
        set_element_and_click(xpath_dict["１問目"])
        set_element_and_click(xpath_dict["八幡平市"])
        set_element_and_click(xpath_dict["2問目"])
        set_element_and_click(xpath_dict["大更小学校"])
        set_element_and_click(xpath_dict["三問目"])
        set_element_and_click(xpath_dict["一年生"])
        set_element_and_click(xpath_dict["４問目"])
        set_element_and_click(xpath_dict["1組"])
        set_element_and_click(xpath_dict["5問目"])
        set_element_and_click(xpath_dict["出席番号"])
        set_element_and_click(xpath_dict["６問目"])

        set_element_and_click(xpath_dict["男"])
        set_element_and_click(xpath_dict["７問目"])
        set_element_and_click(xpath_dict["すき"])
        select_radio_button_and_sleep(xpath_dict["８－１"])
        select_radio_button_and_sleep(xpath_dict["８－２"])
        select_radio_button_and_sleep(xpath_dict["９－１"])
        select_radio_button_and_sleep(xpath_dict["９－２"])
        select_radio_button_and_sleep(xpath_dict["１０－１"])
        select_radio_button_and_sleep(xpath_dict["１０－２"])
        select_radio_button_and_sleep(xpath_dict["１０－３"])
        select_radio_button_and_sleep(xpath_dict["１１問目"])
        set_element_and_click(xpath_dict["運動"])
        select_radio_button_and_sleep(xpath_dict["送信"])
        time.sleep(5)


if __name__ == "__main__":
    main()
