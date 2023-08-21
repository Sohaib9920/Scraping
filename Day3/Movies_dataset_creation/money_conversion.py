import re

def money_conversion(money):
    if not money:
        return None
    if isinstance(money, list):
        money = "".join(money)

    pattern = r"""
        (\$|₽)                          # Currency symbol: dollar sign or ₽ (ruble).
        \s?                             # Optional whitespace.
        (\d+(?:\.\d+)?)                 # Digits (integer or decimal part).
        \s?                             # Optional whitespace.
        (?:
            (?:
                (?:–|-|—)               # Dash symbol: – or - or —.
                \$?                     # Optional dollar sign.
                (?:\d+(?:\.\d+)?)       # Digits (integer or decimal part).
            )
            |
            (?:to[^A-Za-z]+)            # "to" followed by non-alphabet characters.
        )?
        \s*                             # Optional whitespace.
        (million|billion)?              # million or billion.
    """

    match = re.search(pattern, money.replace(",", ""), re.VERBOSE | re.IGNORECASE)
    if not match:
        return None
    currency_symbol = match.group(1)
    value = match.group(2)
    ammount = match.group(3)

    # Formating cuurency symbol (in dollars)
    if currency_symbol == "$":
        symbol = 1
    elif currency_symbol == "₽":
        symbol = 0.010661202

    # Formatting value
    value = float(value)

    # Formatting ammount (in dollars)
    if not ammount:
        ammount = 1
    elif ammount.lower() == "million":
        ammount = 1000000
    elif ammount.lower() == "billion":
        ammount = 1000000000
    
    formatted_money = symbol * value * ammount
    return formatted_money
