string=input()
dna_rna={'G':'C', 'C':'G', 'T':'A', 'A':'U' }
newstring=''
for i in string:
    if i not in str(dna_rna.keys()) or i.isalpha()==False:
        print("Invalid Input")
        break
    else:
        newstring=newstring+dna_rna[i]
if len(newstring)==len(string):
    print(newstring)
