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
import textwrap

from bs4 import BeautifulSoup
from reportlab.lib import colors
from reportlab.platypus import Paragraph,Spacer,PageBreak,SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_LEFT,TA_RIGHT,TA_CENTER
from reportlab.lib.styles import ParagraphStyle
# from django_conflux.async_views import status
# from django_conflux.async_views import Response

from django.http import HttpResponse
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


# def formatinr(number):
#     if isinstance(number, str):
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
#         if int(number) <= 0:
#             neg = True
#             number = abs(number)
#         else:
#             neg = False
#         s, *d = str(number).partition(".")
#         r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
#         if neg:
#             r = "-" + r
#         return r

# def formatinr(number,roundoff=None):
#     if isinstance(number, str):
#         # if number == '' : 
#         #     return ''
#         # if number == '-' : 
#         #     return '-'
#         try:
#             if int(eval(number)) < 0:
#                 neg = True
#                 number = abs(eval(number))
#         except:
#             return number
#         else:
#             neg = False
#         if roundoff:
#             number = float(number)
#             number = Roundoff(number, 2)
#         s, *d = str(number).partition(".")
#         r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
#         if neg:
#             r = "-" + r
#         return "".join([r] + d)
#     else:
#         if int(number) < 0:
#             neg = True
#             number = abs(number)
#         else:
#             neg = False
#         if roundoff:
#             number = float(number)
#             number = Roundoff(number,2)
#         s, *d = str(number).partition(".")
#         r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
#         if neg:
#             r = "-" + r
#         return "".join([r] + d)
# # p = formatinr(round(-111000001))
# # p = formatinr(str(Roundoff(float(-111000001))))
# p=52589 - 741259
# print(round(p),type(p))
# # p = formatinr(p,roundoff=True)
# print("{}".format(formatinr(p,roundoff=True)), type(p),"LLLLLLLLLLLL")


# import json
# result = {"value": "Positive", "comment": "fgchvjbn"}
# # result = json.dumps(result) 
# result = json.loads(result)

# value = result['value']
# # comment = result_json['comment']
# print(value)


# def formatinr(number,roundoff=None):
#     if isinstance(number, str):
#         try:
#             if int(eval(number)) < 0:
#                 neg = True
#                 number = eval(number)
#             else:
#                 neg = False
#         except:
#             return number
#         if roundoff:
#             number = float(number)
#             number = Roundoff(number, 2)
#         s, *d = str(number).partition(".")
#         r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
#         if neg:
#             r = "-" + r
#         return "".join([r] + d)
#     else:
#         if int(number) < 0:
#             neg = True
#             number = abs(number)
#         else:
#             neg = False
#         if roundoff:
#             number = float(number)
#             number = Roundoff(number,2)
#         s, *d = str(number).partition(".")
#         r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
#         if neg:
#             r = "-" + r
#         return "".join([r] + d)
    
# p=str(-741259)
# # print(round(p),type(p))
# # p = formatinr(p,roundoff=True)
# print(formatinr(p), type(p),"LLLLLLLLLLLL")
# address_line_1 = '1234567891011121314151617181912021222324252627282930fghgvbdsjhfbkahe;euhljfbsd,mvn ,.szndlfhajhbgjasdz vm zsdkj.f'
# address_line_2 = '1234567891011121314151617181912021222324252627282930121qwertyuiop[lkjhgfdszxcvbnm,oiuytrewertyui]'
# address = ""
# if address_line_1 and len(address_line_1)>100:
#     wrap_text = textwrap.wrap(address_line_1, width=100)
#     address+=wrap_text[0]
# if address_line_2 and len(address_line_2)>100:
#     wrap_text = textwrap.wrap(address_line_2, width=100)
#     address+=(", " + wrap_text[0])

# print(address)


# def html_to_reportlab(html_data) -> str:
    # try:
        # if not html_data:
        #     return []

        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="hello_world.pdf"'
        # doc = SimpleDocTemplate(response, pagesize=letter)

        # text_alignments = {
        #     'left': ParagraphStyle(name='Normal', alignment=0),
        #     'center': ParagraphStyle(name='Normal', alignment=1),
        #     'right': ParagraphStyle(name='Normal', alignment=2),
        # }

        # soup = BeautifulSoup(html_data, 'html.parser')  
        # paragraphs = []

        # for element in soup.find_all(recursive=False):
        #     tag_name = element.name
        #     if tag_name in ['div', 'span', 'i', 'b', 'u']:
        #         style = element.get('style', '')
        #         alignment = 'left'
        #         if 'text-align' in style:
        #             alignment = style.split('text-align: ')[1].split(';')[0]
        #         content = element.text.strip()
        #         p_style = text_alignments.get(alignment, text_alignments['left'])
        #         paragraphs.append(Paragraph(content, p_style))

        # doc.build(paragraphs)
        # return response

        
#         if not html_data:
#             return ""
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="hello_world.pdf"'
#         doc = SimpleDocTemplate(response, pagesize=letter)
#         text_alignments = {
#             'left': TA_LEFT,
#             'center': TA_CENTER,
#             'right': TA_RIGHT,
#         }
#         soup = BeautifulSoup(html_data, 'html.parser')
#         paragraphs = []
#         combined_content = ''
#         for element in soup.find_all(recursive=False):
#             tag_name = element.name
#             if tag_name in ['div', 'span', 'i', 'b', 'u']:
#                 style = element.get('style', '')
#                 alignment = 'left'
#                 if 'text-align' in style:
#                     alignment = style.split('text-align: ')[1].split(';')[0]
#                 content = element.text.strip()
#                 p_style = ParagraphStyle(name='Normal', alignment=text_alignments.get(alignment, TA_LEFT))
#                 if not element.find_all():
#                     paragraphs.append(Paragraph(content, p_style))
#                 else:
#                     content =''
#                     for i in element.contents:
#                         if i.name not in ['span']:
#                             content += '{}'.format(i)
#                         else:
#                             content += '<div>{}</div>'.format(i)
#                     paragraphs.append(Paragraph(content, p_style))
#         doc.build(paragraphs)
#         return paragraphs
    
#     except Exception as e:
#         raise Exception 
# print(1111111111111111111111111111111)


# def search(arr,key):
#     for i in arr:
#         if i == key:
#             return key
# size_arr = int(input("Enter the size : "))
# arr = []
# for i in range(size_arr):
#     ele = int(input("Enter the value : "))
#     arr.append(ele)
# key = int(input("Enter search key : "))
# result = search(arr , key)
# if result == key:
#     print("Successfully found {}".format(key))
# else:
#     print("UnSuccessfully found {}".format(key))

# def compress_string(s):
#     compressed_string = ''
#     count = 1
#     for i in range(len(s)):
#         print('ooooooo')
#         if i < len(s)-1 and s[i] == s[i+1]:
#             count += 1
#         else:
#             compressed_string += s[i] + str(count)
#             count = 1
#     return compressed_string

# # s = 'aaaabbbccczzzzzzooooooooooooooooooooooooooozzzzzzzzzzzzzzzzzz'
# # compressed = compress_string(s)
# # print(compressed)

# s = 'aaaabbbccczzzzzzooooooozzzzzzzz'
# dic={}
# count =0
# for i in range(len(s)):
#     if i =='a':
#         if 'a' not in dic:
#             dic['a'] = 1
#         dic['a'] += count
#     print(dic)

# from datetime import datetime
# # today_date = datetime.date.today()
# today_date = datetime.now().date()

# print(today_date)  


from num2words import num2words

number = 1232223
english_words = num2words(number)
print(english_words)
