'''
4:28~
장르 별로 가장 많이 재생된 노래를 두 개씩 모아

{장르: [[[고유번호1, 횟수1]],총횟수]}
속한 노래가 많이 재생된 장르
장르 내에서 많이 재생된 노래
장르 내에서 재생 횟수가 같은 노래 중 고유번호가 낮은 노래
'''
def solution(genres, plays):
    answer = []
    album = dict()
    for i, (g, p) in enumerate(zip(genres, plays)):
        try:
            album[g][1] += p
            album[g][0].append([i, p])
        except KeyError:
            album[g] = [[[i, p]], p]
    album = album.values()
    album = sorted(album, reverse=True, key=lambda x: x[1])
    print(album)
    for songs in album:
        tmp = songs[0]
        tmp.sort()
        tmp.sort(reverse=True, key=lambda x: x[1])
        if len(tmp) < 2:
            answer.append(tmp[0][0])
        else:
            answer.append(tmp[0][0])
            answer.append(tmp[1][0])
            
    return answer