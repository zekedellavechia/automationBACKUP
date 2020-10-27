from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "xxxxx"
password_valid = "xxxxx"
random_bulk = random.randint(1, 4)
random_int = round(random.uniform(1, 999))
random_float = round(random.uniform(1, 999), 2)

execution_start = time()

testBase.login(user_valid, password_valid)
testBase.add_bulk_item(random_bulk, random_int, random_float)
testBase.start_checkout()
testBase.pay_credit_card()
testBase.transaction_result()

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))
