from transformers import GPT2LMHeadModel
from transformers import GPT2Tokenizer
import torch

xmlModel = GPT2LMHeadModel.from_pretrained("gpt2")

xmlTokenizer = GPT2Tokenizer.from_pretrained("gpt2")

xmlModel.eval()

xmlInput = "example.xml"  # input file

with open(xmlInput, "r", encoding="utf-8") as file:  # reads input xml file
    inputFile = file.read()

# we would put our prompt statements here for gpt2 to use. Need 5. Could probably create a loop to make code easier
# not sure if this is how the prompt is supposed to be
prompt1 = "Please generate an xml file based on animals"
# prompt2
# prompt3
# prompt4
# prompt5

input = prompt1  # combine prompt wth example
# seems to be some sort of error here on line 25
encoded_input = xmlTokenizer.encode(input, return_tensors="pt")
# xmlFile = xmlModel.generate(tokenizer.encode(input))
# output = tokenizer.decode(xmlFile)
output = xmlModel.generate(encoded_input, max_length=50,
                           temperature=1.0, top_k=45, pad_token_id=xmlTokenizer.eos_token_id)

xmlText = xmlTokenizer.decode(output[0], skip_special_tokens=True)
# print(xmlText)

outputFile = "xmlFile1.xml"  # for first prompt
with open(outputFile, "w") as file:
    file.write(xmlText)
