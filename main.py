#!/usr/bin/env python3
# --------------------------------------------------------------------------------- #
# Heads Will Roll dcinside IMPLEMENTATION
#
# Gueia, @ December 21, 2022
# Latest Revision: December 25, 2022
#
#
# ooooo   ooooo                           .o8
# `888'   `888'                          "888
#  888     888   .ooooo.   .oooo.    .oooo888   .oooo.o
#  888ooooo888  d88' `88b `P  )88b  d88' `888  d88(  "8
#  888     888  888ooo888  .oP"888  888   888  `"Y88b.
#  888     888  888    .o d8(  888  888   888  o.  )88b
# o888o   o888o `Y8bod8P' `Y888""8o `Y8bod88P" 8""888P'
#
#
# oooooo   oooooo     oooo  o8o  oooo  oooo
#  `888.    `888.     .8'   `"'  `888  `888
#   `888.   .8888.   .8'   oooo   888   888
#    `888  .8'`888. .8'    `888   888   888
#     `888.8'  `888.8'      888   888   888
#      `888'    `888'       888   888   888
#       `8'      `8'       o888o o888o o888o
#
#
# ooooooooo.             oooo  oooo
# `888   `Y88.           `888  `888
#  888   .d88'  .ooooo.   888   888
#  888ooo88P'  d88' `88b  888   888
#  888`88b.    888   888  888   888
#  888  `88b.  888   888  888   888  .o.
# o888o  o888o `Y8bod8P' o888o o888o Y8P
#
#
# For all kind of problems, requests of enhancements and bug reports,
# please write to me at:
#
# offbeatpersona@gmail.com
#
# End Of Comments
# --------------------------------------------------------------------------------- #

import sys
import time
import logging
import os
from collections import OrderedDict

import chromedriver_autoinstaller
import shutil

# multi from multiprocessing import Pool
# multi from pathos.multiprocessing import ProcessPool
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import pyperclip
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    UnexpectedAlertPresentException,
    NoSuchWindowException,
    TimeoutException,
    ElementNotInteractableException
)
import platform
import getpass
from pyfiglet import Figlet


class HeadtextChanger:
    def __init__(self):
        f = Figlet(font='roman')
        print('\n'+f.renderText('Heads Will Roll.')+'\n')

        chromedriver_update()

        self.post_list = []
        self.headtext_dict = OrderedDict()

        self.headtext_list = []  # ?????? ????????? ????????? ??????  ex) ?????????????
        self.headtext_init = ''
        self.headtext_final = ''

        self.headtextid_list = []  # ????????? id  ex) 170
        self.headtextid_init = ''
        self.headtextid_final = ''

        self.logger = logging.getLogger()
        self.logger.handlers = []
        self.logger.addHandler(logging.StreamHandler())
        self.logger.addHandler(logging.FileHandler('./test.log'))

        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("incognito")
        options.add_argument("headless")
        # options.add_extension("./uBOLite_0.1.22.12166.mv3.zip")  # headless??? extension??? ?????? ??????

        options.add_argument('user-agent='
                             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/108.0.0.0 Safari/537.36')

        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "none"

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.waitaminute = WebDriverWait(self.driver, 60)
        self.action = ActionChains(self.driver)
        self.count = 0

        if not sys.argv:        # ????????? ??????
            self.galleryid = input("GALLERYID: ")
            self.galleryurl = "https://gall.dcinside.com/mgallery/board/lists?id=" + self.galleryid

            self.makelist_headtext()

            print("?????? ??? ?????? ????????? ?????? ???????????? ???????????? ????????? ???????????????.")
            print(*enumerate(self.headtext_list), sep='\n')
            self.selectedNo_init = int(input("??????: "))

            print("?????? ??? ?????? ????????? ?????? ???????????? ????????? ???????????????.")
            print(*enumerate(self.headtext_list), sep='\n')
            self.selectedNo_final = int(input("??????: "))

            self.headtext_init = self.headtext_list[self.selectedNo_init]
            self.headtextid_init = self.headtextid_list[self.selectedNo_init]
            self.headtext_final = self.headtext_list[self.selectedNo_final]
            self.headtextid_final = self.headtextid_list[self.selectedNo_final]
        else:
            if '-r' in sys.argv:        # ????????? ??????
                self.galleryid = "postrockgallery"
                self.galleryurl = "https://gall.dcinside.com/mgallery/board/lists?id=" + self.galleryid
                self.recoverylist = ['NaN',
                                     'NaN',
                                     '??????????',
                                     'NaN',
                                     '??????????',
                                     '??????????',
                                     '??????????',
                                     '??????????',
                                     '?????????????',
                                     '??????????',
                                     'NaN']
                print("?????? ??? ????????? ???????????? ????????? ???????????????.")
                print(*enumerate(self.recoverylist), sep='\n')
                self.selectedNo_init = int(input("??????: "))
                self.selectedNo_final = self.selectedNo_init
                self.headtext_init = self.recoverylist[self.selectedNo_init]
                self.headtext_final = self.recoverylist[self.selectedNo_final]
                self.setdata(self.selectedNo_init, self.selectedNo_final)

            elif '-debug' in sys.argv:
                self.logger.setLevel(level=logging.DEBUG)

            else:
                print('Need help? Visit https://github.com/gueia/heads-will-roll')

        if '-debug' not in sys.argv:
            self.logger.setLevel(level=logging.INFO)

        # ????????? ?????? ????????? ?????? ?????? ??????

        self.identifier = input('USERID: ')
        self.password = getpass.getpass('PASSWORD: ')

        self.logger.info(
            "----------------------------------------------------\n"
            f"| {time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"| OPERATION "
            f"| STATUS "
            f"| COUNT |"
        )

        self.login(self.identifier, self.password)

        # ???????????? ???????????? ????????? ????????? ?????? ?????? ??????

        while 1:  # 50????????? ?????? ????????? ?????? while???
            if self.makelist_post() == 0:
                break
            else:
                self.makelist_post()
                try:
                    for postNum in self.post_list:
                        try:
                            self.run(postNum)
                        except UnexpectedAlertPresentException:
                            print("?????????????????? ????????? ????????? ????????? ?????????????????????. ?????? ??? ?????? ????????? ?????????.")
                            pass
                    # multi pool = Pool(processes=2)
                    # multi pool = ProcessPool(nodes=2)
                    # multi pool.map(self.run, self.post_list)

                except (KeyboardInterrupt, NoSuchWindowException):
                    # multi pool.close()
                    # multi pool.join()
                    self.driver.quit()
                    self.logger.info(f"| {time.strftime('%Y-%m-%d %H:%M:%S')} "
                                     f"| quit "
                                     f"| DONE "
                                     f"| * |")
                    break

    def setdata(self, selectedNo_init, selectedNo_final):  # ???????????? ????????? ID??? (????????? ???????????? ??????)
        if selectedNo_init == 2:
            self.headtextid_init = '130'    # ??????
            self.headtextid_final = '230'
        elif selectedNo_init == 4:
            self.headtextid_init = '100'    # ?????? x
            self.headtextid_final = '170'
        elif selectedNo_init == 5:
            self.headtextid_init = '40'     # ?????? x
            self.headtextid_final = '200'
        elif selectedNo_init == 6:
            self.headtextid_init = '110'    # ?????? ??????
            self.headtextid_final = '210'
        elif selectedNo_init == 7:
            self.headtextid_init = '120'    # ?????? ??????
            self.headtextid_final = '220'
        elif selectedNo_init == 8:
            self.headtextid_init = '90'     # ????????? x
            self.headtextid_final = '180'
        elif selectedNo_init == 9:
            self.headtextid_init = '140'    # ?????? ??????
            self.headtextid_final = '190'
        else:
            print('???????????? ?????? ????????? ???????????????.')
            raise

    def login_pc(self, identifier, password):  # PC ???????????? ????????? ??????
        self.driver.get("https://sign.dcinside.com/login"
                        "?s_url=https%3A%2F%2Fgall.dcinside.com%2Fmgallery%2Fboard%2Flists%3Fid%3Dpostrockgallery")

        elm_id = self.driver.find_element(By.ID, 'id')
        elm_id.click()
        pyperclip.copy(identifier)  # ?????? ?????? ?????? ????????????
        if platform.system() == 'Darwin':
            elm_id.send_keys(Keys.COMMAND, 'v')
        else:
            elm_id.send_keys(Keys.CONTROL, 'v')
        # elm_id.send_keys(self.identifier)
        time.sleep(1)

        elm_pw = self.driver.find_element(By.ID, 'pw')
        elm_pw.click()
        pyperclip.copy(password)
        if platform.system() == 'Darwin':
            elm_id.send_keys(Keys.COMMAND, 'v')
        else:
            elm_id.send_keys(Keys.CONTROL, 'v')
        # elm_pw.send_keys(self.password)
        time.sleep(1)

        self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/article/section/div/div[1]/div/form/fieldset/button').click()
        '''
        self.logger.info("| "
            f"{time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"| login (pc) "
            f"| DONE "
            f"| * |"
        )
        '''
        # self.popupclose_cert()

    def login(self, identifier, password):  # ????????? ???????????? ????????? ?????? (ERR_300016 ?????? ??????)
        self.driver.get("https://msign.dcinside.com/login"
                        "?r_url=https%3A%2F%2Fgall.dcinside.com%2Fmgallery%2Fboard%2Flists%3Fid%3D" + self.galleryid)
        elm_id = self.driver.find_element(By.XPATH, '//*[@id="code"]')
        elm_id.click()
        '''
        pyperclip.copy(self.identifier)
        if platform.system() == 'Darwin':
            elm_id.send_keys(Keys.COMMAND, 'v')
        else:
            elm_id.send_keys(Keys.CONTROL, 'v')
        '''
        elm_id.send_keys(identifier)

        elm_pw = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        elm_pw.click()
        '''
        pyperclip.copy(self.password)
        if platform.system() == 'Darwin':
            elm_id.send_keys(Keys.COMMAND, 'v')
        else:
            elm_id.send_keys(Keys.CONTROL, 'v')
        '''
        elm_pw.send_keys(password)

        try:
            self.driver.find_element(By.XPATH, '//*[@id="loginAction"]').click()
        except UnexpectedAlertPresentException:  # ?????? ??????
            self.waitaminute.until(EC.url_to_be(self.galleryurl))

        # self.wait.until(EC.url_to_be(self.galleryurl))

        if self.driver.current_url == self.galleryurl:  # ????????? ??????
            self.logger.info(f"| {time.strftime('%Y-%m-%d %H:%M:%S')} "
                             "| login (mobile) "
                             "| DONE "
                             "| * |")
            pass
        else:
            print(self.driver.current_url)
            print(self.galleryurl)
            self.logger.info(f"| {time.strftime('%Y-%m-%d %H:%M:%S')} "
                             "| login (mobile) "
                             "| ERROR "
                             "| * |")
            raise

        # self.popupclose_cert()

    def popupclose_cert(self):  # 2?????? ?????? ?????? ??????, ?????? ?????? ??? ?????? ?????? (??? ?????? ????????? ????????? ??????????????? ??????????????? ?????? ?????? ???)
        try:
            self.driver.find_element(By.CLASS_NAME, 'popbtn_bgblueclose').click()
            time.sleep(1)
        except (UnexpectedAlertPresentException, NoSuchElementException):
            WebDriverWait(self.driver, 300).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'popbtn_bgblueclose'))).click()
            time.sleep(1)

    def makelist_post(self):
        self.driver.get(f"{self.galleryurl}&search_head={self.headtextid_init}")
        self.post_list = []
        for tr in self.driver.find_elements(By.CLASS_NAME, 'us-post'):
            self.post_list.append(tr.find_element(By.CLASS_NAME, 'gall_num').get_attribute("textContent"))
        if not self.post_list:
            print("??????/????????? ?????????????????????! ????")
            return 0


    def makelist_headtext(self):
        if self.driver.current_url == self.galleryurl:
            pass
        else:
            self.driver.get(self.galleryurl)

        for i in self.driver.find_elements(By.XPATH, ".//a[contains(@onclick, 'listSearchHead')]"):
            headtextid = i.get_attribute('onclick').lstrip('listSearchHead(').rstrip(')')
            self.headtext_dict[i.get_attribute("textContent")] = headtextid
        # print(self.headtext_dict)
        self.headtext_list = list(self.headtext_dict.keys())
        self.headtextid_list = list(self.headtext_dict.values())

    def run(self, post_num):
        self.driver.get(f"https://gall.dcinside.com/mgallery/board/view/?id={self.galleryid}&no={post_num}")
        """
        # ElementNotVisibleException??? ?????? ?????? ?????? ?????? ?????? ??????
        try:
            self.driver.find_element(By.XPATH, '//*[@id="wif_adx_banner_close"]/img').click()
        except:
            pass
        """

        # ElementNotVisibleException??? ?????? ?????? ??????
        self.action.move_to_element(self.driver.find_element(By.CLASS_NAME, 'repley_add_vote')).perform()

        try:  # Dropdown ????????? ????????? ???????????? (??????: Dropdown??? select??? ????????? div??????.)
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="container"]/section/article[2]/div[1]/div/div[4]/div[2]/div')
                )
            ).click()
        except TimeoutException:
            print("?????? ????????? ????????????.")
            raise
        except UnexpectedAlertPresentException:
            print("?????????????????? ????????? ????????? ????????? ?????????????????????. ?????? ??? ?????? ????????? ?????????.")
            pass

        self.driver.find_element(By.XPATH, f"//li[@data-value='{self.headtextid_final}']").click()

        # js ?????? ????????? ??????
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

        self.count += 1
        self.logger.info(f"| {time.strftime('%Y-%m-%d %H:%M:%S')} "
                         f"| https://gall.dcinside.com/m/postrockgallery/{post_num}"
                         f" ({self.headtext_init} -> {self.headtext_final}) "
                         f"| DONE "
                         f"| {self.count} |")
        time.sleep(0.5)


def chromedriver_update():
    print("Checking for ChromeDriver updates...")
    chromedriver_autoinstaller.install()


if __name__ == '__main__':
    HeadtextChanger()
