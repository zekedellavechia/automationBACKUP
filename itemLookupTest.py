from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "xxxxx"
password_valid = "xxxx"
item_id_valid = "xxx"
item_id_prohibited = "xxx"
random_bulk = random.randint(1, 4)
random_int = round(random.uniform(1, 999))
random_float = round(random.uniform(1, 999), 2)

execution_start = time()

testBase.login(user_valid, password_valid)

print('***ADD NUMBER TEST: ')
testBase.search_item(item_id_valid)
testBase.close_modal()

print('***CLEAR SEARCH TEST: ')
testBase.clear_search()

print('***ADD BULK ITEM TEST: ')
testBase.add_bulk_item(random_bulk, random_int, random_float)

print('***PROHIBITED ITEM TEST: ')
testBase.search_item(item_id_prohibited)

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))
