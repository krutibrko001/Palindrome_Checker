
def is_palindrome():
  usr = list(input("Check your word: "))
  if usr[0:] == usr[::-1]:

    print(f'Its a palindrome: {"".join(usr)}')
  else:
    print(f'Your word is not a palindrome: {"".join(usr)}')

is_palindrome()
