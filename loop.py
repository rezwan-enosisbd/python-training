import random
# WHILE LOOP
random_number = random.randint(1, 3)
limit = int(input('How many time try: '))
tried = 0

while tried < limit:
  entry = int(input('Your guess: '))
  tried += 1

  if entry == random_number:
    print("You won")
    break
else:
  print('Sorry, you didn\'t guess right')


# FOR LOOP
# pattern

line = 5
for i in range(5):
  for j in range(i+1):
    print("*", end='')
  print()


