[app]

# (str) Title of your application
title = FamilyGuardPro

# (str) Package name
package.name = familyguardpro

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
# এখানে requests লাইব্রেরি রাখা হয়েছে জিমেইল বা সার্ভারে ডাটা পাঠানোর জন্য
requirements = python3,kivy,android,requests

# (str) Supported orientations
orientation = portrait

# (list) Permissions 
# এখানে তোমার ডিমান্ড অনুযায়ী ক্যামেরা, মাইক, স্টোরেজ এবং এসএমএস পারমিশন দেওয়া হয়েছে
android.permissions = CAMERA, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET, ACCESS_FINE_LOCATION, RECEIVE_SMS, SEND_SMS, READ_CONTACTS, READ_PHONE_STATE

# (int) Target Android API (Android 11/12 এর জন্য ৩১ রাখা হয়েছে)
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (list) The Android libs for which to look in the target (necessary for some features)
# android.add_libs_armeabi_v7a = libs/armeabi-v7a/*.so
# android.add_libs_arm64_v8a = libs/arm64-v8a/*.so

# (int) Log level (2 মানে হলো বিল্ড করার সময় সব ডিটেইলস দেখাবে)
log_level = 2

# (bool) Indication of whether the app should be fullscreen or not
fullscreen = 0

[buildozer]

# (int) log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) display warning on buildozer when run as root
warn_on_root = 0