# מבקש מהמשתמש שם קובץ, ואח"כ המשתמש מכניס שורות כל פעם של טקסט, ואז שהוא מסיים זה שורה ריקה
filename = input("enter your")
f = open(filename, 'a')

while True:
    text = input("your text here:")
    if text == "":
        break
    f.write(text + '\n')


