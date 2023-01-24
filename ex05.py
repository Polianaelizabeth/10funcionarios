n = int(1)

while n <= 10:
    codigo = int(input("código do funcionário: "))
    horasT = int(input("horas trabalhadas: "))

    enq2 = True
    enq3 = True
    categoria = str
    turno = str

    while enq2:
        categoria = (input("categoria (O – operário; ou G – gerente): "))
        if categoria == 'G' or categoria == 'O':
            enq2 = False
        else:
            print('Digite categoria novamente.')
    while enq3:
        turno = (input("turno (M – matutino; V – vespertino; N – noturno):"))
        if turno == 'M' or turno == 'V' or turno == 'N':
            enq3 = False
        else:
            print('Digite turno novamente.')

    if categoria == 'G':
        if turno == 'N':
            valorH = 0.18 * 450.00
        else:
            valorH = 0.15 * 450.00
    else:
        if turno == 'N':
            valorH = 0.13 * 450.00
        else:
            valorH = 0.1 * 450

    salarioI = horasT * valorH

    if salarioI <= 300:
        aux = float = 0.2 * salarioI
    elif 300 < salarioI <= 600:
        aux = 0.15 * salarioI
    else:
        aux = 0.05 * salarioI

    salarioF = salarioI + aux

    print('codigo: ', codigo, 'horas trabalhadas', horasT, 'valor da hora trabalhada:', valorH, 'auxilio alimentação: ',
          aux, 'salario inicial: ', salarioI, 'salario final: ', salarioF)
    print('laco: ', n)
    n = n + 1