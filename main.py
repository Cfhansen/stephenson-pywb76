###solution to exercise 76 in ben stephenson's "the python workbook".

factor = 2
prime_factors = []

num = int(input('Enter an integer:'))
original_num = num

if num < factor:
  print('Unacceptable value.')
else:
  while factor <= num:
    if num % factor:
      factor += 1
    else:
      prime_factors.append(factor)
      num = num / factor

print(f'The prime factors of {original_num} are:')
for n in prime_factors:
  print(n)
