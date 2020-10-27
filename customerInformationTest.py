from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "300011113"
password_valid = "ezcorp"
customer_info_name = "Pablo"
customer_info_lastname = "Fernandez"
customer_info_phone = "1234567890"
customer_info_email = "pablo.fernandez@softvision.com"
customer_info_invalid_name = "123"
customer_info_invalid_lastname = "456"
customer_info_invalid_phone = "abc"
customer_info_invalid_email = "1a2s"

execution_start = time()

testBase.login(user_valid, password_valid)

print('***CUSTOMER INVALID INFORMATION TEST: ')
testBase.add_customer_info(customer_info_invalid_name, customer_info_invalid_lastname, customer_info_invalid_phone, customer_info_invalid_email)

print('***CUSTOMER VALID INFORMATION TEST: ')
testBase.add_customer_info(customer_info_name, customer_info_lastname, customer_info_phone, customer_info_email)

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))



