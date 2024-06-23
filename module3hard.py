data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    if type(data_structure) is int:
      return data_structure
    elif type(data_structure) is str:
      return len(data_structure)
    elif type(data_structure) in [set, list, tuple]:
      n1 = 0
      for n in data_structure:
        n1 += calculate_structure_sum(n)
      return n1
    elif type(data_structure) is dict:
        d1 = 0
        for d, v in data_structure.items():
            d1 += calculate_structure_sum(d) + calculate_structure_sum(v)
        return d1
    elif data_structure is None:
        return 0



result = calculate_structure_sum(data_structure)
print(result)
