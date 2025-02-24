# Vehicle Traffic Simulator (SOENG)

A web-based vehicle traffic simulation application built with Flask, featuring user authentication and feedback systems.

## Project Overview

This project is a Vehicle Traffic Simulator developed as part of the Software Engineering (CS3110) course. It provides a user-friendly interface for simulating traffic patterns with secure user authentication and feedback capabilities.

## Features

- User Authentication (Sign Up/Sign In)
- Traffic Simulation Visualization
- User Feedback System
- Responsive Design
- Interactive Navigation

## Tech Stack

- **Backend:**
  - Python 3.12
  - Flask
  - SQLAlchemy (Database ORM)
  - Werkzeug (Password Hashing)

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 4.5.2

- **Database:**
  - SQLite

## Project Structure

```
├── static/                 # Static files (CSS, JS, Images)
│   ├── css/               # Stylesheet files
│   ├── js/                # JavaScript files
│   ├── img/               # Image assets
│   └── simulation/        # Simulation assets
├── templates/             # HTML templates
├── instance/              # Database instance
├── env/                   # Virtual environment
├── models.py             # Database models
├── config.py             # Configuration settings
├── run.py               # Application entry point
├── utils.py             # Utility functions
└── requirements.txt     # Project dependencies
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Devcavi19/SE-CS3110-Project.git
cd SE-CS3110-Project
```

2. Create and activate virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Key Components

### Templates
- `base.html` - Base template with common layout elements
- `home.html` - Landing page
- `signin.html`/`signup.html` - Authentication pages
- `simulation.html` - Traffic simulation interface
- `feedback.html` - User feedback form
- `about.html` - About page with team information

### Static Files
- CSS files for styling different components
- JavaScript files for form validation and interactive features
- Images and simulation assets

### Python Files
- `run.py` - Application factory and main entry point
- `models.py` - Database models and schema
- `config.py` - Configuration settings
- `utils.py` - Helper functions
- `database.py` - Database initialization and routes

## Features Documentation

### User Authentication
- Secure signup with email verification
- Password hashing for security
- Session management for logged-in users

### Navigation
- Responsive navbar with dynamic content based on user authentication
- Easy access to all main features

### Simulation
- Interactive traffic simulation visualization
- Customizable simulation parameters
- Real-time updates

### Feedback System
- User feedback form
- Input validation
- Submission confirmation

## Contributors
- Herald
- Jester

## License
© 2024 Vehicle Traffic Simulator. All rights reserved.