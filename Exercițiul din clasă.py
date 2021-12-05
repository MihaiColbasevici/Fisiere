with open('Desktop/Lista Clasei 11A.txt', 'r') as f:
    elevi = f.readlines()
rande = 0
randg = 0
suma = 0
sumae = 0
sumag = 0
for i in elevi:
    rand = i.split()
    suma += int(rand[2])
    if rand[3] == 'Engleza':
        sumae += int(rand[2])
        rande += 1
        with open('desktop/Lista Elevilor 11A Engleza.txt', 'a') as f:
            rand1 = (rand[0] + ' ' + rand[1] + ' ' + rand[2] + '\n')
            f.write(rand1)
    if rand[3] == 'Germana':
        sumag += int(rand[2])
        randg += 1
        with open('desktop/Lista Elevilor 11A Germana.txt', 'a') as f:
            rand1 = (rand[0] + ' ' + rand[1] + ' ' + rand[2] + '\n')
            f.write(rand1)
with open('Desktop/Lista Clasei 11A.txt', 'a') as f:
    f.write('\nMedia clasei => ' + str(suma/len(elevi)))
with open('desktop/Lista Elevilor 11A Engleza.txt','a') as f:
    f.write('Media grupului de limba engleza => ' + str(sumae/rande))
with open('desktop/Lista Elevilor 11A Germana.txt','a') as f:
    f.write('Media grupului de limba germana => ' + str(sumag/randg))