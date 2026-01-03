import requests
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import threading

class RemoteControlApp(App):
    def build(self):
        self.label = Label(text="System: Waiting for Connection...")
        # সার্ভারের সাথে যোগাযোগ শুরু করা
        threading.Thread(target=self.check_commands, daemon=True).start()
        return self.label

    def check_commands(self):
        # তোমার পিসির আইপি অ্যাড্রেস এখানে দাও
        URL = "http://192.168.59.213:5000/get_commands"
        
        while True:
            try:
                r = requests.get(URL, timeout=5)
                if r.status_code == 200:
                    cmd = r.json()
                    self.label.text = f"Connected! \nCamera: {cmd['camera']} \nScreenshot: {cmd['screenshot']}"
                    
                    # ক্যামেরা অন করার কমান্ড পেলে ফোনের ক্যামেরা সচল হবে
                    if cmd['camera'] == 'ON':
                        print("Phone Camera Request Received")
                        # এখানে ফোনের ইন্টারনাল ক্যামেরা ফাংশন কাজ করবে
            except:
                self.label.text = "Error: Server Not Found!"
            time.sleep(3)

if __name__ == '__main__':
    RemoteControlApp().run()