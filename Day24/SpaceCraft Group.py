def spaceship_fleets(k, pos, speed):
    """
    Write your logic here.
    Parameters:
        k (int): Distance of the star system from Earth
        pos (list): List of integers representing the current distance of each spaceship from Earth
        speed (list): List of integers representing the speed of each spaceship
    Returns:
        int: Number of spacecraft fleets that will arrive at the destination
    """
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer 'n'
    k = int(data[1])  # Second input is the integer 'k'
    pos = list(map(int, data[2:n+2]))  # Third input is the array of current distances
    speed = list(map(int, data[n+2:2*n+2]))  # Fourth input is the array of speeds
    
    # Call user logic function and print the output
    result = spaceship_fleets(k, pos, speed)
    print(result)

if __name__ == "__main__":
    main()