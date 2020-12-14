import random
tagList = ["NC", "NP", "VB"]

newf=""

def nonblank_lines(f):
    for l in f:
            line = l.rstrip()
            if line:
                    yield line

with open('LUGANDA_EVALUATING_CORPUS.words','r') as f_in:

    for line in nonblank_lines(f_in):
        newf+=line.strip() + "\t" + random.choice(tagList) +"\n"
    f_in.close()

with open('LUGANDA_EVALUATING_CORPUS.words','w') as f:
    f.write(newf)
    f.close()

output = open("LUGANDA_EVALUATING_CORPUS.words", "r")
print(output.read())