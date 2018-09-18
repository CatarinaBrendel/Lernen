print "-" * 45
print "{:^45}".format("Price List")
print "-" * 45

tup = ('Pencil', 0.15, 'Eraser', 0.20, 'Notebook', 2.00, 'Ruler', 1.20, 'Backpack', 15.00, 'Book', 14.50)

for i in range(0,len(tup)-1,2):
    print "{:.<36}{} {:5.2f}".format(tup[i],"E$", tup[i+1])
print "-" * 45