import googletrans

Translator = googletrans.Translator()

print(Translator.translate(text="Beispiel", dest="en", src="auto"))