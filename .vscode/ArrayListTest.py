from ArrayList import ArrayList
L = ArrayList(50)

print("최초 ", L)
L.insert(0,10)
L.insert(1,20)
L.insert(2,50)
print("삽입*3",L)
L.delete(2)
print(L)