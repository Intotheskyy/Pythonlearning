# for x in range(1, 21):
#     if x == 13 or x == 4:
#         print(f"{x} is unlucky")
#     elif x % 2 == 0:
#         print(f"{x} is even")
#     else:
#         print(f"{x} is odd")

for x in range(1, 21):
    if x == 13 or x == 4:
        state = "unlucky"
    elif x % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print(f"{x} is {state}")
