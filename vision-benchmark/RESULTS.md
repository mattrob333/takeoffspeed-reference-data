| Task kind | Model | Resolution | Calls | Errors | Precision | Recall | F1 / count or cell accuracy | Exact tag counts | Mean cost per scored call (USD) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| count | gpt-6-sol | orig | 2 | 0 |  |  | MAPE 8.2% | 22/32 exact, 22 within 5% | 0.1185 |
| count | gpt-6-sol | hi | 2 | 0 |  |  | MAPE 1.6% | 28/32 exact, 28 within 5% | 0.0558 |
| count | gpt-6.1-sol | orig | 2 | 0 |  |  | MAPE 0.6% | 30/32 exact, 30 within 5% | 0.1188 |
| count | gpt-6-astra | orig | 2 | 0 |  |  | MAPE 0.5% | 30/32 exact, 31 within 5% | 0.5841 |
| count | gpt-6.1-sol | hi | 2 | 0 |  |  | MAPE 1.2% | 28/32 exact, 29 within 5% | 0.0447 |
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
| dimensions | gpt-6.1-sol | hi | 5 | 0 | 0.983 | 0.964 | 0.973 |  | 0.0309 |
| dimensions | gpt-6-astra | orig | 5 | 0 | 0.980 | 0.964 | 0.971 |  | 0.3996 |
| dimensions | gpt-6.1-sol | orig | 5 | 0 | 0.980 | 0.964 | 0.971 |  | 0.0784 |
| dimensions | claude-fable-5-1 | hi | 12 | 0 | 0.991 | 0.949 | 0.969 |  | 0.0962 |
| dimensions | claude-opus-5-5 | hi | 12 | 0 | 0.991 | 0.947 | 0.968 |  | 0.0311 |
| dimensions | claude-opus-5-5 | lo | 12 | 0 | 0.989 | 0.942 | 0.964 |  | 0.0194 |
| dimensions | claude-sonnet-5-5 | lo | 12 | 0 | 0.993 | 0.934 | 0.962 |  | 0.0111 |
| dimensions | gpt-6-sol | hi | 5 | 0 | 0.973 | 0.944 | 0.958 |  | 0.0315 |
| dimensions | claude-sonnet-5-5 | hi | 12 | 0 | 0.986 | 0.931 | 0.957 |  | 0.0171 |
| dimensions | claude-haiku-5-5 | hi | 12 | 0 | 0.977 | 0.912 | 0.942 |  | 0.0014 |
| dimensions | gpt-6-sol | orig | 5 | 0 | 0.939 | 0.861 | 0.894 |  | 0.1040 |
| measure | gpt-6-sol | hi | 4 | 0 |  |  | MAPE 25.7% | 0/20 exact, 4 within 5% | 0.0827 |
| measure | gpt-6-sol | orig | 4 | 0 |  |  | MAPE 68.1% | 0/20 exact, 3 within 5% | 0.1576 |
| measure | gpt-6.1-sol | hi | 5 | 1 |  |  | MAPE 20.1% | 0/20 exact, 6 within 5% | 0.1172 |
| measure | gpt-6.1-sol | orig | 6 | 2 |  |  | MAPE 17.1% | 0/20 exact, 7 within 5% | 0.2232 |
| measure | gpt-6-astra | orig | 6 | 2 |  |  | MAPE 10.1% | 0/20 exact, 9 within 5% | 1.3249 |
| measure | gpt-6-astra | hi | 5 | 1 |  |  | MAPE 9.1% | 0/20 exact, 9 within 5% | 0.6583 |
| measure | claude-sonnet-5-5 | hi | 2 | 0 |  |  | MAPE 27.5% | 0/10 exact, 1 within 5% | 0.0236 |
| measure | claude-fable-5-1 | hi | 2 | 0 |  |  | MAPE 33.6% | 0/10 exact, 1 within 5% | 0.1809 |
| measure | claude-haiku-5-5 | hi | 2 | 0 |  |  | MAPE 59.4% | 0/10 exact, 0 within 5% | 0.0020 |
| measure | claude-opus-5-5 | hi | 2 | 0 |  |  | MAPE 12.8% | 0/10 exact, 4 within 5% | 0.0606 |
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

Resolution: `hi` = 2,576 px long edge, `lo` = 1,280 px (Claude: as sent; OpenAI: sent with `detail: "high"`, which gpt-6-astra and the Sol models downscale to about 2,500 32-px patches, roughly 1,600x1,600 px). `orig` = OpenAI only, rendered by `render_openai.py` at up to 6,000 px long edge and at most 30,000 patches, sent with `detail: "original"` (not downscaled). `zoom-tool` = `hi` overview plus up to 10 re-rendered 2,576 px zooms (OpenAI zooms also sent with `detail: "high"`).
