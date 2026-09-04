valid_bases = {"A", "G", "C", "T"}

DNA_samples = []

number = int(input(f"How many DNA samples do you want to enter? "))

for i in range(number):

    DNA = input(f"Enter your DNA sample { i + 1 }: ").upper()


    while not DNA or not set(DNA).issubset(valid_bases):
        print(f"Invalid DNA!")
        DNA = input(f"Enter your DNA sample { i + 1 } again: ").upper()

    DNA_samples.append(DNA)

results = []

for DNA in DNA_samples:

    G = 0
    A = 0
    C = 0
    T = 0

    for base in DNA:
        if base == "A":
             A += 1
        elif base == "G":
            G += 1
        elif base == "C":
            C += 1
        elif base == "T":
            T += 1

    length = len(DNA)

    GC = ((G+C)/ length * 100)

    complement = ""

    for base in DNA:

        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
    sample = {
    "DNA": DNA,
    "Length": length,
    "A_Count": A,
    "T_Count": T,
    "G_Count": G,
    "C_Count": C,
    "GC_Content": GC,
    "Complement": complement
    } 

    results.append(sample)

print("\n ------|DNA ANALYSIS RESULTS|------")

for i, sample in enumerate(results, start=1):
    print(f"\nSample {i}")
    print(f"DNA: {sample['DNA']}")
    print(f"Length: {sample['Length']}")
    print(f"A: {sample['A_Count']}")
    print(f"T: {sample['T_Count']}")
    print(f"G: {sample['G_Count']}")
    print(f"C: {sample['C_Count']}")
    print(f"GC Content: {sample['GC_Content']:.2f}%")
    print(f"Complement: {sample['Complement']}")
