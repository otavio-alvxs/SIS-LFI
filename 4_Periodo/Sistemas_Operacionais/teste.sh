#!/bin/bash

DIR_BACKUP="/root/backup"

if [ ! -d "$DIR_BACKUP" ]; then
	echo "Criando o diretório $DIR_BACKUP."
	mkdir "DIR_BACKUP"

fi

echo "Localizando arquivos modificados nos ultimos 7 dias..."
ARQUIVOS=$( find / -ctime 7 2> /dev/null)

echo "Fazendo backup..."
for I in $ARQUIVOS; do
	echo "Copiando arquivo $I..."
	cp "$I" "$DIR_BACKUP" 2> /dev/null

done
