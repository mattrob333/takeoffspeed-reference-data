| Task kind | Model | Resolution | Calls | Errors | Precision | Recall | F1 / count or cell accuracy | Exact tag counts | Mean cost per call (USD) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| count | claude-fable-5-1 | hi | 2 | 0 |  |  | MAPE 1.1% | 29/32 exact, 30 within 5% | 0.1308 |
| count | claude-opus-5-5 | hi | 2 | 0 |  |  | MAPE 1.2% | 29/32 exact, 29 within 5% | 0.0386 |
| count | claude-sonnet-5-5 | hi | 2 | 0 |  |  | MAPE 3.0% | 26/32 exact, 27 within 5% | 0.0231 |
| count | claude-haiku-5-5 | hi | 2 | 0 |  |  | MAPE 1.8% | 29/32 exact, 29 within 5% | 0.0020 |
| count | gpt-6-astra | hi | 2 | 0 |  |  | MAPE 0.7% | 30/32 exact, 30 within 5% | 0.2621 |
| count | claude-opus-5-5 | zoom-tool | 1 | 0 |  |  | MAPE 0.9% | 18/19 exact, 18 within 5% | 0.2005 |
| count | claude-sonnet-5-5 | zoom-tool | 1 | 0 |  |  | MAPE 0.9% | 18/19 exact, 18 within 5% | 0.0631 |
| count | gpt-6-astra | zoom-tool | 1 | 0 |  |  | MAPE 0.9% | 18/19 exact, 18 within 5% | 0.7530 |
| count | claude-fable-5-1 | zoom-tool | 1 | 0 |  |  | MAPE 3.5% | 17/19 exact, 17 within 5% | 1.0521 |
| dimensions | gpt-6-astra | hi | 12 | 0 | 0.996 | 0.982 | 0.989 |  | 0.1341 |
| dimensions | claude-fable-5-1 | hi | 12 | 0 | 0.991 | 0.949 | 0.969 |  | 0.0962 |
| dimensions | claude-opus-5-5 | hi | 12 | 0 | 0.991 | 0.947 | 0.968 |  | 0.0311 |
| dimensions | claude-opus-5-5 | lo | 12 | 0 | 0.989 | 0.942 | 0.964 |  | 0.0194 |
| dimensions | claude-sonnet-5-5 | lo | 12 | 0 | 0.993 | 0.934 | 0.962 |  | 0.0111 |
| dimensions | claude-sonnet-5-5 | hi | 12 | 0 | 0.986 | 0.931 | 0.957 |  | 0.0171 |
| dimensions | claude-haiku-5-5 | hi | 12 | 0 | 0.977 | 0.912 | 0.942 |  | 0.0014 |
| measure | claude-sonnet-5-5 | hi | 2 | 0 |  |  | MAPE 27.5% | 0/10 exact, 1 within 5% | 0.0236 |
| measure | claude-fable-5-1 | hi | 2 | 0 |  |  | MAPE 33.6% | 0/10 exact, 1 within 5% | 0.1809 |
| measure | claude-haiku-5-5 | hi | 2 | 0 |  |  | MAPE 59.4% | 0/10 exact, 0 within 5% | 0.0020 |
| measure | claude-opus-5-5 | hi | 2 | 0 |  |  | MAPE 12.8% | 0/10 exact, 4 within 5% | 0.0606 |
| measure | gpt-6-astra | hi | 2 | 1 |  |  | MAPE 3.8% | 0/4 exact, 2 within 5% | 0.2537 |
| measure | claude-opus-5-5 | zoom-tool | 2 | 0 |  |  | MAPE 18.3% | 0/10 exact, 3 within 5% | 0.2276 |
| measure | claude-sonnet-5-5 | zoom-tool | 2 | 0 |  |  | MAPE 25.1% | 0/10 exact, 1 within 5% | 0.1744 |
| measure | gpt-6-astra | zoom-tool | 2 | 0 |  |  | MAPE 10.8% | 0/10 exact, 4 within 5% | 1.1681 |
| measure | claude-fable-5-1 | zoom-tool | 2 | 0 |  |  | MAPE 13.6% | 0/10 exact, 4 within 5% | 2.3255 |
| schedule | claude-haiku-5-5 | hi | 2 | 0 |  |  | 1.000 |  | 0.0010 |
| schedule | claude-fable-5-1 | hi | 2 | 0 |  |  | 1.000 |  | 0.0723 |
| schedule | claude-opus-5-5 | hi | 2 | 0 |  |  | 1.000 |  | 0.0325 |
| schedule | gpt-6-astra | hi | 2 | 0 |  |  | 1.000 |  | 0.0765 |
| schedule | claude-sonnet-5-5 | hi | 2 | 0 |  |  | 0.993 |  | 0.0145 |
| tag-count | claude-opus-5-5 | hi | 3 | 0 |  |  | 0.958 | 12/12 | 0.0237 |
| tag-count | claude-fable-5-1 | hi | 3 | 0 |  |  | 0.958 | 12/12 | 0.0717 |
| tag-count | claude-sonnet-5-5 | hi | 3 | 0 |  |  | 0.958 | 12/12 | 0.0123 |
| tag-count | claude-haiku-5-5 | hi | 3 | 0 |  |  | 0.958 | 12/12 | 0.0007 |
| tag-count | claude-opus-5-5 | lo | 3 | 0 |  |  | 0.958 | 12/12 | 0.0126 |
| tag-count | gpt-6-astra | hi | 3 | 0 |  |  | 0.958 | 12/12 | 0.0583 |
| tag-count | claude-sonnet-5-5 | lo | 3 | 0 |  |  | 0.917 | 11/12 | 0.0063 |
