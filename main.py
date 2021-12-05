from translate import Translator

options = Translator(from_lang = "pt-br", to_lang = "english")

inputString = "Projeto tradutor!"

translate = options.translate(inputString)
print(translate)
