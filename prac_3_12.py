def build_family_tree(n, relationships):
    parent_dict = {}
    
    for relationship in relationships:
        child, parent = relationship.split()
        parent_dict[child] = parent

    return parent_dict

def is_ancestor(ancestor, descendant, parent_dict):
    while descendant in parent_dict:
        if parent_dict[descendant] == ancestor:
            return True
        descendant = parent_dict[descendant]
    return False

def main():
    n = int(input("Введите количество элементов в генеалогическом древе: "))
    relationships = []

    for _ in range(n - 1):
        relationships.append(input("Введите имя потомка и имя родителя: "))

    parent_dict = build_family_tree(n, relationships)

    k = int(input("Введите количество запросов: "))
    
    results = []
    
    for _ in range(k):
        first, second = input("Введите два элемента дерева: ").split()
        
        if is_ancestor(first, second, parent_dict):
            results.append(1)  
        elif is_ancestor(second, first, parent_dict):
            results.append(2)  
        else:
            results.append(0)  

    print("\nРезультаты запросов:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
