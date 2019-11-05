def brackets_check(string):
  brackets = []
  opening_brackets = ['(', '[', '{']
  closing_brackets = [')', ']', '}']

  for i, char in enumerate(string):
    if char in closing_brackets:
      if len(brackets) == 0 or brackets.pop()[0] != opening_brackets[closing_brackets.index(char)]:
        return (i + 1)
    elif char in opening_brackets:
      brackets.append((char, i))
  if len(brackets) > 0:
    return (brackets.pop()[1] + 1)
  return 'Sucess'
  
if __name__ == '__main__':
    string = input()
    print(brackets_check(string))
