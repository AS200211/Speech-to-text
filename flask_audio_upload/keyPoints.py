import os
import openai
from config import apikey


def keyPointFinder(f):
  openai.api_key = apikey
  response = openai.Completion.create(
    engine="davinci",
    prompt=f"Extract the key points in the points from below text {f}",
    max_tokens=150 
    
  )
  return response.choices[0].text.strip()



# keyPointFinder("In recent years, artificial intelligence has made significant progress in various industries. It has improved efficiency in manufacturing and has revolutionized the way we interact with technology. AI has also been integrated into the healthcare sector, leading to more accurate diagnoses and personalized treatments.")
