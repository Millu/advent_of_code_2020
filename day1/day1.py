file_path = 'input.txt'

def read_file(path):
	nums = {}
	with open(path) as f:
		for line in f:
			nums[int(line)] = 0
	return nums


def find_answer(nums):
	for n in nums:
		if 2020-n > nums:
			return (n*(2020-n))

nums = read_file(file_path)
print(find_answer(nums))