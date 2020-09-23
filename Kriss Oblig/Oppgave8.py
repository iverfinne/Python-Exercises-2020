#Oppgave 8
my_list = [[1, 0, 1, 0], [0, 1, 1, 0,], [0, 1, 1, 1], [0, 0, 0, 1]]

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in my_list]))

