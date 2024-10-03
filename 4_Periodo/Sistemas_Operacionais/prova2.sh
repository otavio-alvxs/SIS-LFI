#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "O script especificado deve ser executado como superusuário"
    exit 1
fi

LEVANTA_ESPACO() {
    for user in $(ls /home); do
        if [ -d "/home/$user" ]; then
            space=$(du -sh "/home/$user" 2>/dev/null | cut -f1)
            echo "O usuário [$user] está ocupando [$space]"
        fi
    done
}

ARQ_ALTERADOS_2_DIAS() {
    echo "Foram modificados nos últimos 2 dias os arquivos:"
    find /home -type f -mtime -2
}

while true; do
    echo "---| PROVA SHELL SCRIPT |-----"
    echo "[1] Verificar o espaço utilizado por todos os usuários do sistema operacional"
    echo "[2] Verificar no /home (todos usuários) quais arquivos foram modificados nos últimos 2 dias"
    echo "[3] Sair"
    
    read -p "Escolha uma opção: " option

    case $option in
        1)
            LEVANTA_ESPACO
            ;;
        2)
            ARQ_ALTERADOS_2_DIAS
            ;;
        3)
            exit 0
            ;;
        *)
            echo "Opção inválida. Tente novamente."
            ;;
    esac

    echo ""
done
