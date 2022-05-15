#horarios entrada 07:30 almoço 11:30 retorno 13:00 saida 17:00
nome = str(input('Nome do colaborador: '))
anoDeNasc = int(input('Qual ano de nascimento: '))
sexo = int(input('GENERO:\n[1]MASCULINO\n[2]FEMININO\nResposta: '))
print('\033[92m===========================================\033[0m')
mes = int(input('[1]Janeiro\n[2]Fevereiro\n[3]Março\n[4]Abril\n[5]Maio\n[6]Junho\n[7]Julho\n[8]Agosto'
                '\n[9]Setembro\n[10]Outubro\n[11]Novembro\n[12]Dezembro\nMes vigente: '))
print('\033[92m===========================================\033[0m')
cont = 0
totalHrsE = 0
if mes == 1:
    for dia in range(31):
        cont = cont + 1
        print('Mes referente: Dia {} de Janeiro'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt

if mes == 2:
    for dia in range(28):
        cont = cont + 1
        print('Mes referente: Dia {} de Fevereiro'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt
if mes == 3:
    for dia in range(31):
        cont = cont + 1
        print('Mes referente: Dia {} de Março'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt
if mes == 4:
    for dia in range(30):
        cont = cont + 1
        print('Mes referente: Dia {} de Abril'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt
if mes == 5:
    for dia in range(31):
        cont = cont + 1
        print('Mes referente: Dia {} de Maio'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt
if mes == 6:
    for dia in range(30):
        cont = cont + 1
        print('Mes referente: Dia {} de Junho'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt
if mes == 7:
    for dia in range(31):
        cont = cont + 1
        print('Mes referente: Dia {} de Julho'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt
if mes == 8:
    for dia in range(31):
        cont = cont + 1
        print('Mes referente: Dia {} de Agosto'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt
if mes == 9:
    for dia in range(30):
        cont = cont + 1
        print('Mes referente: Dia {} de Setembro'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt
if mes == 10:
    for dia in range(31):
        cont = cont + 1
        print('Mes referente: Dia {} de Outubro'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt
if mes == 11:
    for dia in range(30):
        cont = cont + 1
        print('Mes referente: Dia {} de Novembro'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt
if mes == 12:
    for dia in range(31):
        cont = cont + 1
        print('Mes referente: Dia {} de Dezembro'.format(cont))
        horaEnt = float(input('Entrada: '))
        saidaAlc = float(input('Saida do almoço: '))
        retornoAlm = float(input('Retorno do almoço: '))
        horaSaida = float(input('Saida: '))
        print('\033[92m===========================================\033[0m')
        matutino = saidaAlc - horaEnt
        vespertino = horaSaida - retornoAlm
        cargaHor = matutino + vespertino
        horaExt = cargaHor - 8
        totalHrsE = totalHrsE +horaExt

anos = 2022 - anoDeNasc

print('\033[92m===========================================\033[0m')
print('Colaborador:\033[92m{}\n\033[0mIdade:\033[92m{} anos\033[0m'.format(nome,anos,))
if sexo == 1:
    print('Genero: \033[92mMASCULINO\033[0m')
if sexo == 2:
    print('Genero: \033[92mFEMININO\033[0m')
if totalHrsE > 0:
    print('Seu banco de horas esta \033[92mpositivo \033[0mem {} horas'.format(totalHrsE))
elif totalHrsE < 0 :
    print('Seu banco de horas esta \033[91mnegativo \033[0mem {} horas'.format(totalHrsE))
else:
    print('\033[92mVoce não possui banco de horas')
print('\033[92m===========================================\033[0m')
print('\033[92m===========================================\033[0m')