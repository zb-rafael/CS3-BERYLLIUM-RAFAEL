Chinese Zodiac Sign

```python
  #RAFAEL,ZYA KYNDER TARHATA B.
  #9 - BERYLLIUM

  print("Hello ! Welcome to Zya's Chinese Zodiac Sign Revealer Program.")
  #ASKS THE USER TO INPUT THEIR BIRTH YEAR
  birth_year = int(input("Enter your birth year. Note that your birth year must not be earlier than 1900. (ex: 2011, 2000):"))

  #CHECKS IF USER'S INPUT IS VALID (YEAR 1900+ ONLY)
  if birth_year < 1900:
    print("Invalid input. Sorry, your birth year must not be earlier than 1900.")
    exit() #EXITS THE PROGRAM AFTER INVALID INPUT
  else:
    zodiac_sign = (birth_year - 1900) % 12 #CALCULATES THE ZODIAC SIGN BASED ON THE BIRTH YEAR

  #IF-ELIF-ELSE STATEMENTS TO DETERMINE THE ZODIAC SIGN BASED ON THE CALCULATED VALUE
  if zodiac_sign == 0:
    print("Your Chinese Zodiac Sign is: Rat 鼠 (shǔ)")
  elif zodiac_sign == 1:
    print("Your Chinese Zodiac Sign is: Ox 牛 (niú) ")
  elif zodiac_sign == 2:
    print("Your Chinese Zodiac Sign is: Tiger 虎 (hǔ)")
  elif zodiac_sign == 3:
      print("Your Chinese Zodiac Sign is: Rabbit 兔 (tù) ")
  elif zodiac_sign == 4:
      print("Your Chinese Zodiac Sign is: Dragon 龙 (lóng) ")
  elif zodiac_sign == 5:
      print("Your Chinese Zodiac Sign is: Snake 蛇 (shé) ")
  elif zodiac_sign == 6:
      print("Your Chinese Zodiac Sign is: Horse 马 (mǎ)")
  elif zodiac_sign == 7:
      print("Your Chinese Zodiac Sign is: Goat 羊 (yáng) ")
  elif zodiac_sign == 8:
      print("Your Chinese Zodiac Sign is: Monkey 猴 (hóu) ")
  elif zodiac_sign == 9:
      print("Your Chinese Zodiac Sign is: Rooster 鸡 / 雞 (jī) ")
  elif zodiac_sign == 10:
      print("Your Chinese Zodiac Sign is: Dog 狗 (gǒu) ")
  else:
      print("Your Chinese Zodiac Sign is: Pig: 猪 (zhū) ")
  
  print("Goodbye ! Thank you for stopping by.") 

```

<img width="1648" height="694" alt="ChineseZodiacSign" src="https://github.com/user-attachments/assets/c8b5e442-07ae-4867-974f-abcb10adea03" />



