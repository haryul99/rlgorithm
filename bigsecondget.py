n,m,k = map(int, input().split()) # n은 배열의 개수이다.
array = list(map(int, input().split()))

array.sort() # 정렬
first = array[n-1] # 가장 큰 수 얻음
second = array[n-2] # 그 다음 큰 수

'''
while True:
    for i in range(k): #k 만큼 돌고 while문 덕분에 m이 0이 아닌 이상 second를 거치고 다시 시작
        if m == 0 :
            break # m이 0이면 for문 종료
        result += first
        m -= 1
    if m == 0 :
        break # m이 0이면 while문 종료
    result += second # range(k)가 끝나고 m이 0이 아닐 때 수행
    m -= 1 # 더한 횟수 빼기
'''

cycle = (first * k) + second
a = m//(k+1)
b = m % (k+1)
d = b * first 

result =(a*cycle) + d  
print(result) 