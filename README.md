# Mateus Odonto — hotsite Odont

Hotsite do plano odontológico **Mateus Odonto**, operado pela Odont (ANS nº 42.208-8), no molde dos hotsites de produto white label da Sempre Odonto (ex.: Odonto Eskala).

Conteúdo, preços, carências e benefícios seguem a proposta `ODONT_Proposta_RFP_08_2026` (resposta ao item 3.2 da RFP do Grupo Mateus).

## Estrutura

- `index.html` — página única: hero com carteirinha digital, benefícios, procedimentos cobertos, sorteio semanal, desconto em farmácia, rede credenciada, app, planos (Standard / Advanced / Diamond), carências, atendimento e rodapé com ANS.
- `styles.css` — identidade Odont (roxo `#45138E`, roxo escuro `#241046`, magenta `#DE217D`, lilás `#F4EFFC`), fonte Outfit.
- `assets/` — logos Odont e selo Prêmio RA 2026 extraídos do deck.

Sem dependências nem build: abra `index.html` ou publique a pasta em qualquer host estático (GitHub Pages, Vercel, Netlify).

## Pendências antes de publicar

- Links de **Termo de adesão**, **Condições Gerais** e **Regulamento do sorteio** apontam para odont.com.br — substituir pelos PDFs definitivos.
- Consulta do número da sorte e busca de rede são apenas UI; integrar à API da operadora.
- Preços são os de venda sugeridos na proposta e podem mudar no lançamento.
- Nome e marca "Mateus Odonto" dependem de aprovação do Grupo Mateus; o logo do Mateus não foi incluído.
