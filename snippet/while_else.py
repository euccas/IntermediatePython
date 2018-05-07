def find(seq, target):
	x = 0
	while x < len(seq):
		if seq[x] == target:
			break
		else:
			x += 1
	else:
		return -1
	return x

def find2(seq, target):
	found = -1
	x = 0
	while x < len(seq):
		if seq[x] == target:
			found = x
			break
		else:
			x += 1
	return found

if __name__ == "__main__":
	seq = [1,2,3,4,5]
	print("find, pos = {0}".format(find(seq, 4)))
	print("find2, pos = {0}".format(find2(seq, 4)))
	print("find, pos = {0}".format(find(seq, 6)))
	print("find2, pos = {0}".format(find2(seq, 6)))