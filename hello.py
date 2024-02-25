# print("Hello this is Untold_mystery\n")

# def num(n):
#     for i in range(n):
#         for j in range(i,n):
#             print("*",end=" ")
#         print()
# num(5)

# list_val = [1,2,3,4,5]

# #py round fun using nearest even algorithm for round off function
# var = round(12.5)-round(11.5)
# print(var)

# #enumerate
# l1 = ['apple','banana','chocolate','coffee','boost']
# for i,j in enumerate(l1):
#     if i%2==0:
#         print(i,j)


# #multiple input 
        
# a,b=map(int , input("Enter the value : ").split(','))
# print(f'The value of A+B is {a+b}')

# import locale

# locale.setlocale(locale.LC_NUMERIC, 'en_IN')

# amount = 123456725.1

# formatted_amount = locale.format('%0.2f', amount, grouping=True)

# print(f"Formatted Amount: ₹{formatted_amount}", type(formatted_amount))

# # Sample currency value
# amount = 1234567852

# # Format the currency value with commas
# formatted_amount = '{:,.2f}'.format(amount)

# print(f"Formatted Amount: ₹{formatted_amount}")


# # Sample currency value
# amount = 123456725.89

# # Convert the amount to a string with commas as thousands separators
# formatted_amount = '{:,.2f}'.format(amount)

# # Split the formatted string into integer and decimal parts
# integer_part, decimal_part = formatted_amount.split('.')

# # Add commas for Indian numbering system
# formatted_integer_part = ','.join(reversed([integer_part[i:i + 2][::-1] for i in range(0, len(integer_part), 2)]))

# # Combine the formatted integer part with the decimal part
# final_formatted_amount = f"₹{formatted_integer_part}.{decimal_part}"

# print(f"Formatted Amount: {final_formatted_amount}")


# import locale

# # Set the locale to the user's default
# locale.setlocale(locale.LC_ALL, 'en_IN')

# # Get and print the current locale
# current_locale = locale.getlocale()
# print("Current locale????????????????:", current_locale)

# # Format a number using the user's locale
# formatted_number = locale.format("%d", 1234567, grouping=True)
# # print("Formatted number>>>>>>>>>>>>>>>.:", formatted_number)


# def format_indian_currency(amount):
#     formatted_amount = '{:,.2f}'.format(amount)

#     # Split the formatted string into integer and decimal parts
#     integer_part, decimal_part = formatted_amount.split('.')

#     # Add commas for Indian numbering system
#     formatted_integer_part = ','.join(reversed([integer_part[i:i + 2][::-1] for i in range(0, len(integer_part), 2)]))

#     # Combine the formatted integer part with the decimal part
#     final_formatted_amount = f"₹{formatted_integer_part}.{decimal_part}"

#     return final_formatted_amount

# # Sample usage
# amount = 123456725.89
# formatted_amount = format_indian_currency(amount)
# print(f"Formatted Amount: {formatted_amount}")


# def custom_format(number):
#     # Convert the number to a string
#     str_number = str(number)

#     # Split the string into integer and decimal parts
#     integer_part, *decimal_part = str_number.split('.')

#     # Add commas for Indian numbering system to the integer part
#     formatted_integer_part = ','.join([integer_part[i:i + 2][::-1] for i in range(0, len(integer_part), 2)])

#     # Combine the formatted integer part with the decimal part (if exists)
#     formatted_number = formatted_integer_part + ('.' + decimal_part[0] if decimal_part else '')

#     return formatted_number

# # Sample usage
# number = 1234567
# formatted_number = custom_format(number)
# print(f"Formatted number: {formatted_number}")

# def custom_format(number):
#     # Convert the number to a string with commas as thousands separators
#     formatted_number = '{:,.0f}'.format(number)

#     # Split the formatted string into integer and decimal parts
#     integer_part, decimal_part = formatted_number.split('.')

#     # Add commas for Indian numbering system
#     formatted_integer_part = ','.join(reversed([integer_part[i:i + 2][::-1] for i in range(0, len(integer_part), 2)]))

#     # Combine the formatted integer part with the decimal part
#     final_formatted_number = f"{formatted_integer_part}.{decimal_part}"

#     return final_formatted_number

# # Sample usage
# number = 1234567
# formatted_number = custom_format(number)
# print(f"Formatted number: {formatted_number}")


# def custom_format(number):
#     # Convert the number to a string with commas as thousands separators
#     formatted_number = '{:,.0f}'.format(number)

#     # Check if there is a decimal part
#     if '.' in formatted_number:
#         # Split the formatted string into integer and decimal parts
#         integer_part, decimal_part = formatted_number.split('.')
#     else:
#         # If there is no decimal part, set it to an empty string
#         integer_part, decimal_part = formatted_number, ""

#     # Add commas for Indian numbering system
#     formatted_integer_part = ','.join(reversed([integer_part[i:i + 2][::-1] for i in range(0, len(integer_part), 2)]))

#     # Combine the formatted integer part with the decimal part
#     final_formatted_number = f"{formatted_integer_part}.{decimal_part}"

#     return final_formatted_number

# # Sample usage
# number = 1234567
# formatted_number = custom_format(number)
# print(f"Formatted number: {formatted_number}")


# def custom_format(number):
#     # Convert the number to a string with commas as thousands separators
#     formatted_number = '{:,.0f}'.format(number)

#     # Add commas for Indian numbering system
#     formatted_integer_part = ','.join(reversed([formatted_number[i:i + 2][::-1] for i in range(0, len(formatted_number), 2)]))

#     return formatted_integer_part

# # Sample usage
# number = 1234567
# formatted_number = custom_format(number)
# print(f"Formatted number: {formatted_number}")

# from reportlablearn import formatINR


# currency = "INR"
# total_bill =1500
# result = (str(total_bill) if total_bill else "0.0") if currency == "USD" else formatINR(total_bill)
# print(result,"LLLLLLlllll")


# result = (str(r['amount_net']) if r['amount_net'] else "0.0") if currency.currency_type == "USD" else formatinr(r['amount_net'])



# def formatinr(number):
#     if type(number) is str:
#         num = number
#     else:
#         num = str(number)
#     s, *d = num.partition(".")
#     r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
#     return "".join([r] + d)
# print(formatinr(150002.2222))


# grand_total_amount = 52836
# va = formatinr(str(float(grand_total_amount)))
# print(va)

# total_amount = 147852
# VAR = str(['total_amount']) if 'total_amount' else "0.0"
# print(VAR)

# def formatinr(number):
#     s, *d = str(number).partition(".")
#     r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
#     return "".join([r] + d)

# pharmacy_bills = '7411236'
# pharmacy_bills+='Bill Amt:'
# pharmacy_bills+=(('\n') + (formatinr(str(74123))))
# pharmacy_bills+=(('\n') + ('Balance :'))
# pharmacy_bills+=(('\n') + (formatinr(str(7413741852658))))

# print(pharmacy_bills)


# import num2words
# print("wordssssssssssssssssssssss-----",num2words(452893))



# from num2words import num2words

# number = 452893000000
# words = num2words(number)
# words = words.replace(',', '')
# print(words)


# print(">>>>>>>>>>>>>>>>>>>>>>>>",num2words((55555555555).replace(',', '')))



# from num2words import num2words

# number = 452893000000
# words = num2words(number)
# words = words.replace(',', '')
# print(words)

# # a=num2words(50265555)
# print(">>>>>>>>>>>>>>>>>>>>>>>>",num2words(50265555).replace(',', ''))



# def formatinr(number):
#     num =int(number)
#     if num <=0:
#         neg = True
#         number = abs(neg)
#     else:
#         neg = False
#     s, *d = str(number).partition(".")
#     r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
#     return "".join([r] + d)

# p = formatinr(str(Roundoff(-147)))
# print(p,"LLLLLLLLLLLL")

import math
def Roundoff(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

# def formatinr(number):
#     if isinstance(number,str):
#         if int(eval(number)) <= 0:
#             neg = True
#             number = abs(eval(number))
#         else:
#             neg = False
#         s, *d = str(number).partition(".")
#         r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
#         if neg:
#             r = "-" + r
#         return "".join([r] + d)
#     else:
#         s, *d = str(number).partition(".")
#         r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
#         return "".join([r] + d)
# # p = formatinr(str(Roundoff(float(-111000001))))
# # p = formatinr(str(-111000001))
# p = formatinr(round(-111000001))

# print(p, "LLLLLLLLLLLL")




# asd = "-11412543.0"
# asd = int(eval(asd))
# print(asd, type(asd))


def formatinr(number):
    if isinstance(number, str):
        if int(eval(number)) <= 0:
            neg = True
            number = abs(eval(number))
        else:
            neg = False
        s, *d = str(number).partition(".")
        r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
        if neg:
            r = "-" + r
        return "".join([r] + d)
    else:
        if int(number) <= 0:
            neg = True
            number = abs(number)
        else:
            neg = False
        s, *d = str(number).partition(".")
        r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
        if neg:
            r = "-" + r
        return r

# p = formatinr(round(-111000001))
# p = formatinr(str(Roundoff(float(-111000001))))
p = formatinr(str(-111000001))
print("{:.2f}".format(p), "LLLLLLLLLLLL")
