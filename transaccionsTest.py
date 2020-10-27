from test import *
testBase = TestBase()
print(testBase.driver.session_id)

itemIds = ["010050782684", "010050761557", "010050763993", "234569999999", "456789999999", "345679999999"]
i = 0
random_bulk = random.randint(1, 4)
random_int = round(random.uniform(1, 999))
random_float = round(random.uniform(1, 999), 2)
try:
    testBase.login("300011113", "ezcorp")
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

