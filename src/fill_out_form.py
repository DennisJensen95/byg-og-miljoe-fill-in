# Standard library
import time

# Third party libraries
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import tkinter.messagebox
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class FillOutForm:
    """Fills out the byg og miljø form"""
    
    def __init__(self, data: dict):
        self.options = Options()
        self.options.headless = False
        
        self.data = data
        
        
    def start_browser(self):
        self.driver = webdriver.Firefox(options=self.options)

        self.driver.get("https://www.bygogmiljoe.dk/projekter/nyt/ikke-gemt/overblik")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
        tkinter.messagebox.askyesno("", "Please log in to byg og miljø and press yes to continue or no to exit")
    
    def fill_out_form(self):
        # The flow of filling stuff out
        self.start_browser()
        self.get_away_cookie_policy()
        self.get_info_boxes_away()
        self.fill_out_project_name(self.data["udførelsesadresse"])
        self.click_next()
        self.insert_adress(self.data["udførelsesadresse"])
        self.click_next()
        self.click_next()
        time.sleep(2)
        self.add_removal_of_oil_tank()
    
    def add_removal_of_oil_tank(self):
        search_field = self._find_button_element_xpath('//input[@role="combobox"]')
        search_field.send_keys("olie")
        
        
        remove_oil_tank = self._find_button_element_xpath("/html/body/bom-root/bom-layout-page/div/bom-projekt/bom-fixed-menu/div/div[2]/div/bom-aktiviteter/bom-workspace/div/bom-aktiviteter-soegning/div/div[1]/div/bom-autocomplete/div/ng-select/ng-dropdown-panel/div/div[2]/div[5]/div/div")
        remove_oil_tank.click()
        
    def _find_element_xpath(self, xpath: str):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    
    def _find_button_element_xpath(self, xpath: str):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    
    def _find_element_visibility(self, xpath: str):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        
    def fill_out_project_name(self, project_name: str):
        
        element = self._find_element_xpath('//input[@formcontrolname="projektNavn"]')
        element.send_keys(project_name)
        time.sleep(0.5)
        
    def click_next(self):
        element = self._find_button_element_xpath('//button[@accesskey="n"]')
        element.click()
        time.sleep(0.3)
    
    def insert_adress(self, adress):
        element = self._find_element_xpath('//input[@placeholder="Skriv adresse"]')
        element.send_keys(adress[:-3])
        
        time.sleep(0.5)
        
        tkinter.messagebox.askokcancel("Adress", message="Please choose the correct adress and press ok to continue")
        time.sleep(0.5)
        
    def get_away_cookie_policy(self):
        element = self._find_button_element_xpath('//label[@for="hideGDPR-checkbox"]')
        element.click()
        time.sleep(0.1)
        
        # TODO: Find a way to close the cookie policy box
        # element = self._find_element_visibility('//button[contains(text(), "Luk")]')
        # element.click()
        tkinter.messagebox.askokcancel("Close cookie policy", message="Please close the cookie policy and press ok to continue")
        
    def get_info_boxes_away(self):
        element = self._find_button_element_xpath('//button[@class="button button-primary btn-tooltip px-7"]')
        element.click()
        
        element = self._find_button_element_xpath('//label[@for="dontShow_Overblik"]')
        element.click()
        
        element = self._find_button_element_xpath('//button[@class="button button-primary btn-tooltip px-7"]')
        element.click()
        
        