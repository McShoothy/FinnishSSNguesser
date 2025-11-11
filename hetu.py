lst = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","H","J","K","L","M","N","P","R","S","T","U","V","W","X","Y"]

def generate_possible_ssns(bday, gender, ccs):
    CS = lst.index(ccs)

    print("Possible SSNs:")

    for i in range(0, 1000):
        if (i + int(bday) * 1000) % 31 == CS and ((gender == "M" and i % 2 == 1) or (gender == "F" and i % 2 == 0)):
            print(f"{bday}A{i} {ccs}")

def main():
    bday = input("birthday (DD/MM/YY): ")
    gender = input("gender (M/F): ")
    ccs = input("last character of your SSN: ")

    generate_possible_ssns(bday, gender, ccs)

if __name__ == "__main__":
    main()
