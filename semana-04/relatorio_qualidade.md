# Relatório de qualidade — base de solicitações

> Execute o notebook `02_limpeza.ipynb` para preencher os números reais automaticamente. A célula final gera este relatório com as contagens calculadas.

| Problema | Linhas afetadas | O que eu fiz |
|---|---:|---|
| Linhas repetidas | A preencher ao executar | Removi com `drop_duplicates()` |
| Categoria escrita de jeitos diferentes | A preencher ao executar | Padronizei espaços, maiúsculas/minúsculas e grafias equivalentes |
| Status fora do padrão | A preencher ao executar | Removi espaços e padronizei a capitalização |
| Prioridade fora do padrão | A preencher ao executar | Removi espaços e padronizei a capitalização |
| Avaliações inválidas (notas fora de 1 a 5) | A preencher ao executar | Não usei essas notas na média e registrei a decisão |

## Conferência

A soma das solicitações por categoria deve ser igual ao total de linhas da base limpa. O notebook faz essa conferência automaticamente.

## Decisão sobre avaliações

Somente notas numéricas de 1 a 5 entram no cálculo da média por categoria. Avaliações fora desse intervalo não entram na média, mas as solicitações são mantidas na base.
