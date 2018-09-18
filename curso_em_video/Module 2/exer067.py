print ("{:-^50}".format(" Das Einmaleins! "))

while True:
    n = int(input("Schreiben Sie hier einen Number: > "))
    print ("-" * 50)
    if n < 0:
        break
    for i in range(1, 10):
        print ("{} * {} = {}".format(n, i, n * i))
    print ("-" * 50)
print ("End des Programmes. Vielen Dank!")