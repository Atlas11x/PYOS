file = "test"
fyle_sys = []
act = "test"


import os
os.system("clear")

print("Type help for info")
while True:
	act = str(input("user>> "))
	if act == "help":
		print("commands: clear, crt, echo, fm, calc, exit")
	elif act == "clear":
		os.system("clear")
	elif act == "calc":
		print('for exit input ".."')
		while True:
			try:
				act = input("user>calc>")
				if act == "..":
					os.system("clear")
					break
				print("|Answer: " + str(eval(act)) + "|")
			except:
					os.system("clear")
					print("user> calc: Error")
					break


	elif act[0:4] == "crt ":
		l = len(act)
		file = act[4:]
		print("sys> saved")
	elif act[0:len(act)] == "echo":
		print("sys> " + file)
	elif act[0:len(act)] == "exit":
		os.system("clear")
		exit()
	elif act == "fm":
		os.system("clear")
		print("for help type help")
		while True:
			act = input("user>fylemod> ")
			if act[0:len(act)] == "..":
				os.system("clear")
				break
			elif act[0:2] == "n ":
				fyle_sys.append(act[2:len(act)])
				print("fm> saved")
			elif act[0:len(act)] == "fl":
				print(fyle_sys)
			elif act[0:4] == "del ":
				fyle_sys.pop(int(act[4:])-1)
			elif act == "clear":
				os.system("clear")
			elif act == "help":
				print("commands: clear, n, fl, del, .., echo")
			elif act[0:5] == "echo ":
				try:
					print("fm> " + str(fyle_sys[int(act[5:len(act)])-1]))
				except:
					print("fm>echo: Error")
			else:
				print("fm: Error")
	else:
		print(act + ": Error")
