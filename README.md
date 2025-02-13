# Flask & StackExchange API Fun Times 🎉

Welcome to the coolest project ever! We're diving into the world of Flask, SQLAlchemy, and the StackExchange API. Buckle up, because this is going to be a wild ride! 🚀

## What's This About? 🤔

We're building a super awesome REST API using Flask. We'll be fetching questions from StackExchange (because who doesn't love StackExchange?) and storing them in our very own database. Oh, and did I mention we're using SQLAlchemy for that? Yeah, we're fancy like that. 😎

## Getting Started 🛠️

First things first, let's get you set up. Follow these steps and you'll be up and running in no time!

### Prerequisites 📋

Make sure you have Python installed. If not, go get it [here](https://www.python.org/downloads/). We'll wait... ⏳

### Installation 📦

1. Clone this repo (because it's awesome):
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment (because we're cool like that):
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment (activate!):
   ```bash
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On MacOS/Linux
   ```

4. Install the required packages (pip it up!):
   ```bash
   pip install Flask SQLAlchemy requests flasgger
   ```

## Running the Show 🎬

1. Fire up the Flask app:
   ```bash
   python Tester.py
   ```

2. Open your browser and head to `http://127.0.0.1:5000/apidocs` to see the magic happen. ✨

## The Code Breakdown 🧩

### Fetching StackExchange Questions

In consume_api.py, we're making a request to the StackExchange API to fetch the latest questions. Here's a sneak peek:

```python
import requests

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

count = 0
for each_item in response.json()['items']:
    count += 1
    print('Question ', str(count) + " : "+ each_item['title'], '\nIs answered: ', each_item['is_answered'], end='\n')

print()
count = 0
for each_item in response.json()['items']:
    if each_item['answer_count'] == 0:
        count += 1
        print("Question "+ str(count) + ": ", each_item['title'], "\n")
print("There are", count, "question unanswered.")
```

### Storing Questions in the Database

In `Tester.py`, we're using SQLAlchemy to create a `Question` model and store the fetched questions in our SQLite database. Check it out:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    is_answered = db.Column(db.Boolean, nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

## Contributing 🤝

Want to make this project even cooler? Fork it, make your changes, and submit a pull request. We'll review it and merge it if it's awesome (which it will be, because you're awesome).

## License 📜

This project is licensed under the MIT License. Do whatever you want with it, just don't blame us if it breaks the internet. 😉

## Acknowledgements 🙌

- StackExchange, for being our savior in times of coding despair.
- Flask, for making web development fun and easy.
- SQLAlchemy, for making databases less scary.

Happy coding! 🎉