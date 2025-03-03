from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Register:
    # Locators
    id_first_name = "customer.firstName"
    id_last_name = "customer.lastName"
    id_address = "customer.address.street"
    id_city = "customer.address.city"
    id_state = "customer.address.state"
    id_zip = "customer.address.zipCode"
    id_customer_ssn = "customer.ssn"
    id_username = "customer.username"
    id_password = "customer.password"
    id_confirm_pass = "repeatedPassword"
    class_submit_btn = "button"
    xpath_register = "//a[text()='Register']"

    def __init__(self, driver):
        self.driver = driver

    # Methods to interact with elements
    def click_on_registerlink(self):
        self.driver.find_element(By.XPATH,self.xpath_register).click()
    

    def enter_first_name(self,first_name):
        self.driver.find_element(By.ID, self.id_first_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.id_last_name).send_keys(last_name)

    def enter_address(self, address):
        self.driver.find_element(By.ID, self.id_address).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element(By.ID, self.id_city).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(By.ID, self.id_state).send_keys(state)

    def enter_zip(self, zip_code):
        self.driver.find_element(By.ID, self.id_zip).send_keys(zip_code)

    def enter_customer_ssn(self, ssn):
        self.driver.find_element(By.ID, self.id_customer_ssn).send_keys(ssn)

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.id_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.id_password).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.id_confirm_pass).send_keys(confirm_password)

    def click_submit(self):
        self.driver.find_element(By.CLASS_NAME, self.class_submit_btn).click()
