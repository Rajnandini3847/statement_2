from googletrans import Translator

def translate_hindi_to_english(input_text):
    try:
        translator = Translator()

        translation = translator.translate(input_text, src='en', dest='hi')

        return translation.text

    except Exception as e:
        return f"Translation error: {str(e)}"