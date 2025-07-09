from pynput import mouse, keyboard
import threading

def on_click(x, y, button, pressed):
    if pressed:
        print(f"坐标：({x}, {y})")

def on_press(key):
    if key == keyboard.Key.esc:
        print("检测到 Esc，退出程序。")
        listener_mouse.stop()
        return False

# 启动提示
print("请点击鼠标，我会记录每次点击的坐标。按 Esc 键可退出。")

# 启动鼠标监听
listener_mouse = mouse.Listener(on_click=on_click)
listener_mouse.start()

# 启动键盘监听（非阻塞）
with keyboard.Listener(on_press=on_press) as listener_keyboard:
    listener_keyboard.join()
