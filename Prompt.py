from transformers import GPT2LMHeadModel
from transformers import GPT2Tokenizer
import torch

xmlModel = GPT2LMHeadModel.from_pretrained("gpt2")

xmlTokenizer = GPT2Tokenizer.from_pretrained("gpt2")

xmlModel.eval()

xmlInput = "example.xml"  # input file

with open(xmlInput, "r") as file:  # reads input xml file
    inputFile = file.read()

# we would put our prompt statements here for gpt2 to use. Need 5. Could probably create a loop to make code easier
# not sure if this is how the prompt is supposed to be
prompt1 = "Here is an exammple xml file:\n" + \
    inputFile + "\n Please generate another xml file"
# prompt2
# prompt3
# prompt4
# prompt5

# input = prompt1 + inputFile  # combine prompt wth example
input = prompt1
encoded_input = xmlTokenizer.encode(input, return_tensors="pt")
output = xmlModel.generate(encoded_input, max_length=1000, do_sample=True,
                           temperature=1.0, top_k=45, top_p=0.75, pad_token_id=xmlTokenizer.eos_token_id)

xmlText = xmlTokenizer.decode(output[0], skip_special_tokens=True)

outputFile = "xmlFile1.xml"  # for first prompt
with open(outputFile, "w") as file:
    file.write(xmlText)
