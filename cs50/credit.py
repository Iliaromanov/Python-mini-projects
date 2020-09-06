
def main():
    number = input("Number: ")
    card = card_type(number)
    
    if validate(number):
        print(card)
    else:
        print("INVALID")


def card_type(num: str) -> str:
    """ Determines the type of card (i.e American Express, MasterCard, or Visa)
        
        Args:
            num(str): the card number in string format
        Returns:
            a string of the cards name (AMEX, MASTERCARD or VISA)
    """
    # check conditions for American Express card
    if len(num) == 15 and (int(num) // 10**13 == 34 or int(num) // 10**13 == 37):
        return "AMEX"
        
    # check conditions for MasterCard and visa 
    elif len(num) == 16:
        first_two_digs = int(num) // 10**14
        first_dig = int(num) // 10**15
        
        # check conditions for MasterCard
        if first_two_digs in range(51, 56):
            return "MASTERCARD"
        # check conditions for visa card
        elif first_dig == 4:
            return "VISA"

    # check conditions for visa card
    elif len(num) == 13 and int(num) // 10**12 == 4:
        return "VISA"
    
    return "INVALID"


def validate(num: str) -> bool:
    """ Determines if the number provided is a valid card number according to Luhn's algorithm
        
        Args:
            num(str): the card number in string format
        Returns:
            bool: True if valid, False if invalid
    """
    even_index_digs = []
    odd_index_digs = []
    
    for i in range(len(num)):
        if i % 2 == 0 and i != 0:
            even_index_digs.append(int(num[i]))
        else:
            odd_index_digs.append(int(num[i]))
    
    
if __name__ == "__main__":
    main()
