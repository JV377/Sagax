#!/bin/bash
set -e

APP_NAME="SponteStudy"
EXEC_NAME="sponte-study"
DESKTOP_NAME="sponte-study"
VERSION="1.0.0"

echo "==> Limpando build anterior..."
rm -rf build/ dist/ *.spec "${APP_NAME}.AppDir" "${APP_NAME}.AppImage"

echo "==> Compilando com PyInstaller..."
pyinstaller --onefile \
  --add-data "imagens_app:imagens_app" \
  --add-data "CTkCodeBox:CTkCodeBox" \
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

echo "==> Baixando appimagetool..."
if [ ! -f "appimagetool-x86_64.AppImage" ]; then
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