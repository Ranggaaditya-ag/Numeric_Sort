#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Baca data dari file CSV ke dalam DataFrame
df = pd.read_csv('Data Sort.csv')


# In[2]:


# Fungsi untuk radix sort
def radix_sort(arr):
    max_num = max(arr)  # Menemukan nilai maksimum dalam array
    exp = 1
    while max_num // exp > 0:  # Loop hingga semua digit diurutkan
        counting_sort(arr, exp)  # Memanggil fungsi counting_sort untuk mengurutkan berdasarkan digit ke-exp
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Membuat array kosong untuk menyimpan hasil pengurutan
    count = [0] * 10  # Membuat array untuk menghitung frekuensi setiap digit

    # Menghitung frekuensi setiap digit pada kolom saat ini
    for i in range(n):
        index = (arr[i] // exp)  # Mengambil digit ke-exp dari angka
        count[index % 10] += 1

    # Menghitung jumlah kumulatif frekuensi
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)  # Mengambil digit ke-exp dari angka
        output[count[index % 10] - 1] = arr[i]  # Menempatkan angka ke posisi yang sesuai dalam output
        count[index % 10] -= 1
        i -= 1

    # Menyalin hasil pengurutan dari output ke array asli
    for i in range(n):
        arr[i] = output[i]

# Mengurutkan kolom tanpa nama menggunakan radix sort
radix_sort(df.iloc[:, 0].values)

# Menampilkan DataFrame yang telah diurutkan
print(df)


# In[3]:


#Fungsi Untuk Counting Sort

# Ambil kolom data yang akan diurutkan menjadi array
arr_to_sort = df.iloc[:, 0].values

# Fungsi Counting Sort
def counting_sort(arr):
    # Mencari nilai maksimum dalam array
    max_num = max(arr)
    
    # Membuat array untuk menghitung frekuensi setiap elemen
    count = [0] * (max_num + 1)
    
    # Menghitung frekuensi setiap elemen dalam array
    for num in arr:
        count[num] += 1
    
    # Membuat array baru untuk menyimpan hasil pengurutan
    sorted_arr = []
    
    # Memasukkan elemen sesuai dengan frekuensinya
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

# Memanggil fungsi counting_sort untuk mengurutkan array
sorted_arr = counting_sort(arr_to_sort)

# Mengganti kolom dalam DataFrame dengan array yang sudah diurutkan
df.iloc[:, 0] = sorted_arr

# Menampilkan DataFrame yang sudah diurutkan
print(df)


# In[4]:


#Fungsi Untuk Bucket Sort

# Ambil kolom data yang akan diurutkan menjadi array
arr_to_sort = df.iloc[:, 0].values

# Fungsi Bucket Sort
def bucket_sort(arr):
    # Menentukan jumlah ember (bucket) yang akan digunakan
    num_buckets = 10  # Anda bisa menyesuaikan jumlah ember sesuai kebutuhan
    
    # Menentukan batasan atas (range) setiap ember
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value + 1) / num_buckets
    
    # Membuat ember kosong
    buckets = [[] for _ in range(num_buckets)]
    
    # Menempatkan setiap elemen dalam ember yang sesuai
    for num in arr:
        index = int((num - min_value) / bucket_range)
        buckets[index].append(num)
    
    # Mengurutkan masing-masing ember
    sorted_buckets = []
    for bucket in buckets:
        sorted_buckets.extend(sorted(bucket))
    
    return sorted_buckets

# Memanggil fungsi bucket_sort untuk mengurutkan array
sorted_arr = bucket_sort(arr_to_sort)

# Mengganti kolom dalam DataFrame dengan array yang sudah diurutkan
df.iloc[:, 0] = sorted_arr

# Menampilkan DataFrame yang sudah diurutkan
print(df)


# In[ ]:




