# GS 2026.2 — SERS | Praça Sustentável

**FIAP — Ciência da Computação, turma 1CC**  
**Disciplina:** Soluções em Energias Renováveis e Sustentáveis  
**Desafio:** Neighborhood Action Dashboard — CitizenTech  
**Integrantes:** Gabriel Akira — RM 576082; Caio Gotardo — RM 574768
**DashBoard:** https://gabrielakira2809.github.io/gs-2026-citizentech-praca-sustentavel/

## 1. Problema e proposta
Uma praça comunitária precisa de iluminação noturna segura e eficiente. O consumo elevado de luminárias antigas pode aumentar os gastos e desperdiçar energia. A proposta é comparar **10 luminárias convencionais de 150 W**, **10 luminárias LED de 50 W** e **10 luminárias LED solares autônomas de 50 W**. O público beneficiado são moradores, pedestres e responsáveis pela manutenção do espaço.

A solução busca reduzir desperdício, apoiar decisões transparentes e avaliar a viabilidade de energia renovável. Relaciona-se aos **ODS 7, 11 e 13**.

## 2. Como abrir o dashboard
Abra `dashboard.html` no navegador. Não precisa instalar bibliotecas nem acessar a internet. É possível alterar horas diárias, tarifa e fator de emissões; os gráficos e indicadores se atualizam automaticamente.

Para conferir os cálculos no terminal, execute `python calculos.py` (Python 3). O diagrama está em `diagrama.svg` e os dados em `dados_cenarios.csv` e `premissas.json`.

## 3. Premissas (cenário hipotético, não levantamento de campo)
- 10 pontos de luz; 12 h/dia; 30 dias/mês.
- Convencional: 150 W por ponto; LED: 50 W por ponto.
- Tarifa ilustrativa: R$ 0,90/kWh, sem impostos ou estrutura tarifária detalhada.
- Investimento adicional ilustrativo: LED na rede R$ 6.000; LED solar autônomo R$ 45.000 (painéis, baterias, luminárias e instalação como estimativa de exercício).
- Operação solar: reserva ilustrativa de R$ 100/mês para manutenção, não representa orçamento real; operação LED na rede considera apenas energia elétrica.
- Solar: 4,5 horas de sol pico/dia e rendimento global de 75%, hipóteses de dimensionamento; autonomia nominal de bateria: 2 dias, fração utilizável de 80%.
- Fator de emissão **hipotético** de 0,05 kg CO₂e/kWh de eletricidade de rede, somente para mostrar a conta; deve ser substituído por fator oficial adequado ao período antes de qualquer divulgação ambiental.
- A comparação solar supõe atendimento integral por energia renovável; não comprova autonomia real em dias nublados, perdas adicionais, degradação ou necessidade de backup.

## 4. Cálculos e indicadores
Fórmula: **E (kWh) = quantidade × potência (W) × horas/dia × dias/mês / 1000**.

| Indicador | Convencional | LED na rede | LED solar autônomo (projeção) |
|---|---:|---:|---:|
| Consumo das cargas (kWh/mês) | 540 | 180 | 180 |
| Energia comprada da rede (kWh/mês) | 540 | 180 | 0 |
| Economia da carga vs. convencional | — | 360 kWh/mês (66,7%) | 360 kWh/mês (66,7%) |
| Custo de energia / operação (R$/mês) | 486 energia | 162 energia | 100 reserva de manutenção |
| Implantação incremental (R$) | 0 | 6.000 | 45.000 |
| Participação renovável no atendimento | 0% | 0% | 100% (hipótese) |

**Economia de energia com LED:** 540 − 180 = **360 kWh/mês** (66,7%).  
**Economia financeira com LED:** 360 × R$ 0,90 = **R$ 324/mês** na conta de energia (sem manutenção).  
**Payback simples ilustrativo do LED:** 6.000 / 324 ≈ **18,5 meses**; não inclui juros, manutenção ou substituição.  
**Solar:** geração requerida antes das perdas = 180 / 0,75 = **240 kWh/mês**; potência fotovoltaica teórica = 240 / (4,5 × 30) = **1,78 kWp**.  
**Bateria teórica nominal:** (180 / 30) × 2 / 0,80 = **15 kWh**; ainda exige projeto elétrico detalhado.  
**Emissões evitadas hipotéticas com LED:** 360 × 12 × 0,05 = **216 kg CO₂e/ano**.  
**Emissões evitadas hipotéticas com solar (comparação com a rede convencional):** 540 × 12 × 0,05 = **324 kg CO₂e/ano**. Não inclui ciclo de vida dos equipamentos.

**Nota sobre custos:** para comparar alternativas, custos de implantação e operação foram separados. O valor de R$ 100/mês no cenário solar é uma reserva simplificada, não uma medição. O investimento solar é maior e depende de cotação, instalação, baterias, manutenção e segurança do local. Comparações de custo total exigiriam horizonte, taxa de desconto e troca de baterias.

## 5. Alternativas: vantagens e limitações
**A — LED na rede:** menor investimento inicial, instalação mais simples, grande redução de consumo. Continua dependente da rede elétrica e não gera energia renovável no local.  
**B — LED solar autônomo:** mesma eficiência das lâmpadas LED e potencial de reduzir a compra de energia da rede, usando geração fotovoltaica e baterias. Exige maior investimento, área sem sombra, dimensionamento para noites e dias nublados, proteção contra furtos, manutenção e descarte correto de baterias.

**Recomendação:** começar pela troca por LED e avaliar a solução solar em etapa posterior, com visita técnica, cotação e estudo de sombreamento. A alternativa solar pode ser prioritária em locais sem acesso confiável à rede, mas isso precisa ser confirmado.

## 6. Diagrama e integração CitizenTech
O `diagrama.svg` mostra fonte de energia, luminárias, bateria/controlador, dados de consumo, processamento e dashboard. O `dashboard.html` contém os indicadores reais do modelo: consumo (kWh/mês), economia (kWh e %), custo (R$/mês), participação renovável (%), emissões evitadas (kg CO₂e/ano), potência solar e bateria teóricas. Não é um painel genérico: todos os números derivam das premissas declaradas.

## 7. Limitações e referências
Este é um estudo conceitual com **valores assumidos para fins didáticos**, sem medição local, orçamento de fornecedor ou garantia de desempenho. O dimensionamento fotovoltaico não substitui projeto técnico e normas de segurança. Antes de implantar, validar potência, horas de funcionamento, insolação, tarifa local, custos e fator de emissão oficial.

Referências de método e consulta:
- Enunciado da FIAP: *Global Solution 2026.2 — SERS — Neighborhood Action Dashboard* (arquivo fornecido pelo professor).
- EPE — Balanço Energético Nacional: https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/balanco-energetico-nacional-ben
- CRESESB/CEPEL — referência para potencial solar: https://www.cresesb.cepel.br/
- INMET — dados meteorológicos: https://portal.inmet.gov.br/
- MCTI — fatores de emissão de eletricidade: https://www.gov.br/mcti/pt-br
- Nações Unidas — Objetivos de Desenvolvimento Sustentável: https://brasil.un.org/pt-br/sdgs
