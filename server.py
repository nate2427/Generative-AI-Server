from flask import Flask
from routes import routes, init_routes

app = Flask(__name__)

# Register project_x routes
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
