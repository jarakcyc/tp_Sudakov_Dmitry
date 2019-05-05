import os

with open('./utest/num.txt', 'r') as f:
	cnt_sessions = int(f.read())

cnt_sessions += 1

with open('./utest/session_' + str(cnt_sessions) + '.txt', 'w+') as f:
	while 1:
		i = input()

		if i == 'break':
			break

		os.system(i)
		print('\nresult(+/-): ')
		result = input()

		f.write(i)
		f.write(' ' + result + '\n')

with open('./utest/num.txt', 'w') as f:
	f.write(str(cnt_sessions))