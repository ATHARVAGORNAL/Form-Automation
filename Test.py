from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Set up the webdriver (Ensure you have the correct driver installed, e.g., chromedriver)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)  # Implicit wait

# Loop to submit the form 20 times
for i in range(170):
    # Open the Google Form
    driver.get("google form link here")

    # Locate and select multiple-choice answers (Modify XPath as per your form structure)
    try:
        # Finding all multiple-choice question blocks
        question_blocks = driver.find_elements(By.XPATH, "//div[contains(@role, 'radiogroup')]")

        for block in question_blocks:
            options = block.find_elements(By.XPATH, ".//div[@role='radio']")
            if options:
                random.choice(options).click()  # Randomly select an option
                  # Small delay to mimic human behavior

        # Clicking submit
        submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
        submit_button.click()

        print(f"Form submitted successfully! Iteration: {i + 1}")
    except Exception as e:
        print(f"Error filling the form on iteration {i + 1}:", e)

    time.sleep(2)  # Wait before next iteration

# Close the browser after all submissions
driver.quit()
