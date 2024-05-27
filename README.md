# Automated WhatsApp Messager

## This small script helps you send automated WhatsApp messages to the list of numbers.

### Create a csv file with phone numbers an messages, send personalized messages to your contact list.

- Dependencies:
    - Google Chrome should be installed on your machine 
    - selenium
    - webdriver-manager
    - pyperclip

### Usage
- Webdriver will open a chrome window with web.whatsapp.com
- Once page is open you need to scan QR code to link your device.
- After you link your device and the WhatsApp page is ready to use, click ENTER. Script will wait for your prompt as this process duration can vary significantly from user to user. this will be done once for each use of the script.
- Once ENTER is pressed, script will iterate through the CSV lines.
- For the first message, script will ask you to press ENTER again. This is to make sure conversation screenşs loaded. For the next messages, script will wait for 12 sec and send automatically.
- You can change 12 sec in the codes.
- Every successful message will be printed on the console.
- Once all is done, driver will quit itself.