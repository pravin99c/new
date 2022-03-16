import os,glob
# os.remove("geek.txt")
# print(os.getcwd())# output is  current working directory

# os.chdir('/server/accesslogs')   # Change current working directory
# os.system('mkdir today')   # Run the command mkdir in the system shell



# print(dir(os))
# <returns a list of all module functions>
# help(os)
# <returns an extensive manual page created from the module's docstrings> 

# x=os.getcwd()
# print(x)
# print(os.chdir(f'{x}/python_training/data_structure'))
# print(glob.glob('*.py'))

from datetime import date
now = date.today()
now
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

# dates support calendar arithmetic
birthday = date(1999, 6, 12)
age = now - birthday
age.days
print(age)