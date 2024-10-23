from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
# Passe a variavel opts para o webdriver
navegador = webdriver.Chrome(options = opts)


# url = r'C:\Users\08163\Desktop\mensageiro\webscrap\produtos.html'
# navegador.get(url)
# titulo = navegador.find_element(By.ID, "titulo")
# precos = navegador.find_elements(By.CLASS_NAME, "price")
# for preco in precos:
#     print(preco.text)
# produtos = navegador.find_elements(By.CLASS_NAME, "product_name")
# for produto in produtos:
#     print(produto.text)
#
# precos = navegador.find_elements(By.XPATH, "/html/body/div[1]/div/p")
# print(preco.text)

url = r'C:\Users\08163\Desktop\mensageiro\webscrap\contato.html'
navegador.get(url)

campo_nome = navegador.find_element(By.ID, "nome")
campo_nome.send_keys("Kauê Eduardo")
sleep(3)
mensagem = navegador.find_element(By.ID, "mensagem")
mensagem.send_keys("A Globo é um lixo.")
sleep(3)
botao = navegador.find_element(By.XPATH, "/html/body/form/button")
botao.click()
