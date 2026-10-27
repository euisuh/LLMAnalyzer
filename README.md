# LLMAnalyzer

Course project (course and term not stated in the repo; commits are from April 2024). Notebooks and helpers for building a small English/Arabic prompt-response dataset from public Hugging Face datasets and scoring LLM responses with GPT-3.5 as a judge.

## What it shows

- `1DataGen.ipynb`: samples 200 prompt/response pairs per source dataset (listed below), machine-translates prompts and responses to Arabic with `deep_translator` (`utils.py`), and collects them in one dataframe.
- `2Eval.ipynb`: queries GPT-3.5 for its own answers (`lmQuery.py`) and asks it to rate each response from 1 to 10 (prompt templates in `lmQuery.py`).
- No results or metrics are reported in this repo; it is the data and evaluation pipeline only.

## How to run

```
pip install pandas datasets deep_translator langdetect tqdm openai==0.28 jupyter
```

Create `config.ini` (git-ignored) with an `[openai]` section containing `api_type`, `api_base`, `api_version`, `api_key`. `lmQuery.py` uses the Azure-style `engine='adversarial'` deployment name; change it to your own. Then run `1DataGen.ipynb` followed by `2Eval.ipynb`. The notebooks read and write CSVs under `assets/`, which is git-ignored, and `2Eval.ipynb` starts from a CSV produced outside this repo (`assets/analyzeDataset1.csv`). I did not re-run the notebooks when tidying this repo (they need paid API access).

## Datasets from Hugging Face

- [Akoksal/LongForm](https://huggingface.co/datasets/Akoksal/LongForm)
- [Mlabonne/alpagasus](https://huggingface.co/datasets/Mlabonne/alpagasus)
- [HuggingFaceH4/Koala-test-set](https://huggingface.co/datasets/HuggingFaceH4/Koala-test-set)
- [HuggingFaceH4/ultrachat_200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k)
- [HuggingFaceH4/mt_bench_prompts](https://huggingface.co/datasets/HuggingFaceH4/mt_bench_prompts)
- [reciprocate/alpaca-eval](https://huggingface.co/datasets/reciprocate/alpaca-eval)
- [natolambert/xstest-v2-copy](https://huggingface.co/datasets/natolambert/xstest-v2-copy)

The resulting dataset is published at [euisuh15/fanar-analyzer](https://huggingface.co/datasets/euisuh15/fanar-analyzer). Thanks to the dataset authors.
