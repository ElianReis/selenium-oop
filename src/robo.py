from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from src.logger import logger
from src.estrutura import Estrutura
import time
import os
import glob


class RoboPetro:
    def __init__(self, country):
        base = Estrutura()
        self.remove("\\downloads\\*")
        self.chrome = "chromedriver.exe"
        self.path = os.getcwd() + "\\" + "downloads"
        self.browser = self.config_browser()
        self.wait = WebDriverWait(self.browser, 10)
        url = eval('base.' + country.lower().replace(" ", "") + 'url')
        clicks = eval('base.' + country.lower().replace(" ", ""))
        self.search(url, clicks)

    def config_browser(self):
        ua = UserAgent()
        user_agent = ua.random
        prefs = {"download.default_directory": self.path}
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument(f"user-agent={user_agent}")
        options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(options=options, executable_path=self.chrome)
        return browser

    def search(self, url: str, clicks: list):
        if url.startswith("https://www-genesis"):
            logger.info("Acessando o link {}".format(url))
            self.browser.get(url)
            self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#disclaimerAcceptId"))
            ).click()
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#Inhalt_6+ .border-right .btn-flex-grid")
                )
            ).click()
            t = self.browser.find_element(
                By.CSS_SELECTOR, ".emph+ .schemaBorderColorLevel5"
            )
            t.click()
            t.send_keys("2010")
            time.sleep(2)
            s = self.browser.find_element(
                By.CSS_SELECTOR, ".schemaBorderColorLevel5+ .schemaBorderColorLevel5"
            )
            s.click()
            s.send_keys("2022")
            time.sleep(2)
            for elements in clicks:
                time.sleep(2)
                self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, elements))
                ).click()
            self.downloading()

        elif url.startswith("https://www.stat-search"):
            logger.info("Acessando o link {}".format(url))
            self.browser.get(url)
            self.browser.find_element(By.CSS_SELECTOR, "#txtDirect").send_keys(
                "PR01'PRCG15_2200000000"
            )
            time.sleep(2)
            for elements in clicks:
                time.sleep(2)
                self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, elements))
                ).click()
            self.browser.find_element(By.CSS_SELECTOR, "#fromYear").send_keys("2010")
            self.browser.find_element(By.CSS_SELECTOR, "#toYear").send_keys("2022")
            self.browser.find_element(
                By.CSS_SELECTOR,
                "#resultArea > div.abstractionMenuArea.clearfix > ul > li:nth-child(1) > a",
            ).click()
            w2 = self.browser.window_handles[1]
            self.browser.switch_to.window(w2)
            self.browser.find_element(
                By.XPATH, "/html/body/div[2]/div/div[2]/table/tbody/tr[2]/td[5]/a"
            ).click()
            w3 = self.browser.window_handles[2]
            self.browser.switch_to.window(w3)
            self.browser.find_element(By.CSS_SELECTOR, ".tbl a").click()
            self.downloading()

        elif url.startswith("https://www.e-stat.go.jp"):
            self.browser.get(url)
            lista = self.browser.find_elements(
                By.CSS_SELECTOR, ".stat-cycle_ul_other:nth-child(1) .stat-item_child"
            )[-1]
            lista.click()
            time.sleep(2)
            self.browser.find_element(
                By.CSS_SELECTOR,
                ".stat-dataset_list-item:nth-child(1) .stat-download_icon_left .stat-dl_text",
            ).click()
            self.downloading()

        else:
            self.browser.get(url)
            logger.info("Acessando o link {}".format(url))
            for elements in clicks:
                WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, elements))
                ).click()
            self.downloading()

    def downloading(self):
        time.sleep(5)
        self.wait = True
        if self.wait is True:
            for fname in os.listdir(self.path):
                logger.info("Realizando o download de {}".format(fname))
                if fname.endswith(".tmp"):
                    time.sleep(10)
                else:
                    self.wait = False
                logger.info("Realizado o download de {}".format(fname))

                return fname

    @staticmethod
    def remove(folder):
        directory = os.getcwd()
        files = glob.glob(directory + folder)
        for f in files:
            os.remove(f)
        logger.info("Pasta {} removida".format(folder))
