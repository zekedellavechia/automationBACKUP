from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "xxxx"
password_valid = "xxxx"
customer_info_name = "xxxx"
customer_info_lastname = "xxxxx"
customer_info_phone = "xxxx"
customer_info_email = "xxxxxxx@mail"
customer_info_invalid_name = "xxxx"
customer_info_invalid_lastname = "xxxx"
customer_info_invalid_phone = "xxxx"
customer_info_invalid_email = "xxxx"

execution_start = time()

testBase.login(user_valid, password_valid)

print('***CUSTOMER INVALID INFORMATION TEST: ')
testBase.add_customer_info(customer_info_invalid_name, customer_info_invalid_lastname, customer_info_invalid_phone, customer_info_invalid_email)

print('***CUSTOMER VALID INFORMATION TEST: ')
testBase.add_customer_info(customer_info_name, customer_info_lastname, customer_info_phone, customer_info_email)

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))



