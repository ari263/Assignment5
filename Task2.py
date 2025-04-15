x = list(range(1, 11))

x_slice = x[0:5]

x_slice_reverse = x_slice.copy()
x_slice_reverse.reverse()

print(f"Original list: {x}")
print(f"Extracted first five elements: {x_slice}")
print(f"Reversed extracted elements: {x_slice_reverse}")
