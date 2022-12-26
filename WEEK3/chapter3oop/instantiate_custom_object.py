class MyFirstClass:
    print("Who wrote this?")
    index = "Author-Book"
    
    def hand_list(self, philosopher , book, year):
        print(MyFirstClass.index)
        print(str(philosopher) + "wrote the book" + str(book) + " in the year " + year)
        
        
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War", "5th century BC")


