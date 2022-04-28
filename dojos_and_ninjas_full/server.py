from flask_app import app
from flask_app.controllers import dojo_controller , ninja_controller

# @app.route('/')
# def index():
#     return f'testing testing '


# @app.route('/test')
# def test():
#     return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)