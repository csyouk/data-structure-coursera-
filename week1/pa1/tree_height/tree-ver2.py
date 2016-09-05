int_list =[1, 2, -1, 1, 8, 1, 5, 5, 2, 8, 8]

pairs = []

root_tuple = None

for vertex_key, parent_key in enumerate(int_list):
    pairs.append((vertex_key, parent_key))
    if(parent_key == -1):
        root_tuple = (vertex_key, parent_key)
