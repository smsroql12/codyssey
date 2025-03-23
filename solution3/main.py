import pandas as pd

file_path = "Mars_Base_Inventory_List.csv"
df = pd.read_csv(file_path)

csv_list = df[['Substance', 'Flammability']].to_dict(orient='records')

for item in csv_list:
    try:
        item['Flammability'] = float(item['Flammability'])
    except ValueError:
        item['Flammability'] = 0

sort_list = sorted(csv_list, key=lambda x: x['Flammability'], reverse=True)

dangerous = [item for item in sort_list if item['Flammability'] >= 0.7]
dangerous_df = pd.DataFrame(dangerous)
dangerous_file = "Mars_Base_Inventory_danger.csv"
dangerous_df.to_csv(dangerous_file, index=False)

print("인화성이 높은 5개 품목")
for item in sort_list[:5]:
    print(item)

print("\n인화성 0.7 이상 품목")
for item in dangerous:
    print(item)
