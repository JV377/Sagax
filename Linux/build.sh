#!/bin/bash

APP_NAME="SponteStudy"

echo "Iniciando o processo de build para $APP_NAME..."

if ! command -v python3 &> /dev/null; then
    echo "Erro: Python3 não encontrado."
    exit 1
fi

sudo apt-get install -y python3-pip python3-venv python3-tk
sudo apt-get install -y espeak espeak-data libespeak-dev python3-dbus

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install customtkinter CTkToolTip pyttsx3 Pillow pygments pyinstaller

CTK_PATH=$(python3 -c "import customtkinter; import os; print(os.path.dirname(customtkinter.__file__))")

rm -rf build dist __pycache__ *.spec

pyinstaller --noconfirm --onefile --windowed \
    --add-data "imagens_app:imagens_app" \
    --add-data "$CTK_PATH:customtkinter" \
    --add-data "CTkCodeBox:CTkCodeBox" \
    --hidden-import "customtkinter" \
    --hidden-import "CTkToolTip" \
    --hidden-import "pyttsx3" \
    --hidden-import "pyttsx3.drivers" \
    --hidden-import "pyttsx3.drivers.espeak" \
    --hidden-import "pygments" \
    --hidden-import "pygments.lexers" \
    --hidden-import "pygments.formatters" \
    --hidden-import "PIL" \
    --hidden-import "PIL._tkinter_finder" \
    --collect-all customtkinter \
    --name "$APP_NAME" \
    interface.py

if [ -f "dist/$APP_NAME" ]; then
    chmod +x "dist/$APP_NAME"
    echo " Build concluído! Executável em: dist/$APP_NAME"
else
    echo " Falha no build. Verifique os erros acima."
    deactivate
    exit 1
fi

deactivate