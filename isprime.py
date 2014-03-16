def isPrime(x):
  for i in range(2, x):
    if x%i ==0:
        return "This is not Prime"
    else:
       return "This is prime"
if __name__ == "__main__":
  x = raw_input("Please enter a number")
  try:
    print isPrime(int(x))
  except:
    print "This is not a number"
