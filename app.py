# Import necessary Flask classes and functions
from flask import Flask, render_template, request, redirect, url_for

# Create an instance of the Flask class for web application
app = Flask(__name__)

#personData object to collect the question answers
class PersonData:
    def __init__(self, name, date, question1, question2, question3, question4, question5):
        self.name = name
        self.date = date
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.question4 = question4
        self.question5 = question5

        # Create an instance of PersonData with the form data
        person_data = PersonData(name, date, question1, question2, question3, question4, question5)
        

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
        date = request.form['date']  # Get the value of the 'email' field
        # Get the value of the question field 
        question1 = request.form['question1']  
        question2 = request.form['question2']
        question3 = request.form['question3']
        question4 = request.form['question4']
        question5 = request.form['question5']
        
        # Process the extracted data 
        print(f"Name: {person_data.name}")
        print(f"Date: {person_data.date}")
        print(f"Question 1: {person_data.question1}")
        print(f"Question 2: {person_data.question2}")
        print(f"Question 3: {person_data.question3}")
        print(f"Question 4: {person_data.question4}")
        print(f"Question 5: {person_data.question5}")
        
        # Redirect the user back to the home page after processing the form data
        return redirect(url_for('index'))

# Check if this script is run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask web application in debug mode (auto-reloads code changes)
    app.run(debug=True)
