import json
import time


class ContactManager:
    def __init__(self, path='-') -> None:
        self.contact_list = []
        
        """user can give dirctions and search
            for the contact from the direction
        """ 
                
                
    def __add(self, name:str, number:int):
        """add name and number contact
        """
        self.contact_list.append({
            "name": name,
            "number":number})
        
        print("Contact save.")
    
    def __search(self, name:str, path='-'):
        result = []
        
        """user can give dirctions and search
            for the contact from the direction
        """     
        if path != '-':
            print("loding...")
            time.sleep(1)   
            f = open(path, 'r')
            self.contact_list = json.loads(f.read())
               
            print(self.contact_list) 
            
        else:
            """search contact if contacts were add
            """
            if self.contact_list is not None:
                for item in self.contact_list:
                    if name.lower() in item['name'].lower():
                        result.append(item)
                        
                print(result)
                
               
        
    def __backup(self):
        """if add contacts this func will backup else show error
        """            
        if self.contact_list is not None:
            f = open('./contact_manager.json', 'w')
            f.write(json.dumps(self.contact_list))
            print("Contacts Save Done.")
        else:
            print("First You Must Add contact and Backup!!")   
            
             
    def __contact_show(self):
        """show contanct list
        """
        if self.contact_list is not None:
            print(self.contact_list)
        
        
        
    def main(self):
        """if call this func users add and save contact json file.
        1.Add Contact
        2.Search Contact 
        3.Backup
        4.Show Contact list
        5.Exit
        """
        while True:
            data = int(input("1.Add Contact\n2.Search Contact\n3.Backup\n4.Show Contact list\n5.Exit\n=> "))
            if data == 1:
                name_input = input("Enter Contact Name: ")
                number_input = int(input("Enter Contact Number: "))
                self.__add(name_input, number_input)
            
            elif data == 2:
                path_input = input("if you have another path please Enter..., else Enter - : ")
                name_input = input("Enter Contact Name for Search: ")
                self.__search(name_input, path_input)
            
            elif data == 3:
                self.__backup()
            
            elif data == 4:
                self.__contact_show()
                
            elif data == 5:
                break
            
    

c = ContactManager()

c.main()