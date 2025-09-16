#!/bin/bash

echo "Setting up Normality Testing Web Application..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running database migrations..."
python manage.py migrate

echo "Setup complete! Run 'source venv/bin/activate && python manage.py runserver' to start the server."