#!/bin/bash

APP_NAME="SponteStudy"

echo "Iniciando o processo de build para $APP_NAME..."

if ! command -v python3 &> /dev/null; then
    echo "Erro: Python3 não encontrado."
    exit 1
fi

sudo apt-get install -y python3-pip python3-venv python3-tk
sudo apt-get install -y espeak espeak-data libespeak-dev python3-dbus file

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install customtkinter CTkToolTip pyttsx3 Pillow pygments pyinstaller CustomtkinterCodeViewer

if [ ! -f "appimagetool-x86_64.AppImage" ]; then
    wget -q "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
    chmod +x appimagetool-x86_64.AppImage
fi

CTK_PATH=$(python3 -c "import customtkinter; import os; print(os.path.dirname(customtkinter.__file__))")
CCV_PATH=$(python3 -c "import CustomtkinterCodeViewer; import os; print(os.path.dirname(CustomtkinterCodeViewer.__file__))")

rm -rf build dist __pycache__ *.spec AppDir

pyinstaller --noconfirm --onefile \
    --add-data "imagens_app:imagens_app" \
    --add-data "$CTK_PATH:customtkinter" \
    --add-data "$CCV_PATH:CustomtkinterCodeViewer" \
    --add-data "CTkCodeBox:CTkCodeBox" \
    --hidden-import "customtkinter" \
    --hidden-import "CTkToolTip" \
    --hidden-import "CustomtkinterCodeViewer" \
    --hidden-import "pyttsx3" \
    --hidden-import "pyttsx3.drivers" \
    --hidden-import "pyttsx3.drivers.espeak" \
    --hidden-import "pygments" \
    --hidden-import "pygments.lexers" \
    --hidden-import "pygments.formatters" \
    --hidden-import "PIL" \
    --hidden-import "PIL._tkinter_finder" \
    --collect-all customtkinter \
    --collect-all CustomtkinterCodeViewer \
    --name "$APP_NAME" \
    interface.py

mkdir -p AppDir/usr/bin
mkdir -p AppDir/usr/share/applications
mkdir -p AppDir/usr/share/icons/hicolor/256x256/apps

cp "dist/$APP_NAME" "AppDir/usr/bin/$APP_NAME"

if [ -f "imagens_app/logo.png" ]; then
    cp "imagens_app/logo.png" "AppDir/usr/share/icons/hicolor/256x256/apps/$APP_NAME.png"
    cp "imagens_app/logo.png" "AppDir/$APP_NAME.png"
else
    python3 -c "
from PIL import Image
img = Image.new('RGB', (256, 256), color='#3b82f6')
img.save('AppDir/usr/share/icons/hicolor/256x256/apps/$APP_NAME.png')
import shutil; shutil.copy('AppDir/usr/share/icons/hicolor/256x256/apps/$APP_NAME.png', 'AppDir/$APP_NAME.png')
"
fi

cat > "AppDir/usr/share/applications/$APP_NAME.desktop" << EOF
[Desktop Entry]
Name=Sponte Study
Exec=$APP_NAME
Icon=$APP_NAME
Type=Application
Categories=Education;
EOF

cp "AppDir/usr/share/applications/$APP_NAME.desktop" "AppDir/$APP_NAME.desktop"

cat > "AppDir/AppRun" << 'EOF'
#!/bin/bash
HERE="$(dirname "$(readlink -f "${0}")")"
exec "$HERE/usr/bin/SponteStudy" "$@"
EOF
chmod +x "AppDir/AppRun"

ARCH=x86_64 ./appimagetool-x86_64.AppImage AppDir "${APP_NAME}.AppImage"

if [ -f "${APP_NAME}.AppImage" ]; then
    chmod +x "${APP_NAME}.AppImage"
    echo "✅ AppImage gerado: ${APP_NAME}.AppImage"
else
    echo "❌ Falha ao gerar AppImage."
    deactivate
    exit 1
fi

deactivate