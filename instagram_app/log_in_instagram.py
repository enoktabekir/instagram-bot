from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

url = 'https://www.instagram.com/accounts/login/'
browser = webdriver.Chrome()

# instagram linkini buradan çekiyoruz
browser.get(url)
time.sleep(3)

#mesaj gönderilecek hesabın kullanıcı adı ve şifresini yazıyoruz
browser.find_element(By.NAME, 'username').send_keys('')
browser.find_element(By.NAME, 'password').send_keys('')

#giriş butonuna tıklıyoruz
login = browser.find_element('xpath', '//*[@id="loginForm"]/div/div[3]/button')
login.click()
time.sleep(3)

#giriş bilgileri kaydedilsin mi
simdi_degil = browser.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
simdi_degil.click()
time.sleep(2)

#bildirimler açılsın mı
simdi_degil_2 = browser.find_element('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
simdi_degil_2.click()
time.sleep(1)

#mesajlara giriş
dm = browser.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/span/div/a')
dm.click()
time.sleep(3)

#yeni mesaj oluşturma
new_message = browser.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div[4]/div')
new_message.click()
time.sleep(3)

#mesaj gönderilecek kullanıcı arama
search = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/input')
search.send_keys('')
time.sleep(3)

#onaylama
tik = browser.find_element('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div[1]/div[1]/div/div/div[3]/div/div')
tik.click()
time.sleep(3)

#sohbete giriş
sohbet = browser.find_element('xpath', '/html/body/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[4]')
sohbet.click()
time.sleep(3)

#mesaj yazdırma
mesaj = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
mesaj.send_keys('bu mesaj bot tarafından gönderilmiştir')
time.sleep(3)

#mesaj gönderme
gonder = browser.find_element('xpath', '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]')
gonder.click()
time.sleep(3)

input("")
browser.quit()