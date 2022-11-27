import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def english_To_French(englishText):
    englishText = "Hello madame."
    if(englishText==""):
        frenchText = "No input (null) detected."
    else:
        x = language_translator.translate(englishText, model_id='en-fr').get_result()
        frenchText = (x["translations"][0]["translation"])
    return frenchText

def french_To_English(frenchText):
    if(frenchText==""):
        englishText = "No input (null) detected."
    else:
        x2 = language_translator.translate(frenchText, model_id='fr-en').get_result()
        englishText = (x2["translations"][0]["translation"])
    return englishText
