A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

sum = 0
for score in A:
    if score >= 50:
        print(f"score: ",score)
        sum += score
    
print(sum)