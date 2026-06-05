[app]

# (string) Title of your application
title = LotoDaSorte

# (string) Package name
package.name = lotodasorte

# (string) Package domain (needed for android packaging)
package.domain = org.kelcarvalho

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (string) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = hostpython3,python3,kivy==2.3.1,sdl2,pillow

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1


# =============================================================================
# Android specific configurations
# =============================================================================

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API (Compatível com Java 17)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Versão das ferramentas de construção
android.build_tools_version = 33.0.0

# (bool) Use --private data storage for binary removal
android.private_storage = True

# (str) Android entry point
android.entrypoint = main.py

# (list) Architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.androidx = True


# =============================================================================
# Buildozer specific profiles
# =============================================================================

[buildozer]

# (int) Log level (2 = debug completo)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
