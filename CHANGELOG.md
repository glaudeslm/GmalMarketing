# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-15

### Added
- Initial release of AI Email Marketing Assistant
- AI-powered email content generation using Groq API
- Bulk email sending with Gmail SMTP integration
- Modern GUI built with CustomTkinter
- CSV contact list import with Email and FirstName columns
- Customizable email generation rules:
  - Mandatory conditions for email content
  - Forbidden words filter
  - Subject line templates
  - Site link integration
  - Extra links support
- Scheduled email sending with specific time selection
- Activity logging with real-time updates
- Human-like sending delays (45-150 seconds between emails)
- Campaign pause/stop functionality
- Email validation and error handling
- Settings panel for API keys and credentials
- MIT License for open-source distribution
- Comprehensive README with setup instructions
- Requirements.txt for easy dependency installation

### Features
- Support for dynamic content personalization with recipient names
- Gmail app password support (secure, doesn't require main password)
- Rate limiting to avoid spam filters
- Automatic error recovery with retry logic
- Clear activity logs with timestamps

### Documentation
- README.md with complete setup and usage guide
- LICENSE file (MIT)
- CONTRIBUTING.md for contributors
- This CHANGELOG

## [Unreleased]

### Planned Features
- Email template builder with drag-and-drop interface
- Database integration (SQLite/PostgreSQL) for persistent contact management
- Campaign analytics and reporting dashboard
- Multiple account support
- Scheduled task automation with cron-like scheduling
- Email preview before sending with edit capability
- A/B testing framework for subject lines
- Support for additional AI models (OpenAI, Anthropic, etc.)
- Docker containerization
- Web dashboard interface

### Under Consideration
- Webhook integrations
- API for external applications
- Mobile app companion
- Telegram bot for notifications
- Support for other email providers (Outlook, Custom SMTP)
- Internationalization (i18n) for multiple languages
- Advanced filtering and segmentation
- Bounce and complaint handling

---

## How to Update

To update to the latest version:

```bash
# Pull latest changes
git pull origin main

# Install any new dependencies
pip install -r requirements.txt

# Run the application
python GmalMarketing.py
```

## Version History

| Version | Date | Status |
|---------|------|--------|
| 1.0.0 | 2024-01-15 | Latest |

## Support

For issues or questions about specific versions:
- Open a GitHub Issue
- Check existing discussions
- Refer to README.md for setup help

---

**Last Updated**: January 15, 2024
