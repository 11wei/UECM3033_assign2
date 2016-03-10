import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy as sp


def svd(n):

    #Create a new matrix Sigma
    #Since we know there are no one zero elememts in 3 Sigma
    #keep first n nonzero elements, make all other become zeros
    Sr_new=Sr.copy()
    Sr_new[n:800]=np.zeros_like(Sr_new[n:800])
    Sg_new=Sg.copy()
    Sg_new[n:800]=np.zeros_like(Sg_new[n:800])
    Sb_new=Sb.copy()
    Sb_new[n:800]=np.zeros_like(Sb_new[n:800])

    #create a matrix for dot multiplication
    #change the dimension of Sigma from (800,1) to (800,1000)
    Sr_new= sp.linalg.diagsvd(Sr_new,800,1000)
    Sg_new= sp.linalg.diagsvd(Sg_new,800,1000)
    Sb_new= sp.linalg.diagsvd(Sb_new,800,1000)
    
    r_new=np.dot(np.dot(Ur,Sr_new),Vr)
    g_new=np.dot(np.dot(Ug,Sg_new),Vg)
    b_new=np.dot(np.dot(Ub,Sb_new),Vb)
    
    #Create and display new resolution image
    img[:,:,0]=r_new
    img[:,:,1]=g_new
    img[:,:,2]=b_new
    
    fig2 = plt.figure(2)
    ax1 = fig2.add_subplot(2,2,1)
    ax2 = fig2.add_subplot(2,2,2)
    ax3 = fig2.add_subplot(2,2,3)
    ax4 = fig2.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r_new, cmap = 'Reds')
    ax3.imshow(g_new, cmap = 'Greens')
    ax4.imshow(b_new, cmap = 'Blues')
    plt.show()


 
img=mpimg.imread('SVD.jpg')#Original Image  
[r,g,b] = [img[:,:,i] for i in range(3)]


fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()


#Compute U,Sigma and V for red,greeb,blue matrices
Ur, Sr, Vr = sp.linalg.svd(r)
Ug, Sg, Vg = sp.linalg.svd(g)
Ub, Sb, Vb = sp.linalg.svd(b)
    
#Count how many non zero elements in Sigma respectively
non_zero_red=np.count_nonzero(Sr)
non_zero_green=np.count_nonzero(Sg)
non_zero_blue=np.count_nonzero(Sb)
print("The number of nonzero elements in Sigma of red,green and blue are",
          non_zero_red,",",non_zero_green,"and",non_zero_blue,"respectively.")
    

#Lower resolution picture
print('\nLower resolution picture')
svd(30)

#Better resolution picture
print('\nHigher resolution picture')
svd(200)