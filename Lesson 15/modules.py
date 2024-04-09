from googletrans import Translator

translator = Translator()
first = translator.translate('안녕하세요.')

# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
second = translator.translate('안녕하세요.', dest='ja')

# <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
third = translator.translate('veritas lux mea', src='la')

print(first)
print(second)
print(third)