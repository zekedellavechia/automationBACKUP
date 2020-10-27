from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "300011113"
password_valid = "ezcorp"
item_id_valid = "010050761557"
regular_item_id = "456789999999"
jewerly_item_id = "010050761557"

execution_start = time()

testBase.login(user_valid, password_valid)

print('***PRODUCT DETAIL PRICING & EDIT TEST: ')
testBase.search_item(item_id_valid)
testBase.regular_item_edit("15.98")
testBase.close_modal()

print('***PRODUCT DETAIL PROTECTION PLAN GENERAL ITEM TEST: ')
testBase.search_item(regular_item_id)
testBase.protection_gm_six_months()

print('***PRODUCT DETAIL PROTECTION PLAN JEWERLY TEST: ')
testBase.search_item(jewerly_item_id)
testBase.protection_jw_one_year()

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))