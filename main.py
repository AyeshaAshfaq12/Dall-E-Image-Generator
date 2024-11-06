import os
from openai import OpenAI
from flask import Flask, render_template, jsonify

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
client = OpenAI()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generateimages/<prompt>')
def generate(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    # image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-HE6wyixkZNOcbrpVRMmMjV22/user-mivia3o3DXtWwf3M0pPG27LG/img-ybNfmyZ2pIlO5KDCnzP4Ip09.png?st=2024-11-06T10%3A23%3A40Z&se=2024-11-06T12%3A23%3A40Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-11-05T20%3A01%3A41Z&ske=2024-11-06T20%3A01%3A41Z&sks=b&skv=2024-08-04&sig=RC3Ode/H42bA9Gv/jZ6J9KuYc%2BNvhwYgImJlFosUxSs%3D"

    return jsonify({'image_url': image_url})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
