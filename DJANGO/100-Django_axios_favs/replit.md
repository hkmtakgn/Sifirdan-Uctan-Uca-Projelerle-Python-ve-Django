# Django Weblog Project

## Overview

This is a Django-based weblog application that provides a content management system for creating and managing web pages. The project features a dynamic page system where pages can be created through the Django admin interface and displayed on the frontend with custom slugs. The application includes both static pages (home, contact, user registration, share post) and dynamic pages stored in the database.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
The application follows Django's Model-View-Template (MVT) architecture pattern:

- **Models**: The `Page` model serves as the core data structure, storing page information including title, slug, background image, avatar, content, and activation status
- **Views**: Function-based views handle both static pages and dynamic page rendering using slug-based routing
- **URL Routing**: Two-tier URL configuration with project-level routing in `config/urls.py` and app-level routing in `weblog/urls.py`
- **Admin Interface**: Django admin is configured for content management of pages

### Frontend Architecture
- **Template System**: Django template inheritance with a base template (`base.html`) and component-based navbar
- **Static Content**: Bootstrap 5.3.8 CDN integration for responsive UI components
- **Dynamic Navigation**: Context processor provides global access to active pages for navigation menu
- **Media Handling**: Configured for image uploads with separate directories for page backgrounds and avatars

### Database Design
- **Single Model Architecture**: Simple schema centered around the `Page` model
- **Auto-slug Generation**: Uses `django-autoslug` for SEO-friendly URL generation
- **Image Storage**: File upload fields for page backgrounds and avatars
- **Content Management**: Text field for rich content with activation toggle

### URL Structure
- Static routes: `/`, `/register-user/`, `/share-post/`, `/contact/`
- Dynamic routes: `/<slug>/` for database-driven pages
- Admin interface: `/admin/`
- Media serving: `/media/` for uploaded images

### Security Configuration
- Development settings with debug mode enabled
- CSRF protection configured for Replit environment
- Allowed hosts configured for local and Replit deployment

## External Dependencies

### Python Packages
- **Django 5.0.2**: Core web framework
- **django-autoslug**: Automatic slug field generation for SEO-friendly URLs
- **Pillow**: Python Imaging Library for image field support (implied by ImageField usage)

### Frontend Dependencies
- **Bootstrap 5.3.8**: CSS framework loaded via CDN for responsive design and UI components
- **Bootstrap JavaScript**: Bundle for interactive components

### Development Environment
- **Python 3.10**: Runtime environment
- **Replit**: Cloud-based development and hosting platform
- **Static File Serving**: Django's built-in static file handling for development

### Database
- **SQLite**: Default Django database for development (database file not visible in repository)
- **Django ORM**: Object-relational mapping for database operations
- **Migration System**: Django's built-in database schema management