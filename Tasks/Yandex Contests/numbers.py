n = int(input())
numbers = {}

array = list(map(int, input().split()))

for x in array:
	if x in numbers.keys():
		numbers[x] += 1
	else:
		numbers[x] = 1

print(max(numbers.items(), key=lambda x: x[1])[0])