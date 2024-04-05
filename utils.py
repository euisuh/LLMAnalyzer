from langdetect import detect
from deep_translator import GoogleTranslator
import ast

MAX_GOOGLE_TRANSLATE_LEN = 5000

def google_translator(s, source='auto', target='ar'):
    try:
        if len(s) >= MAX_GOOGLE_TRANSLATE_LEN:
            s = s[0:MAX_GOOGLE_TRANSLATE_LEN-1]
        tr = GoogleTranslator(source, target).translate(s)
        if tr is None:
            tr = s
    except:
        tr = f"EXCEPTION caught by KORQAR"
    return tr

def get_correct_format(text):
    try:
        return ast.literal_eval(text)
    except:
        return text
        