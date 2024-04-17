from random import randint, choice


class Game:
    def __init__(self):
        self.playerdict = {}
    
    
    def __Mulitplayer(self, _input:int, player1:str, player2:str, rnd1:int, rnd2:int):  
      
        if _input == 1:
            if rnd1 > rnd2:
                print(f"{player1} won : {rnd1}")
            elif rnd2 > rnd1:
                print(f"{player2} won :{rnd2}")
            else:
                print("game is equal")            
                        
            print(f"{player1} : {rnd1}")
            print(f"{player2} : {rnd2}")
            
        # multiplay seke    
        if _input == 2:
            print(f"{player1} : {rnd1}")
            print(f"{player2} : {rnd2}") 
            
                
            if rnd1 == ['shir']:
                print(f"player1: {player1},won: {rnd1}")
            else:
                print(f"player1: {player1},loser: {rnd1}")
            if rnd2 == ['khat']: 
                print(f"player2: {player2},loser: {rnd2}")
            else:
                print(f"player2: {player2} won: {rnd2}")    
            
            
    def __singelplayer(self, _input:int, rnd1):
        if _input == 1:
            print(f"Number Tas is: {rnd1}")
            
        elif _input == 0:
            print(f"Seke: {rnd1}")
               
            
        
    def __tas(self):
        rnd1 = randint(1, 6) 
        rnd2 = randint(1, 6) 
                
        return (rnd1, rnd2)
        
        
    def __seke(self):
        
        p1 = choice(["shir", "khat"])
            
        return (p1)
        
    
    def start(self):
        while True:
            data = int(input("1 is tas, 2 is seke, 3 to exit: "))
            
            if data == 1:
                print("Tas Game!")
                _input = int(input("1 Mlitiplayer Tas, 2 Miltiplayer Seke: "))
                
                if _input == 1:
                    print("Multiplayer Tas On!")
                    
                    if self.playerdict.get('player1') is not None:
                        player1 = self.playerdict['player1']
                    else:
                        player1 = input("playe1 Enter your name: ")
                        self.playerdict['player1'] = player1
                        while player1 == "":
                            player1 = input("playe1 Enter your name: ")
                            self.playerdict['player1'] = player1
                            
                        
                    if self.playerdict.get('player2') is not None:
                        player2 = self.playerdict['player2']
                    else:
                        player2 = input("playe2 Enter your name: ")
                        self.playerdict['player2'] = player2
                        while player2 == "":
                            player2 = input("playe2 Enter your name: ")
                            self.playerdict['player2'] = player2
                            
                    
                    
                    self.__Mulitplayer(int(_input), player1, player2, *self.__tas())
                        
                elif _input == 2:
                    print("Single Tas On!")
                    self.__singelplayer(int(_input), self.__tas()[0])

        
            
            elif data == 2:
                print("Multiplayer Seke Game!")
                _input = int(input("1 Mlitiplayer, 2 Singleplayer: "))
                
                if self.playerdict.get('player1') is not None:
                            player1 = self.playerdict['player1']
                else:
                            player1 = input("playe1 Enter your name: ")
                            self.playerdict['player1'] = player1
                            while player1 == "":
                                player1 = input("playe1 Enter your name: ")
                                self.playerdict['player1'] = player1
                                
                            
                if self.playerdict.get('player2') is not None:
                            player2 = self.playerdict['player2']
                else:
                            player2 = input("playe2 Enter your name: ")
                            self.playerdict['player2'] = player2
                            while player2 == "":
                                player2 = input("playe2 Enter your name: ")
                                self.playerdict['player2'] = player2
                                
                        
                rnd2 = input("player2 shir ya Khat: ")
                    
                self.__Mulitplayer(int(_input), player1, player2, self.__seke(), rnd2)
                
            elif _input == 0:
                    print("singelplayer seke on")
                    self.__singelplayer(int(_input), self.__seke()[0])
            
            
            elif data == 3:
                break
            
            
            
g = Game()
g.start()

  
    