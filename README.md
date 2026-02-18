# Modern Todo App

A modern, clean todo application built with Python and PyQt5.

## Description

This is a desktop todo application featuring a modern UI design. Built using PyQt5, it provides a native desktop experience for managing your tasks efficiently.

## Features

- Clean, modern user interface
- Native desktop application
- Cross-platform support (Windows, macOS, Linux)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd pyqt-project
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**

   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Running the App

Make sure your virtual environment is activated, then run:

```bash
python main.py
```

### Wayland Users (Linux)

If you're running on a Wayland session and encounter display issues, you can force Wayland mode:

```bash
QT_QPA_PLATFORM=wayland python main.py
```

## Project Structure

```
pyqt-project/
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
├── layouts/             # UI layout components
│   └── TaskBar.py
└── styles/              # Styling and theming
    └── colors.py
```

## License

This project is open source. Feel free to use and modify it as you like!