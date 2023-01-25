#/----------SETUP_CODE----------\
from random import randint

def random_between_plus_minus_90():
  range_start = -89
  range_end = 89
  return randint(range_start, range_end)

def random_between_plus_minus_180():
  range_start = -179
  range_end = 179
  return randint(range_start, range_end)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

'''n = randint(1, 5)
n2 = randint(1, 5)
o1 = ('{0}.{1}'.format(random_between_plus_minus_90(), random_with_N_digits(n)))
o2 = ('{0}.{1}'.format(random_between_plus_minus_180(), random_with_N_digits(n2)))'''

def linker(x):
  i = 0
  while i < x:
    n = randint(1, 5)
    n2 = randint(1, 5)
    o1 = ('{0}.{1}'.format(random_between_plus_minus_90(), random_with_N_digits(n)))
    o2 = ('{0}.{1}'.format(random_between_plus_minus_180(), random_with_N_digits(n2)))
    print('https://www.google.com/maps/search/{0}+{1}/'.format(o1, o2))
    i += 1

x = 0
def input_eval():
  x = input('Number of links to generate: ')
  b = x.isnumeric()
  if b == True:
    x1 = int(x)
    linker(x1)
  else:
    print('Not a number!')
    input_eval()

#/----------PROGRAM_CODE----------\
print('Hello, welcome to Coordinator, the app that randomly generates coordinates on google maps!\n')
input_eval()
