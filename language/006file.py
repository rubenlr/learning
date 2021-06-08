
introducao = ['ola',
              'oi',
              'olá',
              'Oi',
              'Ola',
              'Olá']
meio = ['Peguei seu contato',
        'Peguei o seu contato',
        'Peguei seu telefone',
        'Peguei o seu telefone',
        'Peguei o seu whatsapp',
        'Peguei seu whatsapp',
        'Peguei o seu whatsapp',
        'Peguei seu whatsapp',
        'Peguei o seu Whatsapp',
        'Peguei seu Whatsapp',
        'Peguei o seu zap',
        'Peguei seu zap',
        'Peguei teu contato',
        'Peguei o teu contato',
        'Peguei teu telefone',
        'Peguei o teu telefone',
        'Peguei o teu whatsapp',
        'Peguei teu whatsapp',
        'Peguei o teu whatsapp',
        'Peguei teu whatsapp',
        'Peguei o teu Whatsapp',
        'Peguei teu Whatsapp',
        'Peguei o teu zap',
        'Peguei teu zap']

sabermais = ['queria saber mais da sua proposta',
             'queria saber mais sua proposta',
             'queria conhecer sua proposta',
             'queria conhecer mais o seu trabalho',
             'queria conhecer mais seu trabalho',
             'queria ver mais da sua proposta',
             'queria ver mais sua proposta',
             'queria conhecer a sua proposta',
             'queria conhecer sua proposta']

fechamento = ['Gravei seu contato',
              'Salvei seu contato',
              'Gravei seu número aqui',
              'Salvei seu número aqui']

f = open("temp.txt", "r")

for it in introducao:
    for m in meio:
        for sm in sabermais:
            for f in fechamento:
                f.write(f"{it} Rafael, {m} em uma ação de rua, {sm}. {f}")

f.close()