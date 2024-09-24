def build_family_tree(n, relationships):
    parent_dict = {}
    
    for relationship in relationships:
        child, parent = relationship.split()
        parent_dict[child] = parent 

    return parent_dict

def calculate_height(name, parent_dict, height_cache):
    if name in height_cache:
        return height_cache[name]
    
    if name not in parent_dict:
        height_cache[name] = 0
        return 0
    
    parent_height = calculate_height(parent_dict[name], parent_dict, height_cache)
    height_cache[name] = parent_height + 1
    return height_cache[name]

def main():
    n = int(input("Введите количество элементов в генеалогическом древе: "))
    relationships = []

    for _ in range(n - 1):
        relationships.append(input("Введите имя потомка и имя родителя: "))

    parent_dict = build_family_tree(n, relationships)

    height_cache = {}

    for person in parent_dict.keys():
        calculate_height(person, parent_dict, height_cache)

    root_name = next(iter(set(parent_dict.values()) - set(parent_dict.keys())))
    height_cache[root_name] = 0

    all_names = sorted(height_cache.keys())
    
    print("\nВысоты элементов генеалогического древа:")
    for name in all_names:
        print(f"{name}: {height_cache[name]}")

if __name__ == "__main__":
    main()
