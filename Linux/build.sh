#!/bin/bash
set -e

APP_NAME="SponteStudy"
EXEC_NAME="sponte-study"
DESKTOP_NAME="sponte-study"
VERSION="1.0.0"

PACMAN_DEPS=(
  "tk"
  "espeak-ng"
  "fuse2"
  "python-pip"
)

echo "==> Verificando dependências do sistema..."
MISSING_PACMAN=()
for dep in "${PACMAN_DEPS[@]}"; do
  if ! pacman -Q "$dep" &>/dev/null; then
    MISSING_PACMAN+=("$dep")
  fi
done

if [ ${#MISSING_PACMAN[@]} -gt 0 ]; then
  echo "    Instalando: ${MISSING_PACMAN[*]}"
  sudo pacman -S --noconfirm "${MISSING_PACMAN[@]}"
else
  echo "    Todas as dependências do sistema OK."
fi


echo "==> Verificando dependências Python..."
MISSING_PIP=()

python3 -c "import customtkinter" &>/dev/null 2>&1     || MISSING_PIP+=("customtkinter")
python3 -c "import CTkToolTip" &>/dev/null 2>&1         || MISSING_PIP+=("CTkToolTip")
python3 -c "import CustomtkinterCodeViewer" &>/dev/null || MISSING_PIP+=("CustomtkinterCodeViewer")
python3 -c "import tklinenums" &>/dev/null 2>&1         || MISSING_PIP+=("tklinenums")
python3 -c "import pyttsx3" &>/dev/null 2>&1            || MISSING_PIP+=("pyttsx3")
python3 -c "import PIL" &>/dev/null 2>&1                || MISSING_PIP+=("pillow")
python3 -c "import pygments" &>/dev/null 2>&1           || MISSING_PIP+=("pygments")
python3 -c "import darkdetect" &>/dev/null 2>&1         || MISSING_PIP+=("darkdetect")
python3 -c "import PyInstaller" &>/dev/null 2>&1        || MISSING_PIP+=("pyinstaller")

# Remover duplicatas
MISSING_PIP=($(echo "${MISSING_PIP[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))

if [ ${#MISSING_PIP[@]} -gt 0 ]; then
  echo "    Instalando: ${MISSING_PIP[*]}"
  pip install "${MISSING_PIP[@]}" --break-system-packages
else
  echo "    Todas as dependências Python OK."
fi

export PATH="$HOME/.local/bin:$PATH"

echo "==> Limpando build anterior..."
rm -rf build/ dist/ *.spec "${APP_NAME}.AppDir" "${APP_NAME}-${VERSION}-x86_64.AppImage"

echo "==> Compilando com PyInstaller..."
pyinstaller --onefile \
  --add-data "imagens_app:imagens_app" \
  --add-data "CTkCodeBox:CTkCodeBox" \
  --hidden-import customtkinter \
  --hidden-import CTkToolTip \
  --hidden-import CTkCodeBox \
  --hidden-import pyttsx3 \
  --hidden-import pyttsx3.drivers \
  --hidden-import pyttsx3.drivers.espeak \
  --hidden-import PIL \
  --hidden-import PIL.Image \
  --hidden-import tklinenums \
  --hidden-import CustomtkinterCodeViewer \
  --hidden-import pygments \
  --collect-all customtkinter \
  --collect-all CTkToolTip \
  --collect-all pygments \
  interface.py

echo "==> Montando AppDir..."
mkdir -p "${APP_NAME}.AppDir/usr/bin"
mkdir -p "${APP_NAME}.AppDir/usr/share/icons"

cp dist/interface "${APP_NAME}.AppDir/usr/bin/${EXEC_NAME}"
cp imagens_app/Sponte.png "${APP_NAME}.AppDir/${DESKTOP_NAME}.png"
cp imagens_app/Sponte.png "${APP_NAME}.AppDir/usr/share/icons/${DESKTOP_NAME}.png"

echo "==> Criando AppRun..."
cat > "${APP_NAME}.AppDir/AppRun" << 'EOF'
#!/bin/bash
HERE="$(dirname "$(readlink -f "${0}")")"
exec "$HERE/usr/bin/sponte-study" "$@"
EOF
chmod +x "${APP_NAME}.AppDir/AppRun"

echo "==> Criando .desktop..."
cat > "${APP_NAME}.AppDir/${DESKTOP_NAME}.desktop" << EOF
[Desktop Entry]
Name=Sponte Study
Exec=${EXEC_NAME}
Icon=${DESKTOP_NAME}
Type=Application
Categories=Education;
EOF

echo "==> Verificando appimagetool..."
if [ ! -f "appimagetool-x86_64.AppImage" ]; then
  echo "    Baixando appimagetool..."
  wget -q --show-progress \
    https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
  chmod +x appimagetool-x86_64.AppImage
else
  echo "    appimagetool já existe, pulando download."
fi

echo "==> Gerando AppImage..."
ARCH=x86_64 ./appimagetool-x86_64.AppImage \
  "${APP_NAME}.AppDir" \
  "${APP_NAME}-${VERSION}-x86_64.AppImage"

chmod +x "${APP_NAME}-${VERSION}-x86_64.AppImage"

echo ""
echo "✅ Pronto! AppImage gerado: ${APP_NAME}-${VERSION}-x86_64.AppImage"
echo "   Execute com: ./${APP_NAME}-${VERSION}-x86_64.AppImage"