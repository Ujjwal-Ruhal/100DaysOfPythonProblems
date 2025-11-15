tup = (10,20,30,40,50,60)
tup_new = (60,) + tup[1:-1] + (10,)

print(f"Original tuple : {tup}")
print(f"Replace first and last element : {tup_new}")