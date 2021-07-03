import random

def primary():
  print("Keep it logically awesome.")
  f = open("E:/python-random-quote/quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  for i in quotes:
    print(i,end="")
  print('\nLast quote: ' + quotes[rnd])

def adddata():
  str1 = "This quote random-number is: " + str(random.randrange(0, 999))
  data = ['', str1]
  f = open("E:/python-random-quote/quotes.txt","a")
  f.writelines('\n'.join(data))
  f.close()

if __name__== "__main__":
  primary()
  adddata()

