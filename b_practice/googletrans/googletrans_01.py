from googletrans import Translator

translator = Translator()
print(translator.translate('안녕하세요', src='ko', dest='en').origin)
print(translator.translate('안녕하세요.', src='ko', dest='en').text)