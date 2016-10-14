# -*- coding: utf-8 -*-


import json
import watson_developer_cloud
reload (watson_developer_cloud)
from watson_developer_cloud import LanguageTranslationV2 as LanguageTranslator


uname = 'f47107b0-f115-428b-a3c9-96db2ad635e7'
passwd = 'amR1PVMZEvm5'


language_translator = LanguageTranslator(
    username='f47107b0-f115-428b-a3c9-96db2ad635e7',
    password='amR1PVMZEvm5')

translation = language_translator.translate(
    text='Cómo hacer yo Goto terminal 4, puerta 12',
    source='es',
    target='en')
print(json.dumps(translation, indent=2, ensure_ascii=False))