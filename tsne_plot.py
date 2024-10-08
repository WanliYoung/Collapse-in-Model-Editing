import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE


collapse_keys_without_prefix = []
collapse_keys_with_prefix = []
normal_keys_without_prefix = []
normal_keys_with_prefix = []

# load tensors
directory = './collapse_path/keys_without_prefix/'
for filename in os.listdir(directory):
    if filename.endswith('.npy'):
        file_path = os.path.join(directory, filename)
        tensor = np.load(file_path)
        collapse_keys_without_prefix.append(tensor.flatten())

directory = './normal_path/keys_without_prefix/'
for filename in os.listdir(directory):
    if filename.endswith('.npy'):
        file_path = os.path.join(directory, filename)
        tensor = np.load(file_path)
        normal_keys_without_prefix.append(tensor.flatten())

directory = './collapse_path/keys_with_prefix/'
for filename in os.listdir(directory):
    if filename.endswith('.npy'):
        file_path = os.path.join(directory, filename)
        tensor = np.load(file_path)
        collapse_keys_with_prefix.append(tensor.flatten())

directory = './normal_path/keys_with_prefix/'
for filename in os.listdir(directory):
    if filename.endswith('.npy'):
        file_path = os.path.join(directory, filename)
        tensor = np.load(file_path)
        normal_keys_with_prefix.append(tensor.flatten())

uni_tensors = collapse_keys_without_prefix + normal_keys_without_prefix + collapse_keys_with_prefix + normal_keys_with_prefix

uni_data = np.stack(uni_tensors)

# project into two-dimensional space
tsne = TSNE(n_components=2, random_state=42)
embedded_uni_data = tsne.fit_transform(uni_data)

idx1 = len(collapse_keys_without_prefix)
idx2 = idx1 + len(normal_keys_without_prefix)
idx3 = idx2 + len(collapse_keys_with_prefix)
idx4 = idx3 + len(normal_keys_with_prefix)

plt.scatter(embedded_uni_data[:idx1, 0], embedded_uni_data[:idx1, 1], c='red', label='Collapse '+'$k^{u}$')
plt.scatter(embedded_uni_data[idx1:idx2, 0], embedded_uni_data[idx1:idx2, 1], c='black', label='Normal '+'$k^{u}$')
plt.scatter(embedded_uni_data[idx2:idx3, 0], embedded_uni_data[idx2:idx3, 1], c='blue', label='Collapse '+'$\overline{k}$')
plt.scatter(embedded_uni_data[idx3:idx4, 0], embedded_uni_data[idx3:idx4, 1], c='purple', label='Normal '+'$\overline{k}$')

plt.legend()

plt.savefig("./xxx.png")
plt.close()