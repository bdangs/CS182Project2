from transformers import GPT2LMHeadModel
from transformers import GPT2Tokenizer

xmlGenerator = GPT2LMHeadModel.from_pretrained("gpt2")

tokens = GPT2Tokenizer.from_pretrained("gpt2")

xmlGenerator.eval()

xmlInput = "example.xml"  # input file

with open(xmlInput, "r", encoding="utf-8") as file:  # reads input xml file
    inputFile = file.read()

# we would put our prompt statements here for gpt2 to use. Need 5. Could probably create a loop to make code easier
# not sure if this is how the prompt is supposed to be
prompt1 = "Please generate an xml file based on animals like the xml file provided."
# prompt2
# prompt3
# prompt4
# prompt5

input = prompt1 + inputFile  # combine prompt wth example
# seems to be some sort of error here on line 25
xmlFile = xmlGenerator.generate(tokens.encode(input))
output = tokens.decode(xmlFile)

outputFile = "xmlFile1.xml"  # for first prompt
with open(outputFile, "w") as file:
    file.write(output)
