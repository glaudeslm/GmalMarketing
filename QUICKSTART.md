# Quick Start Guide 🚀

Get up and running in **5 minutes**!

## Prerequisites ✅

- Python 3.8 or higher
- Gmail account with 2-Step Verification
- Groq API key (free)

## Step-by-Step Setup

### 1️⃣ Get Your API Keys (2 minutes)

#### Groq API Key
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Go to API Keys section
4. Create new API key
5. Copy the key (looks like: `gsk_...`)

#### Gmail App Password
1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click **Security** on the left
3. Find **App passwords** (requires 2FA enabled)
4. Select **Mail** and **Windows Computer** (or your device)
5. Google generates a 16-digit password
6. Copy it (format: `xxxx xxxx xxxx xxxx`)

> ⚠️ **Important**: Use this app password, NOT your Gmail password!

### 2️⃣ Install the Application (1 minute)

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-email-marketing-assistant.git
cd ai-email-marketing-assistant

# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Prepare Your Contact List (1 minute)

Create a file named `contacts.csv`:

```csv
Email,FirstName
john@example.com,John
jane@example.com,Jane
bob@example.com,Bob
```

**Requirements**:
- CSV format
- Columns: `Email`, `FirstName`
- One contact per row

### 4️⃣ Run the Application (1 minute)

```bash
python GmalMarketing.py
```

The GUI will open!

### 5️⃣ Configure & Send

**In the left sidebar:**
1. Enter your Gmail address
2. Paste your app password
3. Paste your Groq API key
4. Set send time (e.g., 09:00)
5. Click "📥 Import CSV List" and select your contacts.csv

**In the tabs:**
- **Mandatory Conditions**: Set tone, style requirements
- **Forbidden Words**: Words to avoid
- **Email Subject**: Subject line template
- **Official Site Link**: Your website URL
- **Extra Links**: Additional resources

**Start Campaign:**
1. Review all settings
2. Click "🚀 START CAMPAIGN"
3. Watch the Activity Log
4. Use "🛑 STOP CAMPAIGN" to pause anytime

---

## Common Tasks

### Change Email Content Rules

1. Click the **"Mandatory Conditions"** tab
2. Edit the text box with your requirements
3. Example:
```
1. Keep it professional and friendly
2. Maximum 3 paragraphs
3. Always personalize with first name
4. Include a clear call to action
```

### Add Forbidden Words

1. Click **"Forbidden Words"** tab
2. Add words (one per line, uppercase):
```
FREE
LIMITED TIME
URGENT
CLICK HERE
```

### Set Email Subject

1. Click **"Subject"** tab
2. Type your subject template:
```
{FirstName}, Check This Out!
```

The `{FirstName}` will be replaced with each person's name.

### Add Extra Links

1. Click **"Extra Links"** tab
2. Add URLs (one per line):
```
https://example.com/blog
https://example.com/tutorial
https://youtube.com/yourChannel
```

---

## Troubleshooting 🔧

### "Gmail authentication failed"
- ✅ Are you using the 16-digit **app password**?
- ✅ Is 2-Step Verification enabled on your Gmail?
- ✅ Did you generate a new app password recently? Try generating another one.

### "Groq API error"
- ✅ Is your API key correct? (Copy it exactly)
- ✅ Do you have API credits? (Check at console.groq.com)
- ✅ Is your internet connection working?

### "CSV import failed"
- ✅ Does your CSV have `Email` and `FirstName` columns?
- ✅ Are all rows filled in (no empty cells)?
- ✅ Is the file actually a CSV (not Excel)?

### "No emails sending"
- ✅ Check the Activity Log for error messages
- ✅ Are email addresses in your CSV valid?
- ✅ Start with 1-2 test emails first

### "Process is very slow"
- ✅ This is intentional! Random delays between emails prevent spam filters
- ✅ Each email takes 45-150 seconds (this is good)
- ✅ For 100 emails, plan 1-3 hours

---

## Next Steps 📚

Once you're running successfully:

1. **Read the Full README** - Comprehensive setup and features
2. **Check CONTRIBUTING.md** - How to improve the project
3. **Review SECURITY.md** - Important security practices
4. **Explore CHANGELOG** - What's new and planned

---

## Video Tutorial (if available)

Look for video tutorials at:
- YouTube (search: "AI Email Marketing Assistant")
- Project wiki

---

## Getting Help 💬

**Something not working?**

1. Check this Quick Start again
2. Read the main [README.md](README.md)
3. Open a [GitHub Issue](https://github.com/yourusername/ai-email-marketing-assistant/issues)
4. Ask in [GitHub Discussions](https://github.com/yourusername/ai-email-marketing-assistant/discussions)

**Have a feature idea?**
- Open a [GitHub Discussion](https://github.com/yourusername/ai-email-marketing-assistant/discussions)
- Or submit a feature request as an Issue

---

## Key Reminders ⚡

✅ **Always**:
- Start with small test batches (5-10 emails)
- Monitor your email's "Sent" folder
- Check for bounces and complaints
- Comply with email marketing laws
- Include an unsubscribe mechanism

❌ **Never**:
- Share your API keys
- Commit passwords to GitHub
- Use for spam or unsolicited emails
- Ignore bounce/complaint warnings
- Send to inactive addresses repeatedly

---

## Success Checklist ✨

- [ ] Python installed (3.8+)
- [ ] Gmail account with 2FA enabled
- [ ] Gmail app password created
- [ ] Groq API key obtained
- [ ] Repository cloned
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] contacts.csv created with test data
- [ ] Application running (`python GmalMarketing.py`)
- [ ] Settings configured
- [ ] Test campaign sent successfully
- [ ] Ready for production!

---

**Estimated Time: 5-10 minutes** ⏱️

Enjoy using AI Email Marketing Assistant! 🎉
