# joalex.dev

<p align="center">
    <img src="https://github.com/j-000/joalex.dev/blob/master/static/main.png" />
</p>


This is my personal website. Come have a look.

# Tech details

This project uses Flask for the backend and itt built in jinja2 templating engine to serve HTML pages.

Nginx is used to serve the flask app.

The application is also contained using Docker and at any given time there are 2 apps running simultaneously.

There is no database connected. When the contact form is 
used, SMTP library sends me an email with all the details (escaped!).

I use Flask-Limiter to limit POST requests (form) to 3 per day.

# Employers

[My CV is on Indeed](https://my.indeed.com/p/jooo-2fu0s8b). Contact info available.

Feel free to message me on [my LinkedIn](https://www.linkedin.com/in/joao-oliveira-b2934516b/)
