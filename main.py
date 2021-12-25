names_list = ["Rickey", "Bobby", "Micheal", "Ronnie", "Johnny", "Ralph"]
names_list.append("Ben")
names_list.insert(3, 'Jerry')
names_list.pop()

names_list = ["Rickey", "Bobby", "Micheal", "Ronnie", "Johnny", "Ralph", "Ben", "Jerry"]
del names_list[7]

names_list = ["Rickey", "Bobby", "Micheal", "Ronnie", "Johnny", "Ralph", "Ben", "Jerry"]
del names_list[5]

names_list = ["Rickey", "Bobby", "Micheal", "Johnny", "Ralph", "Ben", "Jerry"]
names_list = sorted(names_list)
print(names_list)
