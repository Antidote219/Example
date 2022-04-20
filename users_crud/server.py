from flask_app import app

from flask_app.controllers import user

# from flask import Flask, render_template, redirect, request

# from users import Users


# app = Flask(__name__)


# @app.route('/')
# def user():
#     return render_template("create.html")
# ## route to display users

# @app.route('/users')
# def display_users():
#     all_users = Users.get_all_users()
#     print(all_users)
#     return render_template("user.html", all_users = all_users)

# @app.route('/create/newuser', methods=['POST'])
# def create_newuser():
#     # print(request.form)
#     Users.create_user(request.form)
#     return redirect('/users')


# #####working below above works do not touch dummy

# @app.route('/edit/user/<int:user_id>')
# def edituser(user_id):
#     user = Users.get_user_by_id({'user_id':user_id})


#     query_data ={
#         "user_id" : user_id
#     }
    
    
#     return render_template("edit.html" , user = user)



# @app.route('/delete/user/<int:user_id>')
# def remove_user(user_id):
#     Users.delete_user({'user_id': user_id})
#     return redirect('/users')
    
    
# @app.route('/user/update/<int:user_id>' , methods=['POST'])
# def update_user(user_id):
#     data = {
#     'user_id': user_id,
#     'first_name': request.form['first_name'],
#     'last_name': request.form['last_name'],
#     'email': request.form['email']
#   }
#     Users.update_user(data)
#     # Users.user_update({'user_id': user_id})
#     return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)