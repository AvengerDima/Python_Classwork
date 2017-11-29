print("1. Юникодный символ с кодом - %d выглядит: %s" % (0x26BD, '\u26BD'))
print("2. Юникодный символ с кодом - %d выглядит: %s" % (0x2665, '\u2665'))
print("3. Юникодный символ с кодом - %d выглядит: %s" % (0x270B, '\u270B'))
print("4. Юникодный символ с кодом - %d выглядит: %s" % (0x1F44D, '\U0001F44D'))
print("5. Юникодный символ с кодом - %d выглядит: %s" % (0x1F44E, '\U0001F44E'))
print("\n")

#---------------------------------------

current_time = '18:38:18'
hours = int (current_time[:2])
minutes = int (current_time[3:5])
seconds = int (current_time[6:8])
print("Текущее время:", hours, ":", minutes,":", seconds, "\n")
total_seconds = hours*3600 + minutes*60 + seconds
print("Всего секунд:", total_seconds, "\n")

#---------------------------------------

current_time = '18:8:1'
lst = (current_time.split(':'))
hours = int(lst[0])
minutes = int(lst[1])
seconds = int(lst[2])
print(hours, minutes, seconds)
total_seconds = hours*3600 + minutes*60 + seconds
print(total_seconds)
