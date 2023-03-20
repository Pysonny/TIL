import sys
sys.stdin = open('input.txt','r')


grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for t in range(1,int(input())+1):
    N, K = map(int,input().split())
    s_score = []
    for i in range(N):
        i_score = list(map(int,input().split()))
        score = i_score[0]*0.35 + i_score[1]*0.45 + i_score[2]*0.2
        s_score.append(score)       
    
    k_score = s_score[K-1] # K 학생 인덱스
    s_score.sort(reverse=True)

    

    # print(f'#{t} {s_grade})