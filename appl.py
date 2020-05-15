from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium.common.exceptions import StaleElementReferenceException

class Scraper():

    def __init__(self):
        self.url = 'https://angel.co/companies?locations[]=1647-India&signal[min]=5.1&signal[max]=10&raised[min]=14998921&raised[max]=100000000'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        sleep(3)
        self.data = []
        self.user_data = []
        
    def scrape(self):
        results_url = '//*[@id="root"]/div[4]/div[2]/div/div[2]/div[2]/div[2]'
        results = []
        h = 1
        while(True):
            try:
                self.driver.find_element_by_class_name("more")
            except:
                break
            sleep(3)
            self.driver.find_element_by_class_name("more").click()
            sleep(3)
            results.extend(self.driver.find_elements_by_xpath(results_url + '/div'))
            sleep(3)
            if h == 1:
                results_url += '/div[22]/div'
                h += 1
            else:
                results_url += '/div[21]/div'
                h += 1
            sleep(3)

        results=results[1:100]

        for company in results:
            ch = company.find_element_by_class_name("company_size")
            print(ch)
            emp = ch.find_element_by_class_name("value")
            print(emp)
            emp = emp.text
            if len(emp)<2:
                continue
            else:
                f = emp.split("-")
                if int(f[0])<50:
                    continue
            photo = company.find_element_by_class_name("photo")
            a = photo.find_element_by_tag_name("a").get_attribute('href')
            self.data.append(a)
            self.driver.close()

    def get_user_data(self):

        for url in self.data:
            d={}
            ur='https://angel.co/'
            d['angel_url']=url
            print(url)
            driver = webdriver.Chrome()
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            c_name = soup.find("div", {"class":"name_af83c"})
            c_name = c_name.find('a', class_='anchor_73052')
            company_name = c_name.text.strip()
            company_url = c_name['href']
            d['company_url'] = ur + company_url
            d['company_name'] = company_name
            u_name = soup.find('h4', class_='name_9d036')
            u_name = u_name.find('a')
            user_name = u_name.text.strip()
            user_url = u_name['href']
            d['user_name'] = user_name
            d['user_url'] = ur + user_url
            self.user_data.append(d)
            driver.close()
        return self.user_data


            

scr = Scraper()
scr.scrape()
l = scr.get_user_data()

