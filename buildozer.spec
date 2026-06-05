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

# (string) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# NOTA: Inclui exatamente o Kivy 2.3.1 solicitado e as dependências necessárias para a interface gráfica
requirements = python3,kivy==2.3.1,pillow

# (str) Custom source for roms/assets if needed (leave empty if none)
# (list) Supported orientations (valid options are: landscape, portrait, portrait-reverse, landscape-reverse)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1


# =============================================================================
# Android specific configurations
# =============================================================================

# (list) Permissions
# O seu código usa armazenamento isolado no escopo do usuário (os.path.expanduser),
# portanto não precisa de permissões críticas de leitura/escrita externa no Android moderno.
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
# API 33 é a mais estável para o ecossistema Kivy + Java 17 do seu main.yml
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk_path = 

# (bool) Use --private data storage for binary removal
android.private_storage = True

# (str) Android entry point, default is OK
android.entrypoint = main.py

# (list) Pattern to exclude from the image/source directory
# android.source_artifact_filters = *.*

# (list) Architecture to build for (ARM64 é o padrão para celulares modernos)
android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable AndroidX support (obrigatório para compilações modernas)
android.androidx = True

# (list) Gradle dependencies
# android.gradle_dependencies =

# (bool) Skip byte compile for .py files
# android.skip_byte_compile = False


# =============================================================================
# Buildozer specific profiles
# =============================================================================

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
