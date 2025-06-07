[app]
title = ScheduleAssistant
package.name = scheduleeassistant
package.domain = org.example
source.dir = .
source.include_exts = py, json, mp3, txt, kv
fullscreen = 1
version = 1.0
requirements = python3,kivy,plyer,openai,requests,pyjnius>=1.5.0

android.permissions = INTERNET, VIBRATE
android.miniapi = 21
android.target = 31
android.archs = arm64-v8a, armeabi-v7a

entrypoint = app.py

icon = %(source.dir)s/mobileAssistant/public/logo.jpg

android.packaging = zip

android.api = 31
android.gradle_dependencies = com.android.support:support-v4:28.0.0
