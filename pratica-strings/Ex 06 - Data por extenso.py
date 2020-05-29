data = input('Informe a sua data de nascimento (dd/mm/aaaa): ')
data = data.split('/')
if data[1] == '01':
    print('Você nasceu em {} de {} de {}'.format(data[0], 'janeiro', data[2]))
else:
    if data[1] == '02':
        print('Você nasceu em {} de {} de {}'.format(data[0], 'fevereiro', data[2]))
    else:
        if data[1] == '03':
            print('Você nasceu em {} de {} de {}'.format(data[0], 'março', data[2]))
        else:
            if data[1] == '04':
                print('Você nasceu em {} de {} de {}'.format(data[0], 'abril', data[2]))
            else:
                if data[1] == '05':
                    print('Você nasceu em {} de {} de {}'.format(data[0], 'maio', data[2]))
                else:
                    if data[1] == '06':
                        print('Você nasceu em {} de {} de {}'.format(data[0], 'junho', data[2]))
                    else:
                        if data[1] == '07':
                            print('Você nasceu em {} de {} de {}'.format(data[0], 'julho', data[2]))
                        else:
                            if data[1] == '08':
                                print('Você nasceu em {} de {} de {}'.format(data[0], 'agosto', data[2]))
                            else:
                                if data[1] == '09':
                                    print('Você nasceu em {} de {} de {}'.format(data[0], 'setembro', data[2]))
                                else:
                                    if data[1] == '10':
                                        print('Você nasceu em {} de {} de {}'.format(data[0], 'outubro', data[2]))
                                    else:
                                        if data[1] == '11':
                                            print('Você nasceu em {} de {} de {}'.format(data[0], 'novembro', data[2]))
                                        else:
                                            if data[1] == '12':
                                                print('Você nasceu em {} de {} de {}'.format(data[0], 'dezembro', data[2]))