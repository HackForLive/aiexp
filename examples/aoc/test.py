from pathlib import Path
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

def mistral_v2():
   mistral_v2_base = '/home/malisha/huggingface/mistral_7B_instruct_v02'
   model = AutoModelForCausalLM.from_pretrained(mistral_v2_base, device_map="auto")
   tokenizer = AutoTokenizer.from_pretrained(mistral_v2_base)
   while True:
      query = input("Enter your prompt: ")
      if query == "0":
        with open(Path('./examples/aoc/2023_1_1_more_targeted.txt'), encoding='utf-8', mode='r') as f:
           query = f.read() 
      
      messages = [
         {"role": "user", "content": str(query)}
      ]
      encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
      generated_ids = model.generate(encodeds, max_new_tokens=300, do_sample=False)
      decoded = tokenizer.batch_decode(generated_ids)
      print("Query: ",query)
      print("Result")
      print(decoded[0])
      # optional break here
      break


def codestral_v1():
   codestral_v1_base = '/home/malisha/huggingface/codestral_7B'
   compute_dtype = getattr(torch, "float8_e4m3fn")
   # bnb_config = BitsAndBytesConfig(
   #    load_in_4bit=True,
   #    bnb_4bit_quant_type="nf4", 
   #    llm_int8_enable_fp32_cpu_offload=True)
   
   device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
   print(device)
   model = AutoModelForCausalLM.from_pretrained(codestral_v1_base, device_map="cpu")#, quantization_config=bnb_config)
   tokenizer = AutoTokenizer.from_pretrained(codestral_v1_base)
   while True:
      query = input("Enter your prompt: ")
      if query == "0":
        with open(Path('./examples/aoc/2023_1_1_more_targeted.txt'), encoding='utf-8', mode='r') as f:
           query = f.read() 
      
      text = query
      inputs = tokenizer(text, return_tensors="pt").to('cpu')

      outputs = model.generate(**inputs, max_new_tokens=300)
      
      for o in outputs:
         print(tokenizer.decode(o, skip_special_tokens=False))
      break
      messages = [
         {"role": "user", "content": str(query)}
      ]
      encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
      generated_ids = model.generate(encodeds, max_new_tokens=300, do_sample=False)
      decoded = tokenizer.batch_decode(generated_ids)
      print("Query: ",query)
      print("Result")
      print(decoded[0])
      # optional break here
      break
   

# mistral_v2()
codestral_v1()