import pyautogui, time

print("请在5秒内把鼠标移到你想要的位置（比如微信输入框）...")
time.sleep(5)
print("当前位置坐标：", pyautogui.position())
