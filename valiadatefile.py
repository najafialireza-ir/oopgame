class File:
    def __init__(self, path:str) -> None:
        self.path = path

    
    def __write(self, data:str):
        """write word in file
        """
        if data != None:
            f = open(self.path, 'a')
            f.write(data)
            print("Done Succesfully.")
        
        
            
    def __readlines(self):
        """counting line"""
        try:
            f = open(self.path, 'r')
            content = f.readlines()
            line_n = 0
            for i in content:
                line_n += 1
                
            print("lines:",line_n)
        
        except FileNotFoundError:
            print(f"{self.content} Not Found!")
            
            
    def __word_count(self):
        """counting word
        """
        f = open(self.path, 'r')
        content = f.read() 
        total = len(content.split())
        print(f"total word is=>{total}")
        
        
    def __pagecount(self):
        """counting pages
        """
        f = open(self.path, 'r')
        content = f.read()
        _split = content.split(" ")
        total = len(_split)
        
        per_page = 100
        
        pages = total // per_page
        if total % per_page > 0:
            pages += 1
        
        print(f"Page Count=>{pages}")    
        
    
    def main(self):
        """if users call this func
        their can receive file information
        1.read file
        2.readline
        3.word count
        4.page count
        5.Exit
        """
        while True:
            data = int(input("1.Write\n2.ReadLine\n3.WordCount\n4.PageCount\n5.Exit\n=>"))
            if data == 1:
                _data = input("Enter a word for write: ")
                self.__write(_data)
                """ if users want continue must enter a zero number.
                """
                d = int(input("If you Continue Enter 0 or Exit Enter 1: "))
                if d == 0:
                    self.main
                else:
                    break    
                
            elif data == 2:
                self.__readlines()
                d = int(input("If you Continue Enter 0 or Exit Enter 1: "))
                if d == 0:
                    self.main
                else:
                    break    
                
            elif data == 3:
                self.__word_count()
                d = int(input("If you Continue Enter 0 or Exit Enter 1: "))
                if d == 0:
                    self.main
                else:
                    break   
                
            elif data == 4:
                self.__pagecount()
                d = int(input("If you Continue Enter 0 or Exit Enter 1: "))
                if d == 0:
                    self.main
                else:
                    break    
                
            elif data == 5:
                break
            
            else:
                print("something is wrong!")



f = File("./test.txt")

f.main()