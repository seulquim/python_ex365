import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class NcafeMemberExr:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="F:\DEV\PythonPJT\PJT\Section3\webdriver\chrome\chromedriver")
        self.driver.implicitly_wait(5)

    def getMemberList(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('quim99')
        self.driver.find_element_by_name('pw').send_keys('')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

        self.driver.get('https://cafe.naver.com/CafeMemberView.nhn?m=view&clubid=10419250')
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')
        self.driver.implicitly_wait(15)
        self.driver.switch_to_frame('innerframe')
        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        return soup.select('div.mem_wrap > div.mem_list div.ellipsis.m-tcol-c')

    def printMemberList(self,list):
        f = open("F:\DEV\PythonPJT\PJT\Section3\mbm.txt",'wt')
        for i in list:
            f.write(i.string.strip()+"\n")
            print(i.string.strip())

        f.close()

    def __del__(self):
        self.driver.quit()
        print("Remove driver Object")


if __name__ == '__main__':

    a = NcafeMemberExr()

    start_time = time.time()

    a.printMemberList(a.getMemberList())

    print("=====Total %s secont======" % (time.time() - start_time))

    del  a
