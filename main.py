'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n <= 1:
     return False
  for i in range (2, n//2):
    if n % i == 0:
      return False
  return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  p = 1
  for i in lst:
    p *= int(i)
  return p
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  if y == 0:
    return x
  else:  
    return get_cmmdc_v1(y, x % y)
      
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while x != y: 
    if x > y:
      x = x - y
    else:
      y = y - x
  return y
  
  
  
def main():
  print("1. Verificarea primalitatii unui nr.")
  print("2. Produsul elementelor unei liste.")
  print("3. Cel mai mare divizor comun (v1).")
  print("4. Cel mai mare divizor comun (v2).")


  while True:
    opt = int(input("Introduceti optiunea: "))
    if opt == 1:
      x = int(input("introduceti numarul: "))
      if is_prime(x):
        print(x, "este numar prim\n" )
      else:
        print(x, "nu este numar prim\n")
      
    elif opt == 2:
      lista_numere = input("Introduceti numerele: ")
      lst = lista_numere.split()
      print(get_product(lst), "este produsul numerelor din lista\n")
    
    elif opt == 3:
      x = int(input("Introduceti primul nr: "))
      y = int(input("Introduceti al doilea nr: "))
      print(get_cmmdc_v1(x, y), "este cmmmdc-ul nr\n")

    elif opt == 4:
      x = int(input("Introduceti primul nr: "))
      y = int(input("Introduceti al doilea nr: "))
      print(get_cmmdc_v2(x, y), "este cmmmdc-ul nr\n")

    else:
      break
    

if __name__ == '__main__':
  main()
