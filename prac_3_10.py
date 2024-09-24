def process_sales_data(sales_data):
    sales_dict = {}

    for entry in sales_data:
        buyer, product, quantity = entry.split()
        quantity = int(quantity) 

        if buyer not in sales_dict:
            sales_dict[buyer] = {}  

        if product not in sales_dict[buyer]:
            sales_dict[buyer][product] = 0 
        sales_dict[buyer][product] += quantity 

    return sales_dict

def print_sales_report(sales_dict):
    for buyer in sorted(sales_dict.keys()):
        print(buyer + ":")
        for product in sorted(sales_dict[buyer].keys()):
            print(f"  {product}: {sales_dict[buyer][product]}")

if __name__ == "__main__":
    n = int(input("Введите количество записей о продажах: "))
    sales_data = []

    for _ in range(n):
        sales_data.append(input("Введите запись о продаже (Покупатель товар количество): "))

    sales_dict = process_sales_data(sales_data)

    print("\nОтчет о продажах:")
    print_sales_report(sales_dict)
