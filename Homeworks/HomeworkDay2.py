#1.Question
mylist = [42, 32, 53, 12]

mylist1, mylist2 = mylist[:len(mylist)//2], mylist[len(mylist)//2:]

mylist2.extend(mylist1)
print(mylist2)


#2.Question

num = int(input("Enter a single digit number:\n"))

start, end = 0, num

for num in range(start, end):
  if num % 2 == 0:
    print(num, end = " ")

