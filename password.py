password = 'a123456'
i = 3
while True:
	pwd = input('please enter your password: ')
	if pwd == password:
		print('you are correct!')
		break
	else:
		i = i - 1
		if i > 0:
			print('you have', i , 'times')
		else:
			break
