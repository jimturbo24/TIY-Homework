This is a nice module that checks a script for its pep8-ness.

~/git/TIY-Homework/week_3 $pip3 install pep8
Collecting pep8
  Downloading pep8-1.7.0-py2.py3-none-any.whl (41kB)
    100% |████████████████████████████████| 51kB 629kB/s
Installing collected packages: pep8
Successfully installed pep8-1.7.0
~/git/TIY-Homework/week_3 $cd ../week_2/
~/git/TIY-Homework/week_2 $pep8 blackjack.py
blackjack.py:4:1: E302 expected 2 blank lines, found 1
blackjack.py:146:80: E501 line too long (84 > 79 characters)
blackjack.py:155:80: E501 line too long (84 > 79 characters)
~/git/TIY-Homework/week_2 $cd ../week_1/
~/git/TIY-Homework/week_1 $pep8 mysteryWord.py
mysteryWord.py:6:5: E265 block comment should start with '# '
mysteryWord.py:10:9: E265 block comment should start with '# '
mysteryWord.py:32:19: E225 missing whitespace around operator
mysteryWord.py:53:32: E231 missing whitespace after ','
mysteryWord.py:53:36: E231 missing whitespace after ','
mysteryWord.py:62:80: E501 line too long (88 > 79 characters)
mysteryWord.py:64:80: E501 line too long (86 > 79 characters)
mysteryWord.py:67:80: E501 line too long (82 > 79 characters)
mysteryWord.py:71:80: E501 line too long (87 > 79 characters)
mysteryWord.py:75:80: E501 line too long (83 > 79 characters)
mysteryWord.py:76:80: E501 line too long (81 > 79 characters)
mysteryWord.py:82:80: E501 line too long (80 > 79 characters)
