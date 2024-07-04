from . import config
from . import prompts
import json

model = config.model

def create_stat(name="Jake", origin="house", gender="male", plot="warrier"):
    prompt = prompts.character_creation_prompt(name,origin,gender,plot)
    print(prompt)
    raw_response = model.generate_content(prompt)
    response = json.loads(raw_response.text)
    print(response)
    return response