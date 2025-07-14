    ###########################################################

    #  Computer Project #10

    #

    #  Solitaire

    #    create a basic game of solitaire by asking

    #       the user to input basic commands

    #    

    ###########################################################
import cards        # this is required

YAY_BANNER = """
__   __             __        ___                       _ _ _ 
\ \ / /_ _ _   _    \ \      / (_)_ __  _ __   ___ _ __| | | |
 \ V / _` | | | |    \ \ /\ / /| | '_ \| '_ \ / _ \ '__| | | |
  | | (_| | |_| |_    \ V  V / | | | | | | | |  __/ |  |_|_|_|
  |_|\__,_|\__, ( )    \_/\_/  |_|_| |_|_| |_|\___|_|  (_|_|_)
           |___/|/                                            

"""

RULES = """
    *------------------------------------------------------*
    *-------------* Thumb and Pouch Solitaire *------------*
    *------------------------------------------------------*
    Foundation: Columns are numbered 1, 2, ..., 4; built 
                up by rank and by suit from Ace to King. 
                You can't move any card from foundation, 
                you can just put in.

    Tableau:    Columns are numbered 1, 2, 3, ..., 7; built 
                down by rank only, but cards can't be laid on 
                one another if they are from the same suit. 
                You can move one or more faced-up cards from 
                one tableau to another. An empty spot can be 
                filled with any card(s) from any tableau or 
                the top card from the waste.
     
     To win, all cards must be in the Foundation.
"""

MENU = """
Game commands:
    TF x y     Move card from Tableau column x to Foundation y.
    TT x y n   Move pile of length n >= 1 from Tableau column x 
                to Tableau column y.
    WF x       Move the top card from the waste to Foundation x                
    WT x       Move the top card from the waste to Tableau column x        
    SW         Draw one card from Stock to Waste
    R          Restart the game with a re-shuffle.
    H          Display this menu of choices
    Q          Quit the game
"""

def valid_fnd_move(src_card, dest_card):
    """
        Determine whether or not a move is valid
    """
    src_card=tab[x-1]
    dest_card=tab[y-1]
    if src_card.suit==dest_card.suit:
        if src_card.rank == dest_card.rank +1:
            True 
    else:
        False
    return

def valid_tab_move(src_card, dest_card):
    """
        Determine whether or not a tableau move is valid
    """    
    if src_card.rank +1 == dest_card.rank:
        if src_card.suit != dest_card.suit:
            True
    else:
        False
    return
            
def tableau_to_foundation(tab, fnd):
    """
        Moves cards from the tableau to the foundation
    """   
    valid_move=valid_fnd_move(src_card,dest_card)
    if valid_move == False:
        print("{:s}\nTry again.")       
    else:
        if card.isfaceup() in tab:
            fnd.append(card)
    return

def tableau_to_tableau(tab1, tab2, n):
    """
        Moves cards from a selected tableau to another tableau
    """   
#    valid_move=valid_tab_move(src_card,dest_card)
#    if valid_move == False:
#        raise RuntimeError       
#    else:
    tab[x].pop()
    tab[y].append(tab[x-1].pop())

def waste_to_foundation(waste, fnd, stock):
    """
        Moves cards from the waste to the foundation
    """   
    card=waste[-1]
    fnd.append(card)
    return 

def waste_to_tableau(waste, tab, stock):
    """
        Moves cards from the waste to the tableau
    """   
    card=waste[-1]
    tab.append(card)
    return
    
def stock_to_waste(stock, waste):
    """
        moves cards form the stock to the waste
    """    
    card=stock[-1]
    stock.deal(card)
    waste.append(card)
    return 
    
def is_winner(foundation):
    """
        YOU WON YAY
    """   
    
    if len(foundation)==52:
        print(YAY_BANNER)
    pass  # stub; delete and replace it with your code

def setup_game():
    """
        The game setup function, it has 4 foundation piles, 7 tableau piles, 
        1 stock and 1 waste pile. All of them are currently empty. This 
        function populates the tableau and the stock pile from a standard 
        card deck. 

        7 Tableau: There will be one card in the first pile, two cards in the 
        second, three in the third, and so on. The top card in each pile is 
        dealt face up, all others are face down. Total 28 cards.

        Stock: All the cards left on the deck (52 - 28 = 24 cards) will go 
        into the stock pile. 

        Waste: Initially, the top card from the stock will be moved into the 
        waste for play. Therefore, the waste will have 1 card and the stock 
        will be left with 23 cards at the initial set-up.

        This function will return a tuple: (foundation, tableau, stock, waste)
    """
    # you must use this deck for the entire game.
    # the stock works best as a 'deck' so initialize it as a 'deck'
    stock = cards.Deck()
    stock.shuffle()
    # the game piles are here, you must use these.
    foundation = [[], [], [], []]           # list of 4 lists
    tableau = [[], [], [], [], [], [], []]  # list of 7 lists
    waste = []                              #one list
    count=0    
    times=0                      
    for i in range (28): 
        onecard=stock.deal()
        tableau[count].append(onecard)
        count+=1
        if count==7:
            times+=1
            count=times  
    for list in tableau:
        for item in list:
            if item is not list[-1]:
                item.flip_card()
        print(list)

    for i in range (1):
        card=stock.deal()
        waste.append(card)


    return foundation, tableau, stock, waste

def display_game(foundation, tableau, stock, waste):
    """
        Created the display setup for the game
    """ 
    print("=================FOUNDATIONS================")
    print(" f1      f2      f3      f4")
    print(foundation)
    print("")
    print("===================TABLEAU==================")
    for item in tab:
        print(item)
    print("")
    print("=================STOCK/WASTE================")
    print("Card in Play:",waste)
    print("")
    print(len(stock))
    print("")
    print(foundation)
    return


once = False
print(RULES)
fnd, tab, stock, waste = setup_game()
display_game(fnd, tab, stock, waste)
print(MENU)
command = input("prompt :> ")
while command.lower() != 'q' or command[0].lower() != 'q':
    listy=[]   
    listy=command[2:]
    x=int(listy[1])
    y=int(listy[3])
    tab1=tab[x]
    tab2=tab[y]
    try:
        if command[:2] == "tf":
            x=int(listy[1])
            y=int(listy[3])
            start=tableau_to_foundation(tab1, fnd[x])
        elif command[:2]=="tt":
            x=int(listy[1])
            y=int(listy[3])
            n=int(listy[5])
            start=tableau_to_tableau(tab1, tab2, n)

        elif command[:2] == "wf":
            x=int(listy[1])
            start=waste_to_foundation(waste, fnd[x], stock)
        elif command[:2] == "wt":
            x=int(listy[1])
            start=waste_to_tableau(waste, tab1, stock)
        elif command [:2] == "sw":
            start=stock_to_waste(stock, waste)
#        elif command[:2] == "r":
#            
        elif command[:2] == "h":
            print(MENU)

        
    except RuntimeError as error_message:  # any RuntimeError you raise lands here
        print("{:s}\nTry again.".format(error_message))       
    display_game(fnd, tab, stock, waste)                
    command = input("prompt :> ")



