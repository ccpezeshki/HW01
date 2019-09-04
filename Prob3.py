#---------------- Problem 3 ------------------
#
# Name:
#
# Who did you work with (if anyone)?:
#
# --------------------------------------------


def big_odd_finder():
# Pls don't change this line, for my own purposes
    # Your code goes below here and WILL NEED TO BE INDENTED like
    # these comments are (sorry, it has to do with my own purpose above)

    # Prompt for variable inputs
numx=5
numy=9
numz=7
    # Logic to check for being largest odd:
if not numx%2==0 and numy%2==0 and numz%2==0:
    print(numx)
if numx%2==0 and not numy%2==0 and numz%2==0:
    print(numy)
if numx%2==0 and numy%2==0 and not numz%2==0:
    print(numz)
if not numx%2==0 and not numy%2==0 and numz%2==0 and numx>numy:
    print(numx)
if not numx%2==0 and numy%2==0 and not numz%2==0 and numx>numy:
    print(numx)
if not numx%2==0 and not numy%2==0 and numz%2==0 and numy>numx:
    print(numy)
if numx%2==0 and not numy%2==0 and not numz%2==0 and numy>numz:
    print(numy)
if not numx%2==0 and numy%2==0 and not numz%2==0 and numz>numx:
    print(numz)
if numx%2==0 and not numy%2==0 and not numz%2==0 and numz>numy:
    print(numz)
if not numx%2==0 and not numy%2==0 and not numy%2==0 and numx>numy and numx>numz:
    print(numx)
if not numx%2==0 and not numy%2==0 and not numy%2==0 and numy>numx and numy>numz:
    print(numy)
if not numx%2==0 and not numy%2==0 and not numy%2==0 and numz>numx and numz>numy:
    print(numz)
    # Print out largest odd value
    # or "No odd numbers found." if no odds exist
if numx%2==0 and numy%2==0 and numz%2==0:
    print("No odd numbers found")


# Don't modify code below here please!
if __name__ == '__main__':
    big_odd_finder()
