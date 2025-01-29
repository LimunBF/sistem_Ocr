import torch
print(torch.cuda.is_available())  # Harus True jika CUDA tersedia
print(torch.cuda.device_count())  # Harus lebih dari 0 jika ada GPU
print(torch.cuda.get_device_name(0))  # Menampilkan nama GPU
