# A.-Square-String-
t = int(input())
for _ in range(t):
	_str = input().strip()
	ln = len(_str) // 2
	if len(_str) % 2 == 0:
		if _str[:ln] == _str[ln:]:
			print('YES')
		else:
			print('NO')
	else:
		print('NO')
