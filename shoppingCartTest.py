from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "xxxx"
password_valid = "xxxx"
random_bulk = random.randint(1, 4)
random_int = round(random.uniform(1, 999))
random_float = round(random.uniform(1, 999), 2)

execution_start = time()

testBase.login(user_valid, password_valid)

print('***CART REMOVE ALL TEST: ')
testBase.add_bulk_item(random_bulk, random_int, random_float)
testBase.cart_clear_all()

print('***CART REMOVE ITEM TAP TEST: ')
testBase.add_bulk_item(random_bulk, random_int, random_float)
testBase.cart_remove_item_tap()

print('***CART REMOVE ITEM SWIPE TEST: ')
testBase.add_bulk_item(random_bulk, random_int, random_float)
testBase.cart_remove_item_swipe()

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))
