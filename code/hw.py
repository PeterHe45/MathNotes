#! python3

import sys

NAME_IDX = 0
PHONE_IDX = 1
OFFICE_IDX = 2

INFO_TEXT = "Input the following function ID to operate:\n 1. List staff info in alphabetical order\n 2. List staff info by offices\n 3. Add a new staff\n 4. Quit\n 5. Help"
    
class Staff:
    def __init__(self, name, phone, office):
        self.name = name
        self.phone = phone
        self.office = office

    def print_info(self):
        print("%s\t %s\t %s" %(self.name, self.phone, self.office))
        
    
class StaffManager:
    def __init__(self, staff_list):
        self.staff_list = staff_list

    def print_staff_aphabetically(self):
        self.staff_list.sort(key=lambda x: x.name)
        for staff in self.staff_list:
            staff.print_info()

    def print_staff_by_office(self):
        data = {}
        for staff in self.staff_list:
            office = staff.office
            if not office in data:
                data[office] = [staff]
            else:
                data[office].append(staff)

        for k in data.keys():
            print('++ Office %s ++' % k)
            for staff in data[k]:
                staff.print_info()
            print("\n")
    
    def add_new_staff(self):
        while True:
            print("Please input: <name> <phone> <office>")
            info = input()
            tokens = info.split()
            if len(tokens) != 3:
                print("invalid input!")
            else:
                name = tokens[NAME_IDX].strip()
                phone = tokens[PHONE_IDX].strip()
                office = tokens[OFFICE_IDX].strip()

                staff = Staff(name, phone, office)
                self.staff_list.append(staff)
                print("New staff added successfully!")
                break

def init_staff_with_data(filename):
    staff_list = []
    
    f = open(filename, 'r')
    line = f.readline()
    while line:
        tokens = line.split(',')

        name = tokens[NAME_IDX].strip()
        phone = tokens[PHONE_IDX].strip()
        office = tokens[OFFICE_IDX].strip()

        staff = Staff(name, phone, office)
        staff_list.append(staff)
        
        line = f.readline()
        
    f.close()

    return staff_list

        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)

    filename = sys.argv[1]
    staff_list = init_staff_with_data(filename)
   
    staff_manager = StaffManager(staff_list)

    print(INFO_TEXT)
    
    while True:
        print("----\nYour input here:")
        option = input()

        if option == '1':
            staff_manager.print_staff_aphabetically()
        elif option == '2':
            staff_manager.print_staff_by_office()
        elif option == '3':
            staff_manager.add_new_staff()
        elif option == '4':
            print('Terminating the program ... done!')
            break
        elif option == '5':
            print(INFO_TEXT)
        else:
            print("Invliad input! Please input correct option number:")
        
    
