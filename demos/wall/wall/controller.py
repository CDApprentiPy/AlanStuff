from flask import Flask, render_template, redirect, g, request, session
from .models.User import UserManager

class RouteBuilder(object):
    def __init__(self, app):
        # landing page route
        self.Users = UserManager
        @app.route('/')
        def landing():
            "takes us to landing page"
            return render_template('landing.html')

        # register user 
        @app.route('/user/create', methods=['POST'])
        def create_user():
            """Adds a user to the databse"""
            # validate inputs
            # insert into db
            # redirect to correct page
            data = request.form 
            if self.Users.add_user(data):
                User.set_session_user(data['email'])
                return redirect('/wall')

        # login user
        @app.route('/user/login', methods=['POST'])
        def login():
            # grab user matching email
            # compare passwords submitted
            # redirect to the correct page
            query = ""
            data = {

            }
            mysql = g.get_db()
            mysql.query_db(query, data)
            return redirect('/wall')
        # logout user
        @app.route('/user/logout')
        def logout():
            """clear session"""
            session.clear()
            return redirect("/")
        # go to the wall
        @app.route('/wall', methods=['POST'])
        def wall():
            return render_template('wall.html')
        # crate a message
        @app.route('/message/create', methods=['POST'])
        def create_message():
            """Adds a message to the databse"""
            # validate inputs
            # insert into db
            # redirect to correct page 
            query = ""
            data = {

            }
            mysql = g.get_db()
            mysql.query_db(query, data)
            return redirect('/wall')
        # crate a comment
        @app.route('/', methods=['POST'])
        def create_comment():
            """Adds a comment to the db"""
            # validate inputs
            # insert into db
            # redirect to correct page 
            query = ""
            data = {

            }
            mysql = g.get_db()
            mysql.query_db(query, data)
            return redirect('/wall')
