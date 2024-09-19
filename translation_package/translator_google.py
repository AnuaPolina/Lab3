from googletrans import Translator, LANGUAGES
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0

def TransLate(text: str, src: str, dest: str) -> str:
    translator = Translator()
    try:
        detected_lang = detect(text) if src == 'auto' else src
        lang_code = CodeLang(dest)
        if lang_code == "Error":
            return "Error: Target language code or name not recognized."
        translated = translator.translate(text, src=detected_lang, dest=lang_code)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        lang = detect(text)
        confidence = 1.0  # LangDetect does not provide confidence directly
        if set == "lang":
            return lang
        elif set == "confidence":
            return str(confidence)
        else:
            return f"{lang}, {confidence}"
    except LangDetectException:
        return "Error: Language detection failed."

def CodeLang(lang: str) -> str:
    if lang in LANGUAGES.values():
        for code, name in LANGUAGES.items():
            if name == lang:
                return code
    elif lang in LANGUAGES.keys():
        return lang
    else:
        return "Error"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        table = "N  Language     ISO-639 code    Text\n--------------------------------------------------------\n"
        translator = Translator()
        for i, (code, name) in enumerate(LANGUAGES.items(), 1):
            translated_text = translator.translate(text, dest=code).text if text else ""
            table += f"{i} {name:12} {code:10} {translated_text}\n"
        if out == "screen":
            print(table)
        elif out == "file":
            with open("languages_list.txt", "w") as file:
                file.write(table)
        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
