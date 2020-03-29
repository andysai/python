def member():
    four_numbers = []
    five_numbers = []
    six_numbers = []
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                four_number = '1{}{}{}'.format(i, j, k)
                four_numbers.append(four_number)
                for l in range(0, 10):
                    five_number ='1{}{}{}{}'.format(i,j,k,l)
                    five_numbers.append(five_number)
                    for m in range(0, 10):
                        number = '1{}{}{}{}{}'.format(i, j, k, l, m)
                        six_numbers.append(number)

    return four_numbers,five_numbers,six_numbers



print(member())

#print(seren())
#print(eight())
#print(nine())
#print(ten())