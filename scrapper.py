from selenium import webdriver;
from bs4 import BeautifulSoup;
import pandas as pd;

driver = webdriver.Chrome("")

driver.get("https://edhrec.com/commanders/ghen-arcanum-weaver/curses")

driver.quit()