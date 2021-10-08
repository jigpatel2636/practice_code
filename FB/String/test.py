def riddle (x,y):
   if x>0 & y>0:
    riddle(x/y, y)
    print(x%y)

riddle(6,2)