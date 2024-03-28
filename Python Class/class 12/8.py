#add elements from 2nd set to 1st set
thisset={"apple","banana","cherry"}
tropical={"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)
tropical.update(thisset)
print(tropical)