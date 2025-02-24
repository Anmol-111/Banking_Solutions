import Bussiness_Entities.AccountEntities as Bent
import pymssql

class RecurringAccountDB:
    def m_mssql_connect(self):
        global constr, cursor
        constr=pymssql.connect(server="LAPTOP-8T8MA06J\\SQLEXPRESS",
                               user="root",
                               password="Admin@1234",
                               database="Banking_Solutions_Database")
        cursor=constr.cursor()

    def Recurring_Account_info(self, obj_ent=Bent.AccountsEntities()):
        cursor.callproc('sp_insert_Recurring_account_info',
                        (obj_ent.getaccountno(), obj_ent.getaccholdername(), obj_ent.get_acc_opening_date(),
                         obj_ent.getacctype(), obj_ent.get_phone_no(), obj_ent.get_email_id(), obj_ent.get_initial_amount()))
        constr.commit()

    def Recurring_Account_transaction(self, obj_ent=Bent.AccountsEntities()):
        cursor.callproc('sp_insert_Recurring_account_transaction',(obj_ent.get_transaction_id(), obj_ent.getaccountno(), obj_ent.gettransaction_date(),
             obj_ent.getacctype(), obj_ent.gettranstype(), obj_ent.getamount(), obj_ent.get_total_amount()))
        constr.commit()

    def Automatic_Account_id(self, obj_ent=Bent.AccountsEntities()):
        cursor.execute('EXEC sp_Recurring_max_account_id')
        data=cursor.fetchone()
        return data[0]

    def fetch_last_Recurring_acc_amount(self, obj_ent=Bent.AccountsEntities()):
        cursor.callproc('sp_fetch_last_Recurring_acc_amount', (obj_ent.getaccountno(),))
        data = cursor.fetchone()
        if data is None:
            return None
        else:
            return data[0]

    def fetch_all_Recurring_acc_details(self, obj_ent=Bent.AccountsEntities()):
        cursor.callproc('sp_fetchall_Recurringacc_details', (obj_ent.getaccountno(),))
        data=cursor.fetchall()
        return data

    def fetch_all_Recurring_acc_transactions(self, obj_ent=Bent.AccountsEntities()):
        cursor.callproc('sp_fetchall_Recurring_account_transaction',(obj_ent.getaccountno(),))
        data=cursor.fetchall()
        return data

    def data_updation(self, obj_ent=Bent.AccountsEntities()):
        cursor.callproc('sp_Recurring_account_data_updation',
                        (obj_ent.getaccountno(), obj_ent.get_column_name(), obj_ent.get_column_value()))
        constr.commit()

    def data_deletion(self, obj_ent=Bent.AccountsEntities()):
        cursor.callproc('sp_Recurring_account_transaction_delete_data', (obj_ent.getaccountno(),))
        cursor.callproc('sp_Recurring_account_delete_data', (obj_ent.getaccountno(),))
        constr.commit()