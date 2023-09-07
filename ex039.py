""" Faça um programa qye leia o ano de nascimento de um jovem e informe, conforme a sua idade:
> Se ele ainda vai se alistar ao serviço militar.
> Se é hora de se alistar
> Se ja passou o tempo do alistamento
O seu programa também deverá mostrar o tempo que falta ou que passou do prazo
 """
from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em \33[0:31m{}\33[0m tem \33[0:31m{}\33[0m anos em \33[0:31m{} \33[0m'.format(nasc, idade, atual))
if idade == 18:
    print('\33[0:33mALERTA!\33[0m Você tem que se alistar \33[0:31mIMEDIATAMENTE!\33[0m')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta \33[0:31m{}\33[0m ano(s) para o alistamento militar!'.format(saldo))
    ano = atual + saldo
    print('\33[032mSeu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há \33[0:31m{}\33[0m ano(s)'.format(saldo))
    ano = atual - saldo
    print('\33[;49;96mSeu alistamento foi em {}'.format(ano))
