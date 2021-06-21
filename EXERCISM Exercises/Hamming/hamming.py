def distance(strand_a, strand_b):
<<<<<<< HEAD
    if len(strand_a) != len(strand_b):
        raise ValueError ("Strand A Does Not Equal To Strand B")

    return len([[x,y] for x,y in zip(strand_a, strand_b) if x != y])

=======
    if len (strand_a) != len (strand_b):
        raise ValueError("Error")
    return len ([[x,y] for x,y in zip(strand_a, strand_b) if x != y])
>>>>>>> 9122ec3683dc29979c572b8b34b6561343c1ae65
