array = [x for x in range((int(input("Enter your starting range: "))),(int(input("Enter your ending range: "))+1))]
squares = list(map(lambda x: x**2, array))
for i in squares:
    print(i)