# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import copy
import itertools
import xlsxwriter

while True:
    try:
        num_of_factors = int(input("Podaj liczbe czynników: "))
        break
    except:
        print("That's not a valid option!")

factors = []


for num in range(num_of_factors):
    temp_tuple = ()
    print ("Podaj trzy wartosci: najmniejsza, srodkowa oraz najwieksza dla czynnika nr.: ", num+1)
    while True:
        try:
            min_ = float(input("Najmniejsza: "))
            if min_ < 0:
                raise Exception
            mid_ = float(input("Srodkowa: "))
            if mid_ < 0:
                raise Exception
            max_ = float(input("Najwieksza: "))
            if max_ < 0:
                raise Exception
            break
        except:
            print("That's not a valid option!")



    temp_tuple = temp_tuple + (min_,) + (mid_,) + (max_,)
    print (temp_tuple)
    factors.append(temp_tuple)

#rysuje trojkaty, srodkowy na niebiesko
for i, ftc in enumerate(factors):
    fig = plt.figure()
    filename = 'plot' + str(i) + '.png'
    plt.plot([ftc[0], ftc[1]], [0, 1], color="blue")
    plt.plot([ftc[2], ftc[1]], [0, 1], color="blue")

    plt.plot([ftc[0], ftc[1]], [1, 0], color="red")

    plt.plot([ftc[2], ftc[1]], [1, 0], color="green")
    fig.savefig(filename)


sum_of_object = []

for element in itertools.product(*factors):
    sum_of_object.append(element)

pars = []


for i in range(len(sum_of_object)):
    for j in range(i+1, len(sum_of_object)):
        temp_pars = []
        par_1 = sum_of_object[i]
        par_2 = sum_of_object[j]
        temp_pars.append(par_1)
        temp_pars.append(par_2)
        pars.append(temp_pars)

matrix_MEJ = np.zeros((len(sum_of_object), len(sum_of_object)))
np.fill_diagonal(matrix_MEJ, 0.5)

for i in range(len(matrix_MEJ)):
    matrix_MEJ[i][j] = 0.5
    for j in range(i+1, len(matrix_MEJ)):
        print ("Pary do wyboru:", sum_of_object[i], sum_of_object[j])
        while True:
            try:
                result = int(input("Wybierz ktory obiekt lepszy, jeśli lewy wybierz 1, jeśli prawy wybierz 2, jeśli są rowne wybierz 3."))
                if result < 0 or result > 3:
                    raise Exception
                break
            except:
                print("That's not a valid option!")
        if result == 1:
            matrix_MEJ[i][j] = 1.0
            matrix_MEJ[j][i] = 0.0
        if result == 2:
            matrix_MEJ[i][j] = 0.0
            matrix_MEJ[j][i] = 1.0
        if result == 3:
            matrix_MEJ[i][j] = 0.5
            matrix_MEJ[j][i] = 0.5

SJ = np.sum(matrix_MEJ, axis=1)
# SJ.sort()

k = len(np.unique(SJ))
P = np.zeros((len(sum_of_object), 1))
for i in range(1, k+1):
    ind = int(SJ.argmax())
    P[ind] = (k - i) / float(k - 1)
    SJ[ind] = 0


object_and_P = [list(elem) for elem in sum_of_object]
for i in range(len(P)):
    object_and_P[i].extend(P[i])

workbook = xlsxwriter.Workbook('LBWIZ.xlsx')

worksheet = workbook.add_worksheet('MEJ')
row = 0
for col, data in enumerate(matrix_MEJ):
    worksheet.write_row(col, row, data)

worksheet2 = workbook.add_worksheet('Object and P')

row = 0
for col, data in enumerate(object_and_P):
    worksheet2.write_row(col, row, data)

workbook.close()


for i in range(len(object_and_P)):
    print("IF K1:", object_and_P[i][0], "AND", object_and_P[i][1], "AND", object_and_P[i][2], "THEN", object_and_P[i][3])




