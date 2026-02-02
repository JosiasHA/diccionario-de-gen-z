meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "BRUH": "sorpresa desaprovacion decepcion es como decir enserio? eso es",
            "XD": "que da risa o es gracioso",
            "NAH": "desacuerdo",
            "BRO": "amigo, hermano, persona de confiansa amistosa",
            "STALKER": "acosador, o persona que sigue a otra de forma denunciable",
            "MOOD": "la emocion del momento",
            "GOAT": "que es el mejor en algo especifico",
            "BASADO": "persona que dice lo que cree sin miedo a que lo juzgen",
            }

word = input("Escribe una palabra que no entiendas entre estas palabras (¡con mayúsculas!): CRINGE, LOL, XD, BRUH, NAH, BRO, STALKER, MOOD, GOAT, BASADO")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print('Su palabra no fué encontrada')
