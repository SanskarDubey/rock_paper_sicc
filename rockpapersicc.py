from random import choice
print("********************GAME******************************")
while True:
	while True:
		user_input=input("select \nr for Rock \ns for Scissors\np for Paper\n")

		if user_input not in {'r','p','s'}:
			print("\n\nsNOT VAILD INPUT \n TRY AGAIN!!!!!!!")
		else:
			break

	comp_input=choice(['r','p','s'])
	
	if(user_input==comp_input):
		print(" DRAW")
	elif(user_input=='r'and comp_input=='s'):
		print("YOU WIN !!!!!!!")
	elif(user_input=='s'and comp_input=='p'):
		print("YOU WIN !!!!!!!")
	elif(user_input=='r'and comp_input=='s'):
		print("YOU WIN !!!!!!!")
	else:
		print("YOU LOOSE !!!!!")
	break

