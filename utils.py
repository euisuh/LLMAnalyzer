from langdetect import detect
from deep_translator import GoogleTranslator
 
MAX_GOOGLE_TRANSLATE_LEN = 5000

def google_translator(s, source='auto', target='ar'):
    try:
        if len(s) >= MAX_GOOGLE_TRANSLATE_LEN:
            s = s[0:MAX_GOOGLE_TRANSLATE_LEN-1]
        tr = GoogleTranslator(source, target).translate(s)
        if tr is None:
            tr = s
    except:
        tr = f"EXCEPTION in GoogleTranslator: {s[0:100]}..."
    return tr