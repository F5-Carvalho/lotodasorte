[app]

# (str) Title of your application
title = Loto da Sorte

# (str) Package name
package.name = lotodasorte

# (str) Package domain (needed for android packaging)
package.domain = org.kelson

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.3.1,pillow,openssl

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# ==============================================================================
# CONFIGURAÇÕES ESPECÍFICAS DO ANDROID
# ==============================================================================

# (num) Target Android API, should be as high as possible.
android.api = 34

# (num) Minimum API your APK will support. 
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 26b

# (bool) If True, then skip trying to update the Android sdk tools
android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
android.accept_sdk_license = True

# (list) Arquiteturas para o APK (Compila para celulares novos de 64 bits e antigos de 32 bits)
android.archs = arm64-v8a

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target sandbox level
android.numeric_version = 1

# (str) Bootstrap to use for android outputs
android.bootstrap = sdl2

# (set) List of gleX extensions to enable
android.wakelock = False

# ==============================================================================
# CONFIGURAÇÕES DO BUILDOZER
# ==============================================================================

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build output
bin_dir = ./bin
