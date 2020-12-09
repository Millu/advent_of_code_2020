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
		password_text = p.split(':')[1]
		rule_breakdown = rule.split()
		min_repeats = int(rule_breakdown[0].split('-')[0])
		max_repeats = int(rule_breakdown[0].split('-')[1])
		letter = rule_breakdown[1][0]
		count = p.count(letter) - 1
		if count >= min_repeats and count <= max_repeats:
			valid_passwords = valid_passwords + 1
	return valid_passwords

passwords = read_file(file_path)
print(verify(passwords))
