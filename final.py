from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import pyperclip

def copy2clip(txt):
    pyperclip.copy(txt)

# CSV file directory / name
csv_file = "mesajlar.csv"

# Start Chrome WebDriver
option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
driver = webdriver.Chrome(options=option)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("Press enter after you link your device and WhatsApp is raedy...")

# Read CSV file for numbers and massages
with open(csv_file, newline='\n', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile) 
    #reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        phone_number = row[0]  # first column mobile phone number
        message = row[1].replace("\\n", "\n")  # second column message

        # We start chat with user's phone number. 
        # we dont add '&text={message}' at the end of url
        # bcs we need to send message with formatting
        url = f"https://web.whatsapp.com/send?phone={phone_number}"

        driver.get(url)
        
        # Wait for the message box to load. 
        # This will be manuel for the first time as it takes longer. 
        # for the next iterations, script will wait for 12 secs.
        # if it is not enough for your case, you can increase or decrease the time
        if i == 0:
            input("Press ENTER after meeage screen is loaded...")
        else:
            sleep(12)  # Wait for some time to load conversation screen
        # Copy message to clipboard for formatting purposes and then paste it to message box
        copy2clip(message)
        element = driver.switch_to.active_element
    
        # Simulate keyboard shortcut to paste (Ctrl + V)
        element.send_keys(Keys.CONTROL, 'v')
        
        # Click button to send message
        click_btn = driver.find_element(By.CLASS_NAME, 'x1lfpgzf')
        click_btn.click()
        # Wait a short period of time for the next message
        sleep(1)
        print(f"{phone_number}: message has been sent!")

# End driver after all is done
driver.quit()
