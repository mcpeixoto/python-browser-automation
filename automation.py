#!/usr/bin/env python3
"""
A Firefox browser automation script with three parts:
  1. Recording actions (navigate, click, input, wait)
  2. Modifying/adding extra actions
  3. Executing actions using Selenium

This version uses Firefox (and Selenium Manager will automatically handle geckodriver).
Optionally, you can specify your Firefox profile path to reuse your logged-in session.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def record_actions():
    """Interactively record a sequence of actions."""
    actions = []
    print("=== Recording Actions ===")
    print("Enter your actions one by one. When finished, type 'done'.")
    while True:
        action_type = input("Enter action type (navigate, click, input, wait) or 'done': ").strip().lower()
        if action_type == 'done':
            break
        if action_type == 'navigate':
            url = input("Enter URL to navigate to: ").strip()
            actions.append({'action': 'navigate', 'url': url})
        elif action_type == 'click':
            locator_type = input("Enter locator type (id, xpath, css_selector): ").strip()
            locator = input("Enter locator value: ").strip()
            actions.append({'action': 'click', 'locator_type': locator_type, 'locator': locator})
        elif action_type == 'input':
            locator_type = input("Enter locator type (id, xpath, css_selector): ").strip()
            locator = input("Enter locator value: ").strip()
            text = input("Enter text to input: ")
            actions.append({'action': 'input', 'locator_type': locator_type, 'locator': locator, 'text': text})
        elif action_type == 'wait':
            seconds = input("Enter seconds to wait: ").strip()
            try:
                seconds = float(seconds)
            except ValueError:
                print("Invalid number, defaulting to 1 second.")
                seconds = 1
            actions.append({'action': 'wait', 'time': seconds})
        else:
            print("Unknown action type. Please try again.")
    return actions

def modify_actions(actions):
    """Allow the user to modify or insert additional actions."""
    print("\n=== Modify Actions ===")
    while True:
        print("\nCurrent actions:")
        for idx, act in enumerate(actions):
            print(f"{idx}: {act}")
        choice = input("Do you want to add an extra action? (yes/no): ").strip().lower()
        if choice != 'yes':
            break
        position_input = input("At which position index? (enter number, or 'end' to append): ").strip()
        if position_input.lower() == 'end':
            pos = len(actions)
        else:
            try:
                pos = int(position_input)
            except ValueError:
                print("Invalid input, appending at the end.")
                pos = len(actions)
        action_type = input("Enter new action type (navigate, click, input, wait): ").strip().lower()
        if action_type == 'navigate':
            url = input("Enter URL: ").strip()
            actions.insert(pos, {'action': 'navigate', 'url': url})
        elif action_type == 'click':
            locator_type = input("Enter locator type (id, xpath, css_selector): ").strip()
            locator = input("Enter locator value: ").strip()
            actions.insert(pos, {'action': 'click', 'locator_type': locator_type, 'locator': locator})
        elif action_type == 'input':
            locator_type = input("Enter locator type (id, xpath, css_selector): ").strip()
            locator = input("Enter locator value: ").strip()
            text = input("Enter text to input: ")
            actions.insert(pos, {'action': 'input', 'locator_type': locator_type, 'locator': locator, 'text': text})
        elif action_type == 'wait':
            seconds = input("Enter seconds to wait: ").strip()
            try:
                seconds = float(seconds)
            except ValueError:
                print("Invalid input, defaulting to 1 second.")
                seconds = 1
            actions.insert(pos, {'action': 'wait', 'time': seconds})
        else:
            print("Unknown action type, skipping.")
    return actions

def execute_actions(actions):
    """Execute the recorded actions in a Firefox browser using Selenium."""
    print("\n=== Executing Actions ===")
    options = Options()

    # Optionally load your Firefox profile so that session data (e.g., corporate logins) is reused.
    use_profile = input("Do you want to use a specific Firefox profile? (yes/no): ").strip().lower()
    if use_profile == "yes":
        profile_path = input("Enter the full path to your Firefox profile directory: ").strip()
        try:
            # Using FirefoxProfile (available in Selenium) to load your profile.
            from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
            profile = FirefoxProfile(profile_path)
            options.profile = profile
        except Exception as e:
            print("Error loading Firefox profile:", e)
            print("Proceeding without a custom profile.")

    # Initialize Firefox. Selenium Manager (Selenium 4.6+) will automatically manage geckodriver.
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()

    for act in actions:
        if act['action'] == 'navigate':
            url = act['url']
            print(f"Navigating to {url}")
            driver.get(url)
            time.sleep(2)  # Adjust as needed for page load
        elif act['action'] == 'click':
            locator_type = act['locator_type']
            locator = act['locator']
            print(f"Clicking element with {locator_type}: {locator}")
            try:
                if locator_type.lower() == 'id':
                    element = driver.find_element(By.ID, locator)
                elif locator_type.lower() == 'xpath':
                    element = driver.find_element(By.XPATH, locator)
                elif locator_type.lower() == 'css_selector':
                    element = driver.find_element(By.CSS_SELECTOR, locator)
                else:
                    print("Unsupported locator type. Skipping click action.")
                    continue
                element.click()
                time.sleep(1)
            except Exception as e:
                print(f"Error during click action: {e}")
        elif act['action'] == 'input':
            locator_type = act['locator_type']
            locator = act['locator']
            text = act['text']
            print(f"Inputting text into element with {locator_type}: {locator}")
            try:
                if locator_type.lower() == 'id':
                    element = driver.find_element(By.ID, locator)
                elif locator_type.lower() == 'xpath':
                    element = driver.find_element(By.XPATH, locator)
                elif locator_type.lower() == 'css_selector':
                    element = driver.find_element(By.CSS_SELECTOR, locator)
                else:
                    print("Unsupported locator type. Skipping input action.")
                    continue
                element.clear()
                element.send_keys(text)
                time.sleep(1)
            except Exception as e:
                print(f"Error during input action: {e}")
        elif act['action'] == 'wait':
            seconds = act['time']
            print(f"Waiting for {seconds} seconds")
            time.sleep(seconds)
        else:
            print(f"Unknown action: {act}")
    print("All actions executed. Closing browser.")
    driver.quit()

def main():
    print("Welcome to the Firefox Browser Automation Script")
    record_choice = input("Do you want to record a new set of actions? (yes/no): ").strip().lower()
    if record_choice == 'yes':
        actions = record_actions()
        print("\nRecorded actions:")
        for act in actions:
            print(act)
        modify_choice = input("\nDo you want to modify/add actions? (yes/no): ").strip().lower()
        if modify_choice == 'yes':
            actions = modify_actions(actions)
    else:
        print("No actions recorded. Exiting.")
        return

    print("\nFinal list of actions:")
    for idx, act in enumerate(actions):
        print(f"{idx}: {act}")

    execute_choice = input("\nProceed with executing these actions? (yes/no): ").strip().lower()
    if execute_choice == 'yes':
        execute_actions(actions)
    else:
        print("Execution cancelled.")

if __name__ == "__main__":
    main()
