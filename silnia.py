def rekursja(podstawa):
     if (podstawa < 1):
          return 1
     else:
          return podstawa * rekursja(podstawa - 1)

print("Wskaż liczbę od której chcesz obliczyć silnię")
liczba = int(input())
print(rekursja(liczba))