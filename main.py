def findDoubles(w):
    for i in w:
        if w.count(i) > 1:
            return True
    return False

print(findDoubles("y"))
