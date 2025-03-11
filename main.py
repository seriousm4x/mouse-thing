import threading
import time

import rumps
from pynput import keyboard, mouse


class MouseThing:
    def __init__(self):
        self.saved_position = None
        self.last_position = None
        self.last_moved_time = time.time()
        self.lock = threading.Lock()
        self.mouse = mouse.Controller()

    def on_move(self, x, y):
        with self.lock:
            self.last_position = (x, y)
            self.last_moved_time = time.time()

    def monitor_mouse(self):
        while True:
            time.sleep(0.1)
            with self.lock:
                if (
                    self.last_position
                    and self.last_position != self.saved_position
                    and (time.time() - self.last_moved_time) > 1
                ):
                    print("New idle position:", self.last_position)
                    self.saved_position = self.last_position

    def restore_cursor(self):
        with self.lock:
            if self.saved_position:
                print("Set cursor to:", self.saved_position)
                self.mouse.position = self.saved_position

    def on_hotkey(self):
        self.restore_cursor()

    def start_keyboard_listener(self):
        kb_listener = keyboard.GlobalHotKeys(
            {"<cmd>+<shift>+a": self.on_hotkey})
        kb_listener.run()

    def start(self):
        mouse_listener = mouse.Listener(on_move=self.on_move)
        mouse_listener.start()

        mouse_thread = threading.Thread(target=self.monitor_mouse, daemon=True)
        mouse_thread.start()

        keyboard_thread = threading.Thread(
            target=self.start_keyboard_listener, daemon=True
        )
        keyboard_thread.start()

        mouse_listener.join()
        keyboard_thread.join()


if __name__ == "__main__":
    mt = MouseThing()

    mouse_thread = threading.Thread(target=mt.start, daemon=True)
    mouse_thread.start()

    tray = rumps.App("MouseThing")
    tray.icon = "icon.png"
    tray.run()
