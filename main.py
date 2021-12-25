Exercise Lab 1:
  
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

Exercise Lab 2:
  
num_list = ['0','1','2','3','4']
print(num_list)

num_list.append('5')
print(num_list)

num_list = ['0','1','2','3','4']
num_list.insert(0,7)
print(num_list)

num_list = ['0','1','2','3','4']
del num_list[2]
print(num_list)

num_list = ['0','1','2','3','4']
num_list.sort(unsort=True)
print(num_list)


num_list = ['5','6','7', '8','9']
print(num_list)

num_list = ['0','1','2','3','4','5','6','7','8','9']
print(num_list)
