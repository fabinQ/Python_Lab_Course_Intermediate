import pickle

data = ["hello", "world", 123]
filename = "data.pickle"

# zapisz dane do pliku binarnego za pomocą pickle
with open(filename, "wb") as f:
    pickle.dump(data, f)

# odczytaj dane z pliku binarnego
with open(filename, "rb") as f:
    loaded_data = pickle.load(f)

# zapisz dane do pliku tekstowego
with open("data.txt", "w") as f:
    for item in loaded_data:
        f.write("%s\n" %item)