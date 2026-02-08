# Deployment Checklist for Internship Project Portal

## 🚀 Pre-Deployment Requirements

### 1. System Requirements
- [ ] Python 3.8+ installed
- [ ] Node.js 16+ installed
- [ ] PostgreSQL 12+ installed and running
- [ ] Git installed (for version control)

### 2. Environment Setup
- [ ] Create `.env` file with database credentials
- [ ] Verify PostgreSQL server is running
- [ ] Create database `MyPortalDb` in PostgreSQL
- [ ] Install Python dependencies: `pip install -r requirements.txt`
- [ ] Install frontend dependencies: `cd frontend && npm install`

## 📋 Deployment Steps

### Step 1: Backend Setup
```bash
# 1. Navigate to project root
cd Internship-Project-Portal-main

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Create .env file (if not exists)
# Copy .env.example to .env and update credentials

# 4. Test database connection
python test_db_connection.py

# 5. Initialize database tables
python init_postgres_db.py

# 6. Seed initial data (optional)
python seed_data.py
```

### Step 2: Frontend Setup
```bash
# 1. Navigate to frontend directory
cd frontend

# 2. Install dependencies
npm install

# 3. Build for production
npm run build
```

### Step 3: Run Application
```bash
# Option 1: Development mode (separate servers)
# Terminal 1 - Backend:
cd Internship-Project-Portal-main
python app.py

# Terminal 2 - Frontend:
cd Internship-Project-Portal-main/frontend
npm run dev

# Option 2: Production mode (Flask serves built frontend)
# Build frontend first:
cd frontend
npm run build

# Then run Flask:
cd ..
python app.py
```

## 🔧 Configuration Files

### .env File Structure
```env
# Database Configuration
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=MyPortalDb

# Security
SECRET_KEY=your-secret-key-change-in-production
JWT_SECRET_KEY=jwt-secret-key-change-in-production

# Optional: Supabase for file storage
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
SUPABASE_BUCKET=student-docs
```

## 🌐 Production Deployment Options

### Option 1: Traditional Hosting (VPS/Shared Hosting)
1. Upload code to server
2. Install dependencies
3. Configure web server (Nginx/Apache)
4. Set up process manager (PM2, systemd)
5. Configure SSL certificate

### Option 2: Cloud Platforms

#### Heroku Deployment
```bash
# 1. Create Heroku app
heroku create internship-portal

# 2. Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev

# 3. Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set JWT_SECRET_KEY=your-jwt-secret

# 4. Deploy
git push heroku main
```

#### Render Deployment
1. Create new Web Service on Render
2. Connect GitHub repository
3. Add environment variables in dashboard
4. Set build command: `cd frontend && npm install && npm run build`
5. Set start command: `python app.py`

#### AWS Deployment
1. Use Elastic Beanstalk for Flask application
2. Use S3 for static file storage
3. Use RDS for PostgreSQL database
4. Configure Load Balancer and Auto Scaling

### Option 3: Docker Deployment
```dockerfile
# Dockerfile for backend
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

```dockerfile
# Dockerfile for frontend
FROM node:18-alpine as build
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## 🔍 Testing Checklist

### Backend Tests
- [ ] Database connection test: `python test_db_connection.py`
- [ ] API endpoints test: `python test_api_endpoints.py`
- [ ] Authentication test: `python test_login.py`

### Frontend Tests
- [ ] Build process: `npm run build`
- [ ] Development server: `npm run dev`
- [ ] All pages load without errors

### Integration Tests
- [ ] User registration flow
- [ ] Login/logout functionality
- [ ] Student profile creation
- [ ] Company opportunity posting
- [ ] Application submission
- [ ] File upload functionality

## 🛡️ Security Considerations

### Production Security
- [ ] Change default SECRET_KEY and JWT_SECRET_KEY
- [ ] Use HTTPS in production
- [ ] Set DEBUG=False in production
- [ ] Configure proper CORS settings
- [ ] Set up rate limiting
- [ ] Implement proper input validation
- [ ] Regular security updates

### Database Security
- [ ] Use strong database passwords
- [ ] Limit database user permissions
- [ ] Regular backups
- [ ] Secure database connections

## 📊 Monitoring and Maintenance

### Logging
- [ ] Set up application logging
- [ ] Configure error tracking
- [ ] Monitor database performance

### Backups
- [ ] Regular database backups
- [ ] File backup strategy
- [ ] Recovery procedures documented

### Updates
- [ ] Regular dependency updates
- [ ] Security patch monitoring
- [ ] Version control for deployments

## 🆘 Troubleshooting

### Common Issues

1. **Database Connection Failed**
   - Check PostgreSQL service status
   - Verify credentials in .env
   - Ensure database exists

2. **Frontend Build Failures**
   - Check Node.js version compatibility
   - Clear npm cache: `npm cache clean --force`
   - Reinstall dependencies

3. **File Upload Issues**
   - Check upload folder permissions
   - Verify Supabase configuration (if used)
   - Check file size limits

4. **Authentication Errors**
   - Verify JWT configuration
   - Check token expiration settings
   - Test with different user roles

## 📞 Support

For deployment issues:
1. Check the project documentation
2. Review error logs
3. Test components individually
4. Refer to platform-specific deployment guides

---

**Last Updated:** February 2026
**Version:** 1.0