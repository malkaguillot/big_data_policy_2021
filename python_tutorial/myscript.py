'''
NOTIONS

comments: # or three apostrophes for multiline

single equal sign: =  'take the value of'
double equal sign: == 'is equal to'

Dataframe columns = variables / rows = observations

inputs: data you will use (beginning = import)
outputs: result of your data manipulation (end = export)

functions take arguments (inputs), apply changes to it, then returns an output

module: set of useful python scripts
'''


'''
IMPORT MODULES AND DATA
'''

import os

os.chdir('/home/leops95/Desktop/python_course/')


import pandas as pd

df_econ = pd.read_csv('grades_econ.csv')   #read_excel, read_dta, read_pickle

df_econ.to_pickle('grades_econ.pkl')



'''
DATA SELECTION
'''

df_grades = df_econ[['student_id', 'grade']] #.groupby('student_id').mean()

brainiacs = df_econ[(df_econ['grade'] == 6) & (df_econ['course'] == 'Microeconomics')]

# | == 'or' operator
# & == 'and' operator



'''
EFFICIENT DATA MANIPULATION
'''

# loops are inefficient, use functions instead

def function_name(arg):
    new_grade = arg - 1
    
    return new_grade


df_econ['new_grade'] = df_econ['grade'].apply(function_name)



# multiple outputs

import numpy as np

def function_name(arg):
    new_grade = arg - 1
    
    passed = np.where(new_grade >= 4, True, False)
    
    return new_grade, passed


df_econ['new_grade'], df_econ['success'] = zip(*df_econ['grade'].apply(function_name))


# multiple inputs

def function_name(arg, arg2):
    new_grade = arg - 1
    
    passed = np.where(new_grade >= 4, True, False)
    
    if arg2 == 'Business Cycles':
        arg2 = 'Macroeconomics'
    
    return new_grade, passed, arg2


df_econ['new_grade'], df_econ['success'], df_econ['course'] = zip(*df_econ.apply(lambda x: function_name(x['grade'], x['course']), axis = 1))


# axis = 1 observations/ rows
# axis = 0 variables / columns


'''
APPEND AND MERGE DATASETS
'''

df_law = pd.read_csv('grades_law.csv')
df_majors = pd.read_csv('majors.csv')


# appending files

df_all = df_econ.append(df_law)


# merge files

df_merge = df_all.merge(df_majors, how = 'outer')

