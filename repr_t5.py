from transformers import T5ForConditionalGeneration, T5Tokenizer
from easyeditor.models.rome.compute_v import get_module_input_output_at_word
import json, os
import numpy as np


def replace_first_word(s):
    parts = s.split(' ', 1)
        if len(parts) > 1:
        return "{} " + parts[1]
    else:
        return "{}"

data_path = "./data/counterfact/normal_cases.json"  # load data from your path, collapse cases for first token, normal cases for subsequent tokens
data = json.load(open(data_path, 'r', encoding='utf-8'))

device = "cuda"
model_name = "./hugging_cache/t5-3B"

model = T5ForConditionalGeneration.from_pretrained(model_name)
model.to(device)
tok = T5Tokenizer.from_pretrained(model_name)
layer = 23  

for d in data:
    prompt = d["prompt"]
    subject = d["subject"]
    prompt = prompt.replace(subject, "{}")
    cur_input, cur_output = get_module_input_output_at_word(
        model,
        tok,
        layer,
        context_template=prompt,
        word=subject,
        module_template="encoder.block.{}.layer.1.DenseReluDense.wo",
        fact_token_strategy="subject_last",
    )

    # save key tensor
    key_cpu = cur_input.clone().detach().cpu()
    numpy_key = key_cpu.numpy()
    prefix = 'key'
    directory = "/path/to/save"
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.startswith(prefix) and f.endswith('.npy')]
    numbers = [int(f.replace(prefix, '').replace('.npy', '')) for f in files]
    next_number = 1 if not numbers else max(numbers) + 1
    next_filename = f'{directory}{prefix}{next_number}.npy'
    np.save(next_filename, numpy_key)