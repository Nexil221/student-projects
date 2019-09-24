# coding=utf-8
import numpy as np
import random
import math
import statistics



#Tworzenie planszy wraz z losowym ustawieniem hetmanów
def create_table():
    no_of_queens = input("Podaj liczbe hetmanów: ")
    chessboard = np.zeros(shape=(no_of_queens, no_of_queens))
    for j in range(no_of_queens):
        table_index = (random.randrange(0, no_of_queens))
        chessboard[table_index][j] = 1
    return chessboard, no_of_queens

#zliczanie bić dla wszystkich hetmanów przy danym ustawieniu
def sum_of_collision(chessboard, chessborad_size):
    collisions = 0
    queens  = []
    for i in range(chessborad_size):
        for j in range(chessborad_size):
            # print(table_queens[i][j])
            if chessboard[i][j] == 1.:
                #zapisujemy tablice z queens gdzie są
                queens.append(tuple((i, j)))

    for i in range(chessborad_size):
        for j in range(i+1, chessborad_size):
            queen_1 = queens[i]
            queen_2 = queens[j]
            if queen_1[0] == queen_2[0]:
                collisions += 1
            if (queen_1[0] + queen_1[1]) == (queen_2[0] + queen_2[1]):
                collisions += 1
            if queen_1[1] - queen_1[0] == queen_2[1] - queen_2[0]:
                collisions += 1

    return queens, collisions

# def each_energy(queens, no_of_queens):
#     collisions = 0
#     tmp_queen = queens[]
#     for i in range(no_of_queens)


def change_pos(no_of_queens, chessboard, queens):
    # print(queens)
    #wylosuj losowego hetmana
    queen_index = (random.randrange(0, no_of_queens))
    #wylosuj dla niego nowa pozycje w swojej kolumnie
    new_column_position = (random.randrange(0, no_of_queens))
    #dopoki nowa pozycja jest taka sama jak stara losuj dalej
    while queens[queen_index][0] == new_column_position:
        new_column_position = (random.randrange(0, no_of_queens))

    chessboard[queens[queen_index][0]][queens[queen_index][1]] = 0
    queens[queen_index] = tuple((new_column_position, queens[queen_index][1]))

    chessboard[queens[queen_index][0]][queens[queen_index][1]] = 1
    #chessboard[queens[new_column_position][0]][queens[new_column_position][1]] = 1
    # chessboard[1][1] = 7
    # print (chessboard)
    # print(queens)

    return chessboard, queens

def generate_random_var_from_positions(chessboard, no_of_queens, num_of_steps = 1000):
    collisions_rand_var = []
    for i in range(num_of_steps):
        queens, collisions = sum_of_collision(chessboard, no_of_queens)
        collisions_rand_var.append(collisions)
        chessboard, queens = change_pos(no_of_queens, chessboard, queens)

    return collisions_rand_var

def annealing(chessboard, no_of_queens):
    kb = 1.380650524 * pow(10, -23)
    # Tk + 1 = Tk * 0.95
    k = 4096
    collisions_rand_var = generate_random_var_from_positions(chessboard, no_of_queens, num_of_steps=k)
    # print (collisions_rand_var)
    T = statistics.stdev(collisions_rand_var)
    # print (T)

    for i in range(k):
        T *= 0.95

        queens, collisions_num = sum_of_collision(chessboard, no_of_queens)
        new_chessboard, queens_new = change_pos(no_of_queens, chessboard, queens)
        queens_new, collisions_num_new = sum_of_collision(new_chessboard, no_of_queens)

        delta_collisions = (collisions_num_new - collisions_num)
        if delta_collisions > 0:
            probability = math.exp(-delta_collisions/(T)) #T*Kb
            print '%s'%probability
        else:
            probability = 1

        if probability >= random.uniform(0.0, 1.0):
            queens = queens_new
            collisions_num = collisions_num_new

        if collisions_num == 0:
            break
        # print (collisions_num)

    return queens, collisions_num


chessboard, no_of_queens = create_table()
# print(chessboard)
collisions_rand_var = []
for i in range(20):
    queens, collisions = annealing(chessboard, no_of_queens)
    collisions_rand_var.append(collisions)


print (np.mean(collisions_rand_var))



# queens, collisions = all_energy(chessboard, no_of_queens)
# print(collisions)
# chessboard, queens = change_pos(no_of_queens, chessboard, queens)
# queens, collisions = all_energy(chessboard, no_of_queens)
# print(collisions)


