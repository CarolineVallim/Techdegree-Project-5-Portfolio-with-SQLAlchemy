Project 5 - Portfolio with SQLAlchemy

A description of the project
Create an interface for a portfolio web application. The main (index) page lists your projects including the project title and short description. Each project links to a detail page that displays the title, date, and description.
The application lets the user add or edit project information. When adding or editing a project, the application prompts the user for title, date, skills, description, and a link to a repo. The results for these entries are stored in a database and displayed on the homepage. The HTML/CSS for this site has been supplied for you.

How to run the project:
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

What I learned:
Create a route for the aplication
Cleanig and update the data
Using Flask-SQLAlchemy to connect and interact with the database
Catching 404 error and show it