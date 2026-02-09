meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            'FLOPAR': "Algo que não fez sucesso, fracassou",
            'POV': "Significa ponto de vista, muito usado em vídeos de TikTok para encenar situações.",
            'MEWING': "Técnica de posicionamento da língua usada para definir o maxilar.",
            'SIGMA': 'Homem descolado, "o melhor" ou mais bem-sucedido, porém modesto.'
            }
word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Sua palavra não foi encontrada.')
