# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the 
# code that you submit.  Do not use break or continue statements.


def clean_message(message):
    """(str) -> str
    
    Return message_copy that includes only alphabetical characters in message,
    where each of those characters has been converted to uppercase.
        
    >>>clean_message('ABc123')
    'ABC'
    >>>clean_message('asdasd33432434')
    'ASDASD'
    """    
    message_copy=''
    for char in message:
        if char.isalpha()==True:
            message_copy += char.upper()
    return message_copy

def encrypt_letter(letter,Keystream_value):
    """(str,int) -> str
    
    Return the encrypted result by applying the Keystream_value to the letter

    >>>encrypt_letter('A',3)
    'D'   
    >>>encrypt_letter('X',4)
    'B'
    """   
    if (ord(letter) + Keystream_value) > 91:
        return chr(ord(letter) + Keystream_value - 26)
    else:
        return chr(ord(letter) + Keystream_value)

def decrypt_letter(letter,Keystream_value):
    """(str,int) -> str
    
    Return the decrypted result by applying the Keystream_value to the letter
    
    >>>decrypt_letter('A',4)
    'W'
    >>>decrypt_letter('E',3)    
    """
    'B' 
    if (ord(letter) - Keystream_value)<65:
        return chr(ord(letter) - Keystream_value + 26)
    else:
        return chr(ord(letter) - Keystream_value)

def swap_cards(deck_of_cards,index):
    """(list of int, int) -> NoneType
        
    precondition:index<len(deck_of_cards)        
    
    Swap the card at the index with the card that follows it in the given deck,
    deck_of_cards. Treat the deck as circular: if the card at the index is on 
    the bottom of the deck, swap that card with the top card.    
    
    >>>a=[1,2,3,4,5]
    >>>swap_cards(a,1)
    >>>a
    [1,3,2,4,5]
    
    >>>a=[1,2,4,3,5,6]
    >>>swap_cards(a,2)
    >>>a
    [1, 2, 3, 4, 5, 6]
    """
    if index==(len(deck_of_cards)-1):
        temp1 = deck_of_cards[0]
        deck_of_cards[0]=deck_of_cards[index]
        deck_of_cards[index]= temp1
    else:
        temp2 =deck_of_cards[index+1]
        deck_of_cards[index+1]= deck_of_cards[index]
        deck_of_cards[index]= temp2

def get_small_joker_value(deck_of_cards):
    """(list of int) -> int    
    
    Return the value of the small joker from the given deck_of_cards
    
    >>>get_small_joker_value([1,2,3,4,5,6])
    5
    >>>get_small_joker_value([1,7,2,6,3,5,4])
    6
    """
    deck_without_big_joker=[]
    for item in deck_of_cards:
        if item != max(deck_of_cards):
            deck_without_big_joker.append(item)
    return max(deck_without_big_joker)

def get_big_joker_value(deck_of_cards):
    """(list of int) -> int
    
    Return the value of the small joker from the given deck_of_cards 
    
    >>>get_big_joker_value([1,2,3,4,5,6])
    6
    >>>get_big_joker_value([1,7,2,6,3,5,4])
    7    
    """
    return max(deck_of_cards)

def move_small_joker(deck_of_cards):
    """(list of int) -> NoneType
    
    Swap the small joker in the given deck_of_cards with 
    the card that follows it, Treat the deck as circular
    
    >>>a=[1,2,3,4,5,6]
    >>>move_small_joker(a)
    >>>a
    [1, 2, 3, 4, 6, 5]
    
    >>>a=([1,7,2,6,3,5,4])
    >>>move_small_joker(a)
    >>>a
    [1, 7, 2, 3, 6, 5, 4]
        
    """
    small_joker_index=deck_of_cards.index(get_small_joker_value(deck_of_cards))    
    swap_cards(deck_of_cards,small_joker_index)    

def move_big_joker(deck_of_cards):
    """(list of int) -> NoneType
    
    Move the big joker two cards down in the given deck_of_cards. 
    Treat the deck as circular. 
    
    >>>a=[1,2,3,4,5,6]
    >>>move_big_joker(a)
    >>>a
    [1, 6, 2, 3, 4, 5]
    
    >>>a=([1,7,2,6,3,5,4])
    >>>move_big_joker(a)
    >>>a
    [1, 2, 6, 7, 3, 5, 4]
        
    """
    big_joker_value=get_big_joker_value(deck_of_cards)   
    big_joker_index=deck_of_cards.index(big_joker_value)         
    
    if big_joker_index==len(deck_of_cards)-1:
        index=1      
    elif big_joker_index==len(deck_of_cards)-2:
        index=0
    else:
        index=big_joker_index+2               
    
    deck_of_cards.remove(big_joker_value)        
    deck_of_cards.insert(index,big_joker_value)         

def triple_cut(deck_of_cards):
    """(list of int) -> NoneType
        
    Call the joker closest to the top of the deck the first joker, 
    and the one closest to the bottom the second joker. 
    Swap the stack of cards above the first joker 
    with the stack of cards below the second joker in the given deck_of_cards   

    >>>a=([1,7,2,6,3,5,4])
    >>>triple_cut(a)
    >>>a
    [3, 5, 4, 7, 2, 6, 1]
    
    >>>a=[1,2,3,4,5,6]
    >>>triple_cut(a)
    >>>a
    [5, 6, 1, 2, 3, 4]
    
    """
    big_joker_index = deck_of_cards.index(get_small_joker_value(deck_of_cards))
    small_joker_index = deck_of_cards.index(get_big_joker_value(deck_of_cards))
    
    first_joker = min(small_joker_index,big_joker_index)   
    second_joker = max(big_joker_index,small_joker_index)
        
    deck_above_first_joker = deck_of_cards[0:first_joker]   
    deck_below_second_joker = deck_of_cards[second_joker+1:]    
    
    deck_of_cards[second_joker+1:] = deck_above_first_joker
    deck_of_cards[0:first_joker] = deck_below_second_joker
    
def insert_top_to_bottom(deck_of_cards):
    """(list of int) -> NoneType
    
    In the given deck_of_cards v represents the value of the bottom card
    If the bottom card is the big joker, 
    take v to be the value of the small joker instead.  
    Take the group of v cards from the top of the deck, 
    and insert the group above the bottom card in the deck. 
    
    >>>a=[1,7,2,6,3,5,4]
    >>>insert_top_to_bottom(a)
    >>>a
    [3, 5, 1, 7, 2, 6, 4]
     
    >>>a=[1,2,3,4,5,6]
    >>>insert_top_to_bottom(a)
    >>>a
    [1, 2, 3, 4, 5, 6]
    
    """    
    if deck_of_cards[-1] == get_big_joker_value(deck_of_cards):
        v = get_small_joker_value(deck_of_cards)
    else:
        v = deck_of_cards[-1]
    
    temp = deck_of_cards[0:v]
    for i in range(v):
        deck_of_cards.remove(deck_of_cards[0])
        deck_of_cards.insert(-1,temp[i])
        
def get_card_at_top_index(deck_of_cards):
    """(list of int) -> int
    
    Return the card at the index of the equal value of the first card  
    in the given deck_of_cards    
    
    >>>get_card_at_top_index([1,7,2,6,3,5,4])
    7
    
    >>>get_card_at_top_index([5,6,1,2,3,4])
    4
    
    """
    big_joker_value = get_big_joker_value(deck_of_cards)
    small_joker_value = get_small_joker_value(deck_of_cards)
    if deck_of_cards[0] == big_joker_value:
        top_card_index =  small_joker_value
       
    else:
        top_card_index = deck_of_cards[0]
    
    return deck_of_cards[top_card_index]

def get_next_keystream_value(deck_of_cards):
    """(list of int) -> int

    Return the key_stream by repeating all five steps of the algorithm untill
    the key_stream value is not equal to the jokers in the given deck_of_cards
    
    >>>get_next_keystream_value([1,2,3,4,5,6])
    2
    
    >>>get_next_keystream_value([5,6,1,2,3,4])
    4        
    
    """
    small_joker_value=get_small_joker_value(deck_of_cards)
    big_joker_value=get_big_joker_value(deck_of_cards)
    key_stream=big_joker_value 
    
    while key_stream == big_joker_value or key_stream == small_joker_value:
        move_small_joker(deck_of_cards)
        move_big_joker(deck_of_cards)
        triple_cut(deck_of_cards)
        insert_top_to_bottom(deck_of_cards)
        key_stream = get_card_at_top_index(deck_of_cards)
    return key_stream
    

def process_messages(deck_of_cards,list_of_message,command):
    """(list of int, list of str, str) -> list of str
    
    Return encrypted or decrypted list_of_message,by the command,
    in the same order as they appear in the given list_of_message, by applying
    to deck_of_cards.   
    
    >>>process_messages([1,2,3,4,5,6],['a','b','c','d','e','f'],'e')
    'IJKLMN'
    
    >>>process_messages([2,1,3,4,5,6],['c','b','d','a','f','e'],'e')
    'LKMJON'
    
    """
    clean_message(list_of_message)   
    message_processed=''    
    if command == 'e':
        for item in list_of_message:
            key_stream=get_next_keystream_value(deck_of_cards)
            message_processed=message_processed+encrypt_letter(item,key_stream)
        return message_processed
                        
    elif command == 'd':
        for item in list_of_message:
            key_stream=get_next_keystream_value(deck_of_cards)
            message_processed=message_processed+decrypt_letter(item,key_stream)
        return message_processed

def read_messages(file):
    """(file open for reading) -> list of str
    
    Return the contents of the file as a list of messages, 
    in the order in which they appear in the file.
    Strip the newline from each line.
     
    """
    file_to_read=[]
    file_list = file.readfiles()  
    for i in range(len(a)):
        file_to_read.append(file_list[i].strip())
    return file_to_read
    

def is_valid_deck(deck_of_cards):
    """(list of int) -> bool
    
     Return True iff deck_of_cards is a valid deck
     
     >>>is_valid_deck([1,2,3,4,5,6])
     True
     >>>is_valid_deck([1,2,3,4,5,5])
     False
     
     """   
    deck_of_cards.sort()
    valid_deck=[]
    for i in range(1,len (deck_of_cards)+1):
        valid_deck.append(i)
    return deck_of_cards==valid_deck
                            
def read_deck(file):
    """(file open for reading) -> list of int
   
    Return the numbers that are in the file, 
    in the order in which they appear in the file.    
    
    """
    deck_list=read_messages(file)
    numbers_in_file = []
    for item in deck_list:
        list_of_number=item.split()
        for item in list_of_number:
            numbers_in_file.append(int(item))
        return numbers_in_file