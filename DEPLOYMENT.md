# Internship Project Portal - Production Deployment Guide

## 🚀 Quick Deployment

This guide will help you deploy the Internship Project Portal to production environments.

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL 12+
- Docker & Docker Compose (recommended)

## 🛠️ Deployment Options

### Option 1: Docker Deployment (Recommended)

**Quick Start:**
```bash
# Clone the repository
git clone <repository-url>
cd Internship-Project-Portal-main

# Start with Docker Compose
docker-compose up -d

# Access the application at http://localhost:5000
```

**Docker Services Created:**
- `internship_portal_db` - PostgreSQL database
- `internship_portal_backend` - Flask application

### Option 2: Manual Deployment

#### Backend Setup:
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create .env file
cp .env.example .env
# Edit .env with your configuration

# 3. Initialize database
python init_postgres_db.py

# 4. Start the application
python app.py
```

#### Frontend Setup:
```bash
# 1. Install dependencies
cd frontend
npm install

# 2. Build for production
npm run build

# 3. Serve built files (Flask will serve them automatically)
```

## ⚙️ Configuration

### Environment Variables (.env)
```env
# Database
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=MyPortalDb

# Security
SECRET_KEY=your-very-secure-secret-key
JWT_SECRET_KEY=your-jwt-secret-key

# Application
FLASK_ENV=production
DEBUG=False
```

### Production Security
- Change default SECRET_KEY and JWT_SECRET_KEY
- Use HTTPS in production
- Set DEBUG=False
- Configure proper CORS settings

## ☁️ Cloud Platform Deployment

### Heroku
```bash
# 1. Create Heroku app
heroku create internship-portal

# 2. Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# 3. Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set JWT_SECRET_KEY=your-jwt-secret

# 4. Deploy
git push heroku main
```

### Render
1. Create Web Service
2. Connect GitHub repository
3. Add environment variables in dashboard
4. Set build command: `cd frontend && npm install && npm run build`
5. Set start command: `python app.py`

### AWS
- Use Elastic Beanstalk for Flask app
- Use S3 for static files
- Use RDS for PostgreSQL

## 🔍 Testing Deployment

### Health Checks
```bash
# Test backend API
curl http://localhost:5000/api/health

# Test database connection
python test_db_connection.py

# Test frontend build
cd frontend && npm run build
```

### Common Endpoints
- `/` - Main application
- `/api/auth/login` - Authentication
- `/api/student/dashboard` - Student dashboard
- `/api/company/dashboard` - Company dashboard

## 🛡️ Security Considerations

### Production Checklist
- [ ] Change all default passwords
- [ ] Use HTTPS with SSL certificate
- [ ] Set up proper firewall rules
- [ ] Configure rate limiting
- [ ] Set up monitoring and logging
- [ ] Regular security updates
- [ ] Database backups

### File Upload Security
- Limit file types and sizes
- Scan uploaded files
- Store files outside web root
- Use CDN for file serving

## 📊 Monitoring

### Log Files
- Application logs: Check console output
- Database logs: PostgreSQL logs
- Nginx logs: `/var/log/nginx/`

### Performance Monitoring
- Database query performance
- API response times
- Memory usage
- Disk space

## 🔧 Maintenance

### Regular Tasks
- Update dependencies
- Database maintenance
- Log rotation
- Security patches
- Backup verification

### Backup Strategy
```bash
# Database backup
pg_dump -U postgres MyPortalDb > backup_$(date +%Y%m%d).sql

# File backup
tar -czf uploads_backup_$(date +%Y%m%d).tar.gz uploads/
```

## 🆘 Troubleshooting

### Common Issues

1. **Database Connection Failed**
   ```bash
   # Check PostgreSQL service
   sudo systemctl status postgresql
   
   # Test connection
   python test_db_connection.py
   ```

2. **Application Not Starting**
   ```bash
   # Check logs
   tail -f app.log
   
   # Verify dependencies
   pip list | grep -E "(flask|sqlalchemy)"
   ```

3. **Frontend Issues**
   ```bash
   # Rebuild frontend
   cd frontend
   npm run build --clean
   
   # Check build output
   ls -la dist/
   ```

4. **Permission Errors**
   ```bash
   # Fix upload directory permissions
   sudo chown -R www-data:www-data uploads/
   sudo chmod -R 755 uploads/
   ```

## 📞 Support

For deployment assistance:
1. Check the [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)
2. Review platform-specific documentation
3. Check application logs for error details
4. Verify all prerequisites are met

---

**Version:** 1.0  
**Last Updated:** February 2026