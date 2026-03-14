from transformers import AutoModelForCausalLM
from peft import LoraConfig, get_peft_model
print("Setting up LoRA...")