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
# Kivy 2.3.1 travado conforme especificado + Pillow para processar os elementos gráficos da Splash e das dezenas
requirements = python3,kivy==2.3.1,pillow

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1


# =============================================================================
# Android specific configurations
# =============================================================================

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Versão das ferramentas de construção (CORREÇÃO DE ERRO)
# Travar em 33.0.0 impede que o Buildozer busque a versão 37 (instável) que causou a falha de licença
android.build_tools_version = 33.0.0

# (bool) Use --private data storage for binary removal
android.private_storage = True

# (str) Android entry point
android.entrypoint = main.py

# (list) Architecture to build for (Combinação padrão para abranger 99% dos celulares)
android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable AndroidX support (Essencial para builds modernas do Gradle)
android.androidx = True


# =============================================================================
# Buildozer specific profiles
# =============================================================================

[buildozer]

# (int) Log level (2 = debug com visualização completa de comandos e erros no GitHub)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
