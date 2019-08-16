# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

def donuts(count):
  # +++your code here+++
  # LAB(begin solution)
  if count < 10:
    return print('Number of donuts: ' + str(count))
  else:
    return print('Number of donuts: many')
  # LAB(replace solution)
  # return
  # LAB(end solution)
donuts(5)
donuts(-5)
donuts(10)
donuts(550)