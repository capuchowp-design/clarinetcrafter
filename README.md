# Clarinetcraft

Editor de partituras (piano-roll) com **som real de clarinete**, adaptado do projeto Saxcrafter.
Funciona no navegador, como PWA instalável, e exporta PDF (partitura), MIDI, WAV e JSON.

## Importante: coloque as gravações do clarinete

O app usa **gravações reais** (nenhum som sintético). Elas vêm da biblioteca
[tonejs-instruments](https://github.com/nbrosowsky/tonejs-instruments) (pasta `samples/clarinet`).

1. **Recomendado (funciona offline):** rode uma vez `./baixar-samples.sh` (Mac/Linux) ou
   `baixar-samples.bat` (Windows). Isso cria `samples/clarinet/` com 11 arquivos `.mp3`
   (D3, F3, As3, D4, F4, As4, D5, F5, As5, D6, Fs6). Depois faça commit dessa pasta no GitHub.
2. Se a pasta não existir, o app tenta buscar as mesmas gravações pelo CDN jsDelivr
   (precisa de internet na primeira vez; o service worker guarda para uso offline).

O app acha a gravação mais próxima de cada nota e a ajusta de tom; o trecho sustentado entra em loop
(com ponto de loop calculado automaticamente) para notas longas.

## O que mudou em relação ao Saxcrafter

- Som: clarinete real (carregado de `samples/clarinet`), no lugar de `sax-samples.js`.
- Grade: Ré3 a Fá6 (alcance real do clarinete em Si♭, em som real).
- Partitura: clarinete em Si♭, Lá, Mi♭, clarone ou em dó (transposição automática).
- MIDI exportado usa o programa GM 72 (Clarinet).
- Interface, cores (prata/azul-aço), ícone do app e textos adaptados ao clarinete.

## Publicar (GitHub Pages)

Envie todos os arquivos para a raiz do repositório e ative Pages. É preciso HTTPS para instalar como app.

## Créditos e licença das gravações

Gravações de clarinete: biblioteca tonejs-instruments (N. P. Brosowsky), licença **CC-BY 3.0**.
É exigida atribuição: mantenha este crédito. As fontes originais das amostras estão no arquivo
`sample-source-info.txt` do repositório da biblioteca.
Partitura renderizada com [VexFlow](https://github.com/0xfe/vexflow) (carregado via CDN).
