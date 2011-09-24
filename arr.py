# arr.py (C) 2011 Matoe Productions LLC.

msg = 'this-item-should-not-be-inserted-into-you-list-else-this-will-fail-because-it-is-only-for-pyarr-kthxbai-theiostream'

def checkIfReal(a):
	a.append(msg)
	if a[0]==msg:
		a.remove(msg)
		return 0
	
	a.remove(msg)
	return 1
	
def checkIfThereIsIndex(list, index):	
	list.append(msg)
	
	if list.index(msg)>index:
		list.remove(msg)
		return 1
		
	return 0
	
	