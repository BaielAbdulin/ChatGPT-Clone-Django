# ChatGPT Clone in Django

This Project is a Web App where you can interact with an AI Chatbot built with the OpenAI API.
It is essentially a clone of ChatGPT, however, it displays messages in larger text and better formatting.
It also offers the option to delete specific messages by the click of a button.
You can check out how it works here: https://ika16.pythonanywhere.com/chatbot

It is built in Django and includes some of its built-in features like user authentication.
In Django, I also created a Message database model, where each object stores a question, 
answer, time created, and foreign key relationship to its user
I connected the backend to a MySQL database hosted on Clever Cloud. 
