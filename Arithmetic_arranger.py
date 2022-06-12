#!/usr/bin/env python
# coding: utf-8

# In[14]:


def arithmetic_arranger(problems, con = False):
    if len(problems) > 5 :
        return('Error: Too many problems.')

#Initializtion of lists, strings
foper = list()
soper = list()
opera = list()
res = list()
fline = str()
sline = str()
tline = str()
aline = str()

for problem in problems:
    problem.lstrip()
    problem.rstrip()
    sproblem = problem.split(" ")
    if len(sproblem[0]) > 4 or len(sproblem[2]) > 4:
        return('Error: Numbers cannot be more than four digits.')
    if not (sproblem[1] == '+' or sproblem[1] == '-'):
        return('Error: Operator must be \'+\' or \' -\'.')
    foper.append(sproblem[0])
    opera.append(sproblem[1])
    soper.append(sproblem[2])




counter = 0
while counter < len(problems):
    try:
        a = int(foper[counter])
        b = int(soper[counter])
    except:
        return('Error: Numbers must only contain digits.')
    if opera[counter] == '+':
        res.append(str(a + b))
    elif opera[counter] == '-':
        res.append(str(a - b))

#Finding the width of longest operand
long = max(len(foper[counter]), len(soper[counter]))

for val in range((long + 2) - len(foper[counter])):
    foper[counter] = ' ' + foper[counter]
    fline = fline + foper[counter] + '   '

#creating second line 
for val in range((long + 1) - len(soper[counter])):
    soper[counter] = ' ' + soper[counter]
    sline = sline + opera[counter] + soper[counter] + '  '

#creating third line
for val in range(long + 2):
    tline = tline + '-'
tline = tline + '  '
                 
#creating fourth line
for val in range((long + 2) - len(ren[counter])):
    res[counter] = '' + res[counter]
aline = aline + res[counter] + '  '

counter = counter + 1

#final output
fline = fline.rstrip()
sline = sline.rstrip()
tline = tline.rstrip()
aline = aline.rstrip()
if con == False:
    arranged_problems = fline + '\n' + sline + '\n' + tline
elif con == True:
    arranged_problems = fline + '\n' + sline + '\n' + tline + '\n' + aline


return arranged_problems


# In[ ]:





# In[ ]:




