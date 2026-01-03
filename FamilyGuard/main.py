from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform

# এই পারমিশনগুলো অ্যান্ড্রয়েড ফোনের হার্ডওয়্যার ব্যবহার করতে সাহায্য করবে
if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.CAMERA,
        Permission.RECORD_AUDIO,
        Permission.READ_EXTERNAL_STORAGE,
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.ACCESS_FINE_LOCATION,
        Permission.SEND_SMS,
        Permission.READ_CONTACTS
    ])

class FamilyGuardPro(App):
    def build(self):
        return Label(text="[ FamilyGuard Pro - Full Access Mode ]\n\n"
                          "1. Camera & Mic: Active\n"
                          "2. Live Screen Sync: Ready\n"
                          "3. Gallery & Storage: Linked\n"
                          "4. GPS Tracking: Sending Data\n"
                          "5. SMS Control: Enabled", 
                     halign='center')

if __name__ == "__main__":
    FamilyGuardPro().run()