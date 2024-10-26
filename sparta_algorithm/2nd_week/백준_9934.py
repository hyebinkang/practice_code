# 입력 -> K = depth, 리스트

# 로직: 그래프로 그린 다음 로테이션, 완전 이진 트리의 특성을 이용하는 방법


# 출력 -> 이진트리 모양으로
# 완전 이진 트리? 노드 하나당 두 개의 자식 노드를 갖는 트리
# 좌우 대칭적


# 그래프를 코드로 표현하는 방법 ->

def 완전이진트리(k, buildings):
    def 빌딩트리(buildings, depth):

        mid = len(buildings)//2
        building_level[depth].append(buildings[mid])

        #왼쪽 오른쪽 각각 새로운 빌딩 리스트로 간주하고 재귀적 호출
        빌딩트리(buildings[:mid], depth+1)
        빌딩트리(buildings[mid+1:], depth+1)


    # 각 레벨에 해당하는 빌딩 번호를 저장할 리스트
    building_level=[[] for _ in range(k)]
    빌딩트리(buildings, 0)

    for build_level in building_level:
        print(" ".join(map(str, build_level)))


k = int(input())
buildings = list(map(int, input().split()))

완전이진트리(k, buildings)