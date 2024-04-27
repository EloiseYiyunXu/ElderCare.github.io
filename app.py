from flask import Flask, request, jsonify, render_template, session
from openai import OpenAI, RateLimitError
import os
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__, static_url_path='/static')

# Load environment variables
load_dotenv(find_dotenv())

client = OpenAI(
    api_key='sk-proj-IdwhTgMVcgQpbIvsQLjnT3BlbkFJKlMtRMA8EbjZfkm3qTAV'
)

app.secret_key = os.urandom(24)

@app.route('/')
def my_form():
    return render_template('response2.html')

@app.route('/', methods=['POST'])
def my_form_post():
    user_input = request.form['userInput']
    if 'chat_history' not in session:
        session['chat_history'] = []
    session['chat_history'].append({'role': 'user', 'content': user_input})
    
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=session['chat_history'],
            temperature=0.3,
            max_tokens=500,
        )
        session['chat_history'].append({'role': 'system', 'content': completion.choices[0].message.content})
        session.modified = True
        return render_template('response2.html', response=completion.choices[0].message.content)
    except RateLimitError:
        return jsonify({'error': 'Rate limit reached'}), 429
    except Exception as e:
        return jsonify({'error': str(e)}), 500

"""
@app.route('/', methods=['POST'])
def my_form_post():
    user_input = request.form['userInput']
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Lisa, a 67-year-old woman with diabetes."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3,
            max_tokens=500,
        )
        return completion.choices[0].message.content
    except RateLimitError:
        return jsonify({'error': 'Rate limit reached'}), 429
    except Exception as e:
        return jsonify({'error': str(e)}), 500
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3232,debug=True)