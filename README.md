# Música 8D
Este script tem o objetivo em deixar a música naquele famoso estilo 8D (que nada mais é que simular intercalando entre os canais auditivos, coisa boba), por enquanto o script está o mais básico possível e tentarei implementar mais coisas se possível, e quem puder e quiser ajudar o projeto será muito bem-vindo

## Uso
``python music.py [Arquivo MP3]``
Após o término do procedimento é criado um arquivo com o sufixo ``final``, que é o arquivo final.

## Dependência
Para o funcionamento é necessário as seguinte biblioteca:
``pip install pydub``
e também para abrir e salvar os arquivos mp3 (ffmpeg ou libav), você pode ver como instalar no [próprio pydub](https://github.com/jiaaro/pydub#getting-ffmpeg-set-up).

## TO-DO
- Adicionar sox
- Transições variadas e mais suaves
- Implementar na web