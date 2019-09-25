from array_shift import insert_shift_array

def test_function_exists():
   assert insert_shift_array

def test_insert_to_middle():
   expected = [1, 2, 3, 5, 7, 9]
   actual = insert_shift_array([1, 3, 5, 7, 9], 2)
   assert expected == actual

def test_insert_small_array():
   expected = [0,1]
   actual = insert_shift_array([1], 0)
   assert expected == actual
