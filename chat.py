import os
import datetime
from flask import Flask , redirect, render_template, request

app = Flask(__name__)

messages=[]


@app.route('/')
def get_index():
    return render_template('index.html')
    
@app.route("/login", methods=['POST'])
def get_login():
    username = request.form.get('username')
    return redirect(username)

@app.route("/topics/important", )
def get_important_messages():
    
    important_messages = []
    
    for message in messages:
        if (message['important'] == 'on'):
            important_messages.append(message)
    
    return render_template('chat.html', all_the_messages = important_messages)

@app.route("/topics/hashtag")
def get_hashtags():
    
    chosen_hashtag = []
    
    for message in messages:
        if ('#') in message["body"]:
            chosen_hashtag.append(message)
    
    
    return render_template('chat.html', all_the_messages = chosen_hashtag)

@app.route('/<username>')
def get_username(username):
    
    visible_messages=[]
    
    for message in messages:
        if message['body'].startswith("@"+ username) or not message['body'].startswith("@") or (message['sender'] == username):
            visible_messages.append(message)
        
    return render_template('chat.html', username=username, all_the_messages=visible_messages)

       
            
@app.route('/<username>/new', methods=['POST'])
def add_message(username):
    text = request.form.get('message')
    box = request.form.get('important')
   
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
        'important': box
    }
    
    
    messages.append(message)
    f = open("saved-chats.txt", "a")  
    lines = f.write(str(messages)+"\n")
    f.close()                                      
    
    return redirect(username)
    
    #return 'Hello' + ' ' + username + ': ' + message
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)