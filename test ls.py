#
# kek = ["elie", "tim", "matt"]
# answer = [n[0].upper() for n in kek]
# print(answer)
#
# kek2 = [1, 2, 3, 4, 5, 6]
# answer2 = [num for num in kek2 if num % 2 == 0]
# print(answer2)

# answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
# answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
# Using good old manual loops:
#
# answer = []
# for person in ["Elie", "Tim", "Matt"]:
#     answer.append(person[0])
# answer2 = []
# for num in [1,2,3,4,5,6]:
#     if num % 2 == 0:
#         answer2.append(num)

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
answer = [num for num in [1, 2, 3, 4] if num in [1, 2, 3, 4] and num in [3, 4, 5, 6]]
print(answer)

# list3 = ["Elie", "Tim", "Matt"]
# answer2 = [list3[::-1] for let in list3]
# print(answer2)

Using list comprehensions(the more Pythonic way):

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]
Without list comprehensions, things are a bit longer:

answer = []
for x in [1,2,3,4]:
    if x in [3,4,5,6]:
        answer.append(x)
answer2 = []
for name in ["Elie", "Tim", "Matt"]:
    answer2.append(name[::-1].lower())

