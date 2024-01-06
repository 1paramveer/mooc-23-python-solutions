# # Write your solution here
# from datetime import datetime

# def is_valid_date(date_string, date_format):
#     try:
#         parsed_date = datetime.strptime(date_string, date_format)
#         if parsed_date.year == 0 or (parsed_date.day == 29 and parsed_date.month == 2): 
#             return False
#         return True
#     except ValueError:
#         return False

# # date_input = "301223"  # Replace this with your date in ddmmyy format
# # format_input = "%d%m%y"  # Format corresponding to ddmmyy

# def is_it_valid(pic: str):
#     ddmmyy = pic[:6]
#     X = pic[6]
#     pi = pic[7:10]
#     z = pic[-1]
#     ctrl_chars = '0123456789ABCDEFHJKLMNPRSTUVWXY'

#     ctrl_char_given = int(ddmmyy+pi) % 31
#     actual_ctrl_char = ctrl_chars[ctrl_char_given]

#     if is_valid_date(ddmmyy,"%d%m%y") and (X == "+" or X == "-" or X == "A") and (z == actual_ctrl_char):
#         return True
#     else: 
#         return False

# print(is_it_valid("290200-1239"))


from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    try:
        dd = int(pic[0:2])
        mm = int(pic[2:4])
        yy = int(pic[4:6])
        X = pic[6]
        yyy = int(pic[7:10])
        z = pic[10]
        nums = pic[0:6] + pic[7:10]
        index = int(nums)%31
        control = '0123456789ABCDEFHJKLMNPRSTUVWXY'[index]

        if dd < 1 or dd > 31 or mm < 1 or mm > 12 or X not in ('-','+','A') or z != control:
            return False
        
        century = 0
        if X == '-':
            century = 1800
        elif X == '+':
            century = 1900
        elif X == 'A':
            century = 2000
        
        dob_year = century + yy

        datetime(dob_year, mm, dd)

        return True
    except:
        return False
