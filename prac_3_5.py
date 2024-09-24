def restore_access_control(num_files, file_permissions, num_requests, requests):
    permissions = {}

    for entry in file_permissions:
        parts = entry.split()
        filename = parts[0]
        ops = set(parts[1:]) 
        permissions[filename] = ops

    results = []
    for request in requests:
        operation, filename = request.split()
        if filename in permissions and operation in permissions[filename]:
            results.append("OK")
        else:
            results.append("Access denied")

    return results

if __name__ == "__main__":
    num_files = int(input("Введите количество файлов: "))
    file_permissions = []

    for _ in range(num_files):
        file_permissions.append(input("Введите имя файла и операции: "))

    num_requests = int(input("Введите количество запросов: "))
    requests = []

    for _ in range(num_requests):
        requests.append(input("Введите запрос (операция файл): "))

    results = restore_access_control(num_files, file_permissions, num_requests, requests)
    
    print("\nРезультаты запросов:")
    for result in results:
        print(result)
