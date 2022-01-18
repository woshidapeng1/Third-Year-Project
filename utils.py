# -*- coding:utf-8 -*-
import torch
import csv
import numpy as np
import pandas as pd


class KMEANS():
    def __init__(self, n_clusters = 20, max_iter = None, verbose = True, device = torch.device("cpu")):
        print('Calculating K-means...')
        self.n_clusters = n_clusters
        self.labels = None
        self.dists = None
        self.centers = None
        self.variation = torch.Tensor([float("Inf")]).to(device)
        self.verbose = verbose
        self.started = False
        self.representative_samples = None
        self.max_iter = max_iter
        self.count = 0
        self.device = device

    def fit(self, x):
        x = torch.from_numpy(x).to(self.device)
        init_row = torch.randint(0, x.shape[0], (self.n_clusters,)).to(self.device)
        init_points = x[init_row]
        self.centers = init_points
        while True:
            self.nearest_center(x)

            self.update_center(x)
            if self.verbose:
                print(self.variation, torch.argmin(self.dists, (0)))
            if torch.abs(self.variation) < 1e-3 and self.max_iter is None:
                break
            elif self.max_iter is not None and self.count == self.max_iter:
                break

            self.count += 1

        self.representative_sample()
        return self.labels

    def nearest_center(self, x):
        labels = torch.empty((x.shape[0],)).long().to(self.device)
        dists = torch.empty((0, self.n_clusters)).to(self.device)
        for i, sample in enumerate(x):
            dist = torch.sum(torch.mul(sample - self.centers, sample - self.centers), dim = 1)
            labels[i] = torch.argmin(dist)
            dists = torch.cat([dists, dist.unsqueeze(0)], 0)
        self.labels = labels
        if self.started:
            self.variation = torch.sum(self.dists - dists)
        self.dists = dists
        self.started = True

    def update_center(self, x):
        centers = torch.empty((0, x.shape[1])).to(self.device)
        for i in range(self.n_clusters):
            mask = self.labels == i
            cluster_samples = x[mask]
            centers = torch.cat([centers, torch.mean(cluster_samples, (0)).unsqueeze(0)])
        self.centers = centers

    def representative_sample(self):
        self.representative_samples = torch.argmin(self.dists, (0))

def FS():
    print('Calculating Friendship Similarity...')
    path = './sigcomm2009/friends2.csv'
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    del rows[0]
    data = np.array(rows, dtype = 'uint8')

    Fij = np.zeros([76, 76])
    Fi = np.zeros([76, 1])
    for i in range(76):
        Fi[i] = len(data[np.where(data[:, 0] == i + 1)])

    for i in range(data.shape[0]):
        for j in range(data.shape[0]):
            if i != j:
                if data[j, 1] == data[i, 1]:
                    Fij[data[i, 0] - 1, data[j, 0] - 1] += 1

    Tfs = np.zeros([76, 76])
    for i in range(76):
        for j in range(76):
            if Fi[i] == 0 or Fi[i] == 1:
                continue
            else:
                Tfs[i, j] = Fij[i, j] / (Fi[i] - 1)

    return Tfs / 2


def CoI():
    print('Calculating Community of Interest...')
    path = './sigcomm2009/interests1.csv'
    with open(path) as csvfile1:
        reader1 = csv.reader(csvfile1)
        rows1 = [row for row in reader1]
        csvfile1.close()
    del rows1[0]
    data1 = np.array(rows1, dtype = 'uint8')

    path = './sigcomm2009/interests2.csv'
    with open(path) as csvfile2:
        reader2 = csv.reader(csvfile2)
        rows2 = [row for row in reader2]
        csvfile2.close()
    del rows2[0]
    data2 = np.array(rows2, dtype = 'uint8')

    Cij = np.zeros([76, 76])
    Ci = np.zeros([76, 1])
    for i in range(76):
        Ci[i] = len(data1[np.where(data1[:, 0] == i + 1)]) + len(data2[np.where(data2[:, 0] == i + 1)])

    for i in range(data1.shape[0]):
        for j in range(data1.shape[0]):
            if i != j:
                if data1[j, 1] == data1[i, 1]:
                    Cij[data1[i, 0] - 1, data1[j, 0] - 1] += 1
    for i in range(data2.shape[0]):
        for j in range(data2.shape[0]):
            if i != j:
                if data2[j, 1] == data2[i, 1]:
                    Cij[data2[i, 0] - 1, data2[j, 0] - 1] += 1
    Cij = Cij / 2

    Tcoi = np.zeros([76, 76])
    for i in range(76):
        for j in range(76):
            if Ci[i] == 0 or Ci[i] == 1:
                continue
            else:
                Tcoi[i, j] = Cij[i, j] / Ci[i]

    return Tcoi


def CoP():
    print('Calculating Cooperativeness...')
    path = './sigcomm2009/transmission.csv'
    pd_data = pd.read_csv(path, encoding = 'big5')
    pd_data = pd_data.iloc[0:, :]
    data = pd_data.to_numpy()

    Tp = np.zeros([76, 76])
    Tp[data[:, 3] - 1, data[:, 4] - 1] += data[:, 2]
    for i in range(76):
        if np.sum(Tp[i, :]) == 0:
            continue
        else:
            Tp[i, :] = Tp[i, :] / np.sum(Tp[i, :])

    Tcop = np.zeros([76, 76])
    for i in range(76):
        for j in range(76):
            if Tp[i, j] == 0 or Tp[i, j] == 1:
                continue
            else:
                Tcop[i, j] = - Tp[i, j] * np.log(Tp[i, j]) - (1 - Tp[i, j]) * np.log(1 - Tp[i, j])

    return Tcop


def Reward():
    print('Calculating Reward...')
    path = './sigcomm2009/transmission.csv'
    pd_data = pd.read_csv(path, encoding = 'big5')
    pd_data = pd_data.iloc[0:, :]
    data = pd_data.to_numpy()

    Int = np.zeros([76, 76])
    IntU = np.zeros([76, 76])
    for i in range(data.shape[0]):
        Int[data[i, 3] - 1, data[i, 4] - 1] += 1
        IntU[data[i, 3] - 1, data[i, 4] - 1] += data[i, 6]

    Treward = np.zeros([76, 76])
    for i in range(76):
        for j in range(76):
            if Int[i, j] == 0:
                continue
            else:
                Treward[i, j] = (Int[i, j] - (IntU[i, j])) / Int[i, j] * np.exp(- IntU[i, j] / Int[i, j])

    return Treward
