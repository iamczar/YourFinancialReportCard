import os
import shutil
import re
import csv

def get_all_bankstatements(bank_statements_directory):
    # patter to look for
    csvFilePatern = ".csv"

    bank_statements_filenames = []

    # get all the filenames in the currect directory and put them into a list
    for folders,sub_folders,files in os.walk(bank_statements_directory):
        for file in files:
            # only take in files that are .csv
            if csvFilePatern in file:
                bank_statements_filenames.append(file)

    return bank_statements_filenames

def handle_bankstatement():

    bank_statements_directory = "/home/czar/YourFinancialReportCard/Project/Backend/HandleBankStatement"

    # get all the file names into a list
    bank_statement_filenames = get_all_bankstatements(bank_statements_directory)

    data_lines = []
    # build a transaction list 
    for bank_statement_filename in bank_statement_filenames:
        bank_statement_data = open(bank_statements_directory+"/"+bank_statement_filename)
        csv_data = csv.reader(bank_statement_data)
        data_lines.append(list(csv_data))

    return data_lines[0]


if __name__ == "__main__":
    print(''.join(str(e) for e in handle_bankstatement())) 
