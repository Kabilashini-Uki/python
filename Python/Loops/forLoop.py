#for loop
moterbike=['Tvs','Bujaj','Yamaha','Honda','Hero','Suzuki','BMW']
for i in moterbike:#looping system 
    print(i)

    #print Letters
    Birds="peacock";
for i in Birds:
    print(i)

    #break
for i in moterbike:
    print(i)
    if i=="Honda":
        break;

#continue
print()
print(moterbike)
for i in moterbike:
    if i=="Honda":
        continue;
    print(i);