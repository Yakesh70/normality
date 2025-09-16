# 🚀 Deployment Guide

## Authentication Added ✅
- Login/Registration system implemented
- Users must login to access the normality testing tool
- Secure user sessions

## Deployment Options

### 1. **Heroku (Recommended)**
```bash
# Install Heroku CLI first
heroku create your-normality-app
git init
git add .
git commit -m "Add authentication and deploy"
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DJANGO_DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### 2. **Railway.app**
1. Connect GitHub repo to Railway
2. Set environment variables:
   - `SECRET_KEY`
   - `DJANGO_DEBUG=False`
   - `ALLOWED_HOSTS=your-domain.railway.app`
3. Auto-deploys on git push

### 3. **PythonAnywhere**
1. Upload project files
2. Configure WSGI file
3. Set environment variables in web tab
4. Run migrations in console

### 4. **DigitalOcean App Platform**
```bash
# Create app.yaml
git add .
git commit -m "Deploy to DigitalOcean"
git push origin main
```

## Environment Variables Needed
```
SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

## Post-Deployment Steps
1. Run migrations: `python manage.py migrate`
2. Create superuser: `python manage.py createsuperuser`
3. Test login/registration functionality
4. Share the URL with your manager

## URLs After Deployment
- Main app: `https://your-domain.com/`
- Login: `https://your-domain.com/accounts/login/`
- Register: `https://your-domain.com/accounts/register/`
- Admin: `https://your-domain.com/admin/`