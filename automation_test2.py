from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()

try:
    browser.get("https://shop.one-shore.com/index.php")
    search = browser.find_element(By.XPATH, "//*[@id='search_widget']/form/input[2]")
    search.send_keys("Mug")
    search.submit()
    mugs = browser.find_elements(By.XPATH,"//*[@id='js-product-list']/div[1]")
    for mug in mugs:
        print(mug.text)         

except Exception as e:
    print("ERROR OCCURRED 👇")
    print(e)

print("Mugs found successfully! ✅")
print("Check the browser for results. 👀")

input("Press ENTER to close browser")
browser.quit()
