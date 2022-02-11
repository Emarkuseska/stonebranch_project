import os


def find_data(data1, data2):
    try:
        with open(data1, 'r') as d1r:
            try:
                with open(data2, 'r') as d2r:
                    data3 = "New_" + os.path.basename(data2)
                    try:
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
                    except PermissionError:
                        print(f"You have no permission to open {data3}, the csv file might be already opened.")
            except FileNotFoundError:
                print("The second database or path doesn't exist")
    except FileNotFoundError:
        print("The first database or path doesn't exist")
