from watson_developer_cloud import LanguageTranslationV2 as LanguageTranslator

uname = 'f47107b0-f115-428b-a3c9-96db2ad635e7'
passwd = 'amR1PVMZEvm5'


def authenticate():
    """
    This function authenticates against IBM Bluemix with the globally provided username and password
    """
    #language_translation = LanguageTranslator(username=uname, password=passwd)
    return (LanguageTranslator(username=uname, password=passwd))
    
def translate_text(language_translator, source_text, source_language, target_language):
    """
    This function takes as input the 
    """
    return language_translator.translate( text=source_text,     source=source_language,     target=target_language)
    
def main():
    language_translator = authenticate()
    print translate_text(language_translator,  source_text='How do I goto Terminal One, Gate 12a?', source_language='en', target_language='es')
    
if __name__ == '__main__':
    main()