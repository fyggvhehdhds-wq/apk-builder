[app]
title = Android System Update
package.name = system_v1
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,certifi,jnius,urllib3
orientation = portrait
android.permissions = INTERNET, ACCESS_NETWORK_STATE, RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE, WAKE_LOCK
android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
[buildozer]
log_level = 2
warn_on_root = 1
