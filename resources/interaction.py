def options_view():
    print('''
1- Baixar apenas video;
2- Baixar apenas audio em mp3;
3- Baixar apenas audio em wav;
    ''')

def interaction(options):
    options_view()
    response = int(input('Digite uma opção: '))

    verification = False
    if response in options:
        verification = True
    else:
        while verification == False:
            options_view()
            print('Digite uma opção valida!')
            response = int(input('Digite uma opção: '))
            if response in options:
                verification = True
            else:
                pass

    return response