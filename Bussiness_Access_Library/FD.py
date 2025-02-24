import Bussiness_Access_Library.Account as Account
import Bussiness_Entities as Bent
import Data_Access_Library as Dal
import Common as Comm
import datetime
import random
obj_db=Dal.FDAccountDB()

class CFDaccount(Account.CAccount):
    """Accounts Class is the base class"""
    __balance: float=0.00
    def __init__(self):
        #self.__balance=obj_ent.getamount()
        super().__init__()

    def m_deposit(self, obj_ent=Bent.AccountsEntities()):
        obj_db.m_mssql_connect()
        amount=obj_db.fetch_last_FD_acc_amount(obj_ent) #calling function for fetching last transaction amount
        if amount is None:
            amount = 0.00
        self.__balance= float(amount) + float(obj_ent.getamount())
        obj_ent.set_total_amount(self.__balance)
        obj_db.FD_Account_transaction(obj_ent)

    def m_withdrawal(self, obj_ent=Bent.AccountsEntities()):
        try:
            obj_db.m_mssql_connect()
            amount=obj_db.fetch_last_FD_acc_amount(obj_ent)
            if float(amount-1000)<float(obj_ent.getamount()):
                raise Comm.Insufficient_Fund_Exception("Insufficient amount in the bank.")
            else:
                self.__balance=float(amount) - float(obj_ent.getamount())
                obj_ent.set_total_amount(self.__balance)
                obj_db.FD_Account_transaction(obj_ent)
        except Comm.Insufficient_Fund_Exception:
            print("ERROR: Insufficient balance in the bank account.")

    def m_getbalance(self):
        return self.__balance

    def m_automatic_account_id(self):
        obj_db.m_mssql_connect()
        account_no=obj_db.Automatic_Account_id()
        if account_no is None:
            return "FD1000"
        else:
            starting_string = account_no[0:2]
            last_string = int(account_no[2:])
            increment = last_string + 1
            account_no = starting_string + str(increment)
            return account_no

    def m_insert_account_info(self, obj_ent=Bent.AccountsEntities()):
        obj_db.m_mssql_connect()
        obj_db.FD_Account_info(obj_ent)

    def m_fetch_all_fd_acc_details(self, obj_ent=Bent.AccountsEntities()):
        obj_db.m_mssql_connect()
        return obj_db.fetch_all_FD_acc_details(obj_ent)

    def m_fetch_all_account_transactions(self, obj_ent=Bent.AccountsEntities()):
        obj_db.m_mssql_connect()
        return obj_db.fetch_all_FD_acc_transactions(obj_ent)

    def m_data_updation(self, obj_ent=Bent.AccountsEntities()):
        obj_db.m_mssql_connect()
        obj_db.data_updation(obj_ent)

    def m_delete_data(self, obj_ent=Bent.AccountsEntities()):
        obj_db.m_mssql_connect()
        obj_db.data_deletion(obj_ent)

    def m_transaction_id(self, obj_ent=Bent.AccountsEntities()):
        datetimestamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        randomnumber=str(random.randint(1000, 9999))
        transactionid=f"TXN-{datetimestamp}-{randomnumber}"
        return transactionid