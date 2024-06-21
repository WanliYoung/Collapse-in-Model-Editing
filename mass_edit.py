from easyeditor import ROMEHyperParams, BaseEditor, MEMITHyperParams, MENDHyperParams, FTHyperParams
import json

# Load from datasets
test_data = json.load(open("./data/CounterFact/counterfact-val.json", 'r', encoding='utf-8'))

# Process data
prompts = [test_data_["prompt"] for test_data_ in test_data]  
target_new = [test_data_["target_new"] for test_data_ in test_data]  
subject = [test_data_["subject"] for test_data_ in test_data]
rephrase_prompts = [edit_data_["rephrase_prompt"] for edit_data_ in test_data]
locality_prompts = [edit_data_["locality_prompt"] for edit_data_ in test_data]
locality_ans = [edit_data_["locality_ground_truth"] for edit_data_ in test_data]

locality_inputs = {
    'neighborhood':{
        'prompt': locality_prompts,
        'ground_truth': locality_ans
    },
}

hparams = ROMEHyperParams.from_hparams('./hparams/ROME/gpt-j-6B')  
editor = BaseEditor.from_hparams(hparams)

metrics, edited_model, _ = editor.edit(
    prompts=prompts,
    target_new=target_new,
    rephrase_prompts=rephrase_prompts,
    locality_inputs=locality_inputs,
    subject=subject,
    keep_original_weight=False # True for single editing; False for sequential editing
)

# json.dump(metrics, open("./results.json", 'w'), indent=4)
