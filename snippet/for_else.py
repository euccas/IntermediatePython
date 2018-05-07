def find(seq, target):
	for i, value in enumerate(seq):
		if value == target:
			break
	else:
		return -1
	return i

def find2(seq, target):
	found = -1
	for i, value in enumerate(seq):
		if value == target:
			found = i
			break
	return found

if __name__ == "__main__":
	seq = [1,2,3,4,5]
	print("find, pos = {0}".format(find(seq, 4)))
	print("find2, pos = {0}".format(find2(seq, 4)))
	print("find, pos = {0}".format(find(seq, 6)))
	print("find2, pos = {0}".format(find2(seq, 6)))