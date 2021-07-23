import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

num = input("자애로운 자여, 몇 명이나 먹이려고 하는고?")
result = 1;

print("그렇다면 ",result,"마리를 시키거라!")
print("능히",num,"명을 먹이는데 부족함이 없느니라.")
