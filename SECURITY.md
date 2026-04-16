# Security Policy

## Reporting Security Vulnerabilities 🔒

**Please do NOT open public issues for security vulnerabilities.**

If you discover a security vulnerability, please email the maintainers directly instead of using the issue tracker.

### How to Report
1. Send an email with:
   - Description of the vulnerability
   - Steps to reproduce (if applicable)
   - Potential impact
   - Suggested fix (if you have one)

2. Include the following information:
   - Your name and affiliation
   - Contact information
   - When you discovered the vulnerability

We will acknowledge receipt within 48 hours and provide an estimated timeline for fix and disclosure.

## Security Practices ✅

This project follows these security best practices:

### Credentials & API Keys
- ✅ Never hardcode credentials or API keys
- ✅ Use environment variables or secure input fields
- ✅ Support for sensitive data masking in UI
- ✅ Credentials stored locally, never transmitted to third parties (except to legitimate services)

### Dependencies
- ✅ Regular dependency updates
- ✅ Monitor for security advisories
- ✅ Use pinned versions in requirements.txt
- ✅ Regular security audits

### Code Security
- ✅ Input validation on CSV files
- ✅ Email validation before sending
- ✅ SQL injection prevention (if database used)
- ✅ HTTPS for API communications
- ✅ Secure random number generation for delays

### Gmail Integration
- ✅ Uses official Gmail SMTP (smtp.gmail.com:587)
- ✅ Requires app-specific passwords (more secure than main password)
- ✅ 2-Factor Authentication recommended
- ✅ TLS encryption for email transmission
- ✅ No password storage - only in memory during session

### Groq API
- ✅ Uses official Groq API endpoints
- ✅ API key transmitted securely via HTTPS
- ✅ No API key logging or storage
- ✅ Key input field masked (*) in UI

## Known Security Considerations ⚠️

### Local Storage
- API keys and credentials are stored in application memory only
- Not persisted to disk (except manual config files)
- Recommend keeping config files secure and outside git

### CSV Data
- User responsible for securing contact lists
- CSV files may contain sensitive email addresses
- Recommend not storing CSVs in public repositories

### Email Content
- Generated content goes to Groq API for generation
- Users should ensure compliance with data privacy regulations
- Not recommended for highly sensitive information

## Security Updates

We commit to:
- Addressing critical vulnerabilities within 48 hours
- Addressing high-severity vulnerabilities within 1 week
- Releasing security patches independently of feature releases
- Documenting security fixes in release notes

## Dependency Security

### Current Dependencies
```
customtkinter==5.2.2  - GUI framework
pandas==2.1.4         - Data processing
groq==0.4.2           - AI API client
python-dotenv==1.0.0  - Environment management
```

### Checking for Vulnerabilities
```bash
# Check for known vulnerabilities
pip install safety
safety check

# Or using pip-audit
pip install pip-audit
pip-audit
```

## Email Marketing Compliance 📧

When using this tool, ensure compliance with:

### CAN-SPAM Act (USA)
- ✅ Include physical address in emails
- ✅ Provide clear unsubscribe mechanism
- ✅ Honor unsubscribe requests within 10 days
- ✅ Include accurate subject lines
- ✅ Identify emails as advertisements

### GDPR (EU)
- ✅ Obtain explicit consent before sending
- ✅ Easy opt-out mechanism
- ✅ Data retention policies
- ✅ Privacy notices in emails
- ✅ Right to be forgotten compliance

### CASL (Canada)
- ✅ Explicit consent required
- ✅ Clear sender identification
- ✅ Unsubscribe mechanism
- ✅ Honor unsubscribe requests

### LGPD (Brazil)
- ✅ Explicit consent required
- ✅ Transparent data usage
- ✅ Right to access personal data
- ✅ Easy unsubscribe mechanism

## Best Practices 🛡️

### For Users
1. Use strong, unique Gmail passwords
2. Enable 2-Factor Authentication on Gmail
3. Use app-specific passwords, not main account password
4. Keep your Groq API key confidential
5. Store contact lists securely
6. Review generated content before sending
7. Include unsubscribe mechanism in emails
8. Monitor bounce rates and spam complaints
9. Test campaigns with small batches first
10. Comply with local email marketing laws

### For Developers
1. Never commit credentials to version control
2. Use `.env` files (not in git) for local development
3. Validate and sanitize all user inputs
4. Keep dependencies updated
5. Use security-focused linters
6. Test for common vulnerabilities
7. Follow OWASP guidelines
8. Use HTTPS for all external communication
9. Implement proper error handling
10. Log security events (without exposing sensitive data)

## Security Checklist

Before deploying to production:
- [ ] All credentials are externalized
- [ ] Dependencies are up to date
- [ ] No hardcoded passwords or keys
- [ ] Input validation is implemented
- [ ] Error messages don't expose sensitive info
- [ ] HTTPS is used for external APIs
- [ ] Rate limiting is configured
- [ ] Logging doesn't capture credentials
- [ ] User data is protected
- [ ] Compliance requirements are met

## Third-Party Services

### Groq API
- **Privacy**: Check [Groq's Privacy Policy](https://groq.com/privacy/)
- **Terms**: Check [Groq's Terms of Service](https://groq.com/terms/)
- **Data**: Requests may be used to improve service

### Gmail
- **Privacy**: Check [Google's Privacy Policy](https://policies.google.com/privacy)
- **Terms**: Check [Gmail Terms of Service](https://policies.google.com/terms)
- **Security**: Use official Gmail SMTP servers

## Vulnerability Disclosure Timeline

When a vulnerability is reported:
1. **Immediate**: Acknowledge receipt and begin investigation
2. **24-48 hours**: Confirm vulnerability and assess impact
3. **48-72 hours**: Develop and test fix
4. **At release**: Publish fix and security advisory
5. **Post-release**: Monitor for any issues

## Versioning

Security updates are released as patch versions (e.g., 1.0.1) to ensure easy installation.

## Questions?

If you have security-related questions:
1. Check this security policy
2. Review the README security section
3. Check CONTRIBUTING.md for contact info
4. Open a private discussion if needed

---

**Last Updated**: January 15, 2024

This security policy is subject to change. We recommend checking back regularly for updates.
