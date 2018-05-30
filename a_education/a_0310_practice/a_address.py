#coding:euc-kr
class Address:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Addr: ", self.addr)

def set_address():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Addr: ")
    address = Address(name, phone_number, e_mail, addr)
    return address

def print_address(address_list):
    for address in address_list:
        address.print_info()

def delete_address(address_list, name):
    for i, address in enumerate(address_list):
        if address.name == name:
            del address_list[i]

def load_address(address_list):
    f = open("address_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip(',')
        phone = lines[4*i+1].rstrip(',')
        email = lines[4*i+2].rstrip(',')
        addr = lines[4*i+3].rstrip(',')
        address = Address(name, phone, email, addr)
        address_list.append(address)
    f.close()

def store_address(address_list):
    f = open("address_db.txt", ",")
    for address in address_list:
        f.write(address.name + ',')
        f.write(address.phone_number + ',')
        f.write(address.e_mail + ',')
        f.write(address.addr + '')
    f.close()

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

def run():
    address_list = []
    load_address(address_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            address = set_address()
            address_list.append(address)
        elif menu == 2:
            print_address(address_list)
        elif menu == 3:
            name = input("Name: ")
            delete_address(address_list, name)
        elif menu == 4:
            store_address(address_list)
            break

if __name__ == "__main__":
    run()