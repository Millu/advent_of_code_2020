file_path = 'input.txt'

def read_file(path):
	nums = {}
	with open(path) as f:
		for line in f:
			nums[int(line)] = 0
	return nums

def find_answer(nums):
	for n in nums:
		new_sum = 2020-n
		for y in nums:
			if new_sum-y in nums:
				return (n*y*(2020-n-y))

nums = read_file(file_path)
print(find_answer(nums))
