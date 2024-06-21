from easyeditor import ROMEHyperParams, MEMITHyperParams, MENDHyperParams, FTHyperParams
from easyeditor import BaseEditor

hparams = ROMEHyperParams.from_hparams('./hparams/ROME/llama-7b')

prompts = [
            "The profession of Arun Nehru is",
            ]
ground_truth = [
                "politician",
                ]
target_new = [
              "actor",
              ]
subject = [
            "Arun Nehru",
            ]
rephrase_prompt = [
            "Arun Nehru is known for",
            ]
locality_prompt = [
            "George Washington's profession is a",
            ]
locality_ground_truth = [
            "politician"
            ]

locality_inputs = {
    'neighborhood':{
        'prompt': locality_prompt,
        'ground_truth': locality_ground_truth
    },
}

editor = BaseEditor.from_hparams(hparams)

metrics, edited_model, _ = editor.edit(
    prompts=prompts,
    target_new=target_new,
    rephrase_prompts=rephrase_prompt,
    locality_inputs=locality_inputs,
    subject=subject,
    keep_original_weight=True
)
