#An iterator is an object that can be iterated upon (looped through). It implements two methods:

#__iter__() - Returns the iterator object itself.
#__next__() - Returns the next value from the iterator.


#Creating an Iterator:
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.end:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration


#Using the Iterator:
my_iter = MyIterator(1, 5)
for number in my_iter:
    print(number)


#The StopIteration Exception: When there are no more items left to return, the StopIteration exception is raised, signaling the end of the iteration.
my_iter = MyIterator(1, 3)
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
while True:
    try:
        print(next(my_iter))  # Raises StopIteration
    except StopIteration:
        break

#Iterating over an Iterable Object: Any object that implements the __iter__() method is considered an iterable (e.g., lists, tuples, dictionaries, strings).
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
print(next(my_iter))  # 1
print(next(my_iter))  # 2


#Using for Loop with Iterators: The for loop automatically calls the __next__() method to iterate over the iterator.
my_iter = iter([10, 20, 30, 40])
for item in my_iter:
    print(item)


#Built-in Iterators: Python has built-in iterators like range(), which returns an iterator that iterates over a sequence of numbers.
for i in range(5):  # range is an iterator
    print(i)


'''
Iterators are objects that allow iteration over a sequence.
Iterators implement __iter__() and __next__() methods.
The StopIteration exception is raised when there are no more items to iterate.
Built-in objects like lists and ranges are iterable and can be used with a for loop. 
'''