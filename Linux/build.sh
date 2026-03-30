#!/bin/bash
set -e

APP_NAME="SponteStudy"
EXEC_NAME="sponte-study"
DESKTOP_NAME="sponte-study"
VERSION="1.0.0"
BASE_DIR=$(cd "$(dirname "$0")" && pwd)

cd "$BASE_DIR"

if ! command -v python3 &>/dev/null; then
  exit 1
fi

rm -rf build_venv build dist *.spec "${APP_NAME}.AppDir"

python3 -m venv build_venv
source build_venv/bin/activate

pip install --upgrade pip
pip install customtkinter CTkToolTip tklinenums pyttsx3 pillow pygments darkdetect pyinstaller

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
CTK_PATH="build_venv/lib/python${PYTHON_VERSION}/site-packages/customtkinter"

pyinstaller --noconfirm --onefile --windowed \
  --add-data "imagens_app:imagens_app" \
  --add-data "CTkCodeBox/CTkCodeBox:CTkCodeBox" \
  --add-data "${CTK_PATH}:customtkinter" \
  --collect-all pygments \
  --collect-all CTkToolTip \
  --hidden-import pyttsx3.drivers \
  --hidden-import pyttsx3.drivers.espeak \
  --name "${EXEC_NAME}" \
  interface.py

mkdir -p "${APP_NAME}.AppDir/usr/bin"
mkdir -p "${APP_NAME}.AppDir/usr/share/icons"

cp "dist/${EXEC_NAME}" "${APP_NAME}.AppDir/usr/bin/${EXEC_NAME}"
cp "imagens_app/Sponte.png" "${APP_NAME}.AppDir/${DESKTOP_NAME}.png"

cat > "${APP_NAME}.AppDir/AppRun" << 'EOF'
#!/bin/bash
HERE="$(dirname "$(readlink -f "${0}")")"
export PATH="$HERE/usr/bin:$PATH"
exec "${HERE}/usr/bin/sponte-study" "$@"
EOF
chmod +x "${APP_NAME}.AppDir/AppRun"

cat > "${APP_NAME}.AppDir/${DESKTOP_NAME}.desktop" << EOF
[Desktop Entry]
Name=Sponte Study
Exec=${EXEC_NAME}
Icon=${DESKTOP_NAME}
Type=Application
Categories=Education;
EOF

if [ ! -f "appimagetool-x86_64.AppImage" ]; then
  wget -q https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage
  chmod +x appimagetool-x86_64.AppImage
fi

ARCH=x86_64 ./appimagetool-x86_64.AppImage --appimage-extract-and-run "${APP_NAME}.AppDir" "${APP_NAME}-${VERSION}-x86_64.AppImage"

deactivate
rm -rf build_venv