from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options = opts)

#
url1 = r'https://www.magazineluiza.com.br/'
navegador.get(url1)
pesquisar_dell = navegador.find_element(By.ID, "input-search")
pesquisar_dell.send_keys("Dell G15")

#url2

#url3