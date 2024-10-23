from time import sleep
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
opts = ChromeOptions()
opts.add_experimental_option("detach", True)