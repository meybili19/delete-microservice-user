from flask import Flask
from config import Config
from models import db
from routes import delete_user

# Create the application
app = Flask(__name__)

# Application configuration
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the delete user route
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user_route(id):
    return delete_user(id)

if __name__ == '__main__':
    app.run(debug=True) 