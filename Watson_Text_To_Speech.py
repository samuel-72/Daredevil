# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
#import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
import codecs
import sys
import os
import time
reload(sys) 

#—————————————————————————————#
#—————————initialized global variables —————————#
#—————————————————————————————#
sys.setdefaultencoding('utf8')
url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/voices/en-US_MichaelVoice'
username='c146cfb6-c924-43b2-86a8-b70f0b8c484d'
password='dfi1TU0HsL2V'\

voice = 'en-GB_KateVoice'
accept = ''
#say_this = "Hello everyone, this is Vikash and Vignesh for Commvault Hackathon. We are working with IBM Watson's Text to Speech API. This audio was generated via the API. This audio is converted to text using IBM Watson's Speech to Text API. Hope you enjoyed the demo. Please leave us your valuable feedback. Thanks."
say_this = "Hello everyone, this is Vikash and Vignesh for Commvault Hackathon."
time.sleep(3)
#-----------------------Text To Speech API credentials go here--------------------------#
#text_to_speech = TextToSpeechV1(username=' ',password=' ')
text_to_speech = TextToSpeechV1(username=username,password=password)
#---------------------------------------------------------------------------------------#

#-----------------------Do You wish to see the latest API summary-----------------------#
show_me_the_api_summary = 'yes'           #set to yes or no
#---------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------#
#---------------------------extract the information from the texttospeech API       ----#
#---------------------------------------------------------------------------------------#

def see_api_list(input):

		x = text_to_speech.voices()
		all_voices_in_dictionary = x['voices']
		name_voices = []
		y = len(all_voices_in_dictionary)
		i = 0
		for i in range (y):
			record = all_voices_in_dictionary[i]
			print '********** Voices Types ****************'
			print '********** Voice Number ' + str(i+1) + '**************'
			for key in record.keys():
				try:

					g = record[key]
					str(g).strip( unicode( codecs.BOM_UTF8, "utf8" ) )
					g = g.decode('utf-8')
				except AttributeError:
					str(g).strip( unicode( codecs.BOM_UTF8, "utf8" ) )
					g = str(g)
				except UnicodeEncodeError:
					g.encode('utf-8','ignore')
				if input == 'yes':
					print "the API key name is " + key + " and its value is " + g.encode('utf-8')  #.encode('ascii','ignore')
				if key == 'name':
					name_voices.append(g.encode('utf-8'))
		return(name_voices)

if __name__ == "__main__":
	if show_me_the_api_summary == 'yes':
		#name_voices = see_api_list('yes')
		pass
"""
x = len(name_voices)
i = 0
for i in range (x):
	fn = 'output_'+name_voices[i]+'.wav'
	with open(join(dirname(__file__), 'Audio\\'+fn), 'wb') as audio_file:
            audio_file.write(text_to_speech.synthesize(say_this,voice=name_voices[i]))
"""
fn = 'output_'+'intro_1'+'.wav'
with open(join(dirname(__file__), 'Audio\\'+fn), 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize(say_this,voice='en-US_MichaelVoice'))
"""
time.sleep(3)
#fn = 'output_'+'att_intro_2'+'.wav'
with open(join(dirname(__file__), 'Audio\\'+fn), 'ab') as audio_file:
    audio_file.write(text_to_speech.synthesize("We are working with IBM Watson's Text to Speech API. This audio was generated via the API.",voice='en-US_LisaVoice'))
time.sleep(3)
with open(join(dirname(__file__), 'Audio\\'+fn), 'ab') as audio_file:
    audio_file.write(text_to_speech.synthesize("This audio is converted to text using IBM Watson's Speech to Text API.",voice='en-US_MichaelVoice'))
time.sleep(3)
with open(join(dirname(__file__), 'Audio\\'+fn), 'ab') as audio_file:
    audio_file.write(text_to_speech.synthesize("Hope you enjoyed the demo. Please leave us your valuable feedback. Thanks.",voice='en-US_LisaVoice'))
"""
"""
import audiolab, scipy
a, fs, enc = audiolab.wavread('D:\\GRADUATE SCHOOL\\Hackathon\\AT&T Hackathon - Sep 2016\\Audio\\att_intro_1.wav')
b, fs, enc = audiolab.wavread('D:\\GRADUATE SCHOOL\\Hackathon\\AT&T Hackathon - Sep 2016\\Audio\\att_intro_2.wav')
c = scipy.vstack((a,b))
audiolab.wavwrite(c, 'D:\\GRADUATE SCHOOL\\Hackathon\\AT&T Hackathon - Sep 2016\\Audio\\att_intro.wav', fs, enc)
"""