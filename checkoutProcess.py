from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "300011113"
password_valid = "ezcorp"
random_bulk = random.randint(1, 4)
random_int = round(random.uniform(1, 999))
random_float = round(random.uniform(1, 999), 2)
item_id_valid = "010050761557"

execution_start = time()

testBase.login(user_valid, password_valid)

print('***CUSTOMER INFORMATION MANDATORY TEST: ')
testBase.search_item(item_id_valid)
testBase.regular_item_add_tocart()
testBase.customer_info_check_mandatory()
testBase.cart_clear_all()

print('***CUSTOMER INFORMATION OPTIONAL TEST: ')
testBase.search_item(item_id_valid)
testBase.protection_decline()
testBase.regular_item_add_tocart()
testBase.customer_info_check_mandatory()

print('***PAY WITH CASH INVALID TEST: ')
testBase.start_checkout()
testBase.pay_cash_lower()

print('***PAY WITH CASH VALID TEST: ')
testBase.close_modal()
testBase.start_checkout()
testBase.pay_cash_higher()
testBase.transaction_result()
testBase.next_transaction()

print('***PAY WITH CREDIT CARD VALID TEST: ')
testBase.add_bulk_item(random_bulk, random_int, random_float)
testBase.start_checkout()
testBase.pay_credit_card()
testBase.transaction_result()
testBase.next_transaction()

print('***PAY WITH CREDIT CARD INVALID TEST: ')
testBase.add_bulk_item(random_bulk, random_int, random_float)
testBase.start_checkout()
#HERE YOU SHOULD QUICKLY REMOVE THE CREDIT CARD IN ORDER TO TRIGGER THE ERROR
testBase.pay_credit_card()
testBase.transaction_result()