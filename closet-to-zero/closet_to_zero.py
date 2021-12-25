'''The starting files are unrelated to the exercise.

They simply show syntax for writing and testing
  o) a global function
  o) an instance method
Pick the style that best fits the exercise.
Then delete the other one, along with this comment!
'''

'''Given a list of integers find the closest to zero.
If there is a tie, choose the positive value.
'''

def closet_to_zero(arr):
    if len(arr) < 1:
        return None
    closet = arr[0]
    for i in range(1, len(arr)):
        abs_val = abs(arr[i])
        abs_closet = abs(closet)
        if abs_val < abs_closet:
            closet = arr[i]
        elif abs_val == abs_closet:
            if arr[i] > closet:
                closet = arr[i]
    return closet
    

