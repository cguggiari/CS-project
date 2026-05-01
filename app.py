import streamlit as st 

st.write('Yeay, we connected everything')
st.write('celine is a ABBUZZICONA')
st.write('love clarissa')
import numpy as np
 
def f(x):
    return 2 * x
 
# Define x values
x_values = np.arange(-10, 11, 1)
 
# Compute f(x) values
fx_values = f(x_values)
 
# Print the matrix as a table
print("=" * 30)
print(f"{'Matrix for f(x) = 2x':^30}")
print("=" * 30)
print(f"{'x':^15} {'f(x) = 2x':^15}")
print("-" * 30)
 
for x, fx in zip(x_values, fx_values):
    print(f"{x:^15} {fx:^15}")
 
print("=" * 30)
 
# Also display as a NumPy matrix (2 rows: x and f(x))
matrix = np.vstack([x_values, fx_values])
 
print("\nNumPy Matrix representation:")
print("Row 0 → x values")
print("Row 1 → f(x) = 2x values")
print()
print(matrix)
