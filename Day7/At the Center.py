# Enter your code here. Read input from STDIN. Print output to STDOUT
def closest_k_people():
    N = int(input())
    people = []
    for _ in range(N):
        x, y = map(int, input().split())
        dist_sq = x**2 + y**2
        people.append((dist_sq, x, y))

    K = int(input())

    people.sort()

    for i in range(K):
        print(people[i][1], people[i][2])

closest_k_people()