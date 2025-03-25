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
---


➡ **Definition:** A basis of a vector space is a set of linearly independent vectors that span the entire space.

➡ **Key Points:**
- **Linear Independence:** No vector in the set can be written as a combination of the others.
- **Spanning:** Any vector in the space can be expressed as a linear combination of the basis vectors.
- **Dimension:** Number of vectors in a basis defines the dimension of the space.

---

## **2. Basis in Different Vector Spaces**

### **Standard Basis**
➡ The most common basis in \(\mathbb{R}^n\) is the standard basis:
\[ e_1 = (1,0,0), \quad e_2 = (0,1,0), \quad e_3 = (0,0,1) \]

### **Example in \(\mathbb{R}^2\)**
\[ \text{Basis } = \{(1,0), (0,1)\} \]

### **Example in \(\mathbb{R}^3\)**
\[ \text{Basis } = \{(1,0,0), (0,1,0), (0,0,1)\} \]

### **Custom Basis**
➡ Any set of linearly independent vectors that spans the space can be a basis.
\[ \text{Example: } \{(1,1), (1,-1)\} \text{ is a basis for } \mathbb{R}^2 \]

---

## **3. Checking Basis in Python**

### **Step 1: Import Libraries**
```python
import numpy as np
from sympy import Matrix
```

### **Step 2: Define Vectors**
```python
v1 = np.array([1, 0])
v2 = np.array([0, 1])
```

### **Step 3: Check if Vectors Form a Basis**
```python
A = np.column_stack((v1, v2))
print("Matrix formed by basis vectors:")
print(A)

rank = np.linalg.matrix_rank(A)
if rank == 2:
    print("The vectors form a basis of R².")
else:
    print("The vectors do not form a basis.")
```

### **Output:**
```
Matrix formed by basis vectors:
[[1 0]
 [0 1]]
The vectors form a basis of R².
```

➡ **Explanation:** The rank of the matrix formed by basis vectors is equal to the dimension of \(\mathbb{R}^2\), confirming they form a basis.

---

## **4. Converting a Vector to a Different Basis**

### **Change of Basis Formula:**
\[ v' = B^{-1} v \]
Where:
- \( v \) = vector in the original basis
- \( B \) = matrix of new basis vectors
- \( v' \) = vector in the new basis

### **Python Implementation:**
```python
B = np.array([[1, 1], [1, -1]])  # New basis
v = np.array([2, 3])  # Vector in standard basis

B_inv = np.linalg.inv(B)
v_new = B_inv @ v  # Compute new coordinates
print("Vector in new basis:", v_new)
```

### **Output:**
```
Vector in new basis: [ 2.5  0.5]
```
➡ **Explanation:** The vector (2,3) in the standard basis is transformed into (2.5, 0.5) in the new basis.

---

## **5. Visualizing Basis Vectors**

```python
import matplotlib.pyplot as plt

def plot_vectors(vectors, colors=['r', 'b'], labels=['v1', 'v2']):
    for i, v in enumerate(vectors):
        plt.quiver(0, 0, v[0], v[1], color=colors[i], angles='xy', scale_units='xy', scale=1, label=labels[i])
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.show()

v1 = [1, 1]
v2 = [1, -1]
plot_vectors([v1, v2])
```



---




