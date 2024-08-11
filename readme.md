# Distribuidor de documentos - 08-08-2024

No trabalho gastamos uma enorme quantidade de tempo colocando os documentos dos funcionários nas respectivas pastas. Então, Jessica, minha colega de trabalho, me perguntou se não havia maneira de melhorar esse processo. Assim, tive a ideia de criar um script simples usando Python e a sua biblioteca nativa OS. 

A solução envolve criar uma pasta de transição e dentro dessa pasta ficará todos os arquivos que serão distribuídos. Os arquivos precisam ser nomeados de uma forma padronizada para que o script possa ser executado. Além disso, é necessário uma pasta de destino que contenha os diretórios que deseja guardar os arquivos.

No caso da minha empresa, organizamos os arquivos com um diretório principal que contem todas as pastas nomeadas com o nome do colaborador e dentro de cada pasta temos 6 subpastas representando assuntos distintos e nomeadas conforme eles, como: Advertências, atestados, documentos.

## Padrão dos nomes dos arquivos

Visto a necessidade de padronizar os nomes dos arquivos que serão distribuídos, criei um padrão de nome que é divido em três partes:

> NOME DO COLABORADOR - SUBPASTA - DESCRIÇÃO

- **Nome do colaborador:** nome completo do colaborador, precisa ser EXATAMENTE igual ao nome da pasta que representa o respectivo funcionário.
- **Subpasta:** nome EXATO da subpasta em que o arquivo vai ficar;
- **Descrição:** pode ser qualquer coisa, vai depender do objetivo do script,  no meu caso, será a data do documento.

## Passos de funcionamento do Script:

1. Localizar pasta de transição e pasta principal
2. Identificar os nomes de todos os arquivos dentro da pasta de transição e colocar em uma lista
3. Abrir um loop iterando a lista.
4. Tratar o elemento da lista (NOME DO COLABORADOR - SUBPASTA - DESCRIÇÃO) dividindo cada parte do nome e colocando em uma variável temporária.
5. Verificar se a pasta do colaborador e subpasta existem.
6. Mover e renomear o arquivo (caso a pasta exista).
