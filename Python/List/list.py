moterbike=['Honda', 'yamaha','suzuki'];
print(moterbike)
moterbike[0]='ducati';
print(moterbike)

#append used to add the value at last without replacing like .push in js
moterbike.append('honda')
print(moterbike)

#insert item in spesific index
moterbike.insert(2,'TVS')
print(moterbike)


#remove to relete
moterbike.remove('honda')
print(moterbike)

#pop item deleting indecating by the index
moterbike.pop(3)
print(moterbike)

#clear to delete all
moterbike.clear()
print(moterbike)




