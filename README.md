# Building-an-ATM-Withdrawal-System-using-Python-and-PostgreSQL-with-trigger-function.

Project: Building an ATM Withdrawal System using Python and PostgreSQL with trigger function.

Workflow:

1.    First, I created a database with three tables namely customer_details, debit_details and transaction_logs in PostgreSQL. The customer_details table will store the customer details  such as Name, Account Number,  Address,  Balance, Phone number, Email ID and Branch Code. The Debit_details table will store information such as Debit Card Number, Account Number, CVV, Name, Expiry Month, and Expiry Year. The Transaction_Logs table will store transaction history for the bank account.

2.    After creating the tables in database, I create a Python script that gets input from the user, such as Debit Card number, CVV, Expiry Month, Expiry Year, and Amount to be withdrawn.

3.    The python program will validate the Debit Card information provided by the user. It will check if the entered Debit Card number exists and matches the corresponding Account Number. It will also check whether the entered CVV, Expiry Month, and Expiry Year are valid.

4.    If the Debit Card information is valid, it will check the available balance in the corresponding account from the customer_details table in PostgreSQL. If the requested amount is less than or equal to the available balance, it will proceed with the transaction.

5.    It will then deduct the requested amount from the account's available balance in the table.

6.    Then, it will update the Transaction_Logs table to record the transaction, including the transaction_time, account_no, transaction_type, withdrawal_amount.

7.    At last, it will return a message to the user confirming the transaction was successful. A trigger function will be executed every time a transaction is made. The trigger function will automatically update the available balance in the customer_table by subtracting the transaction amount from the old balance.
