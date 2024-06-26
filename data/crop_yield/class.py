def read_classes(classes_path):
    with open(classes_path, 'r') as f:
        classes = f.readlines()
    class_ids, class_names = [], []
    for row in classes:
        row = row.strip()
        if '|' in row:
            cls_info = row.split('|')
            id_info = [int(x) for x in cls_info[0].split(',')]
            class_ids.extend(id_info)
            class_names.append(cls_info[1])
    unique_class_ids = set(class_ids)
    return unique_class_ids, class_names

# Path to the classes definition file
classes_path = 'data/sentinel2/lombardia-classes/classes25pc.txt'

# Read and count the number of unique classes
unique_class_ids, class_names = read_classes(classes_path)
num_classes = len(unique_class_ids)
print(f'Number of unique classes: {num_classes}')
