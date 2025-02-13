def subtract_until_less(M, N):
    if M < N:
        return M
    else:
        while M >= N:
            M -= N
        return M
        
print(subtract_until_less(10,15))
print(subtract_until_less(15,15))
print(subtract_until_less(15,10))
