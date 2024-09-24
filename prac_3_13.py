def build_family_tree(n, relationships):
    parent_dict = {}
    
    for relationship in relationships:
        child, parent = relationship.split()
        parent_dict[child] = parent

    return parent_dict

def find_ancestors(element, parent_dict):
    ancestors = []
    while element in parent_dict:
        ancestors.append(element)
        element = parent_dict[element]
    ancestors.append(element)  
    return ancestors

def find_lca(first, second, parent_dict):
    first_ancestors = find_ancestors(first, parent_dict)
    second_ancestors = find_ancestors(second, parent_dict)

    first_ancestors.reverse()
    second_ancestors.reverse()

    lca = None
    for ancestor1, ancestor2 in zip(first_ancestors, second_ancestors):
        if ancestor1 == ancestor2:
            lca = ancestor1
        else:
            break

    return lca

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
        lca = find_lca(first, second, parent_dict)
        results.append(lca)

    print("\nНаименьшие общие предки:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
