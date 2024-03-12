from matplotlib import pyplot as plt
from dataclasses import dataclass
from tkinter import *
import time,random

FIELD_X,FIELD_Y =40,40
CELL_SIZE = 20

ix = 0
iy = 0
idm = 0
yn = FIELD_X*FIELD_Y+2

#グラフ作成用

y = [1]

@dataclass
class Agent:
    id: int
    x: int
    y: int
    vx: int
    vy: int
    status: str
    profile: int #影響度
    bond:list #ノード
    time:int #そのターンに新しい情報を受け取ったかどうか
    sens:int #情報の信じやすさ
    interest:int #興味度
    
    
def move(agents):
    for i in agents:
        if i.id >= 0:
            i.vx = random.randint(-1, 1)
            i.vy = random.randint(-1, 1)


#シミュレーション開始時描画       
def srender(agent):
    x = agent.x * CELL_SIZE
    y = agent.y * CELL_SIZE
    if agent.status == "Normal":
        canvas.create_rectangle(
            x, y, x + CELL_SIZE, y + CELL_SIZE,
            outline="black", fill="blue")
        #if agent.x==10 and agent.y==10:
        #    print("ok")
    if agent.status == "True":
        canvas.create_rectangle(
            x, y, x + CELL_SIZE, y + CELL_SIZE,
            outline="black", fill="yellow")
        agent.time =0
    if agent.status == "Doubt":
        canvas.create_rectangle(
            x, y, x + CELL_SIZE, y + CELL_SIZE,
            outline="black", fill="red")
        agent.time =0
        
#エージェント状態描画    
def render(agent,tm):
    x = agent.x * CELL_SIZE
    y = agent.y * CELL_SIZE
    if agent.status == "True" and agent.time == 1:
        canvas.create_rectangle(
            x, y, x + CELL_SIZE, y + CELL_SIZE,
            outline="black", fill="yellow")
        agent.time = 0
        tm -= 1
        #sprint("T")
    if agent.status == "Doubt" and agent.time == 1:
        canvas.create_rectangle(
            x, y, x + CELL_SIZE, y + CELL_SIZE,
            outline="black", fill="red")
        agent.time = 0
        tm += 1
    return tm
        #print("D")

def update(agent,agents):
    if agent.status == "Doubt" and agent.time == 0:
        for b in agent.bond:
            if agents[b].status == "Normal":
                if random.randint(0,100) < agent.profile:
                    agents[b].status = "Doubt"
                    agents[b].time = 1
        #profile = 50 の場合、拡散範囲拡大
        if agent.profile == 50:
            around = [agent.id-1,agent.id+1,agent.id+FIELD_X-1,agent.id+FIELD_X,agent.id+FIELD_X+1,
                      agent.id-FIELD_X-1,agent.id-FIELD_X,agent.id-FIELD_X+1,agent.id-2,agent.id+2,agent.id+FIELD_X-2,agent.id+2*FIELD_X,agent.id+FIELD_X+2,
                      agent.id-FIELD_X-2,agent.id-2*FIELD_X,agent.id-FIELD_X+2]     
        if agent.id % FIELD_X == 0:
            around = [agent.id+1,agent.id+FIELD_X,agent.id+FIELD_X+1,
                  agent.id-FIELD_X,agent.id-FIELD_X+1]
        elif agent.id % FIELD_X == FIELD_X-1:
            around = [agent.id-1,agent.id+FIELD_X-1,agent.id+FIELD_X,
                      agent.id-FIELD_X-1,agent.id-FIELD_X]       
        else:
            around = [agent.id-1,agent.id+1,agent.id+FIELD_X-1,agent.id+FIELD_X,agent.id+FIELD_X+1,
                      agent.id-FIELD_X-1,agent.id-FIELD_X,agent.id-FIELD_X+1]      
        for n in around:
            if 0 < n and n < FIELD_X*FIELD_Y + 3:
                if agents[n].status == "Normal":
                    if random.randint(0,100) < agent.profile:
                        agents[n].status = "Doubt"
                        agents[n].time = 1
    elif agent.status == "True" and agent.time == 0:
        for b in agent.bond:
            if agents[b].status == "Normal" or agents[b].status == "Doubt":
                if random.randint(0,100) < agent.profile:
                    agents[b].status = "True"
                    agents[b].time = 1
        #profile = 50 の場合、拡散範囲拡大
        if agent.profile == 50:
            around = [agent.id-1,agent.id+1,agent.id+FIELD_X-1,agent.id+FIELD_X,agent.id+FIELD_X+1,
                      agent.id-FIELD_X-1,agent.id-FIELD_X,agent.id-FIELD_X+1,agent.id-2,agent.id+2,agent.id+FIELD_X-2,agent.id+2*FIELD_X,agent.id+FIELD_X+2,
                      agent.id-FIELD_X-2,agent.id-2*FIELD_X,agent.id-FIELD_X+2]     
        if agent.id % FIELD_X == 0:
            around = [agent.id+1,agent.id+FIELD_X,agent.id+FIELD_X+1,
                  agent.id-FIELD_X,agent.id-FIELD_X+1]
        elif agent.id % FIELD_X == FIELD_X-1:
            around = [agent.id-1,agent.id+FIELD_X-1,agent.id+FIELD_X,
                      agent.id-FIELD_X-1,agent.id-FIELD_X]
        else:
            around = [agent.id-1,agent.id+1,agent.id+FIELD_X-1,agent.id+FIELD_X,agent.id+FIELD_X+1,
                      agent.id-FIELD_X-1,agent.id-FIELD_X,agent.id-FIELD_X+1] 
            #if agent.id == 500:
                #print("else")
                #print(around)
        for n in around:
            if 0 < n and n < FIELD_X*FIELD_Y+3:
                #if agent.id == 500 and agents[n].status == "Doubt":
                    #print(n)
                    
                if agents[n].status == "Normal"or agents[n].status == "Doubt":
                    if random.randint(0,100) < agent.profile:
                        agents[n].status = "True"
                        #if agent.id == 500:
                        #   print(n)
                        agents[n].time = 1

def check(agents):
    for i in agents:
        print(i)

def checkf(agents):
    for i in agents:
        if i.x < 0 or i.x >= FIELD_X or i.y < 0 or i.y >= FIELD_Y:
            print(i)

def checkd(agents):
    for i in agents:
        if i.status != "True":
            print(i)

def checkpf(agents):
    for i in agents:
        if i.profile == 50:
            print(i)
            
def nrandom(x,y):
    #ランダムにノードを追加
    #bond = random.sample(range(x*y+3),10)
    #ノードなし
    bond = []
    return bond


def prandom():
    a = random.randint(0,100)
    if a > 99:
        return 50
    elif a > 60:
        return 3
    elif a > 10:
        return 5
    else:
        return 1


tk = Tk()
canvas = Canvas(tk, width=CELL_SIZE * FIELD_X, height=CELL_SIZE * FIELD_Y)
canvas.pack()

agents = [
    Agent(0, 0, 0, 0, 0, "Normal",prandom(),nrandom(FIELD_X,FIELD_Y),0,0,0),
    Agent(1, 0, 1, 0, 0, "Normal",prandom(),nrandom(FIELD_X,FIELD_Y),0,0,0),
    Agent(2, 0, 2, 0, 0, "Normal",prandom(),nrandom(FIELD_X,FIELD_Y),0,0,0)
    #random.randint(0,100)
]

def cragentst(agents,x,y):
    r = 0
    q = 3
    p = 3
    for i in range(x):
        for c in range(y):
            agent = Agent(p,r,q,0,0,"Normal",prandom(),nrandom(x,y),0,0,0)
            agents.append(agent)
            p += 1
            q += 1
            if q > y-1:
                q = 0
        r += 1


#エージェント作成
cragentst(agents,FIELD_X,FIELD_Y)

#中央から
#rdt = int((FIELD_X*FIELD_Y)/2)+int(FIELD_Y/2)
#agents[rdt].status = "Doubt"
#agent[10]から
#agents[0].status = "Doubt"


#ランダムなエージェント指定
#rdt = random.randint(0,FIELD_X*FIELD_Y-1)
rdt = FIELD_X*FIELD_Y//2 + FIELD_X//2
agents[rdt].status = "Doubt"
#print(agents[rdt])

#ランダムなエージェント指定(True)
#rdt = random.randint(0,FIELD_X*FIELD_Y-1)
#agents[rdt].status = "True"
#print(agents[rdt])

#中央から(True)
#agents[int((FIELD_X*FIELD_Y)/2)+int(FIELD_Y/2)].status = "True"
#agents[0].status = "True"


#print("Doubt:")
#print(agents[rdt])
#around = [agents[rdt].id-1,agents[rdt].id+1,agents[rdt].id+FIELD_X-1,agents[rdt].id+FIELD_X,agents[rdt].id+FIELD_X+1,
                      #agents[rdt].id+FIELD_Y-1,agents[rdt].id+FIELD_Y,agents[rdt].id+FIELD_Y+1]
#around = [agents[rdt].id-1,agents[rdt].id+1,agents[rdt].id+FIELD_X-1,agents[rdt].id+FIELD_X,agents[rdt].id+FIELD_X+1,
#                      agents[rdt].id-FIELD_X-1,agents[rdt].id-FIELD_X,agents[rdt].id-FIELD_X+1] 
#print(rdt)          
#for n in around:
#    print(n)
#    agents[n].status = "Doubt"

#check(agents)

#一体のエージェントの影響度をprofileを 50 かつ拡散範囲拡大
#rpt = random.randint(0,FIELD_X*FIELD_Y-1)
#rpt = FIELD_X*FIELD_Y//2 + FIELD_X//2
#print("rpt:")
#print(rpt)
#agents[rpt].profile = 50


#checkpf(agents)

do = 0
f = 0
#print(agents[0])
for agent in agents:
    srender(agent)
tk.update()
time.sleep(1) 
    
#check(agents)
t = FIELD_X*60
xn = 0
total = 0
#True時
start = time.time()
for x in range(t):
    tm = 0
    move(agents)
    for agent in agents:
        update(agent,agents)
        tm = render(agent,tm)   
    tk.update()
    #全エージェントがデマ情報を持った場合に訂正情報を流す
    if (x == t/2 or total == FIELD_X*FIELD_Y+1)and f == 0:
    #2.5割のエージェントがデマ情報を持った場合に訂正情報を流す
    #if (x == t/2 or total > (FIELD_X*FIELD_Y+1)//6)and f == 0:

        f = 1
        #agents[0].status = "True"
        #agents[random.randint(0,FIELD_X*FIELD_Y-1)].status = "True"

        #デマ情報を流したエージェントから訂正情報を流す場合
        #start = time.time()
        #agents[rdt].status = "True"
        #agents[rdt].time = 1
        #render(agents[rdt],tm)
        
        #ランダムなエージェントが訂正情報を流す
        #ret = random.randint(0,FIELD_X*FIELD_Y-1)
        #agents[ret].status = "True"
        #agents[ret].time = 1
        #print("True:")
        #print(agents[ret])
        #render(agents[ret],tm)
        #print(agents[ret])

        #固定のエージェントが流す(テスト)
        kgent = FIELD_X*FIELD_Y//2 + FIELD_X//2
        agents[kgent].status = "True"
        agents[kgent].time = 1
        render(agents[kgent],tm)
        yn = x
    #time.sleep(0.1)
    total += tm
    xn += 1
    y.append(total)
    #if total < 10:
        #print("pt")
        #print(total)
    if (x > yn and total <= 0) or total == -(FIELD_X*FIELD_Y+1):
        end = time.time()
        print("time:")
        print(end - start)
        break

canvas.delete("all")
x = list(range(xn+1))
plt.plot(x,y)
plt.show()
#checkd(agents)
tk.mainloop()
