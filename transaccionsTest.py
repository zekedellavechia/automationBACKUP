from test import *
testBase = TestBase()
print(testBase.driver.session_id)

itemIds = ["111111111", "22222222222", "33333333", "4444444444", "55555555555", "66666666"]
i = 0
random_bulk = random.randint(1, 4)
random_int = round(random.uniform(1, 999))
random_float = round(random.uniform(1, 999), 2)
try:
    testBase.login("111111111111", "xxxxxxxxxxx")
    while i < 6:
        testBase.add_bulk_item(random_bulk, random_int, random_float)
        testBase.start_checkout()
        testBase.pay_cash_higher()
        testBase.transaction_result()
        testBase.next_transaction()
        testBase.search_item(itemIds[i])
        testBase.protection_decline()
        testBase.regular_item_add_tocart()
        testBase.start_checkout()
        testBase.pay_cash_higher()
        testBase.transaction_result()
        testBase.next_transaction()
        i += 1
    print("All transactions succesfull!")
except:
    print("FAIL")

