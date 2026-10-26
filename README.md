# LLM Evals Dataset

A structured, source-linked list of 100 LLM evaluation benchmarks, rubric libraries and frameworks, published by Evals Review under CC BY 4.0.

## What's in it

- `data/evals.csv`: 100 rows, one per eval.
- `data/evals.json`: the same 100 evals under an `evals` key, plus `note`, `updated`, `license`, `license_url` and `attribution` fields.

The files were downloaded from https://evalsreview.com/data/evals.csv and https://evalsreview.com/data/evals.json on 26 Oct 2026. The JSON `updated` field reads `2026-10-18`, and the `added` column runs from 2026-10-15 to 2026-10-25.

Rows by category:

| Category | Rows |
| --- | --- |
| Agents & tool use | 15 |
| Reasoning & knowledge | 15 |
| Coding | 14 |
| Rubric libraries & frameworks | 13 |
| Safety & factuality | 9 |
| Image & vision | 8 |
| Writing & instruction following | 7 |
| RAG & retrieval | 7 |
| Healthcare | 6 |
| Multilingual & Indian languages | 4 |
| Customer support | 2 |

## Fields

| Field | Meaning |
| --- | --- |
| `slug` | Stable identifier, also used in the Evals Review URL |
| `name` | Eval name |
| `creator` | Who made it |
| `category` | One of the categories above |
| `source_url` | The eval's own homepage or repo |
| `page_url` | Its page on evalsreview.com |
| `tests` | One line on what it tests |
| `summary` | A short plain-English description |
| `license` | The eval's data or code licence where its sources state it. Empty when not stated (36 rows) |
| `last_updated` | Last update reported by its sources. Empty when not stated (27 rows) |
| `added` | Date the row was added to this dataset (YYYY-MM-DD) |
| `sources` | Space-separated source URLs that the facts restate |

Empty means "not stated in the sources", not "none".

## Load it

Python (pandas):

```python
import pandas as pd

df = pd.read_csv("data/evals.csv", keep_default_na=False)
print(len(df))  # 100
print(df[df["category"] == "Coding"][["name", "source_url"]])
```

JavaScript (Node 18+):

```js
import { readFile } from "node:fs/promises";

const { evals } = JSON.parse(await readFile("data/evals.json", "utf8"));
console.log(evals.length); // 100
```

Both snippets are in `examples/` (`python3 examples/load.py`, `node examples/load.mjs`). They were run against these files on 26 Oct 2026 and printed 100 rows.

## Licence

The dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), and the full legal code is in `LICENSE`. Credit "Evals Review (https://evalsreview.com/data)" when you reuse it. Each linked eval keeps its own licence, given in the `license` column where stated.

## Cite

```bibtex
@misc{evalsreview_llm_evals_dataset_2026,
  author       = {{Evals Review}},
  title        = {LLM Evals Dataset},
  year         = {2026},
  howpublished = {\url{https://evalsreview.com/state-of-llm-evals}},
  note         = {CC BY 4.0}
}
```

You can also use `CITATION.cff`, which GitHub's "Cite this repository" button reads.

---

Maintained by Evals Review. Homepage: [evalsreview.com](https://evalsreview.com). Report and citation: [State of LLM Evals](https://evalsreview.com/state-of-llm-evals).
