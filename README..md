# 🚨 DisasterGuard AI

### AI-Assisted Emergency Response Planning and Coordination

DisasterGuard AI is a prototype designed to help people organize
emergency information and generate actionable response plans
during natural disasters and other emergencies.

It accepts an emergency report, identifies a possible disaster
category, assigns a preliminary priority, recommends safety actions,
and creates a task checklist for human responders.

## 🎯 Problem Statement

During natural disasters, people may struggle to understand the
severity of an emergency, find reliable information, and coordinate
the appropriate response quickly.

Delayed communication and unorganized information can make
emergency response more difficult.

## 💡 Proposed Solution

DisasterGuard AI provides a simple interface for reporting emergencies
and generating an organized preliminary response plan.

The system helps users:

- Submit emergency reports and locations.
- Identify common disaster categories.
- Assign a preliminary priority based on reported warning signs.
- Generate practical safety recommendations.
- Identify suggested emergency resource categories.
- Organize response activities using a task checklist.

## ✨ Features

- Flood, lightning, earthquake, cyclone, and fire detection.
- Rule-based emergency report analysis.
- Preliminary priority classification.
- Disaster-specific safety recommendations.
- Suggested coordination resources.
- Interactive response checklist.
- Simple web interface.

## 🛠️ Technology Stack

- Python
- Streamlit
- Rule-based text classification
- Git and GitHub

## 🏗️ Project Structure

```text
disasterguard-ai/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/disasterguard-ai.git
```

### 2. Open the project directory

```bash
cd disasterguard-ai
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will display a local URL in your terminal.
Open that address in your browser.

## 🧪 Example Emergency Report

Location: Riverside residential area

Report:

"Heavy rain has flooded our street. Water is entering houses,
and three families are trapped."

Expected demonstration behavior:

- Detected incident: Flood
- Preliminary priority: Immediate escalation
- Safety recommendations: Avoid floodwater and report trapped people
  to emergency services.
- Coordination: Generate an organized task checklist.

The output is a demonstration of the prototype, not a verified
assessment of actual conditions.

## 🔭 Future Improvements

- Integrate a language model for richer report analysis.
- Connect verified weather and disaster information APIs.
- Display emergency locations on a map.
- Add a responder coordination dashboard.
- Support multiple languages.
- Integrate verified local emergency contacts.
- Add notifications and authorized task assignment.
- Maintain an auditable record of response activities.

## ⚠️ Safety and Limitations

This prototype is not an official emergency service.

Its current classification system uses keywords and cannot reliably
determine the actual severity of a disaster.

Suggested resources are not live-verified contacts. The application
does not automatically dispatch responders, contact emergency
services, or verify current disaster conditions.

Always follow official emergency instructions and contact verified
local emergency services when someone may be in danger.

## 📄 License

This project is available under the MIT License.
