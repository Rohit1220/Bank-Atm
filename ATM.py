class Atm(object):
    Method = input("Type 1 if you want to debit Payment or type 2 if you want to deposit")
    balance = 100000
    if (Method  == 1):
        TransferAmount = input("Write the amount you want to transfer")
        balance = balance-TransferAmount
        print("Amount Debited")
    else:
        TransferAmount = input("Write the amount you want to transfer")
        balance = balance + TransferAmount
        print("Amount Deposited")
Atm()
