print('==================================================================')
print('                Fibonnaci Sequence')
print('==================================================================')

terms = int(input("How many terms? "))

first = 0
second = 1
count = 0

if terms <= 0 or terms == 1:
	print('try positive numbers only higher than 1')
elif terms == 1:
	print('positive numbers only')
else:
	while count < terms:
		print(first)
		nth = first + second

		first = second
		second = nth
		count += 1