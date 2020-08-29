# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 14:34:14 2020

@author: saura
"""
import pprint
# for printing in matrix format, for styly :-P, and readability ofcourse

puzzle_li = [
    [0,0,6,0,0,7,0,0,0],
    [0,0,0,9,0,0,0,0,5],
    [0,5,0,0,2,0,1,0,0],
    [0,0,0,0,0,0,5,6,0],
    [0,8,0,0,7,3,0,0,0],
    [9,0,0,1,0,0,0,0,0],
    [8,0,0,0,0,0,0,1,3],
    [0,0,9,0,8,0,0,0,7],
    [5,3,0,0,0,0,0,0,4]
    ]
# this is the input, non-zero values are fixed, and code won't touch them.


def num_possible(li):
    '''
    this fuction takes the input list as parameter and appends an empty list with the index values (in a list format)
    of the 'puzzle_li' list where the value is 0
    '''
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i][j] == 0:
                possible_index_list.append([i,j])

def transpose(li):
    '''
    this function just transposes the list passed to it
    '''
    trans_li = []
    for i in range(len(li)):
        row = []
        for item in li:
            row.append(item[i])
        trans_li.append(row)
    return trans_li

def soduku_solver(li):
    '''
    this function solves the sudoko, and returns True once it's solved
    '''
    for i,j in possible_index_list:
        if li[i][j] == 0:
            num_li = assign_num(i,j,li)
            if num_li == []:
                return False
            for num in num_li:
                li[i][j] = num
                func_return = soduku_solver(li)
                if func_return:
                    break
            if not func_return:
                li[i][j] = 0
                return False
            elif func_return:
                return True
    return True

def assign_num(i,j,li):
    '''
    this function takes the index and the list as parameters, and returns a list of the numbers which can
    be written on that index (by validating the corresponding row, column, and box entries)
    '''
    temp_li = []
    for num in range(1,10):
        if (num not in li[i]) and (num not in transpose(li)[j]) and (num not in box(i,j,li)):
            temp_li.append(num)
    return temp_li
            
def box(i,j,li):
    '''
    this function takes the index and the list as parameters, and returns a list of the numbers which contains
    all the numbers which are there in that particular box (the box in which the index is present)
    '''
    temp_list = []
    if i in [0,1,2]:
        if j in [0,1,2]:
            for a in [0,1,2]:
                for b in [0,1,2]:
                    temp_list.append(li[a][b])
            return temp_list
        elif j in [3,4,5]:
            for a in [0,1,2]:
                for b in [3,4,5]:
                    temp_list.append(li[a][b])
            return temp_list
        elif j in [6,7,8]:
            for a in [0,1,2]:
                for b in [6,7,8]:
                    temp_list.append(li[a][b])
            return temp_list
    elif i in [3,4,5]:
        if j in [0,1,2]:
            for a in [3,4,5]:
                for b in [0,1,2]:
                    temp_list.append(li[a][b])
            return temp_list
        elif j in [3,4,5]:
            for a in [3,4,5]:
                for b in [3,4,5]:
                    temp_list.append(li[a][b])
            return temp_list
        elif j in [6,7,8]:
            for a in [3,4,5]:
                for b in [6,7,8]:
                    temp_list.append(li[a][b])
            return temp_list
    elif i in [6,7,8]:
        if j in [0,1,2]:
            for a in [6,7,8]:
                for b in [0,1,2]:
                    temp_list.append(li[a][b])
            return temp_list
        elif j in [3,4,5]:
            for a in [6,7,8]:
                for b in [3,4,5]:
                    temp_list.append(li[a][b])
            return temp_list
        elif j in [6,7,8]:
            for a in [6,7,8]:
                for b in [6,7,8]:
                    temp_list.append(li[a][b])
            return temp_list
    return 0

def soduku_checker(li):
    '''
    this function takes the solved sudoku as the argument and returns True if the sudoku is correctly solved
    this fuction is actually not required as the soduku_solver function takes care of these things
    '''
    for i in range(9):
        for j in range(9):
            if li[i].count(li[i][j]) > 1 or transpose(li)[j].count(li[i][j]) > 1 or box(i,j,li).count(li[i][j]) > 1 or li[i][j] < 1 or li[i][j] > 9:
                return False
    return True
            
possible_index_list = []
num_possible(puzzle_li)    
# this appends the 'possible_index_list' with the index values (in a list format) of the 'puzzle_li' list where the value is 0

soduku_solver(puzzle_li)    # this solves the sudoku

pprint.pprint(puzzle_li)
print(soduku_checker(puzzle_li))    # prints True, if the sudoku is correct solved
