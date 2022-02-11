import os
# importing os so we can find the name of the second database from its path, so we can use it in the making of
# the name of the new database (if the databases are not in the project folder)

"""defining a function that has two parameters data1, data2, with them the function gets the names of two databases
that are in the python project folder as strings or it gets the path to the both databases if they are not in the 
python project folder as string"""


def find_data(data1, data2):
    try:  # Using try block so if the first database doesn't exist we get smaller message and the program still works
        with open(data1, 'r') as d1r:
            # open database one in reading mode as d1r
            # the database with 1000 customer codes,or the new invoice database

            try:  # Again using try block but for the second database
                with open(data2, 'r') as d2r:  # open database two in reading mode as d2r
                    # (the bigger database where we are searching for the additional data of the 1000 customers)
                    data3 = "New_" + os.path.basename(data2)  # making the name for the new database by adding "New_"
                    # to the name of the second database that we get with using os.path.basename

                    try:  # Using try block to catch errors in the writing process
                        with open(data3, 'w', newline='') as d3w:  # opening a new database in writing mode as d3w
                            flag_head = 0  # flag header is not written in the new database
                            flag_type_data = 0  # flag working with customer code

                            for d1line in d1r:  # putting a line from database one in d1line
                                words1 = d1line.strip('\r\n').split(',')
                                # making the sting of strings into a list od stings
                                d2r.seek(0)  # setting data2 reader pointer to position 0

                                for d2line in d2r:  # putting a line from database two in d2line
                                    words2 = d2line.strip('\r\n').split(',')
                                    # making the sting of strings into a list od stings

                                    if flag_head == 0:  # checking if the new database hasn't got a header
                                        d3w.write(d2line)  # writing the header in the new database
                                        flag_head = 1  # raising the flag, header has been written in the new database

                                        if words2[0] != words1[0]:
                                            # checking if we are searching by invoice code
                                            flag_type_data = 1  # raising flag we are working with invoice code

                                    elif flag_type_data == 0 and words1[0] == words2[0]:
                                        # checking if we are working with customer code
                                        # checking if we have a customer code match
                                        d3w.write(d2line)
                                        # writing the row where customer code match was found in the new database

                                    elif flag_type_data == 1 and words1[1] == words2[0]:
                                        # checking if we are working with invoice code
                                        # checking if we have a invoice code match
                                        d3w.write(d2line)
                                        # writing the row where invoice code match was found in the new database
                    # printing different messages for different errors
                    except PermissionError:
                        print(f"You have no permission to open {data3}, the csv file might be already opened.")
            except FileNotFoundError:
                print("The second database or path doesn't exist")
    except FileNotFoundError:
        print("The first database or path doesn't exist")


"""If the csv files are in the python project folder 
than we call the function find_data with the filename.csv as sting as parameters as shown here"""
find_data("customer_file.csv", "invoice.csv")
# calling the function to find the invoice info of the 1000 selected customers in the invoice database
find_data("customer_file.csv", "customer.csv")
# calling the function to find the customer info of the 1000 selected customers in the invoice database
find_data("New_invoice.csv", "invoice_item.csv")
# calling the function to find the invoice item info of the invoices
# of the 1000 selected customers in the new invoice
"""If the csv files are not in the python project folder
than we call the function with the stings of the path of the files as parameters.
The paths can be put in variables first"""
name = str(r'C:\Users\Emilija\Desktop\stonebranch\dcustomer_file.csv')
name2 = str(r'C:\Users\Emilija\Desktop\stonebranch\dinvoice.csv')
find_data(name, name2)