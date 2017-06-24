from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get('http://www.reg.uci.edu/perl/WebSoc')
department_select = Select(driver.find_element_by_name('Dept'))
department_select.select_by_value("EECS")
