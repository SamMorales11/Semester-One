kodon = input("Masukkan kodon = ").split()
penerjemah_kodon = {
    "AUG" : "Methionine",
    "UUU" : "Phenylalanine",
    "UUC" : "Phenylalanine",
    "UUA" : "Leucine",
    "UUG" : "Leucine",
    "UCU" : "Serine",
    "UCC" : "Serine",
    "UCA" : "Serine",
    "UCG" : "Serine",
    "UAU" : "Tyroxsine",
    "UAC" : "Tyroxsine",
    "UGU" : "Tyroxsine",
    "UAC" : "Tyroxsine",
    "UGG" : "Tryptophan",
}
for protein in kodon:
    if protein in penerjemah_kodon:
        print(penerjemah_kodon.get(protein))
    else:
        print(f"{protein} bukan protein")