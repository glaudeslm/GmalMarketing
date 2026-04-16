# Frequently Asked Questions (FAQ) ❓

## General Questions

### Q: Is this application free?
**A:** Yes! It's completely free and open-source under the MIT License. You can use, modify, and distribute it.

### Q: Is this for spam?
**A:** No. This tool is designed for **legitimate email marketing** to opted-in recipients. Using it for spam violates laws (CAN-SPAM, GDPR, CASL, LGPD) and email provider terms of service. Users are responsible for compliance.

### Q: What's the difference between this and other email tools?
**A:** 
- Runs on your computer (not cloud-based)
- Uses AI to generate personalized content
- Completely free and open-source
- Full control over your data
- Perfect for small businesses and campaigns

### Q: Can I contribute to the project?
**A:** Yes! Check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on bug reports, feature requests, and pull requests.

### Q: How do I report security issues?
**A:** See [SECURITY.md](SECURITY.md) for responsible disclosure procedures. Don't post security issues publicly.

---

## Setup & Installation

### Q: I don't have Python installed. How do I get it?
**A:** 
1. Visit [python.org](https://www.python.org/downloads/)
2. Download Python 3.8 or higher
3. Run the installer
4. Make sure to check "Add Python to PATH"

### Q: What version of Python do I need?
**A:** Python 3.8 or higher. Check your version:
```bash
python --version
```

### Q: Do I need all the listed dependencies?
**A:** Yes, all dependencies in `requirements.txt` are required:
- **customtkinter** - GUI framework
- **pandas** - CSV handling
- **groq** - AI API client
- **python-dotenv** - Environment variables

Install them with:
```bash
pip install -r requirements.txt
```

### Q: Can I use this on Mac/Linux?
**A:** Yes! The application works on:
- Windows (10, 11)
- macOS (10.13+)
- Linux (Ubuntu, Debian, etc.)

### Q: I'm getting "ModuleNotFoundError". What's wrong?
**A:** You probably forgot to install dependencies:
```bash
pip install -r requirements.txt
```

Or you're not in the virtual environment (run `source venv/bin/activate`).

---

## Gmail Setup

### Q: What's an "app password"?
**A:** A special 16-digit password Google generates for apps. It's more secure than your main password because you can revoke it anytime.

### Q: Why can't I use my regular Gmail password?
**A:** Google requires app passwords for:
- Better security
- Revoking access without changing your main password
- Protecting your main account

### Q: I don't have "App passwords" option
**A:** You need 2-Step Verification enabled first:
1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click **Security**
3. Find **2-Step Verification** and enable it
4. Then you'll see **App passwords**

### Q: How do I generate a new app password?
**A:**
1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Select **Mail** and your device type
3. Google generates a 16-digit code
4. Copy all 16 digits (including spaces)

### Q: Can I use my Gmail password instead?
**A:** Technically yes, but we strongly advise against it. Use app passwords for security.

### Q: "Invalid login credentials" error - what's wrong?
**A:** Most common causes:
- Using wrong 16-digit app password
- Copying a Gmail password instead of app password
- Missing digits in the 16-digit code
- 2-Step Verification not enabled
- Wrong email address

Try generating a new app password.

### Q: Is my password stored anywhere?
**A:** No. Your credentials are:
- Only stored in memory while the app runs
- Never saved to disk
- Never sent anywhere except Gmail SMTP servers
- Deleted when you close the app

### Q: Can I use this with Gmail for Business?
**A:** Yes! App passwords work the same way with Google Workspace accounts.

---

## Groq API

### Q: Is Groq API free?
**A:** Yes! The free tier includes generous monthly credits (~3-5M tokens). Check [console.groq.com](https://console.groq.com) for current limits.

### Q: How do I get a Groq API key?
**A:**
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Go to **API Keys**
4. Create a new API key
5. Copy the key (looks like: `gsk_...`)

### Q: "Groq API error" - what's wrong?
**A:** Check:
1. Is your API key correct? (Copy it exactly)
2. Do you have remaining API credits? (Check console.groq.com)
3. Is your internet working?
4. Is Groq API down? (Check status.groq.com)

### Q: Can I use other AI models?
**A:** The current version uses Groq's LLaMA 3.1 model. Support for other models is planned for future versions.

### Q: How many emails can I send?
**A:** Limited by:
- Your Groq API credits (free tier has monthly limits)
- Gmail's sending limits (~500-1000/day from new accounts)
- Your contact list size

For large campaigns, contact Groq about higher limits.

### Q: Is my data sent to Groq?
**A:** Yes, the email content and recipient first name are sent to Groq API to generate personalized content. Check [Groq's Privacy Policy](https://groq.com/privacy/).

---

## Contact Lists (CSV)

### Q: What format should my CSV be?
**A:** 
- Columns: `Email` and `FirstName`
- One contact per row
- Comma-separated values
- Can use Excel, Google Sheets, or any text editor

**Example:**
```csv
Email,FirstName
john@example.com,John
jane@example.com,Jane
```

### Q: Can I have more columns?
**A:** Yes, but the app only uses `Email` and `FirstName`. Other columns are ignored.

### Q: What if my CSV has different column names?
**A:** The app requires exactly:
- `Email` (not "email" or "EMAIL")
- `FirstName` (not "first_name" or "First Name")

Column names are case-sensitive.

### Q: Can I import from Excel?
**A:** Yes! Save your Excel file as CSV:
1. Open in Excel
2. File > Save As
3. Select "CSV" format
4. Save and import in the app

### Q: How many contacts can I import?
**A:** Theoretically unlimited, but practical limits depend on:
- Available RAM
- Gmail sending limits
- Groq API credits

Start with smaller batches (100-500) for testing.

### Q: Can I edit the CSV after importing?
**A:** The app doesn't have CSV editing. Edit in Excel or your text editor, then re-import.

### Q: What if I have duplicate emails?
**A:** The app will try to send to all, including duplicates. Remove duplicates in your CSV first:
- Excel: Data > Remove Duplicates
- Google Sheets: Data > Data cleanup > Remove duplicates

### Q: Can I have conditional content based on CSV data?
**A:** Not currently. Planned for future versions.

---

## Sending Campaigns

### Q: Why is sending so slow?
**A:** Intentional! The app waits 45-150 seconds between emails to:
- Avoid Gmail spam filters
- Look human-like
- Respect rate limits

This is actually good - it increases deliverability.

### Q: Can I speed up sending?
**A:** Not recommended - you'll risk:
- Gmail account suspension
- Emails marked as spam
- Blacklisting

The delays are a feature, not a limitation.

### Q: Can I pause and resume?
**A:** You can stop (`🛑 STOP CAMPAIGN`), but there's no "resume". You'd need to:
1. Create a CSV with remaining contacts
2. Start a new campaign

Future versions will support pausing/resuming.

### Q: Can I schedule emails for specific times?
**A:** Yes! Set "Send Time (HH:MM)" in settings. The app waits until that time before starting.

### Q: Can I send on weekends/specific days?
**A:** Not currently. Planned for future versions.

### Q: Will duplicate emails be sent?
**A:** Only if your CSV contains duplicates. Remove them before importing.

---

## Email Content

### Q: How does AI generate the emails?
**A:** The app sends Groq AI:
- Your mandatory conditions (tone, style, length)
- Forbidden words list
- Recipient's first name
- Groq generates personalized email content

### Q: Can I preview emails before sending?
**A:** Currently the first email is generated and sent immediately. Email preview before sending is planned for future versions.

### Q: Can I manually edit generated emails?
**A:** Not currently - the app generates and sends automatically. Manual editing is planned.

### Q: How can I control email tone?
**A:** Use the "Mandatory Conditions" tab:
```
1. Professional, friendly tone
2. No technical jargon
3. Focus on benefits, not features
4. Use conversational language
```

### Q: How can I prevent spam-like content?
**A:** Use the "Forbidden Words" tab to block common spam words:
```
FREE
LIMITED TIME
URGENT
GUARANTEE
EARN MONEY
```

### Q: Can I include my unsubscribe link?
**A:** Add it in "Extra Links" tab. Recommended for compliance with CAN-SPAM, GDPR, etc.

### Q: Can I personalize beyond just first name?
**A:** Currently only first names from CSV. Full name, company, etc. will be supported in future versions.

---

## Troubleshooting

### Q: "CSV must contain 'Email' and 'FirstName' columns"
**A:** Your CSV columns are named differently. Check:
- Column names are exactly `Email` and `FirstName`
- No extra spaces
- Case-sensitive

Rename columns in your CSV file.

### Q: Application crashes when I click START CAMPAIGN
**A:** Check:
1. Is Gmail configured correctly?
2. Is Groq API key valid?
3. Is CSV imported?
4. Check Activity Log for error details

Post the error message in GitHub Issues.

### Q: Activity Log shows errors for every email
**A:** Common causes:
- Wrong Gmail app password
- Groq API key issues
- Email addresses in CSV are invalid
- Gmail account has security issues

Verify credentials and try with 1-2 test emails.

### Q: Application freezes
**A:** The app might be:
- Waiting for scheduled send time
- Generating content with Groq API
- Sending email

Wait a few seconds. If it stays frozen, close and reopen.

### Q: Where are application logs saved?
**A:** Activity logs are shown in the app only. They're not saved to disk by default.

### Q: How do I report a bug?
**A:** 
1. Note the exact error message
2. Note steps to reproduce
3. Open a [GitHub Issue](https://github.com/yourusername/ai-email-marketing-assistant/issues)
4. Include OS, Python version, and full error message

---

## Legal & Compliance

### Q: Is this tool legal?
**A:** Yes, the tool itself is legal. **Using it responsibly is the user's responsibility:**

✅ Legal use:
- Email marketing to opted-in subscribers
- Following CAN-SPAM, GDPR, CASL, LGPD
- Including unsubscribe options
- Honest content

❌ Illegal use:
- Spam to non-subscribers
- Harvested email lists
- Deceptive content
- Phishing

### Q: What laws apply to email marketing?
**A:** Depends on your location and recipients:
- **USA**: CAN-SPAM Act
- **EU**: GDPR
- **Canada**: CASL
- **Brazil**: LGPD

See [README.md](README.md) for compliance links.

### Q: Do I need consent to email people?
**A:** 
- **USA**: Implied consent (if reasonable expectation)
- **EU/Canada**: Explicit consent required
- **Brazil**: Explicit consent required

Always get explicit consent to be safe.

### Q: Should I include an unsubscribe link?
**A:** 
- **Required** by CAN-SPAM (USA)
- **Recommended** for GDPR/CASL compliance
- **Good practice** for deliverability

Add it in "Extra Links" tab or email template.

---

## Performance & Optimization

### Q: How can I improve email deliverability?
**A:** 
1. Use professional tone (set in Mandatory Conditions)
2. Avoid spam words (Forbidden Words)
3. Include unsubscribe link
4. Warm up with small batches
5. Monitor bounce rates
6. Use proper sender name

### Q: Should I send from my main Gmail or a new account?
**A:** 
- **New account**: Better for clean sending reputation
- **Existing account**: May be rate-limited initially

Gmail throttles new accounts - consider warming up gradually.

### Q: Can I send from different Gmail accounts?
**A:** Not in one campaign, but you can:
1. Run campaign with account A
2. Later, run campaign with account B

Each account needs its own app password.

### Q: How do I track opens/clicks?
**A:** This app doesn't track opens/clicks. For analytics, use:
- Gmail's native analytics
- Email service providers (Mailchimp, SendGrid)
- Third-party tracking (future version planned)

---

## Features & Roadmap

### Q: Will there be a web version?
**A:** Planned for future versions. Currently desktop-only.

### Q: Can I schedule recurring campaigns?
**A:** Not yet, but it's planned. Currently one-time campaigns only.

### Q: Will you support other email providers?
**A:** Planned to support Outlook, SendGrid, etc. Currently Gmail only.

### Q: Can I export campaign results?
**A:** Not currently. Planned for future versions.

### Q: Is there a mobile app?
**A:** Not currently. Desktop-focused for now.

---

## Getting Help

### Q: Where do I ask questions?
**A:**
1. Check this FAQ
2. Read [README.md](README.md)
3. Open [GitHub Discussions](https://github.com/yourusername/ai-email-marketing-assistant/discussions)
4. Open a [GitHub Issue](https://github.com/yourusername/ai-email-marketing-assistant/issues) for bugs

### Q: How long does it take to get help?
**A:** 
- Maintainers try to respond within 24-48 hours
- Complex issues may take longer
- Community may respond faster

### Q: Can I contact the developer directly?
**A:** Use GitHub Issues/Discussions. Email may not be checked regularly.

### Q: How do I suggest a feature?
**A:** 
1. Check existing issues/discussions
2. Open a [GitHub Discussion](https://github.com/yourusername/ai-email-marketing-assistant/discussions)
3. Describe the feature and why it would help

---

## Still Have Questions?

- **Quick answers**: Check [QUICKSTART.md](QUICKSTART.md)
- **Detailed guide**: Read [README.md](README.md)
- **Setup issues**: See [SECURITY.md](SECURITY.md)
- **Contributing**: Check [CONTRIBUTING.md](CONTRIBUTING.md)
- **Ask the community**: [GitHub Discussions](https://github.com/yourusername/ai-email-marketing-assistant/discussions)

---

**Last Updated**: January 15, 2024

*Have a question not covered? Open a GitHub Discussion and we'll add it!*
