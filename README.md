# Kindred

Kindred is a lightweight social media communication component built with Python and Flask. It provides a focused conversation experience around a single post, with reactions, comments, and basic moderation controls in a warm, responsive interface.

This project is intended as a simple prototype or starting point for a larger social discussion feature.

## Features

- Like and unlike the featured post.
- Add comments with a 280-character limit.
- Block a user to hide all of their comments.
- Hide an individual comment.
- Restore blocked users and hidden comments from the moderation panel.
- Responsive layout for desktop and mobile screens.
- Server-rendered HTML using Flask and Jinja templates.

## Technology

- Python 3.10+
- Flask 3.x
- Jinja2 templates
- HTML and CSS with no frontend build step

## Installation

### Windows PowerShell

From the project directory, create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

If PowerShell blocks script activation, run the application with the virtual environment's Python directly:

```powershell
.venv\Scripts\python.exe app.py
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

Start the development server from the project directory:

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser.

To interact with the component:

1. Select the heart control to like or unlike the featured post.
2. Enter a message in the comment field and select **Post**.
3. Use **Block user** beside a comment to hide all comments from that account.
4. Use **Hide** to remove only the selected comment from view.
5. Use the moderation panel to unblock a user or restore a hidden comment.

Stop the development server with `Ctrl+C`.

## Testing

The application can be checked with Flask's built-in test client:

```powershell
python -c "from app import app; client = app.test_client(); assert client.get('/').status_code == 200; print('Application check passed')"
python -m py_compile app.py
```

## Project structure

```text
.
├── app.py                  # Flask application and routes
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css            # Responsive visual styling
└── templates/
	└── index.html           # Conversation page
```

## Data and production considerations

This prototype stores posts, comments, likes, and moderation choices in Python process memory. All changes are reset when the server restarts, and the development server is not intended for production use.

For production, add a database, user authentication, CSRF protection, authorization checks, persistent moderation records, and a production WSGI server such as Waitress or Gunicorn.