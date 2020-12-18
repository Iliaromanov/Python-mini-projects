def main():
    while True:
        # get the card number input from the user
        try:
            number = input("Number: ")
            int(number)
            break
        except:
            continue

    # determine the card type
    card = card_type(number)
    
    # validate the card number and print the result
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
    
    return "this INVALID"


def validate(num: str) -> bool:
    """ Determines if the number provided is a valid card number according to Luhn's algorithm
        
        Args:
            num(str): the card number in string format
        Returns:
            bool: True if valid, False if invalid
    """
    even_index_digs = []
    odd_index_digs = []
    
    # loop through the card number and add digits to the even_index_digs list and odd_index_digs list accordingly
    for i in range(len(num) - 1, -1, -2):
        print("i:", i)
        # append to the even_index_digs list
        even_index_digs.append(int(num[i]))
        
        # if the digit x 2 is equal to a double-digit number append the numbers digits to the odd_index_digs list separately
        if i != 0 and int(num[i - 1]) * 2 >= 10:
            odd_index_digs.append(int(num[i - 1]) * 2 // 10)
            odd_index_digs.append(int(num[i - 1]) * 2 % 10)
        # else append the digit x 2 to the ood_index_digits list
        elif i != 0:
            odd_index_digs.append(int(num[i - 1]) * 2)
    
    # Luhn's formula result
    total = sum(even_index_digs) + sum(odd_index_digs)
    print("odd:", odd_index_digs, "even:", even_index_digs)
    if total % 10 == 0:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    main()
