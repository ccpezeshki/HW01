#---------------- Problem 4 ------------------
#
# Name:
#
# Who did you work with (if anyone)?:
#
# --------------------------------------------

def find_area(A,B,d): # Don't change this line, it is for my own purposes
    # Your code goes below here and WILL NEED TO BE INDENTED like
    # these comments are (sorry, it has to do with my own purpose above)

    # Your initial variables are named A, B and d and will have the values
    # you indicated below.
    A, B, d = 1,2,3 
tiny_bottom = A - d / 2
tiny_height = (tiny_bottom) / A * B

big_bottom = A - (d / 2) / 2
big_height = (big_bottom) / A * B

area = (big_bottom * big_height / 2 - tiny_bottom * tiny_height / 2) * 2
if d>A :
    print ("doesn't work")
    # Print whatever the final area is here! Just the value please, nothing else.
    print(area)




if __name__ == '__main__': # please don't change
    # You can change the below values of A, B, and d to try different combinations
    A = 10
    B = 5
    d = 5

    find_area(A,B,d) # don't change this line or add anything below this
