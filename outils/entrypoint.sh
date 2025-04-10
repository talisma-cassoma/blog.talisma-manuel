#!/bin/bash

# Nome do ambiente virtual
VENV_DIR="venv"

# Criar ambiente virtual se não existir
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
    echo "virtual env criated in $VENV_DIR"
fi

# Ativar o ambiente virtual
source $VENV_DIR/bin/activate

echo "virtual env ativated"

# Instalar dependências necessárias
pip install --upgrade pip
pip install pillow qrcode

echo "Deps instaled"

# Executar o script Python
python convert_png_to_webp.py