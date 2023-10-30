from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename
from voice_to_text import transcribe_audio  # Import the transcribe_audio function
from keyPoints import keyPointFinder


app = Flask(__name__)

# Define your upload route

@app.route('/', methods=['GET', 'POST'])
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    transcribed_text = ""
    key_points = ""

    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Generate a unique filename for the uploaded audio file
            filename = secure_filename(file.filename)
            audio_file_path = os.path.join('uploads', filename)
            file.save(audio_file_path)
            transcribed_text =  transcribe_audio(audio_file_path)  # Call the transcribe_audio function
            key_points = keyPointFinder(transcribed_text)

    return render_template('upload.html', transcribed_text=transcribed_text,key_points=key_points)

if __name__ == '__main__':
    app.run(debug=True)