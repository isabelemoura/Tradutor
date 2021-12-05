from translate import Translator

options = Translator(from_lang = "pt-br", to_lang = "english")

inputString = "Melhoras meu amigo, Den!"

translate = options.translate(inputString)
print(translate)
