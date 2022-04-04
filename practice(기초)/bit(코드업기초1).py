# https://codeup.kr/problem.php?id=6084
# 6084 : 소리 파일 저장용량 계산하기

'''
1초 동안 마이크로 소리강약을 체크하는 횟수를 h
(헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)

한 번 체크한 값을 저장할 때 사용하는 비트수를 b
(2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)

좌우 등 소리를 저장할 트랙 개수인 채널 개수를 c
(모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)

녹음할 시간(초) s가 주어질 때,

필요한 저장 용량을 계산하는 프로그램을 작성해보자.
'''

h, b, c, s = map(int, input().split())

bit = h * b * c * s         # 총 비트 계산
byte = bit / 8              # 비트 -> 바이트(8비트는 1바이트)
kbyte = byte / 1024         # 바이트 -> 킬로바이트
mbyte = kbyte / 1024        # 킬로바이트 -> 메가바이트

'''
8 bit(비트)          = 1byte(바이트)     # 8bit=1Byte
1024 Byte(210 byte)  = 1KB(킬로 바이트)  # 1024Byte=1KB
1024 KB(210 KB)      = 1MB(메가 바이트)
1024 MB(210 MB)      = 1GB(기가 바이트)
1024 GB(210 GB)      = 1TB(테라 바이트)
'''

print('%0.1f MB' % mbyte)   # 문자열 포매팅을 사용하여 소수점 첫 째 자리까지 출력
