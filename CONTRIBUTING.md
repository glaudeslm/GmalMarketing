# Contributing to AI Email Marketing Assistant

First off, thank you for considering contributing to this project! It's people like you that make this tool such a great resource.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots and animated GIFs if possible**
* **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and the expected behavior**
* **Explain why this enhancement would be useful**

### Pull Requests

* Fill in the required template
* Follow the Python code style guide
* Include appropriate test cases
* End all files with a newline
* Avoid platform-dependent code

## Development Setup

### 1. Fork and clone the repository

```bash
git clone https://github.com/yourusername/ai-email-marketing-assistant.git
cd ai-email-marketing-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install development dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a feature branch

```bash
git checkout -b feature/your-feature-name
```

## Code Style Guide

### Python Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with the following guidelines:

* Use 4 spaces for indentation
* Maximum line length: 100 characters
* Use descriptive variable and function names
* Add docstrings to all functions and classes
* Use type hints where appropriate

### Example:

```python
def generate_email_content(name: str, conditions: str) -> tuple[str, str]:
    """
    Generate email subject and body using AI.
    
    Args:
        name: Recipient's first name
        conditions: Email generation conditions
    
    Returns:
        Tuple of (subject, body)
    """
    # Implementation here
    pass
```

### Naming Conventions

* Classes: `PascalCase`
* Functions/Methods: `snake_case`
* Constants: `UPPER_SNAKE_CASE`
* Private methods: `_leading_underscore`

## Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Example:
```
Add feature to preview emails before sending

- Add preview button to main interface
- Add modal window for email preview
- Update UI components accordingly

Fixes #123
```

## Testing

Before submitting a pull request:

1. Test with different contact list sizes (small, medium, large)
2. Test with various CSV formats
3. Test error handling (invalid emails, missing columns, etc.)
4. Test on different operating systems if possible
5. Verify no hardcoded paths or personal information

## Documentation

* Update the README if you add features
* Add docstrings to all new functions
* Update CHANGELOG.md with your changes
* Include examples for new features

## Additional Notes

### Issue and Pull Request Labels

* `bug` - Something isn't working
* `enhancement` - New feature or request
* `documentation` - Improvements or additions to documentation
* `good first issue` - Good for newcomers
* `help wanted` - Extra attention is needed
* `question` - Further information is requested

### Project Structure

```
ai-email-marketing-assistant/
├── GmalMarketing.py          # Main application
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
├── CONTRIBUTING.md           # This file
├── LICENSE                   # MIT License
├── .gitignore               # Git ignore rules
├── examples/
│   └── sample_contacts.csv   # Example contact list
└── docs/                     # Additional documentation (optional)
```

## Questions?

Don't hesitate to open an issue with a `question` label or reach out to the maintainers.

## Recognition

Contributors will be recognized in:
* The README.md file
* Release notes
* GitHub Contributors page

Thank you for contributing! 🎉
