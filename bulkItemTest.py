from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "xxxxxx"
password_valid = "xxxxxxx"
random_bulk = random.randint(1, 4)
random_int = round(random.uniform(1, 999))
random_float = round(random.uniform(1, 999), 2)

execution_start = time()

testBase.login(user_valid, password_valid)
testBase.add_bulk_item(random_bulk, random_int, random_float)

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))
