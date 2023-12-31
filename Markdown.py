command_list = [
  'plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line',
  '!help', '!done', 'unordered-list', 'ordered-list'
]


def print_help():
  print(
    'Available formatters: plain bold italic header link inline-code new-line unordered-list and ordered-list'
  )
  print('Special commands: !help !done')


def choice():
  user_input = input('Choose a formatter: ')
  return user_input


def plain(formatted_text):
  text = input('Text:')
  return formatted_text + text


def bold(formatted_text):
  text = input('Text:')
  return formatted_text + f'**{text}**'


def italic(formatted_text):
  text = input('Text:')
  return formatted_text + f'*{text}*'


def header(formatted_text):
  level = int(input('Level:'))
  while not (1 <= level <= 6):
    print('The level should be within the range of 1 to 6')
    level = int(input('Level:'))
  text = input('Text:')
  return formatted_text + f"{'#' * int(level)} {text}\n"


def link(formatted_text):
  label = input('Label:')
  url_adress = input('URL:')
  return formatted_text + f'[{label}]({url_adress})'


def inline_code(formatted_text):
  code = input('Text:')
  return formatted_text + f'`{code}`'


def new_line(formatted_text):
  return formatted_text + '\n'


def ordered_list(formatted_text):
  row_list = []
  rows = int(input('Number of rows:'))
  while rows < 1:
    print('The number of rows should be greater than zero')
    rows = int(input('Number of rows:'))
  else:
    for i in range(1, rows + 1):
      row_list.append(input(f'Row #{i}:'))
    for i in range(1, rows + 1):
      formatted_text += f'{i}. {row_list[i-1]}\n'
    return formatted_text


def unordered_list(formatted_text):
  row_list = []
  rows = int(input('Number of rows:'))
  while rows < 1:
    print('The number of rows should be greater than zero')
    rows = int(input('Number of rows:'))
  else:
    for i in range(1, rows + 1):
      row_list.append(input(f'Row #{i}:'))
    for i in range(1, rows + 1):
      formatted_text += f'- {row_list[i-1]}\n'
    return formatted_text


def save_to_file(formatted_text):
  with open('output.md', 'w') as file:
    file.write(formatted_text)


formatted_text = ""
while True:
  user_input = choice()
  if user_input == '!done':
    save_to_file(formatted_text)
    break
  elif user_input == '!help':
    print_help()
  elif user_input not in command_list:
    print('Unknown formatting type or command')
    continue
  elif user_input == 'plain':
    formatted_text = plain(formatted_text)
  elif user_input == 'bold':
    formatted_text = bold(formatted_text)
  elif user_input == 'italic':
    formatted_text = italic(formatted_text)
  elif user_input == 'header':
    formatted_text = header(formatted_text)
  elif user_input == 'link':
    formatted_text = link(formatted_text)
  elif user_input == 'inline-code':
    formatted_text = inline_code(formatted_text)
  elif user_input == 'new-line':
    formatted_text = new_line(formatted_text)
  elif user_input == 'unordered-list':
    formatted_text = unordered_list(formatted_text)
  elif user_input == 'ordered-list':
    formatted_text = ordered_list(formatted_text)
  print(formatted_text)
