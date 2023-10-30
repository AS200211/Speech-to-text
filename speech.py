import io
from google.oauth2 import service_account
from google.cloud import speech
import os



client_file = 'sa-speech.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)


audio_file = 'problem.wav'
with io.open(audio_file,'rb') as f:
    content = f.read()
    audio = speech.RecognitionAudio(content=content)
    
    
    
config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=44100,
                language_code='en-US',
            )

response = client.recognize(config=config, audio=audio)

t = ''
for result in response.results:
    t += '{}'.format(result.alternatives[0].transcript)

print(t)