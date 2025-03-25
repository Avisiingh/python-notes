# **Vector Operations and Python Implementation**

This document explains various vector operations, their mathematical formulas, and a single Python script that implements them all.

---

## **Mathematical Concepts**

### **1. Norm (Magnitude) of a Vector**  
The norm (or magnitude) of a vector **A** is given by:

$$
||A|| = \sqrt{A_1^2 + A_2^2 + A_3^2}
$$

### **2. Dot Product of Two Vectors**  
The dot product of vectors **A** and **B** is:

$$
A \cdot B = A_1 B_1 + A_2 B_2 + A_3 B_3
$$

### **3. Cosine of the Angle Between Two Vectors**  
The cosine of the angle **θ** between vectors **A** and **B** is:

$$
\cos{\theta} = \frac{A \cdot B}{||A|| \times ||B||}
$$

### **4. Scalar Projection of A onto B**  
The scalar projection of **A** onto **B** is:

$$
\text{proj}_B A = \frac{A \cdot B}{||B||}
$$

### **5. Vector Projection of A onto B**  
The vector projection of **A** onto **B** is:

$$
\text{Proj}_B A = \left(\frac{A \cdot B}{||B||^2}\right) B
$$

### **6. Perpendicular Vectors Condition**  
Two vectors **A** and **B** are **perpendicular** if:

$$
A \cdot B = 0 \Rightarrow A \perp B
$$

### **7. Unit Vector**  
A **unit vector** in the direction of **A** is:

$$
\hat{A} = \frac{A}{||A||}
$$

---

## **Python Implementation**

The following Python script implements all the above vector operations using NumPy.

```python
import numpy as np

# Define vectors
A = np.array([3, 4, 12])  # Example vector A
B = np.array([1, 2, 3])   # Example vector B

# 1. Compute the norm (magnitude) of A
norm_A = np.linalg.norm(A)
print("Norm of A:", norm_A)

# 2. Compute the dot product of A and B
dot_product = np.dot(A, B)
print("Dot Product:", dot_product)

# 3. Compute the cosine of the angle between A and B
cos_theta = dot_product / (np.linalg.norm(A) * np.linalg.norm(B))
print("Cosine of the Angle:", cos_theta)

# 4. Compute the scalar projection of A onto B
scalar_proj = dot_product / np.linalg.norm(B)
print("Scalar Projection of A onto B:", scalar_proj)

# 5. Compute the vector projection of A onto B
vector_proj = (dot_product / np.linalg.norm(B)**2) * B
print("Vector Projection of A onto B:", vector_proj)

# 6. Check if vectors A and B are perpendicular
if dot_product == 0:
    print("Vectors are perpendicular.")
else:
    print("Vectors are not perpendicular.")

# 7. Compute the unit vector of A
unit_vector_A = A / np.linalg.norm(A)
print("Unit Vector of A:", unit_vector_A)


