# Collapse in Model Editing

This repository hosts the code and data for the following two papers: [🦋🌪️ The Butterfly Effect of Model Editing: Few Edits Can Trigger Large Language Models Collapse](https://aclanthology.org/2024.findings-acl.322/) (ACL 2024 Findings) and [The Fall of ROME: Understanding the Collapse of LLMs in Model Editing](https://arxiv.org/abs/2406.11263) (EMNLP 2024 Findings).

#### Requirements:

- **Environment**: `requirements.txt` (Please use Python 3.9+ for this repository)
- **Large Language Models to Edit**: Download the LLMs you want to edit from [Hugging Face](https://huggingface.co/) and put them in `hugging_cache/`
- **Stats for ROME and MEMIT**: If you want to apply editing algorithms ROME and MEMIT, you can download the stats files required for them from [stats for gpt2 and gptj](https://rome.baulab.info/data/stats/) and [stats for llama2](https://drive.google.com/drive/folders/1IGt7NNV-OxXqIljjr02_k0dDY50Z5N_E), and put the `wikipedia_stats` directory into corresponding local directory, e.g. , `data/stats/._hugging_cache_gpt2-xl/wikipedia_stats`
- **Complete Datasets**: 
  - You can get the ME-PPL, HardCF, and HardEdit datasets from [here](https://drive.google.com/drive/folders/1awv48dbYW5X2t51ebB8yE_4VPE_j8-qs?usp=drive_link) and put them in `data/`
  - You can download the complete ZsRE and COUNTERFACT datasets from [here](https://rome.baulab.info/data/dsets/) and put them in `data/`



## 🦋🌪 The Butterfly Effect of Model Editing: Few Edits Can Trigger Large Language Models Collapse


#### Training-required Method MEND:

For training-required method MEND, you need to run `pretrain_mend.py` to train a hypernetwork/editor before editing. This will obtain a trained hypernetwork and store it in `./results/models/MEND/`.

#### Single Case Editing

If you want to observe the editing effects of a single case, you can modify and execute `single_case_edit.py`.

#### Massive Editing

`mass_edit.py` will load massive requests from datasets to apply editing. 

#### Perplexity Calculation

- Our editing program will calculate and report the perplexity of edited model after each editing process. 
- You can adjust the `ppl_sentence_num` field in the configuration file (e.g., `./hparams/ROME/gpt2-xl.yaml`), to control the number of sentences used for calculating perplexity. 
- You can also apply `ppl.py` to calculate the perplexity of the model you want to evaluate.

#### Evaluation of Downstream Tasks for LLMs

If you want to evaluate the downstream task capabilities for LLMs, please refer to [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness).



## The Fall of ROME: Understanding the Collapse of LLMs in Model Editing

