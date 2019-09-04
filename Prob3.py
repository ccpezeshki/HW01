numx=5
numy=9
numz=7

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
if numx%2==0 and numy%2==0 and numz%2==0:
    print("No odd numbers found")
