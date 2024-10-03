#!/bin/bash

# Variável que define o arquivo que irá guardar os resultados
arquivo_resultados="resultados.txt"

# Função para adicionar linha em branco no arquivo
linha_em_branco(){
    echo "" >> "$arquivo_resultados"
}

# Limpa o arquivo antes de executar o script
> "$arquivo_resultados"

# Missão 12: O Espaço é Limitado
echo "Executando missão 12: O espaço é limitado"
echo "Resultado da missão 12: O espaço é limitado" >> "$arquivo_resultados"
echo "Espaço utilizado pelo usuário $(echo $USER) é $(du -sh ~/ | awk '{print $1}')" >> "$arquivo_resultados"
echo "Missão 12 finalizada"
linha_em_branco  # Chamada da função sem parênteses

# Missão 13: Verificando as Áreas Críticas
echo "Executando missão 13: Verificando Áreas Críticas..."
echo "Resultado da missão 13: Verificando Áreas Críticas" >> "$arquivo_resultados"
echo "Espaço utilizado no diretório dos tripulantes $(du -sh /home | awk '{print $1}')" >> "$arquivo_resultados"
echo "Missão 13 finalizada!"
linha_em_branco  # Chamada da função sem parênteses

# Missão 14: Mensagem do Comandante Cow
# Precisamos testar se o comandante Cow, uma inteligência artificial representada por 
# uma vaca falante, está funcionando corretamente. Para isto, utilize o comando
# "cowsay" para que isso ocorra da seguinte maneira: enviar uma mensagem urgente ao
# tripulante atual (você). Vamos fazer com que ele diga o seu nome e registrar isso 
# no arquivo resultado.txt.

echo "Executando missão 14: Mensagem do Comandante Cow"
echo "Resultado da missão 14: Mensagem do comandante Cow" >> "$arquivo_resultados"
echo "$(cowsay `whoami`)" >> "$arquivo_resultados"
