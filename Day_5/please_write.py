filename = 'guest.txt'
name = ''
with open(filename,'a') as file_object:
	while(True):
		name = input("Please inupt your name:")
		if name == "\r\n":
			break
		print("How are you?")
		file_object.write(name+"\n")

