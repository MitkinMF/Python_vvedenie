#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text='dasdsdsa asdasdasd ыфвфыабв  dsasdasабв фывфывфы абв ывацыфу'
my_list = list(filter(lambda x: 'абв' not in x , text.split()))
print(' '.join(my_list))