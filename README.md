# AI Email Marketing Assistant
<img width="1366" height="725" alt="emailmarketing_gmail" src="https://github.com/user-attachments/assets/c249b836-02e2-4b23-9ce8-295346301aa4" />

A powerful, open-source desktop application for generating and sending personalized emails using AI. Powered by **Groq API** and **CustomTkinter**, this tool helps you create professional email campaigns with AI-generated content while respecting rate limits and maintaining a human-like sending pattern.

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-success)

## Features ✨

- 🤖 **AI-Powered Content Generation** - Uses Groq's LLaMA 3.1 model to generate dynamic, personalized email content
- 📧 **Bulk Email Sending** - Send campaigns to hundreds of contacts with automatic pauses between sends
- 🎨 **Modern GUI** - Clean, intuitive interface built with CustomTkinter
- ⚙️ **Fully Customizable** - Set mandatory conditions, forbidden words, subjects, and more
- 🕐 **Scheduled Sending** - Schedule campaigns for specific times
- 📋 **CSV Import** - Easily import contact lists with email and first name
- 🔒 **Security** - Uses Gmail app passwords (not your main password)
- 📝 **Activity Logging** - Real-time log of all campaign activities
- ⏸️ **Stop Anytime** - Pause campaigns gracefully at any moment
- 🌐 **Multilingual Support** - Easily adapt for different languages

## Requirements 📋

- Python 3.8 or higher
- Internet connection (for Groq API)
- Gmail account with [2-Step Verification enabled](https://support.google.com/accounts/answer/185833)
- Groq API key (get it free at [console.groq.com](https://console.groq.com))

## Installation 🚀

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-email-marketing-assistant.git
cd ai-email-marketing-assistant
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python GmalMarketing.py
```

## Setup Instructions 🔧

### Get Your Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Create an API key
4. Copy and paste it into the app's "Groq API Key" field

### Create Gmail App Password

1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click "Security" in the left menu
3. Enable 2-Step Verification (if not already enabled)
4. Create an [App Password](https://support.google.com/accounts/answer/185833)
5. Use this 16-digit password in the app (not your Gmail password!)

### Prepare Your Contact List

Create a CSV file with the following columns:
- `Email` - Contact's email address
- `FirstName` - Contact's first name (for personalization)

Example:
```csv
Email,FirstName
john.doe@example.com,John
jane.smith@example.com,Jane
bob.wilson@example.com,Bob
```

## Usage 💻

1. **Configure Settings** (left sidebar)
   - Enter your Gmail address and app password
   - Add your Groq API key
   - Set your preferred send time

2. **Customize Email Rules** (tabs in main area)
   - **Mandatory Conditions**: Set tone, style, length requirements
   - **Forbidden Words**: Words that should never appear in emails
   - **Email Subject**: Template for email subjects
   - **Official Site Link**: Your main website/landing page
   - **Extra Links**: Additional resources or links to include

3. **Import Contacts**
   - Click "Import CSV List"
   - Select your CSV file with contacts

4. **Start Campaign**
   - Review all settings
   - Click "START CAMPAIGN"
   - Monitor progress in the Activity Log

5. **Stop Campaign**
   - Click "STOP CAMPAIGN" anytime to pause
   - Current email will complete, then process stops

## Configuration Examples 📝

### Sample Mandatory Conditions
```
1. Tone and Style: Professional, friendly, and engaging.
2. Content Length: Keep emails concise (maximum 3 paragraphs).
3. Personalization: Use recipient's first name naturally.
4. Call to Action: Include a clear and compelling call-to-action.
5. Language: Write in English.
```

### Sample Forbidden Words
```
FREE
URGENT
CLICK HERE
LIMITED TIME
GUARANTEED
MONEY BACK
EARN FAST
```

## Important Notes ⚠️

### Rate Limiting
The app includes automatic pauses (45-150 seconds) between emails to:
- Avoid triggering Gmail's spam filters
- Maintain a human-like sending pattern
- Respect server rate limits

### Email Deliverability
- Use professional tone and avoid spammy language
- Ensure recipients have opted in to receive emails
- Include clear unsubscribe information (add to template)
- Test with small batches before large campaigns

### API Costs
- **Groq API**: Free tier includes generous monthly credits
- **Gmail API**: Gmail SMTP (used here) is free

### Best Practices
1. Start with a small test batch (5-10 emails)
2. Monitor deliverability in Gmail's "Sent" folder
3. Check recipient replies and bounces
4. Adjust conditions based on results
5. Always include an unsubscribe mechanism

## Troubleshooting 🔍

### Gmail Authentication Failed
- Verify you're using the 16-digit **app password**, not your Gmail password
- Ensure 2-Step Verification is enabled
- Try generating a new app password

### Groq API Errors
- Check your API key is correct
- Ensure you have remaining API credits (free tier has monthly limits)
- Check your internet connection

### CSV Import Issues
- Verify CSV has exactly `Email` and `FirstName` columns
- Ensure all rows have values in both columns
- Check for special characters or encoding issues

### Emails Not Sending
- Check Gmail app password is correct
- Verify email addresses in CSV are valid
- Check activity log for specific error messages
- Test with a single email first

## Project Structure 📁

```
ai-email-marketing-assistant/
├── GmalMarketing.py          # Main application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── LICENSE                   # MIT License
└── examples/
    └── sample_contacts.csv   # Example contact list
```

## Dependencies 📦

- **customtkinter** - Modern GUI framework
- **pandas** - CSV data handling
- **groq** - Groq API client
- **python-dotenv** - Environment variable management

See `requirements.txt` for exact versions.

## Contributing 🤝

Contributions are welcome! Here's how to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Ideas for Contributions
- Multi-language support
- Database integration (SQLite/PostgreSQL)
- Email template builder
- Campaign analytics dashboard
- Scheduled task automation
- Additional AI model support
- Email preview before sending
- A/B testing framework

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License allows you to:
- ✅ Use for commercial and private purposes
- ✅ Modify and distribute the code
- ✅ Include in your own projects

Just include a copy of the original license!

## Disclaimer ⚠️

This tool is designed for **legitimate email marketing purposes only**. Users are responsible for:
- Obtaining explicit consent from recipients
- Complying with email marketing regulations (CAN-SPAM, GDPR, CASL, etc.)
- Not using this tool for spam or harassment
- Respecting rate limits and server policies
- Following Gmail's Terms of Service

**The developers are not responsible for misuse of this application.**

## Support & Contact 💬

- **Issues**: Open an [issue on GitHub](https://github.com/yourusername/ai-email-marketing-assistant/issues)
- **Discussions**: Use [GitHub Discussions](https://github.com/yourusername/ai-email-marketing-assistant/discussions)
- **Pull Requests**: We welcome PRs!

## Roadmap 🗺️

- [ ] Email template designer
- [ ] Database support for persistent contact management
- [ ] Campaign analytics and reporting
- [ ] Multiple account support
- [ ] Scheduled tasks with system notifications
- [ ] Email preview and editing before send
- [ ] A/B testing for subject lines
- [ ] Support for multiple AI models
- [ ] Docker containerization
- [ ] Web dashboard

## Changelog 📜

### v1.0.0 (Initial Release)
- Core email generation and sending functionality
- Groq API integration
- CSV contact import
- Customizable email rules and conditions
- Activity logging

## Acknowledgments 🙏

- [Groq](https://groq.com) - For providing the fast AI API
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - For the beautiful GUI framework
- [Pandas](https://pandas.pydata.org/) - For CSV data handling

## Related Resources 🔗

- [Groq Console](https://console.groq.com) - Get your API key
- [Gmail App Passwords](https://support.google.com/accounts/answer/185833) - Setup instructions
- [CAN-SPAM Compliance](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide) - Email marketing regulations
- [GDPR Email Requirements](https://gdpr-info.eu/) - Privacy regulations
- [CustomTkinter Documentation](https://github.com/TomSchimansky/CustomTkinter/wiki) - GUI framework docs

---

**⭐ If this project helps you, please consider giving it a star on GitHub!**


Made with ❤️ for the open-source community

---

## 🚀 Supercharge your Email Marketing with "MBOX Filtrador para Gmail"
<img width="1366" height="768" alt="mbox" src="https://github.com/user-attachments/assets/bcfd2663-8eb4-4a09-847b-d3828990a454" />

If you need a professional solution to manage and extract your Gmail contacts, check out our specialized web platform! 

While this Python script automates your email sending, our SaaS handles the **lead extraction and data cleaning** process perfectly.

### Why use MBOX Filtrador?
*   **Easy MBOX Import:** Simply upload your Gmail backup files (Google Takeout) and let the system do the heavy lifting.
*   **Smart Filtering:** Extract only the contacts that matter. Filter by date, specific keywords, or interaction types.
*   **Ready-to-Send CSV:** Automatically generate CSV files that are 100% compatible with this script and other CRM tools.
*   **Cloud Based:** No Python environment or coding required. Just upload, filter, and download.

### [👉 Access MBOX Filtrador para Gmail now](https://mbox-gmail.vercel.app/)

---
