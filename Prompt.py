from transformers import GPT2LMHeadModel
from transformers import GPT2Tokenizer
import torch

xmlModel = GPT2LMHeadModel.from_pretrained("gpt2")

xmlTokenizer = GPT2Tokenizer.from_pretrained("gpt2")

xmlModel.eval()

xmlInput = "newExample1.xml"  # input file

with open(xmlInput, "r", encoding="utf-8") as file:  # reads input xml file
    inputFile = file.read()

# we would put our prompt statements here for gpt2 to use. Need 5. Could probably create a loop to make code easier
# not sure if this is how the prompt is supposed to be
prompt1 = "Make an xml file"
# prompt1 = "Here is an example xml file. Please generate another one <sample-xml> \n" + inputFile
# prompt2 = "Here is an example xml file. Please make a new xml file with a different instructor and a different time \n" + inputFile
# prompt3 = "Here is an example xml file. Please make #a new xml file with a different instructor named 'John Smith' instead of 'Qian Zhang' and a different time\n" + inputFile
# prompt4 = "Here is an example xml file about letters that are dirty and clean. Generate a new xml file with numbers between <dirty> and </dirty> \n" + inputFile
# prompt5 = "Here is an example xml file. It has XML tags and XML elements. XML tags have an opening <xml tag> and a closing </xml tag> All XML elements are between the opening <xml tag> and the closing </xml tag>. Please generate a new XMl file that follows these rules. \n" + inputFile


encoded_input = xmlTokenizer.encode(prompt1, return_tensors="pt")

# output = xmlModel.generate(encoded_input, max_length=500, num_beams=5, early_stopping=True,
# temperature=0.6, top_k=15, top_p=0.45, pad_token_id=xmlTokenizer.eos_token_id)

output = xmlModel.generate(encoded_input, max_length=700, do_sample=True,
                           temperature=1.0, top_k=50, top_p=0.95, pad_token_id=xmlTokenizer.eos_token_id)

xmlText = xmlTokenizer.decode(output[0], skip_special_tokens=True)

outputFile = "xmlFile1.xml"  # for first prompt
with open(outputFile, "w") as file:
    file.write(xmlText)
