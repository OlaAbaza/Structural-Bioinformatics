from itertools import cycle, islice
WMap= {
'G': 57,
'A': 71,
'S': 87,
'P': 97,
'V': 99,
'T': 101,
'C': 103,
'I': 113,
'L': 113,
'N': 114,
'D': 115,
'K': 128,
'Q': 128,
'E': 129,
'M': 131,
'H': 137,
'F': 147,
'R': 156,
'Y': 163,
'W': 186, }
AA_WMap= {
'57':'G',
'71':'A',
'87':'S',
'97':'P',
'99':'V',
'101':'T',
'103':'C',
'113':'I',
'113':'L',
'114':'N',
'115':'D',
'128':'K',
'128':'Q',
'129':'E',
'131':'M',
'137':'H',
'147':'F',
'156':'R',
'163':'Y',
'186':'W', }
def theoretical_spectrum():
    print("enter the peptide:")
    p=input()
    peptide=[]
    for i in range(0,len(p),1):
        peptide.append(WMap[p[i]])
                    
    spectrum = []
    for num in range(1, len(peptide)):
        for start in range(len(peptide)):
            group = islice(cycle(peptide), start, start + num)
            spectrum.append(sum(group))
    spectrum.append(sum(peptide)) 
    spectrum.append(0)
    spectrum.sort()
    print(spectrum);
def Cyclopeptide_sequencing():
    print("enter the Spectrum :")
    spe=input()
    Spectrum=spe.split()
    one_mers=[]
    two_mers=[]
    three_mers=[]
    four_mers=[]
    five_mers=[]
    num_two=[] #spectrum of 2-mers
    num_three=[]#spectrum of 3-mers
    num_four=[]#spectrum of 4-mers
    num_five=[]#spectrum of 5-mers
#-------------calc 1-mers------------
    for number in Spectrum:
        if number in AA_WMap.keys():
            if AA_WMap[number] not in one_mers:
               one_mers.append(AA_WMap[number])
    spe=[int(i)for i in Spectrum]
    print(one_mers)
#-------------calc 2-mers------------
    for latter in one_mers:
       for l in one_mers:
           if(latter!=l):
               x=WMap[latter]+WMap[l]
               if x in spe:
                  num_two.append(x)
                  s=latter+l
                  two_mers.append(s)

    print(two_mers)
    print(num_two)
#-------------calc 3-mers------------
    i=0
    for latter in two_mers:
      for l in one_mers:
          s=latter[1]+l
          if s in two_mers:
             x=num_two[i]+WMap[l]
             if x in spe:
                num_three.append(x)
                s=latter+l
                three_mers.append(s)
      i=i+1
    print(three_mers)
    print(num_three)
    #-------------calc 4-mers------------
    i=0
    for latter in three_mers:
      for l in one_mers:
          s=latter[2]+l
          f=latter[1]+latter[2]+l
          if s in two_mers:
              if f in three_mers:
                x=num_three[i]+WMap[l]
                if x in spe:
                  num_four.append(x)
                  s=latter+l
                  four_mers.append(s)
      i=i+1  
    print(four_mers)
    print(num_four)
    #-------------calc 5-mers------------
    i=0
    for latter in four_mers:
      for l in one_mers:
          s=latter[3]+l
          f=latter[2]+latter[3]+l
          h=latter[1]+latter[2]+latter[3]+l
          if s in two_mers:
              if f in three_mers:
                  if h in four_mers:
                    x=num_four[i]+WMap[l]
                    if x in spe:
                      num_five.append(x)
                      s=latter+l
                      five_mers.append(s)
      i=i+1  
    print(five_mers)
    print(num_five)

#-----------main---------
print("Enter 1 to Generate the theoretical spectrum of a cyclic peptide")
print("Enter 2 to Cyclopeptide sequencing. ")
ch=input()
if ch=='1':
  theoretical_spectrum()
else :
    Cyclopeptide_sequencing() 
    
