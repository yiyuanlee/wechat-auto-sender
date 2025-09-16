# wechat_group_sender_mac.py
import time
import subprocess
import pyautogui
import pyperclip
import schedule

# ========= 配置区 =========
GROUP_NAME = "loveguitar"                  # 目标群名称（WeChat 左侧会话列表显示名）
MESSAGE = "大家好，这是每周自动推送～（macOS 版）"  # 发送内容（建议用粘贴方式避免输入法问题）

SCHEDULE_WEEKDAY = "wednesday"          # monday..sunday
SCHEDULE_TIME = "00:06"              # 24h 格式
# ======== 配置结束 ========

# 延迟（按你机器速度可微调）
SHORT = 0.3
MEDIUM = 0.6
LONG = 1.0

def activate_wechat():
    """用 AppleScript 激活 WeChat 前台"""
    script = '''
    tell application "WeChat" to activate
    '''
    subprocess.run(["osascript", "-e", script], check=False)
    time.sleep(LONG)

def search_and_open_group(group_name: str):
    """
    在 WeChat 中 Command+F 搜索群名并回车进入
    注：WeChat Mac 版搜索快捷键通常是 ⌘F
    """
    pyautogui.hotkey('command', 'f')
    time.sleep(SHORT)
    pyperclip.copy(group_name)
    pyautogui.hotkey('command', 'v')
    time.sleep(MEDIUM)
    pyautogui.press('enter')
    time.sleep(MEDIUM)

def paste_and_send(text: str):
    """
    将文本粘贴到输入框并发送（Enter 发送；Shift+Enter 换行）
    """
    pyperclip.copy(text)
    # 在 paste_and_send 前手动点一下输入框
    pyautogui.click(x=881, y=866)  # 改成你输入框的坐标
    pyautogui.hotkey('command', 'v')
    time.sleep(SHORT)
    pyautogui.press('enter')
    time.sleep(SHORT)

def send_message_to_group():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 开始发送到「{GROUP_NAME}」")
    try:
        activate_wechat()
        search_and_open_group(GROUP_NAME)
        paste_and_send(MESSAGE)
        print("发送完成 ✅")
    except Exception as e:
        print("发送失败：", e)

def schedule_job():
    wd = SCHEDULE_WEEKDAY.lower()
    if wd == "monday":
        schedule.every().monday.at(SCHEDULE_TIME).do(send_message_to_group)
    elif wd == "tuesday":
        schedule.every().tuesday.at(SCHEDULE_TIME).do(send_message_to_group)
    elif wd == "wednesday":
        schedule.every().wednesday.at(SCHEDULE_TIME).do(send_message_to_group)
    elif wd == "thursday":
        schedule.every().thursday.at(SCHEDULE_TIME).do(send_message_to_group)
    elif wd == "friday":
        schedule.every().friday.at(SCHEDULE_TIME).do(send_message_to_group)
    elif wd == "saturday":
        schedule.every().saturday.at(SCHEDULE_TIME).do(send_message_to_group)
    elif wd == "sunday":
        schedule.every().sunday.at(SCHEDULE_TIME).do(send_message_to_group)
    else:
        raise ValueError("SCHEDULE_WEEKDAY 必须是 monday..sunday")

if __name__ == "__main__":
    print("定时器已启动。请确保：WeChat 已登录 & 终端拥有辅助功能/屏幕录制权限。")
    # 你也可以先试发一次：取消下一行注释
    # send_message_to_group()
    schedule_job()
    while True:
        schedule.run_pending()
        time.sleep(20)
