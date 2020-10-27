from test import *

testBase = TestBase()
print(testBase.driver.session_id)

user_valid = "300011113"
user_invalid = "300011112"
password_valid = "ezcorp"
password_invalid = "procze"

execution_start = time()

print('***INVALID PASSWORD TEST: ')
testBase.login(user_valid, password_invalid)

print("***SHOW PASSWORD TEST: ")
testBase.login_show_password()

print('***CHANGE USER TEST: ')
testBase.login_change_user()

print('***INVALID USER TEST: ')
testBase.login(user_invalid, password_invalid)

print('***VALID LOGIN TEST: ')
testBase.login(user_valid, password_valid)

execution_end = time()

execution_time = execution_end - execution_start
print("Execution time: " + str(execution_time))