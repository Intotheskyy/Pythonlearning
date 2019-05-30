# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food == 'apple' or food == 'grape':
    print(f"You got {food}. This is fruit")
elif food == 'bacon' or food == 'steak':
    print(f"You got {food}. This is meat")
else:
    print(f"You got {food}. Yuck!")


# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
