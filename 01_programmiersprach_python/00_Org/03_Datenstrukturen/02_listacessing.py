teilnehmendenliste = ['Lina','Marc','Marie','Sophie','Sven','dennis','olaf']
print(teilnehmendenliste[0])# Lina
print(teilnehmendenliste[-1])#olaf
print(teilnehmendenliste[0:3])
print(teilnehmendenliste[0:7:2])#print(teilnehmendenliste[start idx:end idx:step]) ['Lina', 'Marie', 'Sven', 'olaf']


matrix = [ [1,2] , [ 3,4]]

teil_matrix_1 = matrix[0] # 
teil_matrix_2 = matrix[1] # 
print(teil_matrix_1) # [1,2]
print(teil_matrix_2) # [3,4]

teil_teil_matrix = teil_matrix_1[0]
teil_teil_matrix = matrix[0][0]



print(teil_teil_matrix)


# 4
teil_teil_matrix2 = matrix[1][1]
print(teil_teil_matrix2)




matrix = [   [1,2] , [ 3,4], [9,8] ]
#        [      idx0   ,             idx1      ]  
#        [ [idx0, idx 1] ,     [idx0, idx1]   ]

# 3
print(matrix[1][0])

# 9
print(matrix[2][0])



