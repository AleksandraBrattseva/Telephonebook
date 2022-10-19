from os.path import exists
from file_work import creating
from file_work import writing_scv
from file_work import writing_txt

path = 'file.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()