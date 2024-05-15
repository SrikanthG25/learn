import math


def Roundoff(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
currency_type = "USD"
currency_type_1 = "INR"

import inflect

def convert_number_to_words(number):
    p = inflect.engine()
    words = p.number_to_words(number)
    return words.replace(',', '')

def number_to_words(amount, currency_type):
    print(amount,'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii',currency_type)
    amount = Roundoff(amount,2)
    print(amount,'>>>>>>>>>>>>>>>>>>>>>>>>>>>>...')
    if currency_type.lower() == 'inr':
        crores = int(amount / 10000000)
        lakhs = int((amount % 10000000) / 100000)
        thousands = int((amount % 100000) / 1000)
        rupees = int(amount % 1000)
        paise = int((amount - int(amount)) * 100)
        
        words_inr = ''
        if crores > 0:
            words_inr += convert_number_to_words(crores) + " crore "
        if lakhs > 0:
            words_inr += convert_number_to_words(lakhs) + " lakh "
        if thousands > 0:
            words_inr += convert_number_to_words(thousands) + " thousand "
        if rupees > 0:
            words_inr += convert_number_to_words(rupees) + " rupees"
        if paise > 0:
            words_inr += " and " + convert_number_to_words(paise) + " paise only"
        return words_inr.strip()
    else:
        millions = int(amount / 1000000)
        billions = int((amount % 1000000000) / 1000000000)
        trillions = int((amount % 1000000000000) / 1000000000000)
        dollars = int(amount % 1000000)
        cents = int((amount - int(amount)) * 100)
        
        words_usd = ''
        if trillions > 0:
            words_usd += convert_number_to_words(trillions) + " trillion "
        if billions > 0:
            words_usd += convert_number_to_words(billions) + " billion "
        if millions > 0:
            words_usd += convert_number_to_words(millions) + " million "
        if dollars > 0:
            words_usd += convert_number_to_words(dollars) + " dollars"
        if cents > 0:
            words_usd += " and " + convert_number_to_words(cents) + " cents"
        return words_usd.strip()

print(number_to_words(123456789.12, currency_type))
print(number_to_words(123456789.23, currency_type_1)) 


