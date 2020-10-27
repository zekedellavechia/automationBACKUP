import random
import time as sleep
from time import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions




des_cap = {
  "platformName": "android",
  "deviceName": "Android Emulator",
  "appPackage": "com.xxxxx",
  "appActivity": "com.xxxxxx",
  "newCommandTimeout": 10000
}
#MOCK
"""platformName": "android",
  "deviceName": "Android Emulator",
  "appPackage": "com.xxxxxx",
  "appActivity": "com.xxxxxx",
  "newCommandTimeout": 10000"""

#SV_DEV
"""platformName": "android",
  "deviceName": "Android Emulator",
  "appPackage": "com.xxxxxx",
  "appActivity": "com.xxxxxx",
  "newCommandTimeout": 10000"""

class TestBase():
    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', des_cap)
        self.wait = WebDriverWait(self.driver, 7)
        self.touch = TouchAction(self.driver)
        self.variables = {
            'Login_user_input_field': 'employeeNumberInput',
            'Login_user_submit': 'NextButton',
            'Login_user_error': 'employeeNumberErrorText',
            'Login_pass_input_field': 'passwordInput',
            'Login_pass_submit': 'LoginButton',
            'Login_pass_error': 'passwordErrorText',
            'Login_show_password': "//android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView",
            'Login_change_user': "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[2]",
            'Logout': 'logoutButton',
            'Logout_Confirm': 'confirmSignOutbutton',
            'Search_numpad_1': 'dialpadButton1',
            'Search_numpad_2': 'dialpadButton2',
            'Search_numpad_3': 'dialpadButton3',
            'Search_numpad_4': 'dialpadButton4',
            'Search_numpad_5': 'dialpadButton5',
            'Search_numpad_6': 'dialpadButton6',
            'Search_numpad_7': 'dialpadButton7',
            'Search_numpad_8': 'dialpadButton8',
            'Search_numpad_9': 'dialpadButton9',
            'Search_numpad_0': 'dialpadButton0',
            'Search_numpad_go': 'buttonGo',
            'Search_numpad_del': 'buttonBackSpace',
            'Search_button': 'tabButtonNumber',
            'Search_error': 'itemNumberErrorServerText',
            'Search_add_to_cart_button': 'itemDetailButton',
            'Search_edit_price': 'itemPriceInput',
            'Protection_decline': 'protectionOptionDecline',
            'Protection_gn_six_months': 'protectionOption1',
            'Protection_jw_one_year': 'protectionOption3',
            'Protection_jw_life_time': 'protectionOption4',
            'Protection_gn_six_months_value': '//android.widget.TextView[@content-desc="selectRadioDeclineText"]',
            'Protection_jw_one_year_value': '//android.widget.TextView[@content-desc="selectRadioDeclineText"][1]',
            'Protection_jw_life_time_value': '(//android.widget.TextView[@content-desc="selectRadioDeclineText"])[2]',
            'Bulk_item_button': 'tabButtonBulk',
            'Bulk_item_dropdown': 'android:id/text1',
            'Bulk_item_dropdown_element': '//android.widget.CheckedTextView[%s]',
            'Bulk_item_quantity_input': 'quantityInput',
            'Bulk_item_sale_price_input': 'totalSalePriceInput',
            'Bulk_add_to_cart_button': 'addToCartBulkItem',
            'Bulk_item_total_price': 'bulkItemTotalPrice',
            'Bulk_item_error': 'totalSalePriceError',
            'Customer_info_add_from_cart': 'cartAddCustomerButton',
            'Customer_info_add_from_cart_mandatory': 'cartAddCustomerRequiredButton',
            'Customer_info_add_from_checkout': 'cartAddCustomerButton',
            'Customer_info_name_input': 'firstNameInput',
            'Customer_info_name_error': 'firstNameError',
            'Customer_info_last_name_input':'lastNameInput',
            'Customer_info_last_name_error': 'lastNameError',
            'Customer_info_phone_input':'phoneNumberInput',
            'Customer_info_phone_error': 'phoneNumberError',
            'Customer_info_email_input': 'emailAddressInput',
            'Customer_info_email_error': 'emailAddressError',
            'Customer_info_submit': 'newCustomerButton',
            'Checkout_button': 'cartCheckoutButton',
            'Checkout_total': 'cartSummaryValue3',
            'Cash_select_box': 'payWithCashButton',
            'Cash_input_field': 'cashAmountFormattedInput',
            'Cash_tender_button': 'cashTenderButton',
            'Cash_tender_error': '//android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView[2]/android.view.ViewGroup/android.widget.TextView[3]',
            'Credit_card_select_box': 'payWithCreditCardButton',
            'Credit_card_signature_input': 'signHereText',
            'Credit_card_signature_submit':'confirmSignButton',
            'Receipt_reprint_button': 'reprintReceiptButton',
            'Receipt_reprint_cancel': 'alertLayoutCancelButton',
            'Receipt_reprint_reprint':'alertLayoutConfirmButton',
            'Next_transaction_button': 'nextTransactionButton',
            'Modal_title': 'alertLayoutTitleText',
            'Modal_text': 'alertLayoutText',
            'Modal_button': 'alertLayoutConfirmButton',
            'Close_screen_icon': 'rightSideOperationCloseButton',
            'Cart_item_to_remove': 'deleteItemFromCart0',
            'Cart_item_to_remove_confirm': '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ScrollView[2]/android.view.ViewGroup/android.view.ViewGroup[6]',
            'Cart_clear_all_button': 'clearAllButton',
            'Cart_clear_all_button_confirm': '//android.view.ViewGroup[@content-desc="confirmClearButton"]',
        }

    def close_keyboard(self):
        self.driver.hide_keyboard()

    def close_numpad(self):
        self.driver.hide_keyboard()

    def field_int_check(self, field):
        try:
            self.driver.find_element(By.ACCESSIBILITY_ID, field).send_keys("abc")
            self.driver.find_element(By.ACCESSIBILITY_ID, field).send_keys(123.4)
            print("Int field failed")
        except:
            print("Int field OK")

    def field_float_check(self, field):
        try:
            self.driver.find_element(By.ACCESSIBILITY_ID, field).send_keys("abc")
            self.driver.find_element(By.ACCESSIBILITY_ID, field).send_keys(1234)
            print("FLoat field failed")
        except:
            print("Float field OK")

    def field_text_check(self, field):
        try:
            self.driver.find_element(By.ACCESSIBILITY_ID, field).send_keys(1234)
            self.driver.find_element(By.ACCESSIBILITY_ID, field).send_keys(123.4)
            print("Text field failed")
        except:
            print("Text field OK")

    def logout(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Logout'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Logout']).click()
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Logout_Confirm']).click()
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Login_pass_input_field'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Login_pass_input_field'])
            print("Logout: OK")
        except:
            print("Logout: FAIL")

    def login_change_user(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.variables['Login_change_user'])))
            self.driver.find_element(By.XPATH, self.variables['Login_change_user']).click()
            print('Change user test: OK')
            return True
        except:
            print('Change user test: FAIL')
            return False

    def login_show_password(self):
            try:
                self.driver.find_element_by_xpath(self.variables['Login_show_password']).click()
                self.wait.until_not(expected_conditions.text_to_be_present_in_element((By.ACCESSIBILITY_ID, self.variables['Login_pass_input_field']), "•"))
                hashfield = self.driver.find_element_by_accessibility_id(self.variables['Login_pass_input_field']).get_attribute('text')
                if "•" not in hashfield:
                    print('Show password: OK')
                else:
                    print("Show password: FAIL")
            except:
                print("Show password: FAIL")

    def get_login_user_message(self, user):
        try:
            self.close_numpad()
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Login_user_error'])))
            message = self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Login_user_error']).get_attribute('text')
            print("Login fail in user " + user + ": " + message)
            return True
        except:
            print("User " + user + ": OK")
            return False

    def get_login_pass_message(self, password):
        try:
            self.close_keyboard()
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Login_pass_error'])))
            message = self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Login_pass_error']).get_attribute('text')
            print("Login fail in password: " + message)
            return True
        except:
            print("Password: OK")
            return False

    def login_user(self, user):
        try:
            self.wait.until((expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Login_user_input_field']))))
            self.driver.find_element_by_accessibility_id(self.variables['Login_user_input_field']).send_keys(user)
            self.close_numpad()
            self.driver.find_element_by_accessibility_id(self.variables['Login_user_submit']).click()
        except:
            return False

    def login_password(self, password):
        try:
            self.wait.until((expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Login_pass_input_field']))))
            self.driver.find_element_by_accessibility_id(self.variables['Login_pass_input_field']).set_value(password)
            self.close_keyboard()
            self.driver.find_element_by_accessibility_id(self.variables['Login_pass_submit']).click()
        except:
            return False

    def login(self, user, password):
        try:
            self.login_user(user)
            self.get_login_user_message(user)
            self.login_password(password)
            self.get_login_pass_message(password)
        except:
            #sleep.sleep(5)
            self.wait.until(expected_conditions.presence_of_element_located(By.ACCESSIBILITY_ID, self.variables['Login_user_error']))
            self.get_login_user_message(user)
            exit()
            return False

    def regular_item_edit(self, newValue):
        try:
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Search_edit_price']).send_keys(newValue)
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Search_edit_price']).send_keys(newValue)
            print("Change item price to " + newValue + ": OK ")
        except:
            print("Change item price: FAIL")

    def number_id_toarray (self, id_str):
        id_arr = list(map(int, id_str))
        return id_arr

    def search_item_number_to_action(self, number):
        switcher = {
            0: 'Search_numpad_0',
            1: 'Search_numpad_1',
            2: 'Search_numpad_2',
            3: 'Search_numpad_3',
            4: 'Search_numpad_4',
            5: 'Search_numpad_5',
            6: 'Search_numpad_6',
            7: 'Search_numpad_7',
            8: 'Search_numpad_8',
            9: 'Search_numpad_9'
        }
        index = switcher[number]
        self.driver.find_element(By.ACCESSIBILITY_ID, self.variables[index]).click()

    def regular_item_get_price(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Search_edit_price'])))
            price = self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Search_edit_price']).get_attribute("text")
            print("Item price OK: $"+price)
        except:
            print("Itrem price FAIL")

    def get_search_item_message(self, itemid):
        try:
            self.wait.until(expected_conditions.visibility_of_all_elements_located((By.ACCESSIBILITY_ID, self.variables['Search_error'])))
            message = self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Search_error']).get_attribute("text")
            print(itemid + " search fail: " + message)
        except:
            print(itemid + " search OK")

    def regular_item_add_tocart(self):
        try:
            self.wait.until(expected_conditions.element_to_be_clickable((By.ACCESSIBILITY_ID, self.variables['Search_add_to_cart_button'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Search_add_to_cart_button']).click()
        except:
            return False

    def clear_search(self):
        for index in range(2):
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Search_numpad_del']).click()
            self.touch.long_press(self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Search_numpad_del'])).perform()

    def search_item(self, item_id):
        self.wait.until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Search_button'])))
        self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Search_button']).click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Search_numpad_go'])))
        item_arr = self.number_id_toarray(item_id)
        self.clear_search()
        for num in item_arr:
            self.search_item_number_to_action(num)
        self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Search_numpad_go']).click()
        self.get_search_item_message(item_id)

    def bulk_item_edit(self, newValue):
        try:
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Bulk_item_sale_price_input']).send_keys(newValue)
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Bulk_item_sale_price_input']).send_keys(newValue)
            print("Change price: OK")
        except:
            print("Change price: FAIL")

    def add_bulk_item (self, position, quantity, salePrice):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Bulk_item_button'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Bulk_item_button']).click()
            self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.variables['Bulk_item_dropdown'])))
            self.driver.find_element(By.ID, self.variables['Bulk_item_dropdown']).click()
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.variables['Bulk_item_dropdown_element'] % position)))
            self.driver.find_element_by_xpath(self.variables['Bulk_item_dropdown_element'] % position).click()
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Bulk_item_quantity_input']).send_keys(str(quantity))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Bulk_item_sale_price_input']).set_value(salePrice)
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Bulk_item_sale_price_input']).set_value(salePrice)
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Bulk_item_total_price'])
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Bulk_add_to_cart_button']).click()
            print("Bulk item OK")
        except:
            print ('Error with bulk item: ' + self.driver.find_element((By.ACCESSIBILITY_ID, self.variables['Bulk_item_error'])).get_attribute('text'))

    def protection_decline(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Protection_decline'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Protection_decline']).click()
            print("Manage Protection: OK")
        except:
            print("Manage Protection: Fail")

    def protection_gm_six_months(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Protection_gn_six_months'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Protection_gn_six_months']).click()
            print("Manage Protection: OK")
        except:
            print("Manage Protection: Fail")

    def protection_gm_six_months_get_value(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.variables['Protection_gn_six_months_value'])))
            value = self.driver.find_element(By.XPATH, self.variables['Protection_gn_six_months_value']).get_attribute("text")
            value = value[1:]
            return value
        except:
            print("Protection GM six months value: FAIL")

    def protection_jw_one_year(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Protection_jw_one_year'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Protection_jw_one_year']).click()
            print("Manage Protection: OK")
        except:
            print("Manage Protection: Fail")

    def protection_jw_one_year_get_value(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.variables['Protection_jw_one_year_value'])))
            value = self.driver.find_element(By.XPATH, self.variables['Protection_jw_one_year_value']).get_attribute("text")
            value = value[1:]
            return value
        except:
            print("Protection Jewerly one year value: FAIL")

    def protection_jw_life_time(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Protection_gn_life_time'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Protection_gn_life_time']).click()
            print("Manage Protection: OK")
        except:
            print("Manage Protection: Fail")

    def protection_jw_life_time_get_value(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.variables['Protection_jw_life_time_value'])))
            value = self.driver.find_element(By.XPATH, self.variables['Protection_jw_life_time_value']).get_attribute("text")
            value = value[1:]
            return value
        except:
            print("Protection Jewerly life time value: FAIL")

    def customer_information_validation(self, field_name, field):
        try:
            message = self.driver.find_element(By.ACCESSIBILITY_ID, field).get_attribute('text')
            print('Customer %s Fail: ' % field_name + message)
        except:
            print('Customer %s OK' % field_name)

    def close_modal(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Close_screen_icon'])))
        self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Close_screen_icon']).click()
        self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Close_screen_icon']).click()

    def add_customer_info(self, name, lastName, number, *email):
        self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Customer_info_add_from_cart'])))
        self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Customer_info_add_from_cart']).click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Customer_info_name_input'])))
        self.driver.find_element_by_accessibility_id(self.variables['Customer_info_name_input']).send_keys(name)
        self.driver.find_element_by_accessibility_id(self.variables['Customer_info_last_name_input']).send_keys(lastName)
        self.driver.find_element_by_accessibility_id(self.variables['Customer_info_phone_input']).send_keys(number)
        self.driver.find_element_by_accessibility_id(self.variables['Customer_info_email_input']).send_keys(email)
        #TRIGGERS THE ERROR MESSAGES
        self.driver.find_element_by_accessibility_id(self.variables['Customer_info_name_input']).click()
        self.driver.find_element_by_accessibility_id(self.variables['Customer_info_last_name_input']).click()
        self.driver.find_element_by_accessibility_id(self.variables['Customer_info_phone_input']).click()
        self.driver.find_element_by_accessibility_id(self.variables['Customer_info_email_input']).click()
        self.driver.find_element_by_accessibility_id(self.variables['Customer_info_name_input']).click()
        self.close_keyboard()
        self.wait.until(expected_conditions.element_to_be_clickable((By.ACCESSIBILITY_ID, self.variables['Customer_info_submit'])))
        self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Customer_info_submit']).click()
        self.customer_information_validation('Name ', self.variables['Customer_info_name_error'])
        self.customer_information_validation('Last Name ', self.variables['Customer_info_last_name_error'])
        self.customer_information_validation('Phone Number ', self.variables['Customer_info_phone_error'])
        self.customer_information_validation('Email ', self.variables['Customer_info_email_error'])
        self.wait.until(expected_conditions.element_to_be_clickable((By.ACCESSIBILITY_ID, self.variables['Customer_info_submit'])))
        try:
            self.wait.until(expected_conditions.element_to_be_clickable((By.ACCESSIBILITY_ID, self.variables['Customer_info_submit'])))
            #needs two clicks
            self.close_modal()
            print("Customer information couldn\'t be added")
        except:
            print("Customer information added succesfully")

    def customer_info_check_mandatory(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Customer_info_add_from_cart_mandatory'])))
            print("Customer info mandatory: TRUE")
        except:
            print("Customer info mandatory: OPTIONAL")

    def cart_remove_item_swipe (self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cart_item_to_remove'])))
            TouchAction(self.driver).press(x=654, y=418).wait(2000).move_to(x=281, y=413).release().perform()
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cart_item_to_remove'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cart_item_to_remove']).click()
            print("Item removed OK (swipe)")
        except:
            print('Error removing Item (swipe)')

    def cart_remove_item_tap (self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cart_item_to_remove'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cart_item_to_remove']).click()
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.variables['Cart_item_to_remove_confirm'])))
            self.driver.find_element(By.XPATH, self.variables['Cart_item_to_remove_confirm']).click()
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.variables['Cart_item_to_remove_confirm'])))
            self.driver.find_element(By.XPATH, self.variables['Cart_item_to_remove_confirm']).click()
            print("Item removed OK (tap)")
        except:
            print('Error removing Item (tap)')

    def cart_clear_all(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cart_clear_all_button'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cart_clear_all_button']).click()
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.variables['Cart_clear_all_button_confirm'])))
            self.driver.find_element(By.XPATH, self.variables['Cart_clear_all_button_confirm']).click()
            print("Cart cleared OK")
        except:
            print('Error clearing cart')

    def get_total(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Checkout_total'])))
        self.total = self.driver.find_element(By.ACCESSIBILITY_ID,self.variables['Checkout_total']).get_attribute("text")
        self.total = self.total[1:]

    def start_checkout (self):
        try:
            self.wait.until(expected_conditions.element_to_be_clickable((By.ACCESSIBILITY_ID, self.variables['Checkout_button'])))
            self.get_total()
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Checkout_button']).click()
            print('Checkout started OK')
        except:
            print('Checkout couldn\'t start')

    def pay_cash_exact (self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cash_select_box'])))
            self.total=self.total.replace(",","")
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cash_select_box']).click()
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cash_input_field'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cash_input_field']).send_keys(self.total)
            self.wait.until(expected_conditions.element_to_be_clickable((By.ACCESSIBILITY_ID, self.variables['Cash_tender_button'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cash_tender_button']).click()
            print('Cash Payment Exact: OK')
        except:
            print('Cash Payment Exact: FAIL')

    def pay_cash_higher (self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cash_select_box'])))
            self.total=self.total.replace(",","")
            self.total = round(float(self.total)*1.26, 2)
            self.total = str(self.total)
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cash_select_box']).click()
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cash_input_field'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cash_input_field']).send_keys(self.total)
            self.wait.until(expected_conditions.element_to_be_clickable((By.ACCESSIBILITY_ID, self.variables['Cash_tender_button'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cash_tender_button']).click()
            print('Cash Payment Higher: OK')
        except:
            print('Cash Payment Higher: FAIL')

    def pay_cash_lower (self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cash_select_box'])))
            self.total=self.total.replace(",","")
            self.total = round(float(self.total)*0.74, 2)
            self.total = str(self.total)
            self.wait.until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cash_select_box'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cash_select_box']).click()
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Cash_input_field'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cash_input_field']).send_keys(self.total)
            #This action is needed to trigger the error message
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Checkout_total']).click()
            if self.wait.until(expected_conditions.element_to_be_clickable(By.ACCESSIBILITY_ID, self.variables['Cash_tender_button'])):
                self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Cash_tender_button']).click()
                print('Cash Payment Lower: Was completed. FAIL')
        except:
            message = self.driver.find_element(By.XPATH, self.variables['Cash_tender_error']).get_attribute('text')
            print('Cash Payment Lower OK: ' + message)

    def pay_credit_card (self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.ACCESSIBILITY_ID, self.variables['Credit_card_select_box'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Credit_card_select_box']).click()
            sleep.sleep(30)
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Credit_card_signature_input'])))
            #signature
            TouchAction(self.driver).press(x=538, y=492).move_to(x=1279, y=760).release().perform()
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Credit_card_signature_submit']).click()
            if (self.wait.until(expected_conditions.element_to_be_clickable((By.ACCESSIBILITY_ID, self.variables['Next_transaction_button'])))):
                print('Credit Card Payment: OK')
        except:
            print('Credit Card Payment: FAIL')

    def reprint_receipt (self):
        try:
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Receipt_reprint_button']).click()
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Receipt_reprint_reprint']).click()
            print('Reprint: OK')
        except:
            print('Reprint: FAIL')

    def reprint_receipt_cancel (self):
        try:
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Receipt_reprint_button']).click()
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Receipt_reprint_cancel']).click()
            print('Cancel Reprint: OK')
        except:
            print('Cancel Reprint: FAIL')

    def next_transaction (self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Next_transaction_button'])))
            self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Next_transaction_button']).click()
            print('Next Transaction: OK')
        except:
            print('Next Transaction: FAIL')

    def check_popup(self):
        try:
            sleep.sleep(7)
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Modal_text'])))
            message = self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Modal_text']).get_attribute("text")
            try:
                title = self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Modal_title']).get_attribute("text")
                print(title + ": " + message)
                self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Modal_button']).click()
            except:
                print(message)
                self.driver.find_element(By.ACCESSIBILITY_ID, self.variables['Modal_button']).click()
                return True
        except:
            return False

    def transaction_result(self):
        try:
            self.check_popup()
            self.wait.until(expected_conditions.presence_of_element_located((By.ACCESSIBILITY_ID, self.variables['Next_transaction_button'])))
            print("Transaction Successfull!")
        except:
            print("Transaction couln\'t be completed")
            return False
