import os
import datetime
from flask import Flask , redirect, render_template, request
from pymongo import MongoClient
import json

MONGODB_URI = os.environ.get("MONGODB_URI")
MONGODB_NAME = os.environ.get("MONGODB_NAME")

app = Flask(__name__)



@app.route('/')
def get_index():
    return render_template('index.html')
    
@app.route("/login", methods=['POST'])
def get_login():
    username = request.form.get('username')
    return redirect(username)
    
def turn_to_morse(body):
    
    with open('features/morse-code.json') as f:
        data = json.load(f)
    

    morse_message = ""
    
    for c in body:
        if c in data:
           morse_message += data[c]
        else:
            morse_message += c
        
            
    return morse_message
    
app.jinja_env.globals.update(turn_to_morse=turn_to_morse)

def turn_to_emoji(body):
    
    with open('features/emoji.json') as f:
        data = json.load(f)

    words = body.lower().split(" ")
    emoji_message = ""
    
    for word in words:
        if word in data:
            emoji_message += ' ' + data[word]
        else:
            emoji_message += ' ' + word
    
    return emoji_message

app.jinja_env.globals.update(turn_to_emoji = turn_to_emoji)

def turn_to_braille(body):
    
    with open('features/braille.json') as f:
        data = json.load(f)
    
    bodylow = body.lower()
    braille_message = ""
    
    for c in bodylow:
        if c in data:
           braille_message += data[c]
        else:
            braille_message += c
        
            
    return braille_message
    
app.jinja_env.globals.update(turn_to_braille = turn_to_braille)

def turn_to_binary(body):
    
    with open('features/binary.json') as f:
        data = json.load(f)
    

    binary_message = ""
    
    for c in body:
        if c in data:
           binary_message += data[c] + " "
        else:
            binary_message += c
        
            
    return binary_message
    
app.jinja_env.globals.update(turn_to_binary=turn_to_binary)

@app.route("/topics/important", )
def get_important_messages():
    
    messages = load_messages()
    
    important_messages = []
    
    for message in messages:
        if (message['important'] == 'on'):
            important_messages.append(message)
    
    return render_template('chat.html', all_the_messages = important_messages)
    
@app.route("/topics/hashtag")
def get_hashtags():
    
    messages = load_messages()
    chosen_hashtag = []
    
    for message in messages:
        if ('#') in message["body"]:
            chosen_hashtag.append(message)
    
    
    return render_template('chat.html', all_the_messages = chosen_hashtag)

@app.route('/<username>')
def get_username(username):
    
    messages = load_messages()
    visible_messages=[]
    
    for message in messages:
        if message['body'].startswith("@"+ username) or not message['body'].startswith("@") or (message['sender'] == username):
            visible_messages.append(message)
        
    return render_template('chat.html', username=username, all_the_messages=visible_messages)

       
            
@app.route('/<username>/new', methods=['POST'])
def add_message(username):
    
    text = request.form.get('message')
    important = request.form.get('important')
    morse= request.form.get('morse')
    emoji= request.form.get('emoji')
    braille = request.form.get('braille')
    binary = request.form.get('binary')

    f = open('profanity.txt', 'r')
    banned_words = f.read().split('\n')                  
    f.close()
    words= text.split()
    words =[word[0]+('*' * (len(word)-1)) if word.lower() in banned_words else word for word in words] 
    
    text= ' '.join(words)
    

    message = {
        'sender': username,
        'body': text,
        'time': datetime.datetime.now().strftime("%H:%M"),
        'important': important,
        'morse': morse, 
        'emoji': emoji,
        'braille': braille,
        'binary': binary,
    }
    
    save_to_mongo(message)
     
    return redirect(username)

def save_to_mongo(message):
    with MongoClient(MONGODB_URI) as conn:
       db = conn[MONGODB_NAME]
       coll = db["chat-messages"]
       coll.insert(message)
        
def load_messages():
    with MongoClient(MONGODB_URI) as conn:
        db = conn[MONGODB_NAME]
        coll = db["chat-messages"]
        messages = coll.find()
        return messages

  
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)
 