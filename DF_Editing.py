import pandas as pd

def persian_to_english_numbers(persian_str):
    persian_digits = {
        '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4',
        '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'
    }
    english_str = ''.join(persian_digits.get(c, c) for c in persian_str)
    return english_str

xls = pd.read_excel("F:\\DA\\Projects\\Khodro45.xlsx")
df = pd.DataFrame(xls)

df['Kilometer'] = df['Kilometer'].str.replace(',', '').str.replace('ک', '')

df['Kilometer'] = df['Kilometer'].apply(persian_to_english_numbers)
print(df)