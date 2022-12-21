# --------------------------------------------------------------------------------- #
# Heads Will Roll dcinside IMPLEMENTATION
#
# Gueia, @ December 21, 2022
# Latest Revision: December 21, 2022 (17:54 GMT)
#
#
#
#
#
#
# For all kind of problems, requests of enhancements and bug reports,
# please write to me at:
#
# offbeatpersona@gmail.com
#
#
# 
#
# End Of Comments
# --------------------------------------------------------------------------------- #

import time
import logging
import os

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

import pyperclip
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    UnexpectedAlertPresentException,
    NoSuchWindowException
)
import platform


class HeadtextChanger:
    def __init__(self):
        self.identifier = None
        self.password = None
        self.headtextNum_init = None
        self.headtextNum_final = None
        self.headtext_visible_init = None
        self.headtext_visible_final = None
        self.post_list = None

        self.logger = logging.getLogger()
        self.logger.setLevel(level=logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())
        self.logger.addHandler(logging.FileHandler('./test.log'))

        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("headless")
        # options.add_extension("./uBOLite_0.1.22.12166.mv3.zip") # headless와 extension은 양립 불가
        options.add_argument(
            'user-agent='
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/108.0.0.0 Safari/537.36'
        )

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.action = ActionChains(self.driver)
        self.count = 0

    def setdata(self, headtext_visible_init, headtext_visible_final):
        self.headtext_visible_init = headtext_visible_init
        self.headtext_visible_final = headtext_visible_final

        # 원래 말머리
        if headtext_visible_init == '소식':
            self.headtextNum_init = '130'
        elif headtext_visible_init == '자작':
            self.headtextNum_init = '140'
        elif headtext_visible_init == '인증':
            self.headtextNum_init = '100'
        elif headtext_visible_init == '음추':
            self.headtextNum_init = '40'
        elif headtext_visible_init == '번역':
            self.headtextNum_init = '110'
        elif headtext_visible_init == '후기':
            self.headtextNum_init = '120'
        elif headtext_visible_init == '탑스터':
            self.headtextNum_init = '90'
        else:
            print('지원하지 않는 말머리 형식입니다.')
            raise

        # 목표 말머리
        if headtext_visible_final == '소식':
            self.headtextNum_final = '230'
        elif headtext_visible_final == '자작':
            self.headtextNum_final = '190'
        elif headtext_visible_final == '인증':
            self.headtextNum_final = '170'
        elif headtext_visible_final == '음추':
            self.headtextNum_final = '200'
        elif headtext_visible_final == '번역':
            self.headtextNum_final = '210'
        elif headtext_visible_final == '후기':
            self.headtextNum_final = '220'
        elif headtext_visible_final == '탑스터':
            self.headtextNum_final = '180'
        else:
            print('지원하지 않는 말머리 형식입니다.')
            raise

    def login_old(self, identifier, password):  # PC 환경에서 로그인 시도
        self.identifier = identifier
        self.password = password

        self.driver.get("https://sign.dcinside.com/login"
                        "?s_url=https%3A%2F%2Fgall.dcinside.com%2Fmgallery%2Fboard%2Flists%3Fid%3Dpostrockgallery")

        elm_id = self.driver.find_element(By.ID, 'id')
        elm_id.click()
        pyperclip.copy(self.identifier)  # 캡챠 뜨는 경우 붙여넣기
        if platform.system() == 'Darwin':
            elm_id.send_keys(Keys.COMMAND, 'v')
        elif platform.system() == 'Windows':
            elm_id.send_keys(Keys.CONTROL, 'v')
        elif platform.system() == 'Linux':
            elm_id.send_keys(Keys.CONTROL, 'v')
        else:
            elm_id.send_keys(Keys.CONTROL, 'v')
        # elm_id.send_keys(self.identifier)
        time.sleep(1)

        elm_pw = self.driver.find_element(By.ID, 'pw')
        elm_pw.click()
        pyperclip.copy(self.password)
        if platform.system() == 'Darwin':
            elm_id.send_keys(Keys.COMMAND, 'v')
        elif platform.system() == 'Windows':
            elm_id.send_keys(Keys.CONTROL, 'v')
        elif platform.system() == 'Linux':
            elm_id.send_keys(Keys.CONTROL, 'v')
        else:
            elm_id.send_keys(Keys.CONTROL, 'v')
        # elm_pw.send_keys(self.password)
        time.sleep(1)

        self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/article/section/div/div[1]/div/form/fieldset/button').click()
        '''
        self.logger.info(
            f"{time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"| login (pc) "
            f"| SUCCESS "
            f"| * "
        )
        '''
        self.popupclose_cert()

    def login(self, identifier, password):  # 모바일 환경에서 로그인 시도 (ERR_300016 우회)
        self.identifier = identifier
        self.password = password

        self.driver.get("https://msign.dcinside.com/login"
                        "?r_url=https%3A%2F%2Fgall.dcinside.com%2Fmgallery%2Fboard%2Flists%3Fid%3Dpostrockgallery")
        elm_id = self.driver.find_element(By.XPATH, '//*[@id="code"]')
        elm_id.click()
        if platform.system() == 'Darwin':
            elm_id.send_keys(Keys.COMMAND, 'v')
        elif platform.system() == 'Windows':
            elm_id.send_keys(Keys.CONTROL, 'v')
        elif platform.system() == 'Linux':
            elm_id.send_keys(Keys.CONTROL, 'v')
        else:
            elm_id.send_keys(Keys.CONTROL, 'v')
        # elm_id.send_keys(self.identifier)
        time.sleep(1)

        elm_pw = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        elm_pw.click()
        if platform.system() == 'Darwin':
            elm_id.send_keys(Keys.COMMAND, 'v')
        elif platform.system() == 'Windows':
            elm_id.send_keys(Keys.CONTROL, 'v')
        elif platform.system() == 'Linux':
            elm_id.send_keys(Keys.CONTROL, 'v')
        else:
            elm_id.send_keys(Keys.CONTROL, 'v')
        # elm_pw.send_keys(self.password)
        time.sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="loginAction"]').click()
        time.sleep(1)
        '''
        self.logger.info(
            f"{time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"| login (mobile) "
            f"| SUCCESS "
            f"| * "
        )
        '''
        self.popupclose_cert()

    def popupclose_cert(self):  # 2단계 인증 팝업 닫기, 캡챠 요구 시 수동 입력 (첫 번째 캡챠는 반드시 실패하도록 되어있으니 새로 받을 것)
        try:
            self.driver.find_element(By.CLASS_NAME, 'popbtn_bgblueclose').click()
            time.sleep(1)
        except (UnexpectedAlertPresentException, NoSuchElementException):
            WebDriverWait(self.driver, 300).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'popbtn_bgblueclose'))).click()
            time.sleep(1)

    def makelist(self):
        try:
            self.driver.get(
                "https://gall.dcinside.com/mgallery/board/lists/?id=postrockgallery&search_head="
                + self.headtextNum_init)
            self.post_list = []
            for tr in self.driver.find_elements(By.CLASS_NAME, "us-post"):
                self.post_list.append(tr.find_element(By.CLASS_NAME, 'gall_num').text)
        except:
            pass

    def run(self):
        self.logger.info(
            "--------------------------------------\n"
            f"{time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"| OPERATION "
            f"| STATUS "
            f"| COUNT "
        )

        while True:  # 50번마다 목록 갱신을 위한 while문
            self.makelist()
            print(self.post_list)
            try:
                for postNum in self.post_list:
                    self.realrun(postNum)
                # multi pool = Pool(processes=2)
                # multi pool = ProcessPool(nodes=2)
                # multi pool.map(self.realrun, self.post_list)

            except (KeyboardInterrupt, NoSuchWindowException):
                # multi pool.close()
                # multi pool.join()
                self.driver.quit()
                self.logger.info(
                    f"{time.strftime('%Y-%m-%d %H:%M:%S')} "
                    f"| quit "
                    f"| SUCCESS "
                    f"| * "
                )
                break

    def realrun(self, post_num):
        self.driver.get("https://gall.dcinside.com/mgallery/board/view/?id=postrockgallery&no=" + post_num)
        """
        # ElementNotVisibleException을 막기 위한 광고 닫기 버튼 클릭
        try:
            self.driver.find_element(By.XPATH, '//*[@id="wif_adx_banner_close"]/img').click()
        except:
            pass
        """

        # ElementNotVisibleException을 막기 위한 이동
        self.action.move_to_element(self.driver.find_element(By.CLASS_NAME, 'repley_add_vote')).perform()

        # Dropdown 나타날 때까지 기다리기 (참고: Dropdown이 select가 아니라 div이다.)
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="container"]/section/article[2]/div[1]/div/div[4]/div[2]/div')
            )
        ).click()

        self.driver.find_element(By.XPATH, "//li[@data-value='" + self.headtextNum_final + "']").click()

        # js 확인 경고창 처리
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

        self.count += 1
        self.logger.info(
            f"{time.strftime('%Y-%m-%d %H:%M:%S')} "
            f"| https://gall.dcinside.com/m/postrockgallery/{post_num}"
            f" ({self.headtext_visible_init} -> {self.headtext_visible_final}) "
            f"| SUCCESS "
            f"| {self.count}"
        )
        time.sleep(0.5)


def chromedriver_update():
    chrome_latest_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    current_list = os.listdir(os.getcwd())
    chrome_list = []
    for i in current_list:
        path = os.path.join(os.getcwd(), i)
        if os.path.isdir(path):
            if 'chromedriver.exe' in os.listdir(path):
                chrome_list.append(i)
    old_version = list(set(chrome_list) - {chrome_latest_ver})
    for i in old_version:
        path = os.path.join(os.getcwd(), i)
        shutil.rmtree(path)
    if chrome_latest_ver not in current_list:
        chromedriver_autoinstaller.install()
        print("updating chromedriver")
    else:
        pass


if __name__ == '__main__':
    chromedriver_update()
    hc = HeadtextChanger()

    user_id = input('ID: ')
    user_pw = input('PASSWORD: ')
    hc.login(user_id, user_pw)

    user_ht_init = input("현재 이동할 글이 존재하는 말머리를 다음 중 선택하세요. (소식, 자작, 인증, 음추, 번역, 후기, 탑스터)\n입력: ")
    user_ht_final = input("글을 이동할 목표 말머리를 다음 중 선택하세요. (소식, 자작, 인증, 음추, 번역, 후기, 탑스터)\n입력: ")
    hc.setdata(user_ht_init, user_ht_final)

    hc.run()
