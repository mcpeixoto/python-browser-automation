# Firefox Browser Automation

This project provides a Python script that automates Firefox browser interactions using Selenium. The script is divided into three main parts:

1. **Recording Actions:** Interactively record browser actions (navigate, click, input, wait).
2. **Modifying/Adding Actions:** Optionally modify or add extra actions to the recorded sequence.
3. **Executing Actions:** Execute the recorded actions using Selenium with Firefox.

The script also offers an option to load a custom Firefox profile to reuse session data (for example, to maintain a logged-in session).

## Requirements

- Python 3.6+
- [Selenium](https://www.selenium.dev/)
- Firefox Browser

> **Note:** Selenium Manager (available in Selenium 4.6+) automatically manages the Firefox geckodriver, so no manual driver installation is needed.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/firefox-browser-automation.git
    cd firefox-browser-automation
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script with:

```bash
python automation.py
```
Follow the interactive prompts to record, modify, and execute browser actions.

This project is licensed under the MIT License. See the LICENSE file for details.