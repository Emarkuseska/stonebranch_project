import os


def find_data(data1,data2):
    try:
        with open(data1, 'r') as d1r:
            with open(data2, 'r') as d2r:
                data3 = "New_" + os.path.basename(data2)
                with open(data3, 'w', newline='') as d3w:
                    flag_head = 0
                    flag_type_data = 0
                    for d1line in d1r:
                        words1 = d1line.strip('\r\n').split(',')
                        d2r.seek(0)
                        for d2line in d2r:
                            words2 = d2line.strip('\r\n').split(',')
                            if flag_head == 0:
                                d3w.write(d2line)
                                flag_head = 1
                                if words2[0] != words1[0]:
                                    flag_type_data = 1
                            elif flag_type_data == 0 and words1[0] == words2[0]:
                                d3w.write(d2line)
                            elif flag_type_data == 1 and words1[1] == words2[0]:
                                d3w.write(d2line)
                    print("New database done")
    except FileNotFoundError:
        print("You have a mistake in the name that you entered")


def make_new_databases(name1):
    find_data(name1, "customer.csv")
    # calling the function to find the customer info of the 1000 selected customers in the customer database
    find_data(name1, "invoice.csv")
    # calling the function to find the invoice info of the 1000 selected customers in the invoice database
    find_data("New_invoice.csv", "invoice_item.csv")
    # calling the function to find the invoice item info of the invoices
    # of the 1000 selected customers in the new invoice
