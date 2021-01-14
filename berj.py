N = int(input('Enter N value for NxN matrix: '))

len_row, len_col = N, N
inc_num = 0

matrix = []

c_temp_list = list()
c_total_list = list()

r_temp_list = list()
r_total_list = list()

d_temp_list = list()
d_total_list_1 = list()
d_total_list_2 = list()


for n in range(N):
    matrix.append([0]*len_row)
    
print(matrix)

for row in range(len_row):
    for col in range(len_col):
        inc_num += 1
        matrix[row][col] = inc_num
    if row == 0:
        print('\n', '\n')
        print('A. ', str(N) + 'x' + str(N), 'Table')
        print('\n')
    print(matrix[row])
        

for row in range(len_row):
    if row == 0:
        print('\n', '\n')
        print('B. ', 'Sum of Row')
        print('\n')
    #print(sum(matrix[row]))
    r_total_list.append(sum(matrix[row]))
    print('Sum of row ', row, ": ", sum(matrix[row]))

print('Total: ', sum(r_total_list))

for col in range(len_col):
    if col == 0:
        print('\n', '\n')
        print('C. ', 'Sum of Col')
        print('\n')
    for row in range(len_row):   
        c_temp_list.append(matrix[row][col])
    #print(sum(c_temp_list))
    c_total_list.append(sum(c_temp_list))
    print('Sum of col ', col, ": ", sum(c_temp_list))
    c_temp_list = []
    
print('Total: ', sum(c_total_list))

for row in range(len_row):
    if row == 0:
        print('\n', '\n')
        print('D. Sum of Diagonals')
        print('\n')
    for col in range(len_col):
        if row == col:
            d_temp_list.append(matrix[row][col])

print(sum(d_temp_list))
d_total_list_1 = sum(d_temp_list)
#print(d_total_list_1)
d_temp_list = []

for row in range(len_row):
    matrix[row].reverse()

for row in range(len_row):
    for col in range(len_col):
        if row == col:
            d_temp_list.append(matrix[row][col])

print(sum(d_temp_list))
d_total_list_2 = sum(d_temp_list)
d_temp_list = []

d_total = d_total_list_1 + d_total_list_2

print('Total: ', d_total)


