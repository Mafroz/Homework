import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestVoblerTesteditProfile():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_voblerTesteditProfile(self):
    self.driver.get("http://voblery.com.ua/")
    self.driver.set_window_size(1693, 1050)
    self.driver.find_element(By.ID, "loglink2").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("maxim.zasetski@gmail.com")
    self.driver.find_element(By.ID, "passLabel").click()
    self.driver.find_element(By.ID, "pass").send_keys("Ckjybr13")
    self.driver.find_element(By.CSS_SELECTOR, "#logform2 .button").click()
    self.driver.find_element(By.LINK_TEXT, "Новинки").click()
    self.driver.find_element(By.ID, "loglink4").click()
    self.driver.find_element(By.LINK_TEXT, "Мой профиль").click()
    self.driver.find_element(By.NAME, "name").click()
    self.driver.find_element(By.NAME, "name").send_keys("Hoverclass")
    self.driver.find_element(By.LINK_TEXT, "Обновить аккаунт").click()
    self.driver.find_element(By.ID, "loglink5").click()
  
