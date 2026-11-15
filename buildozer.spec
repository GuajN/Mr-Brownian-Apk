
[app]

title = Mr Brownian
package.name = mrbrownian
package.domain = com.mrbrownian

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf,txt,db,sqlite,csv,xlsx
version = 51.25

requirements = python3==3.12.0,kivy,pyjnius,pillow,openpyxl

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 35
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True
android.private_storage = True

[buildozer]

log_level = 2
warn_on_root = 1
