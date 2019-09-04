from datetime import datetime as dt

lines_to_be_added = ['LINE 1', 'LINE 2', 'LINE 3']

today = dt.now()
if  dt(today.year,today.month, today.day, 9)< today < dt(today.year,today.month, today.day, 17):
    with open('file.txt', 'r+') as fp:
        content = fp.read()     # content is a string 
        for line in lines_to_be_added:
            if not line in content:
                fp.write(line + '\n')
else:
    with open('file.txt', 'r+') as fp:
        content = fp.readlines() # content is a list
        fp.seek(0)
        for cont_lines in content:
            cont_lines = cont_lines[:-1]
            if not cont_lines in lines_to_be_added:
                fp.write(cont_lines+'\n')
        fp.truncate() # cut the rest of the text whereafter cursor is