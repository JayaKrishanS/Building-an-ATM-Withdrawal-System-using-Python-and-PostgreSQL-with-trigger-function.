#Importing the required package
import psycopg2

Jk = psycopg2.connect(user='postgres', password='Jaya@9698', host='localhost', port=5432, database='ATM_withdraw')
x = Jk.cursor()


while True:
    card_no = input("Enter your card number : ")
    x.execute("SELECT DEBIT_CARD_NO FROM DEBIT_DETAILS WHERE DEBIT_CARD_NO = %s", [card_no])
    debit_no = x.fetchone()
    if not debit_no:
        raise ValueError("Invalid debit card number...")
    else:
        break

while True:
    cvv = input("Enter your cvv number : ")
    x.execute("SELECT CVV FROM DEBIT_DETAILS WHERE CVV = %s AND DEBIT_CARD_NO = %s", [cvv, card_no])
    cvv_no = x.fetchone()
    if not cvv_no:
        raise ValueError("Invalid cvv number..")
    else:
        break

while True:
    Ex_year = int(input("Enter the card expiry year : "))
    x.execute("SELECT EXPIRY_YEAR FROM DEBIT_DETAILS WHERE EXPIRY_YEAR = %s AND CVV = %s AND DEBIT_CARD_NO = %s", [Ex_year, cvv, card_no])
    year = x.fetchone()
    if not year:
        raise ValueError('Invalid expiry year..')
    else:
        break

while True:
    Ex_month = int(input("Enter your expiry month : "))
    x.execute("SELECT EXPIRY_MONTH FROM DEBIT_DETAILS WHERE EXPIRY_MONTH = %s AND EXPIRY_YEAR = %s AND CVV = %s AND DEBIT_CARD_NO = %s", [Ex_month, Ex_year, cvv, card_no])
    month = x.fetchone()
    if not month:
        raise ValueError("invalid Expiry month...")
    else:
        break
x.execute("SELECT ACC_NO FROM DEBIT_DETAILS WHERE EXPIRY_MONTH = %s AND EXPIRY_YEAR = %s AND CVV = %s AND DEBIT_CARD_NO = %s", [Ex_month, Ex_year, cvv, card_no])
account = x.fetchone()

while True:
    amount = int(input("Enter the amount for withdrawal : "))
    x.execute("SELECT BALANCE FROM CUSTOMER_DETAILS WHERE ACC_NO = %s", [account])
    balance = x.fetchone()
    if amount < 0:
        raise ValueError("Invalid amount..")
    elif amount > balance[0]:
        print("Insufficient balance..")
    else:
        break

x.execute("UPDATE CUSTOMER_DETAILS SET BALANCE = BALANCE - %s WHERE ACC_NO = %s", [amount, account])
print("collect the cash")
print("Transaction successful..Thanks for your visit...")
Jk.commit()
Jk.close()
x.close()