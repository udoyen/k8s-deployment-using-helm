from flask import Flask

app = Flask(__name__)

# Route for the default page
@app.route("/")
def home():
    # Display message
    return "<center><h3>Welcome to GFG</h3></center>"

if __name__ == '__main__':
    app.run('0.0.0.0')