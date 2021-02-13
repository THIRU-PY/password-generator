import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to password generator!!\n")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
ran_letters=''
ran_num=''
ran_symb=''
for let in range (1,nr_letters+1):
    ran_letters+=letters[random.randint(0,len(letters)-1)]
for sy in range (1,nr_symbols+1):
    ran_symb+=symbols[random.randint(0,len(symbols)-1)]
for num in range (1,nr_numbers+1):
    ran_num+=numbers[random.randint(0,len(numbers)-1)]
pass_gen=ran_letters+ran_symb+ran_num
print(f"Easy password: {pass_gen}\n")
hard_pass=random.sample(pass_gen,len(pass_gen))
emp_str=''
for ele in hard_pass:
    emp_str+=ele
print(f"Hard password: {emp_str}")
