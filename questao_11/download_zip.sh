#!/bin/bash

function download_zip() {
    echo "[download_zip] Starting zip file download"

    # a. Crie uma pasta com seu nome
    USER_NAME="tiago_farias_barbosa"
    mkdir -p "$USER_NAME"
    # b. Dentro da pasta com seu nome crie uma pasta com o nome “resultado”
    mkdir -p "$USER_NAME/resultado"

    # c. Baixe o arquivo hospedado em https://vanilton.net/v1/download/zip.zip
    ZIP_URL="https://vanilton.net/v1/download/zip.zip"
    ZIP_FILE="$USER_NAME/zip.zip"
    curl -o "$ZIP_FILE" "$ZIP_URL"

    if [ ! -f "$ZIP_FILE" ]; then
        echo "[download_zip] Failed to download zip file"
        exit 1
    fi

    # d. Descompacte-o na raiz da pasta com seu nome
    unzip "$ZIP_FILE" -d "$USER_NAME"

    # e. Mova o arquivo descompactado para a pasta “resultado”
    mv "$USER_NAME"/readme.md "$USER_NAME/resultado" 2>/dev/null
    rm "$ZIP_FILE"

    echo "[download_zip] Download finished"
}

download_zip
