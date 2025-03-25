# Vector Operations in Python

## 1. Dot Product
The dot product of two vectors A and B is given by:
\[ A \cdot B = A_1B_1 + A_2B_2 + A_3B_3 \]

### **Python Implementation:**
```python
import numpy as np
A = np.array([4, -3, 5])
B = np.array([-2, 6, 1])
dot_product = np.dot(A, B)
print("Dot Product:", dot_product)
```

---

## 2. Norm (Magnitude) of a Vector
The norm of a vector A is given by:
\[ ||A|| = \sqrt{A_1^2 + A_2^2 + A_3^2} \]

### **Python Implementation:**
```python
norm_A = np.linalg.norm(A)
print("Norm of A:", norm_A)
```

---

## 3. Angle Between Two Vectors
Using the cosine rule:
\[ \cos\theta = \frac{A \cdot B}{||A|| \cdot ||B||} \]

### **Python Implementation:**
```python
norm_B = np.linalg.norm(B)
cos_theta = dot_product / (norm_A * norm_B)
angle = np.arccos(cos_theta)  # in radians
angle_degrees = np.degrees(angle)
print("Angle between A and B (degrees):", angle_degrees)
```

---

## 4. Scalar Projection
Scalar projection of A onto B:
\[ \text{Scalar Projection} = \frac{A \cdot B}{||B||} \]

### **Python Implementation:**
```python
scalar_proj = dot_product / norm_B
print("Scalar Projection of A onto B:", scalar_proj)
```

---

## 5. Vector Projection
The vector projection of A onto B is:
\[ \text{Vector Projection} = \left(\frac{A \cdot B}{||B||^2}\right) B \]

### **Python Implementation:**
```python
vector_proj = (dot_product / (norm_B ** 2)) * B
print("Vector Projection of A onto B:", vector_proj)
```

---

## 6. Unit Vector
A unit vector in the direction of A:
\[ \hat{A} = \frac{A}{||A||} \]

### **Python Implementation:**
```python
unit_vector_A = A / norm_A
print("Unit Vector of A:", unit_vector_A)
```

---

## 7. Checking Perpendicularity
Two vectors are perpendicular if their dot product is **zero**.

### **Python Implementation:**
```python
if np.isclose(dot_product, 0):
    print("A and B are perpendicular")
else:
    print("A and B are not perpendicular")
```

---

## Summary
| Operation | Formula | Python Function |
|-----------|---------|----------------|
| **Dot Product** | \( A \cdot B \) | `np.dot(A, B)` |
| **Norm** | \( ||A|| \) | `np.linalg.norm(A)` |
| **Angle Between Vectors** | \( \cos\theta = \frac{A \cdot B}{||A|| \cdot ||B||} \) | `np.arccos(np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B)))` |
| **Scalar Projection** | \( \frac{A \cdot B}{||B||} \) | `np.dot(A, B) / np.linalg.norm(B)` |
| **Vector Projection** | \( \left(\frac{A \cdot B}{||B||^2}\right) B \) | `(np.dot(A, B) / np.linalg.norm(B)**2) * B` |
| **Unit Vector** | \( \frac{A}{||A||} \) | `A / np.linalg.norm(A)` |
| **Perpendicular Check** | \( A \cdot B = 0 \) | `np.isclose(np.dot(A, B), 0)` |

