from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "xxxxxxx"
password_valid = "xxxxxxx"
random_bulk = random.randint(1, 4)
random_int = round(random.uniform(1, 999))
random_float = round(random.uniform(1, 999), 2)
item_id_valid = "010050761557"

execution_start = time()

testBase.login(user_valid, password_valid)
testBase.search_item(item_id_valid)
testBase.protection_decline()
testBase.regular_item_add_tocart()
testBase.start_checkout()
testBase.pay_cash_higher()
testBase.transaction_result()

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))
