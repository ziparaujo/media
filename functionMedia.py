def media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7:
        return f'Prabéns. Sua média é {media} e você foi aprovado!!!'
    else:
        return f'Sua média é {media} e você foi reprovado.'

print(media(7, 9))