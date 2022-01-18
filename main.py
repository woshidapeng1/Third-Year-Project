# -*- coding:utf-8 -*-
import torch
import numpy as np
import matplotlib.pyplot as plt
import os
from utils import KMEANS, FS, CoI, CoP, Reward
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

Tfs = FS()
Tcoi = CoI()
Tcop = CoP()
Treward = Reward()
Tfs = np.reshape(Tfs, (-1, 1), order = 'C')
Tcoi = np.reshape(Tcoi, (-1, 1), order = 'C')
Tcop = np.reshape(Tcop, (-1, 1), order = 'C')
Treward = np.reshape(Treward, (-1, 1), order = 'C')
feature_pair = np.hstack((Tfs, Tcoi))

n_clusters = 3
max_iter = 10
kmeans = KMEANS(n_clusters = n_clusters, max_iter = max_iter, verbose = False, device = device)

labels = kmeans.fit(feature_pair)
labels_img = labels.cpu().numpy()
colors = ['b', 'g', 'r']
marker = ['.', '*', 'v']

numbers = np.zeros([n_clusters, 1])
for i in range(n_clusters):
    numbers[i] = len(labels_img[np.where(labels_img == i)])
    index = np.where(labels_img == i)
    x = Tfs[index]
    y = Tcoi[index]
    if i == 0:
        l0 = plt.scatter(x, y, s = 300, marker = marker[i], cmap = colors[i])
    elif i == 1:
        l1 = plt.scatter(x, y, s = 300, marker = marker[i], cmap = colors[i])
    else:
        l2 = plt.scatter(x, y, s = 300, marker = marker[i], cmap = colors[i])

plt.xlabel('Friendship Similarity')
plt.ylabel('Community-of-Interest')
plt.legend((l2, l1, l0), ('Untrustworthy', 'Trustworthy', 'Neutral'))
plt.savefig('FS-COI.jpg')
plt.show()


# Trust
DirectTrust = int(input())

T = numbers[0]
U = numbers[1]
N = numbers[2]
recommendations = [T, U, N]

# T,U,N are the number of trusted nodes after clustering; the number of untrusted nodes; the number of neutral nodes.

threshold = 0.5
# change the value of treshold to 0.5;0.6;0.7;0.8;0.9

if recommendations == []:
    print(DirectTrust)

if DirectTrust == 0:
    if U >= T or (N >= T and N >= U):
        print(0)
    else:
        PT = T / U + T + N + 1
        if PT >= threshold:
            print(1)
        else:
            print(0)
elif DirectTrust == 1:
    if T >= U or (N >= T and N >= U):
        print(1)
    else:
        PU = U / U + T + N + 1
        if PU >= threshold:
            print(0)
        else:
            print(1)
elif DirectTrust == 2:
    if T > U:
        print(1)
    else:
        print(0)


