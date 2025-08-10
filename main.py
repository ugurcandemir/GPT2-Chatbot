import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load gpt2 model
model_name = 'gpt2'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, output_hidden_states=True)

# Function to generate text
def gpt2_generate_text(text):
    input = tokenizer.encode(text, return_tensors="pt")
    output = model.generate(
    input, 
    max_length=100, 
    do_sample=True, 
    temperature=0.1,  
    top_k=50,         
    pad_token_id=tokenizer.eos_token_id
)

    return tokenizer.decode(output[0], skip_special_tokens=True)


ui = gr.Interface(
    fn=gpt2_generate_text,
    inputs="text",  
    outputs="text",  
    title="GPT-2 Chatbot",
    description="Anything you wanna talk about? Give it a try and type whatever you want!"
)

ui.launch()

