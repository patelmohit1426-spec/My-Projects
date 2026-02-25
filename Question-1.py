from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.browserstack.com/users/sign_up")
driver.maximize_window()

wait = WebDriverWait(driver, 20)

try:
    print("Page loaded successfully")

    full_name = wait.until(
        EC.visibility_of_element_located((By.NAME, "user[full_name]"))
    )
    full_name.send_keys("Patel Mohit Ghanshyambhai")

    email = driver.find_element(By.NAME, "user[email]")
    email.send_keys("24162121020@gmail.com")

    password = driver.find_element(By.NAME, "user[password]")
    password.send_keys("Hello@123")

    checkbox = wait.until(
        EC.element_to_be_clickable((By.ID, "tnc_checkbox"))
    )
    driver.execute_script("arguments[0].click();", checkbox)

    submit = driver.find_element(By.NAME, "commit")
    submit.click()

    print("Form submitted")

except Exception as e:
    print("ERROR OCCURRED 👇")
    print(e)

input("Press ENTER to close browser")
driver.quit()