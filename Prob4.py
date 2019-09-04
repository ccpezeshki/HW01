A, B, d = 1,2,3 

tiny_bottom = A - d / 2
tiny_height = (tiny_bottom) / A * B

big_bottom = A - (d / 2) / 2
big_height = (big_bottom) / A * B

area = (big_bottom * big_height / 2 - tiny_bottom * tiny_height / 2) * 2
if d>A :
    print ("doesn't work")
print(area)

