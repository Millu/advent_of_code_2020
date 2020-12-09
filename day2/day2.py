file_path = 'input.txt'

def read_file(path):
	passwords = []
	with open(path) as f:
		for line in f:
			passwords.append(line)
	return passwords

def verify(passwords):
	valid_passwords = 0
	for p in passwords:
		rule = p.split(':')[0]
		password_text = p.split(':')[1].strip()
		rule_breakdown = rule.split()
		min_pos = int(rule_breakdown[0].split('-')[0]) - 1
		max_pos = int(rule_breakdown[0].split('-')[1]) - 1
		letter = rule_breakdown[1][0]
		# print("'"+password_text+"'", letter, min_pos, max_pos)
		if bool(password_text[min_pos] == letter) ^ bool(password_text[max_pos] == letter):
			valid_passwords = valid_passwords + 1
	return valid_passwords

passwords = read_file(file_path)
print(verify(passwords))
