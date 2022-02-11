import csv
# importing csv so we can read and write csv files easier
import os
# importing os so we can find the name of the second database from its path, so we can use it in the making of
# the name of the new database (if the databases are not in the project folder)
"""defining a function that has two parameters data1, data2, with them the function gets the names of two databases
that are in the python project folder as strings or it gets the path to the both databases if they are not in the 
python project folder as string"""


def make_new_data(data1, data2):
    try:  # Using try block so if the first database doesn't exist we get smaller message and the program still works
        with open(data1, 'r') as d1r:       # opening the first database in reading mode
            data1_reader = csv.reader(d1r)  # reading the data from the first database and storing it in data1_reader

            try:  # Again using try block but for the second database
                with open(data2, 'r') as d2r:  # opening the second database in reading mode
                    data3 = "CSV_New_" + os.path.basename(data2)
                    # making the name for the new database by adding "CSV_New_"
                    # to the name of the second database that we get with using os.path.basename

                    try:  # Using try block to catch errors in the writing process
                        with open(data3, 'w', newline='') as ndw:  # opening a new database in writing mode as ndw
                            new_data_writer = csv.writer(ndw)
                            flag_head = 0  # flag header is not written in the new database
                            flag_type_data = 0  # flag working with customer code

                            for d1line in data1_reader:  # putting a line from database one in d1line
                                d2r.seek(0)  # setting data2 reader pointer to position 0
                                data2_reader = csv.reader(d2r)
                                # reading the data from d2r and storing it in data2_reader

                                for d2line in data2_reader:  # putting a line from database two in d2line
                                    if flag_head == 0:  # checking if the new database hasn't got a header
                                        new_data_writer.writerow(d2line)  # writing the header in the new database
                                        flag_head = 1  # raising the flag, header has been written in the new database
                                        if d2line[0] != d1line[0]:
                                            # checking if we are searching by invoice code
                                            flag_type_data = 1  # raising flag we are working with invoice code

                                    elif flag_type_data == 0 and d1line[0] == d2line[0]:
                                        # checking if we are working with customer code
                                        # checking if we have a customer code match
                                        new_data_writer.writerow(d2line)
                                        # writing the row where customer code match was found in the new database

                                    elif flag_type_data == 1 and d1line[1] == d2line[0]:
                                        # checking if we are working with invoice code
                                        # checking if we have a invoice code match
                                        new_data_writer.writerow(d2line)
                                        # writing the row where invoice code match was found in the new database
                # printing different messages for different errors
                    except PermissionError:
                        print(f"You have no permission to open {data3}, the csv file might be already opened.")
            except FileNotFoundError:
                print("The second database or path doesn't exist")
    except FileNotFoundError:
        print("The first database or path doesn't exist")


"""If the csv files are in the python project folder 
than we call the function make_new_data with the filename.csv as sting as parameters as shown here"""
make_new_data("customer_file.csv", "invoice.csv")
# calling the function to find the invoice info of the 1000 selected customers in the invoice database
make_new_data("customer_file.csv", "customer.csv")
# calling the function to find the customer info of the 1000 selected customers in the invoice database
make_new_data("CSV_New_invoice.csv", "invoice_item.csv")
# calling the function to find the invoice item info of the invoices
# of the 1000 selected customers in the new invoice
"""If the csv files are not in the python project folder
than we call the function with the stings of the path of the files as parameters.
The paths can be put in variables first"""
name = str(r'C:\Users\Emilija\Desktop\stonebranch\dcustomer_file.csv')
name2 = str(r'C:\Users\Emilija\Desktop\stonebranch\dinvoice.csv')
make_new_data(name, name2)
