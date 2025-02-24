class AccountsEntities:
    """Saving account Metadata"""
    __account_no=''
    __acc_holder_name=''
    __transaction_date=''
    __acc_opening_date=''
    __acc_type=''
    __trans_type=''
    __initial_amount=0.00
    __amount=0.00
    __total_amount=0.00
    __phone_no=''
    __email_id=''
    __column_name=''
    __column_value=''
    __transaction_id=''
    # getter and setter method for account no
    def getaccountno(self):
        return self.__account_no
    def setaccountno(self, __account_no):
        self.__account_no=__account_no
    # getter and setter method for account holder name
    def getaccholdername(self):
        return self.__acc_holder_name
    def setaccholdername(self, __acc_holder_name):
        self.__acc_holder_name=__acc_holder_name
    # getter and setter method for transaction date
    def gettransaction_date(self):
        return self.__transaction_date
    def settransaction_date(self, __transaction_date):
        self.__transaction_date=__transaction_date
    # getter and setter method for account type
    def getacctype(self):
        return self.__acc_type
    def setacctype(self, __acc_type):
        self.__acc_type=__acc_type
    # getter and setter method for transaction type
    def gettranstype(self):
        return self.__trans_type
    def settranstype(self, __trans_type):
        self.__trans_type=__trans_type
    # getter and setter method for amount
    def getamount(self):
        return self.__amount
    def setamount(self, __amount):
        self.__amount=__amount
    def get_initial_amount(self):
        return self.__initial_amount
    def set_initial_amount(self, __initial_amount):
        self.__initial_amount = __initial_amount
    # getter and setter method for amount
    def get_acc_opening_date(self):
        return self.__acc_opening_date
    def set_acc_opening_date(self, __acc_opening_date):
        self.__acc_opening_date=__acc_opening_date
    # getter and setter method for phone_no
    def get_phone_no(self):
        return self.__phone_no
    def set_phone_no(self, __phone_no):
        self.__phone_no=__phone_no
    # getter and setter method for email_id
    def get_email_id(self):
        return self.__email_id
    def set_email_id(self, __email_id):
        self.__email_id = __email_id
    # getter and setter method for total_amount
    def get_total_amount(self):
        return self.__total_amount
    def set_total_amount(self, __total_amount):
        self.__total_amount = __total_amount
    # getter and setter method for column_name
    def get_column_name(self):
        return self.__column_name
    def set_column_name(self, __column_name):
        self.__column_name=__column_name
    # getter and setter method for column_value
    def get_column_value(self):
        return self.__column_value
    def set_column_value(self, __column_value):
        self.__column_value=__column_value
    #getter and setter method for transaction id
    def get_transaction_id(self):
        return self.__transaction_id
    def set_transaction_id(self,__transaction_id):
        self.__transaction_id=__transaction_id