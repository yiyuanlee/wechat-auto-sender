# WeChat Auto Sender (macOS)

A lightweight Python tool to schedule and send automated messages to WeChat groups on macOS.  
基于 Python 的小工具，可在 macOS 上定时向微信群自动发送消息。

---

## ✨ Features
- 📅 Schedule messages to be sent at a fixed time (e.g., every Friday at 10:00).  
- 💬 Automatically paste and send messages into a specified WeChat group.  
- 💻 Runs locally on macOS, no need for WeChat API.  
- 🔒 Uses UI automation (pyautogui), avoids risky reverse engineering.

---

## 🛠 Requirements
- macOS with WeChat (already logged in)  
- Python 3.8+  
- Required Python libraries:
  ```bash
  pip install pyautogui pyperclip schedule
  ```

⚠️ Additionally, you must **grant accessibility and screen recording permissions** to your terminal/IDE:  
`System Settings → Privacy & Security → Accessibility` & `Screen Recording`.

---

## 🚀 Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourname/wechat-auto-sender.git
   cd wechat-auto-sender
   ```

2. Edit `wechat_group_sender_mac.py` and update:
   ```python
   GROUP_NAME = "测试群"
   MESSAGE = "大家好，这是自动推送"
   SCHEDULE_WEEKDAY = "friday"
   SCHEDULE_TIME = "10:00"
   ```

3. Run the script:
   ```bash
   python3 wechat_group_sender_mac.py
   ```

4. Keep the terminal window open. The script will run in the background and send messages at the scheduled time.

---

## 📍 Find Input Box Coordinates (optional)
If messages are not being sent, you may need to add a click on the input box:
```python
import pyautogui
print(pyautogui.position())
```
Move your mouse to the input box → terminal prints `(x, y)` → update the script:
```python
pyautogui.click(x, y)  # e.g., pyautogui.click(500, 800)
```

---

## ⚠️ Disclaimer
- This project uses UI automation and is **not an official WeChat API**.  
- Use responsibly and avoid spammy or commercial mass messaging.  
- Frequent repetitive messages may trigger WeChat’s anti-spam mechanisms.  

---

## 📄 License
MIT License. Free to use and modify.
