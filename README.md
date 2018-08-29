# Babel Chat-app 

![Desktop Demo](https://raw.githubusercontent.com/mboladop/Babel-app-project-Stream3/master/README_files/desktop.gif "Desktop Demo")
 
## Overview
 
### What is this website for?
 
**Babel Chat-app** Is a free to messenger app for smartphones and desktop and is available for anyone. **Babel Chat-app** uses the internet to send messages. The service is very similar to text messaging services, however, because **Babel Chat-app** uses the internet to send messages, the cost of using **Babel Chat-app** is significantly less than texting. 
**Babel Chat-app** includes the possibility of turning your messages into different languages such as Braille, Binary code, Emoji or Morse code. It also permits the users to send private messages addressed to specific users (@username), highlight several messages as important or create hashtags and be able to view all of the specifically.
 
### How does it work?
 
This website uses **Python3** as primary language and **Flask** as the framework to route viewers through the site. The site is styled with **Bootstrap**, **css3** and **Google Fonts**. The chat data is stored in a **MongoDB**. 

## UX

![WIREFRAME Desktop Demo](https://raw.githubusercontent.com/mboladop/Babel-app-project-Stream3/master/README_files/wireframes/desktop.jpg "Desktop Demo")
![WIREFRAME Mobile Demo](https://raw.githubusercontent.com/mboladop/Babel-app-project-Stream3/master/README_files/wireframes/mobile.jpg "Mobile Demo")


## Features
 
### Existing Features

- Simple and clean layout.
- Easy UX display.
- Minimal simple Landing.
- Scrollable access to navigate through the conversation.

## Technologies Used

- **HTML5**, **CSS3** and **Python3**
  - Base languages used to create website.
- **Flask** as the framework for Python.
- [Bootstrap](http://getbootstrap.com/)
    - We use **Bootstrap** to give the project a simple, responsive layout.
- [Google Fonts](http://googlefonts.com/)
    - We use **Google Fonts** to give our project the fonts.
- [Mongo Database](https://www.mongodb.com/)
    - We use **MongoDB** to store the chats.

## Testing

- All code used on the site has been tested to ensure everything is working as expected
- Site viewed and tested in the following browsers:
  - Google Chrome
  - Safari
- Site viewed and tested in the following devices:
  - Iphone 7plus
  - Iphone x 
  - Ipad
  - Macbook 13" and 15"
  - Samsung Galaxy

### Manual:

-Important button:
    * Click on the “Important button” button.
    * Check the website displays in a different tab.
-Hashtag button:
    * Click on the different ”Hashtag” button.
    * Check the ethnicity checkboxes display in the search form for each one.
-Send button:
    * Click on the different ”Send” buttons in the index and chat HTML.
    * Check the ethnicity checkboxes display in the search form for each one.
-Private messages functionality:
    * Send a @username + message to a specific user of the chat
    * Check that sender does see te message.
    * Login as another user (not sender or receiver) check the message doesn´t display.
    * Login as the user the message was aimed to check the message does display.
-Checkboxes for different languages:
    * Write a message for each one of the languages available.
    * Click on the “Checkbox” of the chosen language you want to turn your message to.
    * Send message and Verify it siplays in the chosen language.

### How the project looks and works on different browsers and screen sizes:

![Responsive Demo](https://raw.githubusercontent.com/mboladop/Babel-app-project-Stream3/master/README_files/responsive.gif "Responsive Demo")

### BUGS

To test it in different devices i started using the console toggle device toolbar, when I fixed all the versions for the different tablets and mobile screens I opened the website  from my Iphone and realised the display was not looking as it should.
To fix this I created a specific and new mobile version. For this purpose i downloaded Xcode simulator and served the website via [npm package serve](https://www.npmjs.com/package/serve) to be able to access it instantly and remotely through my own phone.


## Deployment (Heroku)

1. Create workspace in Visual Studio Code.
2. Associate it with GitHub repository.
3. Open a new app in Heroku (Europe) choose GitHub as deployment method and choose the repository of your project. This will enable yopur app to be updated with each push you make to Github if you wish.
4. The first time make sure you deploy it manually and then enable automatic deployments choosing master as the branch.
5. On your project workspace:
	```pip3 freeze --local > requirements.txt```
	```sudo pip3 install gunicorn```
  - Check gunicorn is now in requirements.txt by repeating : 
  ```pip3 freeze --local > requirements.txt ```
  ```touch Procfile```           
  - Open Procfile and paste:               
    web: gunicorn chat:app
  ```git push ```
  - In this case I used a Mongo DB and I was using a bashrc file to store the ```MONGODB_URI``` and ```MONGODB_NAME``` make sure to include these in the Heroku settings Config vars.

### Features Left to Implement

- Flask Login: would provide user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.
  - Include user images for avatars.

## Contributing

### Getting the code up and running

1. Firstly you will need to clone this repository by running the ```git clone <project's Github URL>``` command.
2. After you've done that you'll need to make sure that you have **npm** installed. Link [npm package serve](https://www.npmjs.com/package/serve)
3. The project will now run locally.
4. Make changes to the code and if you think it belongs in here then just submit a pull request.

## Credits

### Media

- The animated Gifs of the different projects are made with the [Giphy Capture App](https://giphy.com/apps/giphycapture)
- The Icons for the languages are from [Flat Icon Website](https://www.flaticon.com/)
- The logo image is from [123rf](https://www.123rf.com/)

### Inspiration

- The inspiration used to create this site was from a number of sources:
     - WhatsApp, desktop and mobile vs.
     - Slack, desktop and mobile vs.
     - Facebook messenger.

## Project Live:

[Link to project](https://babel-chat-app.herokuapp.com/)


