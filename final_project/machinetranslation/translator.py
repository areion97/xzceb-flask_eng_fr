import os
import json
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
class Translator():


    def english_to_french(self,english_text):
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        return french_text

    def french_to_english(self,french_text):
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        return english_text
