# CALL-DIGEST

The CALL-DIGEST Refers to a summary or key points generator from a recorded call or audio file. This process involves converting the audio content into text and extracting important information or key points from the transcribed text. It utilizes the Google Speech API to transcribe an audio file into a textual format then uses OpenAI's GPT-3.5 Turbo to extract key points from the text transcribed by the Google Speech API. 


## Table of Content
- [CALL-DIGEST](#call-digest)
  - [Table of Content](#table-of-content)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Edge Case Handling](#edge-case-handling)

## Features

1. **Speech Recognition**: Convert audio files into textual transcripts.
2. **Accuracy**: Ensure high accuracy in transcribing speech to text.
3. **Audio Conversion**: Convert audio files to a standard format for processing and analysis.
4. **Key Phrase Identification**: Identify and extract important phrases or keywords relevant to the conversation.
5. **Contextual Understanding**: Ensure the extraction process understands the context and meaning of the text.
6. **Coherence and Relevance**: Extract key points that are coherent and relevant to the main topics discussed.
7. **Real-time Processing**: Allow real-time or batch processing of audio files.


## Installation
Follow these steps to use the CALL-DIGEST:

  1.  Clone or download this repository to your local machine.
  2.  Need to install some Python libraries.

      a. For flask use "pip install flask".
      
      b. For google-cloud-speech use "pip install google-cloud-speech".

      c. For google-cloud-storage use "pip install google-cloud-storage".

      d. For google-authentication use "pip install google-auth".

      e. For openAi use "pip install openai".
        - In certain cases, the API key for OpenAI might be disabled due to exposure, requiring the generation of a new API key from the OpenAI API. It is necessary to update the API key in the config.py file.
          
      f. for pydub use "pip install pydub".
        - Encountering an error due to the absence of the ffmpeg dependency while utilizing the AudioSegment functionality from the pydub library.o resolve the ffmpeg missing error, follow these steps:
          
            i.   Download the ffmpeg executable from a trusted source (e.g., https://www.gyan.dev/ffmpeg/builds/).
          
            ii.  Place the ffmpeg executable in a location on your machine, such as in a folder within your program directory.

            iii. Copy the path to the directory where the ffmpeg executable is located.

            iv.  Add the path to the ffmpeg directory to your system's PATH environment variable.

      - By adding the ffmpeg executable to your system's PATH, you'll make it accessible from anywhere on your command line, and the pydub library should be able to locate and use it.
  4. Change the file_path in app.py, Add the path of the audio file stored in your machine.
  5. Now run the code from the terminal and go to the directory where app.py is stored.
  6. Use the command "python app.py" to run the code


## Usage
Using the CALL-DIGEST is very easy.
  1. Prepare an audio file for information extraction.
  2. Run "app.py" then navigate to the local host.
  3. Click on the Upload File button to browse and upload the audio file.
  4. Then click on the generate text button to extract the text from the audio file.
  5. Then click on the generate key points button to extract key points from the transcribed text.


## Edge Case Handling
The CALL-DIGEST is designed to handle various edge cases to ensure a smooth user experience. Here are some of the edge cases it addresses:
  1. **Network Connectivity Failure**: Gracefully handle situations where there is no internet connection.
  2. **Text Generation Failure**: Handle errors that may occur during text generation from the audio file.
  3. **Unexpected Error**: Handle errors the user generates gracefully.
  4. **User Experience**: Prioritize a smooth and user-friendly experience throughout the webpage.
  5. **Compatibility**: Ensure compatibility with various audio formats.
