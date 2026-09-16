# Mateus Odonto — hotsite Odont

Hotsite do plano odontológico **Mateus Odonto**, operado pela Odont (ANS nº 42.208-8), no molde dos hotsites de produto white label da Sempre Odonto (ex.: Odonto Eskala).

Conteúdo, preços, carências e benefícios seguem a proposta `ODONT_Proposta_RFP_08_2026` (resposta ao item 3.2 da RFP do Grupo Mateus).

## Estrutura

- `index.html` — página única: hero com carteirinha digital, benefícios, procedimentos cobertos, sorteio semanal, desconto em farmácia, rede credenciada, app, planos (Standard / Advanced / Diamond), carências, atendimento e rodapé com ANS.
- `styles.css` — identidade visual do Grupo Mateus (azul `#0038A0`, marinho `#051E5A`, azul claro `#0093D9`, vermelho `#EA0A2A`, amarelo `#FFC629`), fonte Montserrat, como em grupomateus.com.br.
- `assets/` — logo Grupo Mateus, logos Odont, carteirinha Mateus Odonto Standard e selo Prêmio RA 2026.

Sem dependências nem build: abra `index.html` ou publique a pasta em qualquer host estático (GitHub Pages, Vercel, Netlify).

## Pendências antes de publicar

- Links de **Termo de adesão**, **Condições Gerais** e **Regulamento do sorteio** apontam para odont.com.br — substituir pelos PDFs definitivos.
- Consulta do número da sorte e busca de rede são apenas UI; integrar à API da operadora.
- Preços são os de venda sugeridos na proposta e podem mudar no lançamento.
- Nome e marca "Mateus Odonto" dependem de aprovação do Grupo Mateus; o logo do Mateus não foi incluído.
