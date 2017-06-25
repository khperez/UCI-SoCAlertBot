from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from send_sms import send_sms

driver = webdriver.Firefox()
driver.get('http://www.reg.uci.edu/perl/WebSoc')
department_select = Select(driver.find_element_by_name('Dept'))
department_select.select_by_value("EECS")
coursenum_element = driver.find_element_by_xpath("//input[@name='CourseNum']")
coursenum_element.send_keys("213")
submit_element = driver.find_element_by_xpath("//input[@value='Display Web Results']")
submit_element.click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
course_table = soup.find('div', {'class':'course-list'})
rows = course_table.findAll('tr')
for tr in rows:
	for l in tr.findAll('td'):
		row = l.getText().strip()
		if row.startswith("EECS"):
			print(row)
		if row.startswith("OPEN"):
			send_sms()
driver.close()

