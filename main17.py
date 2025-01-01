from selenium import webdriver
#from selenium.webdriver import Keys
#from time import sleep
#import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


file = open("log.txt", "w")
#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option(name='detach', value=True)
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get('http://demoqa.com/buttons')
driver.maximize_window()

double_click_button = driver.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')
right_click_button = driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')
standard_click_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button')

action = ActionChains(driver)

action.double_click(double_click_button).perform()
correct_text = "You have done a double click"
current_text = driver.find_element(By.XPATH, '//*[@id="doubleClickMessage"]')
assert correct_text == current_text.text, 'text not matches'
file.write('text double click matches\n')

action.context_click(right_click_button).perform()
correct_text = "You have done a right click"
current_text = driver.find_element(By.XPATH, '//*[@id="rightClickMessage"]')
assert correct_text == current_text.text, 'text not matches'
file.write('text context click matches\n')

standard_click_button.click()
correct_text = "You have done a dynamic click"
current_text = driver.find_element(By.XPATH, '//*[@id="dynamicClickMessage"]')
assert correct_text == current_text.text, 'text not matches'
file.write('text click button matches\n')
