# School Mail Task Manager

> A Django web application that uses the Anthropic API to intelligently parse school emails and present them as clear, actionable tasks.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [User Stories](#user-stories)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Database Models](#database-models)
- [Backend Flow](#backend-flow)
- [Frontend Flow](#frontend-flow)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Templates](#templates)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**School Mail Task Manager** connects to your school email account, reads incoming emails, and uses the **Anthropic Claude API** to extract key actions and deadlines — presenting them to you as a clean, prioritised task list. No more missing important school notices buried in long emails.

---

## Features

- Fetches and parses school emails automatically
- Uses Anthropic Claude API to extract tasks and action points
- Displays tasks in a clean, easy-to-read home dashboard
- View the original source email for full context
- Two-template MVP layout (Home + Email Detail)
- Secure handling of credentials via environment variables

---

## User Stories

---
## Tech Stack

| Layer        | Technology |
|--------------|-|
| Backend      | Django (Python) |
| AI / NLP     | Anthropic Claude API|
| Frontend     | Django Templates, HTML/CSS |
| Email Access | IMAP / Gmail API |
| Environment  ||

---

## Project Structure

```
poke/
├── manage.py
├── .env                    # Environment variables (not committed)
├── requirements.txt
├── poke/                   # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tasks/                  # Main app
    ├── views.py
    ├── urls.py
    ├── models.py
    ├── utils/
    │   ├── email_reader.py     # Email fetching logic
    │   └── anthropic_parser.py # Anthropic API integration
    └── templates/
        └── tasks/
            ├── home.html       # Task list dashboard
            └── email_detail.html # Original email view
```
---

## Database Models

---

## Backend Flow

---

## Frontend Flow

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- An [Anthropic API key](https://console.anthropic.com/)
- Access to your school email (IMAP enabled or Gmail API credentials)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/school-mail-task-manager.git
   cd school-mail-task-manager
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

### Environment Variables

Create a `.env` file in the root directory and add the following:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

# Anthropic
ANTHROPIC_API_KEY=your_anthropic_api_key

# Email credentials
EMAIL_HOST=imap.gmail.com
EMAIL_ADDRESS=your_school_email@example.com
EMAIL_PASSWORD=your_email_password
```

> ⚠️ **Never commit your `.env` file.** Make sure it is listed in `.gitignore`.

---

## Usage

1. Navigate to `http://127.0.0.1:8000/` to view your task dashboard
2. The app will fetch your latest school emails and process them through the Anthropic API
3. Tasks extracted from each email are displayed on the **Home** page
4. Click any task or email entry to view the **original email** in full

---

## Templates

### `home.html` — Task Dashboard
- Displays a list of tasks extracted from school emails
- Each task shows a summary, due date (if detected), and source email reference
- Clean, minimal UI suitable for quick daily review

### `email_detail.html` — Original Email View
- Shows the full original email content
- Provides context behind the extracted tasks
- Includes a back button to return to the dashboard

---

## API Integration

This project uses the **Anthropic Claude API** to analyse email content and extract actionable tasks.

**Example prompt structure:**
```
Given the following school email, extract all tasks, deadlines, 
and action items. Return them as a structured list.

Email:
{email_body}
```

The response is parsed and stored against the relevant email record in the database.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the [MIT License](LICENSE).

---

> Built with using Django and the Anthropic Claude API.