tup =  (2,3,4,6,4,) 
print(tup)
print(type(tup))
print(tup[2])
# tup[0]=3 not allowed in python
# Tuple is immutable
tuple = (5,)
print(type(tuple))
print(tup[1:4])
print(tup.index(4))
print(tup.count(4))
movies = []
mov1 = input(" Write movie1 name")
mov2 = input("Write movie2 name")
mov3 = input("Write movie3 name")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
# Palindrom list
list = [1,3,5,3,1,]

copy_list = list.copy()
print(copy_list)
copy_list.reverse()

if(copy_list == list):
    print("list is palindrom")
else:
    print("list is not palindrom")
Grades = ("C","D","A","A","B","B","A")
print(Grades)
print(Grades.count("A"))
jack = ["C","D","A","A","B","B","A"]
jack.sort()
print(jack)