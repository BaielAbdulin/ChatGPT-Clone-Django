# ChatGPT Clone in Django

This Project is a Web App where you can interact with an AI Chatbot built with the OpenAI API.
It is essentially a clone of ChatGPT, however, it displays messages in larger text and better formatting.
It maintains chat context and also offers the option to delete specific messages by the click of a button.
You can check out how it works here: https://ika16.pythonanywhere.com/chatbot

## Backend
The project is built in Django and includes some of its built-in features like user authentication.
In Django, I also created a Message database model, where each object stores a question, 
answer, time created, and foreign key relationship to its user.

Upon each new message request, the program retrieves all previous messages from the database, sends them to the 
OpenAI API for context, creates the newest message object, and returns all the messages for output.
For the Message deletion function, it simply deletes the message object from the database and refreshes the page.

I connected the backend to a MySQL database hosted on Clever Cloud.
The project is deployed on PythonAnywhere.com

## Frontend
For the frontend, I used Bootstrap for the navbar, text input, and buttons. 
For the user authentication forms I used Django's built in forms and crispy-forms package for styling.
The rest of the pages, I designed myself using basic html and css. This includes the home and chatbot pages.

### If you would like to install the project and use it locally:
* Download Python, Django, mysqlclient, crispy-forms, dotenv
* Create .env file and include your Django secret key, openai api key, and database information
* You would also have to connect the project to your own database, or use sqlite3
