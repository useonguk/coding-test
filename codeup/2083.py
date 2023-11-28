n, s = map(int, input().split())
values = list(map(int, input().split()))

id = 0
start=0
end = n

while start <= end:
    id = (start + end) // 2
    if values[id] == s :
        print(id + 1)
        break
    elif values[id] > s:
        end = id-1
    else :
        start = id+1

else :
    print(-1)
