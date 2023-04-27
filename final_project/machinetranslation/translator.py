'''translator english to french'''
import os

import ibm_watson

import ibm_cloud_sdk_core.authenticators

import dotenv
dotenv.load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']


authenticator = ibm_cloud_sdk_core.authenticators.IAMAuthenticator(APIKEY)
language_translator = ibm_watson.LanguageTranslatorV3(
    version='2023-04-26',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(englishtext):
    '''english to french'''
    frenchtext = language_translator.translate(text=englishtext,
    model_id='en-fr').get_result()
    return frenchtext.get('translations')[0].get('translation')

def french_to_english(frenchtext):
    '''french to english'''

    englishtext = language_translator.translate(text=frenchtext,
    model_id='fr-en').get_result()
    return englishtext.get('translations')[0].get('translation')


#input(englishtext)
#englishtext = 'Hello, how are you today?'
#englishtext = 'I am a woman'
#translation = englishToFrench(englishtext)

#print('Eng:',englishtext)
#print('Fr:',translation)

#englishtext = 'The color is red'
#translation = englishToFrench(englishtext)

#print('Eng:',englishtext)
#print('Fr:',translation)


#print(json.dumps(translation, indent=2, ensure_ascii=False))

#frenchtext='ça va bien?'
#translation = frenchToEnglish(frenchtext)
#print('Fr:',frenchtext)
#print('Eng:',translation)


#frenchtext='Je suis professeur'
#translation = frenchToEnglish(frenchtext)
#print('Fr:',frenchtext)
#print('Eng:',translation)


#print(json.dumps(translation, indent=2, ensure_ascii=False))
