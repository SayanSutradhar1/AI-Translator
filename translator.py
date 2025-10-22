from googletrans import Translator

def translate_text(text:str,target_language:str) -> str :
    try:
       translator = Translator()
       translation = translator.translate(text, dest=target_language)
       return translation.text
    except Exception as e:
       raise RuntimeError(f"Translation failed: {str(e)}")
    
    