import json

database = {
	'home': 'nha', 
	'baby':'em be'
}

try:
	with open('database.json') as f_obj:
		database = json.load(f_obj)
except FileNotFoundError:
	with open('database.json', 'w') as f_obj:
		json.dump(database, f_obj)

def show_menu():
 print('--------------------')
 print('Chuong trinh tu dien')
 print('--------------------')
 print('1.Them tu')
 print('2.Tim tu')
 print('3.Xoa tu')
 print('4.Xem tat ca')
 print('Nhap 0 de thoat chuong trinh')
 print('-------------------')

show_menu()

def save_word():
	with open('database.json', 'w') as f_obj:
		json.dump(database, f_obj)

def add(word = ""):
	word = input('Tu moi : ')
	mean = input('Nghia cua no : ')
	database[word] = mean
	print('Tu da duoc them')
	save_word()

def add_new(word):
	mean = input('Nghia cua no : ')
	database[word] = mean
	print('Tu da duoc them')
	save_word()

def find():
	word = input('Tu ban muon tim : ')
	if word in database.keys():
		print(word + ': ' + database[word])
	else:
		new_word = input('Khong co tu ban tim, ban muon them ' + word + ' vao tu dien k? (y/n): ')
		if new_word == "y":
			add_new(word)

def delete():
	print('Xoa tu')
	word = input("Nhap tu muon xoa")
	del database[word]
	save_word()

def view_all():
	print('Xem tat ca')
	print(database)

while True:
	choice = input('Ban chon so : ')
	if choice == '0':
		break
	elif choice == '1':
		add()
	elif choice == '2':
		find()
	elif choice == '3':
		delete()
	elif choice == '4':
		view_all()


