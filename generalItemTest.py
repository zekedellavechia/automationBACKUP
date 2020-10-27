from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "xxxxx"
password_valid = "xxxx"
item_id_valid = "xxxxx"

execution_start = time()

testBase.login(user_valid, password_valid)
testBase.search_item(item_id_valid)
testBase.protection_jw_life_time()
testBase.regular_item_add_tocart()
testBase.add_customer_info("Name", "Last Name", "xxxx")
testBase.start_checkout()
testBase.pay_cash_exact()
testBase.transaction_result()

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))
