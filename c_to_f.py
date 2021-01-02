#攝氏轉華氏溫度公式：C = (F - 32) * 5/9
Celsius = input('請輸入攝氏溫度')
Celsius = float(Celsius)

Fahrenheit = Celsius * (9 / 5) + 32

print('華氏溫度為： ', Fahrenheit)