from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options = opts)


url1 = r'https://www.kabum.com.br/'
navegador.get(url1)
precos = []
# Preço do primeiro notebook (Dell)
pesquisar_dell = navegador.find_element(By.ID, "input-busca")
pesquisar_dell.send_keys("Dell G15")
sleep(2)
pesquisar_dell.send_keys(Keys.RETURN)
preco1 = navegador.find_element(By.XPATH, "//span[contains(@class,'sc-e5003a21-2 jfrbst priceCard')]")
precos.append(f'Dell G15: {preco1.text}')
sleep(3)

# Preço do segundo notebook (Acer)
pesquisar_dell = navegador.find_element(By.ID, "input-busca")
pesquisar_dell.send_keys("Acer")
sleep(2)
pesquisar_dell.send_keys(Keys.RETURN)
preco2 = navegador.find_element(By.XPATH, "//span[contains(@class,'sc-e5003a21-2 jfrbst priceCard')]")
precos.append(f'Acer: {preco2.text}')

# Preço do terceiro notebook (Lenovo)
pesquisar_dell = navegador.find_element(By.ID, "input-busca")
pesquisar_dell.send_keys("Lenovo IdeaPad")
sleep(2)
pesquisar_dell.send_keys(Keys.RETURN)
preco3 = navegador.find_element(By.XPATH, "//span[contains(@class,'sc-e5003a21-2 jfrbst priceCard')]")
precos.append(f'Lenovo IdeaPad: {preco3.text}')

with open('precos_notebooks.txt', 'w', encoding='utf-8') as file:
    for preco in precos:
        file.write(preco + '\n')