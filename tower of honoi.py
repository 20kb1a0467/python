def tower_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        tower_of_hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n - 1, auxiliary, target, source)

# Example usage:
tower_of_hanoi(3, 'A', 'C', 'B')
