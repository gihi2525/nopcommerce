import time
from selenium.webdriver.support.ui import Select

class addcustomerPage():
    #add customer page
    lnk_customer_menu_xpath = "//a[@href='#']//span[contains(text(),'Customer')]"
    lnk_customer_menuitem_xpath = "//a[@href='/Admin/Customer/List']//span[contains(text(),'Customer')]"
    btnAddNew_xpath = "//a[@class='btn btn-primary']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgOfVendor_xpath = "//*[@id='VendorsId']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@type='submit']//span[contains(text(),'Save')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnk_customer_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.lnk_customer_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)


    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Registereed":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == "Guests":
            #here user can be registered or guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == "Registrered":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
            time.sleep(3)
            #self.listitem.click();
            self.driver.excute_script("srguments[0].click", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgOfVendor_xpath))
        drp.select_by_visible_text(value)
    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self, fName):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fName)

    def setLastName(self, lName):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(lName)

    #date of birth
    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comName):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(comName)

    def setAdminContente(self, contamt):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(contamt)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
