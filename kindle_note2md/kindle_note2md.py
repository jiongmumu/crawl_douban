import csv
with open('./book.csv') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',')
  i = 0
  find = False
  bookname = ''
  result = ''
  for row in spamreader:
    i = i + 1
    if i == 2:
      bookname = row[0]
    if find and len(row) == 4:
      pages = [int(s) for s in row[1].split() if s.isdigit()]
      result = result + '>'+ row[3] + 'P' + str(pages[0]) + '\n\nC：\n\n'
    if len(row) > 0 and row[0].find('批注类型') != -1:
      find = True

with open(bookname + '.md', 'w') as f:
  f.write(result)
