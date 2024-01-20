import numpy as np

def ConvertAdjacencyMatrix(A): # input Adjacency Matrix
    A_transpose = np.transpose(A) # transpose Adjacency Matrix 
    n = A.shape[0]  # n = จำนวนหน้าทั้งหมด

    for j in range(n): # แต่ละ column       
      
        k = 0              
        for i in range(n): # k = จำนวนหน้าที่มี link
            if (A_transpose[i][j] == 1):  
                k = k + 1              
        link_p = 0.8/k + 0.2/(n-1); # ความน่าจะเป็นที่จะไปหน้าที่มี link 
        unlink_p = 0.2/(n-1);       # ความน่าจะเป็นสำหรับหน้าที่ไม่มี link
      
        for i in range(n):
            if (A_transpose[i][j] == 1):     # ถ้าหน้า i มี link ไปหน้า j
                A_transpose[i][j] = link_p   
            elif (i != j):                   # ถ้าหน้า i ไม่มี link ไปหน้า j
                A_transpose[i][j] = unlink_p 
      
    return(A_transpose) # Probability Matrix

# exercise 1
A = np.array([[0,0,0,1,0,1,1,0,0,1],
              [0,0,1,0,0,0,1,1,0,0],
              [1,1,0,1,0,1,1,0,0,1],
              [0,1,0,0,0,0,1,0,0,1],
              [0,0,0,1,0,0,1,0,0,0],
              [1,1,0,1,0,0,1,0,0,1],
              [0,0,0,1,0,1,0,0,0,0],
              [0,1,0,1,0,1,1,0,0,1],
              [0,1,1,1,0,1,0,1,0,0],
              [1,0,1,1,0,0,1,1,0,0],],dtype = float) # Adjacency Matrix
print("Adjacency Matrix :\n")
print(A, '\n')

A_prob = ConvertAdjacencyMatrix(A) # ความน่าจะเป็นที่เบราว์เซอร์นำทางไปยังหน้า i จากหน้า j
print("Probability Matrix :\n")
print(np.round(A,4),'\n')

# exercise 2
B = np.array([[0,1,1,1],     
              [1,0,0,0],
              [0,1,0,0],
              [0,1,1,0],], dtype = float) # Adjacency Matrix
print("Adjacency Matrix :\n")
print(B, '\n')

B_prob = ConvertAdjacencyMatrix(B) # ความน่าจะเป็นที่เบราว์เซอร์นำทางไปยังหน้า i จากหน้า j
print("Probability Matrix :\n")
print(np.round(B_prob,4), '\n')

X = np.array([[0],[1],[0],[0]]) # เริ่มต้นที่หน้าที่ 2
for t in range(100):
    X = B_prob @ X
print("vector ความน่าจะเป็นที่ browser จะไปยังแต่ละหน้า :\n")
print(np.round(X,4)) # โอกาสที่จะอยู่บนหน้าใด