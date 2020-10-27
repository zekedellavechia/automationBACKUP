from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "300011113"
password_valid = "ezcorp"
item_id_valid = "010050761557"

execution_start = time()

testBase.login(user_valid, password_valid)
testBase.search_item(item_id_valid)
testBase.protection_jw_life_time()
testBase.regular_item_add_tocart()
testBase.add_customer_info("Pablo", "Fernandez", "1234567890")
testBase.start_checkout()
testBase.pay_cash_exact()
testBase.transaction_result()

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))