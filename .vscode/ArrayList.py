class ArrayList:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else : return None
        
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else: pass
        
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
            return e
        else: pass
        
    def replace(self, pos, e):
        if 0 <= pos < self.size:
            self.array[pos] = e
        else:
            print("Invalid position for replacement.")
            
    def make_dictionary(self):
        word_freq = {}
        
        for i in range(self.size):
            entry = self.getEntry(i)
            words = entry.split()
            
            for word in words:
                word = word.strip(".,!?")
                if word:
                    word_freq[word] = word_freq.get(word, 0) + 1
                    
        for word, freq in word_freq.items():
            print(f"{word}: {freq}")

        with open("C:/Users/이동훈/OneDrive/바탕 화면/test.txt", "w", encoding="UTF-8") as f:
            for word, freq in word_freq.items():
                f.write(f"{word}: {freq}\n")
        
        
    def __str__(self): 
        return str(self.array[0:self.size])    
    





        