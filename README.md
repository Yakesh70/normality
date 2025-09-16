# Normality Testing Web Application

A Django web application that performs statistical normality testing on small datasets (10-15 numbers).

## Features

- **Statistical Analysis**: Calculates descriptive statistics (mean, median, std dev, skewness, kurtosis)
- **Normality Tests**: Shapiro-Wilk and D'Agostino K² tests with interpretations
- **Visualizations**: Histogram and Q-Q plots
- **Web Interface**: Clean, user-friendly form for data input

## Setup Instructions

### 1. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Start Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to use the application.

## Usage

1. Enter 10-15 numbers separated by commas, spaces, newlines, or semicolons
2. Click "Analyze" to get:
   - Summary statistics
   - Normality test results with interpretations
   - Histogram and Q-Q plot visualizations

## Deployment

The project is configured for Heroku deployment with:
- `Procfile` for web server configuration
- `requirements.txt` for dependencies
- WhiteNoise for static file serving
- Environment variable support

## Dependencies

- Django 4.2+
- NumPy (numerical computations)
- SciPy (statistical tests)
- Matplotlib (plotting)
- Gunicorn (production server)
- WhiteNoise (static files)