# Import necessary Flask classes and functions
from flask import Flask, render_template, request, redirect, url_for

# Create an instance of the Flask class for web application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    # Render and return the HTML template the home page request
    return render_template('index.html')

# Define the route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit():
    # Check if the request method is POST (indicating a form submission)
    if request.method == 'POST':
        # Extract data from the form using the request.form dictionary
        name = request.form['name']  # Get the value of the 'name' field
        email = request.form['email']  # Get the value of the 'email' field
        question1 = request.form['question1']  # Get the value of the 'question1' field more questions pending working on the setup now
        
        
        # Process the extracted data (e.g., print to console, save to a database, etc.)
        print(f'Name: {name}, Email: {email}, Question1: {question1}')
        
        # Redirect the user back to the home page after processing the form data
        return redirect(url_for('index'))

# Check if this script is run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask web application in debug mode (auto-reloads code changes)
    app.run(debug=True)
