from translation_package.translator_google import TransLate, LangDetect, CodeLang, LanguageList

if __name__ == "__main__":
    # Corrected: Specifying source language 'es' for Spanish to avoid misdetection
    print(TransLate("Hola", "es", "en"))  # Translate from Spanish to English

    # Testing language detection with more text for better accuracy
    print(LangDetect("Hola, cómo estás?", "all"))  # Detects Spanish better with more text

    # Test CodeLang function
    print(CodeLang("Spanish"))  # Should return 'es'

    # Test LanguageList function
    print(LanguageList("screen", "Hola"))

