from google.cloud import speech
from google.oauth2 import service_account
import nltk
nltk.download('punkt')

# Path to your Google service account key JSON file
key_file_path = 'sa-speech.json'

# Load the credentials from the JSON key file
credentials = service_account.Credentials.from_service_account_file(key_file_path)

# Initialize the Speech client with these credentials
client = speech.SpeechClient(credentials=credentials)

def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US',
        enable_automatic_punctuation=True,
    )

    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result()

    transcribed_text = ""
    for result in response.results:
        transcribed_text += '{}'.format(result.alternatives[0].transcript)
    

    return transcribed_text

