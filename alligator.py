#Rename A File with current date counter
import os
from datetime import date

b=str(date.today())
src = 'C:\\Users\\Anandram Mariappan\\Desktop\\rig.txt'
dst = 'C:\\Users\\Anandram Mariappan\\Desktop\\rig_'+b+'.txt'
os.rename(src, dst)
