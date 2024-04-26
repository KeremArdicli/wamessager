from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import pyperclip

def copy2clip(txt):
    pyperclip.copy(txt)

# CSV dosyasının adı ve yolu
csv_file = "mesajlar.csv"

# Chrome WebDriver'ı başlat
option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
driver = webdriver.Chrome(options=option)

# WhatsApp Web sitesini aç
driver.get("https://web.whatsapp.com/")
input("WhatsApp QR kodunu tarattıktan sonra Enter tuşuna basın...")

# CSV dosyasını oku ve mesajları gönder
with open(csv_file, newline='\n', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile) # Varsayılan olarak virgülle ayrıldığını belirtiyoruz
    #reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        phone_number = row[0]  # İlk sütun telefon numarasını içerir
        message = row[1].replace("\\n", "\n")  # İkinci sütun mesajı içerir

        # WhatsApp mesaj gönderme URL'sini oluştur
        url = f"https://web.whatsapp.com/send?phone={phone_number}"

        # URL'yi aç
        driver.get(url)
        
        if i == 0:
            input("Mesaj göndermek için ENTER'a basın...")
        else:
            sleep(12)  # Yüklenmesini beklemek için biraz zaman ver
        # Gönder butonunu bul ve tıkla
        copy2clip(message)
        element = driver.switch_to.active_element
    
    # Simulate keyboard shortcut to paste (Ctrl + V)
        element.send_keys(Keys.CONTROL, 'v')
        click_btn = driver.find_element(By.CLASS_NAME, 'x1lfpgzf')
        click_btn.click()
        # Bir sonraki mesaj için biraz bekleyelim
        sleep(1)
        print(f"{phone_number} numarasına mesaj gönderildi")

# İşlem tamamlandıktan sonra tarayıcıyı kapat
driver.quit()
