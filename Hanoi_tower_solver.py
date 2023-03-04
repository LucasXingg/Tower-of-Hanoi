def solver(layer, start='left', midway='middle', destination='right', sequence=[]):
    if layer == 1:
        sequence.append((start, destination))
    else:
        sequence = solver(layer-1, start, destination, midway, sequence)
        sequence.append((start, destination))
        sequence = solver(layer-1, midway, start, destination, sequence)
    return sequence

if __name__ == "__main__":
    print(solver(4))
    print(solver(4))