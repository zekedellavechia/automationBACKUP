from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "xxxx"
user_invalid = "xxxx"
password_valid = "xxxx"
password_invalid = "xxxx"
random_bulk = random.randint(1, 4)
random_int = round(random.uniform(1, 999))
random_float = round(random.uniform(1, 999), 2)
item_id_valid_creditCard = "xxxxx"
item_id_valid_cash = "xxxxx"
item_id_invalid = "xxxxx"
item_id_reuse = item_id_valid_cash
item_id_variety1 = "xxxxx"
item_id_variety2 = "xxxxx"
customer_info_name = "xxxx"
customer_info_lastname = "xxxx"
customer_info_phone = "xxxx"
customer_info_email = "xxxxxxxxx@xxx.com"

execution_start = time()

"""print(100*"-")
print('***INVALID PASSWORD TEST: ')
testBase.login(user_valid, password_invalid)

print('***CHANGE USER TEST: ')
testBase.login_change_user()

print('***INVALID USER TEST: ')
testBase.login(user_invalid, password_valid)"""

print('***VALID LOGIN TEST: ')
testBase.login(user_valid, password_valid)

print('***BULK ITEM TRANSACTION / CASH TEST: ')
testBase.add_bulk_item(random_bulk, random_int, random_float)
testBase.start_checkout()
testBase.pay_cash_exact()
testBase.transaction_result()
testBase.next_transaction()

print('***BULK ITEM TRANSACTION / CREDIT CARD TEST: ')
testBase.add_bulk_item(random_bulk, random_int, random_float)
testBase.start_checkout()
testBase.pay_credit_card()
testBase.transaction_result()
testBase.next_transaction()

print('***GENERAL ITEM TRANSACTION / CASH TEST: ')
testBase.search_item(item_id_valid_cash)
testBase.protection_decline()
testBase.regular_item_add_tocart()
testBase.start_checkout()
testBase.pay_cash_higher()
testBase.transaction_result()
testBase.next_transaction()

print('***GENERAL ITEM TRANSACTION / CREDIT CARD TEST: ')
testBase.search_item(item_id_valid_creditCard)
testBase.protection_gm_six_months()
testBase.regular_item_add_tocart()
testBase.add_customer_info(customer_info_name, customer_info_lastname, customer_info_phone)
testBase.start_checkout()
testBase.pay_credit_card()
testBase.transaction_result()
testBase.next_transaction()

print('***GENERAL ITEM INVALID:  ')
testBase.search_item(item_id_reuse)

print('***VARIETY TRANSACTION:  ')
testBase.add_bulk_item(random_bulk, random_int, random_float)
testBase.search_item(item_id_variety1)
testBase.protection_decline()
testBase.regular_item_add_tocart()
testBase.add_bulk_item(random_bulk, random_int, random_float)
testBase.search_item(item_id_variety2)
testBase.protection_gm_six_months()
testBase.regular_item_add_tocart()
testBase.start_checkout()
testBase.add_customer_info(customer_info_name, customer_info_lastname, customer_info_phone)
testBase.pay_cash_exact()
testBase.transaction_result()
testBase.next_transaction()

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))
