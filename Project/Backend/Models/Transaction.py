
class Transaction:
    
    def __init__(self, Date=None, Type=None, Description=None, Value=None,
                 Balance=None, Account_Name=None, Account_Number=None):
        self.Date = Date
        self.Type = Type
        self.Description = Description
        self.Value = Value
        self.Balance = Balance
        self.Account_Name = Account_Name
        self.Account_Number = Account_Number
        self.CategoryID = 0

    @classmethod
    def from_list(cls, transaction_as_list):

        if(len(transaction_as_list) < 7):
            raise BankStatementDataParserException(
                "Transaction: list does not contain enough elements")

        return cls(

            Date=transaction_as_list[0],
            Type=transaction_as_list[1],
            Description=transaction_as_list[2],
            Value=transaction_as_list[3],
            Balance=transaction_as_list[4],
            Account_Name=transaction_as_list[5],
            Account_Number=transaction_as_list[6],
        )

    @classmethod
    def from_tuple(cls, data):

        return cls(
            Date=data.Date,
            Type=data.Type,
            Description=data.Description,
            Value=data.Value,
            Balance=data.Balance,
            Account_Name=data.Account_Name,
            Account_Number=data.Account_Number
        )

    def convert_date_string_into_epoch(self, date):

        # regular expression for this pattern -> 02 Dec 2019
        firstDateFormat = r'\d{2}\s\D{3}\s\d{4}'

        # regular expression forthis pattern ->  02/12/2019
        secondDateFormat = r'\d{2}/\d{2}/\d{4}'

        if re.search(firstDateFormat, date) is not None:
            # this format -> 02 Dec 2019
            for each_date_element in date.splitlines():
                date = parser.parse(each_date_element)

            year = int(date.strftime("%Y"))
            month = int(date.strftime("%m"))
            date = int(date.strftime("%d"))

            epoch_equivalend = datetime.datetime(
                year, month, date, 0, 0).timestamp()

        elif re.search(secondDateFormat, date) is not None:
            # this format -> 02/12/2019

            for each_date_element in date.splitlines():
                date = parser.parse(each_date_element, dayfirst=True)

            year = int(date.strftime("%Y"))
            month = int(date.strftime("%m"))
            date = int(date.strftime("%d"))

            epoch_equivalend = datetime.datetime(
                year, month, date, 0, 0).timestamp()

        return epoch_equivalend

    def normalise_date(self):
        self.Date = self.convert_date_string_into_epoch(self.Date)