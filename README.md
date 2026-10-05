# Clarinetcrafter

Editor de partituras no navegador (PWA) com **som real de clarinete**: sem síntese, só gravações.
Baseado no projeto Saxcrafter, com interface, ícones, alcance, transposições e motor de som adaptados.

## Como o som funciona
- 11 gravações reais de clarinete (D3 a F#6). As notas intermediárias são obtidas alterando a velocidade de reprodução em até 2 semitons.
- Notas longas usam um trecho de sustentação em loop, calculado automaticamente no navegador (sincronizado com o período da nota, com crossfade).
- As gravações vêm de `samples/clarinet/` se existirem; caso contrário são baixadas da CDN na primeira abertura e guardadas para uso offline (service worker).

### Recomendado: guardar as gravações no seu repositório
```bash
python3 tools/baixar-amostras.py     # ou: bash tools/baixar-amostras.sh
```
Depois faça commit da pasta `samples/clarinet/`. Assim o app não depende de CDN nenhuma.

## Recursos
- Alcance D3 a G6 (som real do clarinete em Si♭).
- Partitura em PDF com transposição: clarinete em Si♭ (+2), Lá (+3), requinta em Mi♭ (−3), clarinete alto em Mi♭ (+9), clarone em Si♭ (+14) ou em dó.
- Exporta MIDI (programa 72, Clarinete), WAV e JSON; biblioteca de projetos e pasta do dispositivo.

## Publicar no GitHub Pages
Envie todos os arquivos da raiz (`index.html`, `sw.js`, `manifest.json`, ícones e a pasta `samples/`) e ative Settings → Pages.

## Créditos e licenças
- Gravações: **tonejs-instruments**, de N. P. Brosowsky (https://github.com/nbrosowsky/tonejs-instruments), licença **CC BY 3.0**. As fontes originais de cada gravação estão no arquivo `sample-source-info.txt` desse repositório. Se publicar o app, mantenha esta atribuição.
- Notação: VexFlow 4.2.5 (carregado de CDN).
