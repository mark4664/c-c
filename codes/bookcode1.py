# Book code
# mgb
# 28/11/21

# Experiment at basic encryption

import random

code='z1the2Owl3and4the5pussycat6went7to8sea9in0azbeautiful0pea1green2boat3they4took5some6honey7and8plenty9ofzmoneywrappediupsinxa7fivepoundnnoteltheoowlplookedkuputozthewstars6above5nd7sang8to9a0small1guitar2lovely3ussy4ussy5my6lovezhatxabeautifulxyzussyouareussysaidtothezxywlouxelegantfowlowcharminglysweetyousingletusbemarriedtoolongwehavetarriedutwhatshallwedoforaringheysailedawayorayearandadayqwhkfothelandwheretheongreegrowsndthereinawoodaiggywigstooditharingattheendofhisnoseisnoseisnoseitharingattheendofhisnoseearigareouwillingtosellforoneshillingourringaid theiggyqwillotheytookitawayandweremarriednextdayytheurkeywholivesonthehillheydinedonminceandslicesofquincehichtheyatewithaunciblespoonndhand inhandontheedgeofthesandheydancedbythelightofthemoon'

#code='0the1quick2brown3fox4jumps5over6the7lazy8dog99the8quick7brown6fox5jumps5over4the3lazy2dog1'
len_code=len(code)
print(len_code)


word_to_encode=input('word to be encoded ')

inital_start=(random.randint(0,3)*100)+(random.randint(0,99))
start=inital_start
print('start ',start)
encoded_word=[str(start)]
for letter in word_to_encode:
    #print('start ',start)
    index=code.find(letter,start)
    if index==-1:
        start=inital_start
        index=code.find(letter,start)
    else:
        start=(start+index)%len(code)
    #print ('index ',index,' letter ',letter)
    encoded_word.append(str(index))
    
print(encoded_word)


# Decode

d_start=int(encoded_word[0])
d_word=''
print(d_start)
for d_index in encoded_word:
    d_index=int(d_index)
    d_word+=code[d_index]
    
print(d_word)
    




