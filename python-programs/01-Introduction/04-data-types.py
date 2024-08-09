"""
Text Type:	        str
Numeric Types:  	int, float, complex
Sequence Types:	    list, tuple, range
Mapping Type:   	dict
Set Types:  	    set, frozenset
Boolean Type:   	bool
Binary Types:   	bytes, bytearray, memoryview
None Type:	        NoneType

"""

stringData = "Rambabu Patidar"
integerData = 100
floatData = 1.324224
complexData = 1 + 3j

listData = [1, 2, 3, 4, 5]
listData2 = list((1, 2, 3, 4))  # require an iterable

tupleData = (1, 2, 3, 4, "Rambabu")
tupleData2 = tuple((1, 2, 3, 4, 5))  # require and iterable

rangeData1 = range(5, 15)  # [5, 15)
rangeData2 = range(15)  # [0, 15)
rangeData3 = range(1, 15, 3)  # [5, 15) but with increament of 3

setData2 = set((1, 2, 3, 4, 5, 6))  # require an iterable
setData = {1, 2, 3, 4}

dictData = {"name": "Ram", "age": "5"}
dictData2 = dict(name="Rambabu", age="5")

boolData = True

# Rest will be on the way of learning path
