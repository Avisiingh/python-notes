
---

```md
# **Vector Operations and Implementation in Python**

This document covers important vector operations, including their mathematical formulas and Python implementations using `NumPy`.

---

## **1. Norm of a Vector (Magnitude)**  
The norm (or magnitude) of a vector **A** is given by:  

$$ ||A|| = \sqrt{A_1^2 + A_2^2 + A_3^2} $$

### **Python Implementation:**
```python
import numpy as np

A = np.array([3, 4, 12])  # Example vector
norm_A = np.linalg.norm(A)
print("Norm of A:", norm_A)
```

---

## **2. Dot Product of Two Vectors**  
The dot product of two vectors **A** and **B** is:  

$$ A \cdot B = A_1 B_1 + A_2 B_2 + A_3 B_3 $$

### **Python Implementation:**
```python
A = np.array([3, 4, 5])
B = np.array([1, 2, 3])

dot_product = np.dot(A, B)
print("Dot Product:", dot_product)
```

---

## **3. Cosine of the Angle Between Two Vectors**  
The cosine of the angle θ between two vectors is given by:  

$$ \cos{\theta} = \frac{A \cdot B}{||A|| \times ||B||} $$

### **Python Implementation:**
```python
cos_theta = dot_product / (np.linalg.norm(A) * np.linalg.norm(B))
print("Cosine of the Angle:", cos_theta)
```

---

## **4. Scalar Projection of A onto B**  
The scalar projection of **A** onto **B** is:  

$$ \text{proj}_B A = \frac{A \cdot B}{||B||} $$

### **Python Implementation:**
```python
scalar_proj = dot_product / np.linalg.norm(B)
print("Scalar Projection of A onto B:", scalar_proj)
```

---

## **5. Vector Projection of A onto B**  
The vector projection of **A** onto **B** is:  

$$ \text{Proj}_B A = \left(\frac{A \cdot B}{||B||^2}\right) B $$

### **Python Implementation:**
```python
vector_proj = (dot_product / np.linalg.norm(B)**2) * B
print("Vector Projection of A onto B:", vector_proj)
```

---

## **6. Perpendicular Vectors Condition**  
Two vectors **A** and **B** are **perpendicular** if their dot product is **zero**:  

$$ A \cdot B = 0 \Rightarrow A \perp B $$

### **Python Implementation:**
```python
if np.dot(A, B) == 0:
    print("Vectors are perpendicular.")
else:
    print("Vectors are not perpendicular.")
```

---

## **7. Unit Vector**  
A **unit vector** in the direction of **A** is:  

$$ \hat{A} = \frac{A}{||A||} $$

### **Python Implementation:**
```python
unit_vector_A = A / np.linalg.norm(A)
print("Unit Vector of A:", unit_vector_A)
```

---

## **8. Angle Between Two Vectors (Using `arccos`)**  
The angle **θ** between two vectors is:

$$ \theta = \cos^{-1} \left(\frac{A \cdot B}{||A|| \times ||B||} \right) $$

### **Python Implementation:**
```python
theta = np.arccos(cos_theta)  # Angle in radians
theta_degrees = np.degrees(theta)  # Convert to degrees
print("Angle between A and B in radians:", theta)
print("Angle between A and B in degrees:", theta_degrees)
```

---

### **📌 Notes:**
- `np.linalg.norm(A)` → Finds the **magnitude** of a vector.
- `np.dot(A, B)` → Computes the **dot product** of two vectors.
- `np.arccos(x)` → Computes **inverse cosine (cos⁻¹ x)** to find the **angle**.
- `np.degrees(x)` → Converts **radians** to **degrees**.

---

## **📝 Summary Table of Formulas**
| Operation | Formula |
|-----------|---------|
| **Norm (Magnitude)** | \( ||A|| = \sqrt{A_1^2 + A_2^2 + A_3^2} \) |
| **Dot Product** | \( A \cdot B = A_1 B_1 + A_2 B_2 + A_3 B_3 \) |
| **Cosine of Angle** | \( \cos{\theta} = \frac{A \cdot B}{||A|| \times ||B||} \) |
| **Scalar Projection** | \( \frac{A \cdot B}{||B||} \) |
| **Vector Projection** | \( \left(\frac{A \cdot B}{||B||^2}\right) B \) |
| **Perpendicular Vectors** | \( A \cdot B = 0 \Rightarrow A \perp B \) |
| **Unit Vector** | \( \hat{A} = \frac{A}{||A||} \) |
| **Angle Between Vectors** | \( \theta = \cos^{-1} \left(\frac{A \cdot B}{||A|| \times ||B||} \right) \) |

---




