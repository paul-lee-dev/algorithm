import math
import sys

vmax = 1000.0       # 최대 속도
amax = 0.5          # 최대 가속도
MAX_CYCLE = 1024

xdest = 0.0         # 목적지까지의 거리
nlight = 0          # 신호등의 개수
lights = []         # 신호등 목록

speed = []          # speed[i][k]는 신호등 i를 k번째 빨간불이 되는 순간에 통과할 때 가능한 최대 속도를 저장
                    # nlight x MAX_CYCLE 크기의 2차원 리스트

class Light:
    def __init__(self, x, red, green):
        self.x = x
        self.red = red
        self.green = green


# 지정된 행동 Q로 거리 dx를 이동하는 데 필요한 최소 시간을 반환
# Q > 0 인 경우, 초기 속도를 Q로 시작한 후 (최대 vmax까지) 가속
# Q가 음수이면, (정지 상태에서) (-Q)초 동안 대기한 후 가속함을 의미

def find_dt(dx, q):
    assert dx > 0
    v = q if q > 0 else 0.0
    vmax_dt = (vmax - v) / amax
    vmax_dx = v * vmax_dt + 0.5 * amax * vmax_dt * vmax_dt
    if vmax_dx > dx:
        dt = math.sqrt(v * v + 2 * amax * dx) / amax - v / amax
    else:
        dt = vmax_dt + (dx - vmax_dx) / vmax
    # 만약 q가 음수이면, 대기 시간을 추가
    return dt - q if q < 0 else dt

# find_q(dx, dt)
# dx를 dt초 내에 이동해야 할 때, 필요한 초기 행동 Q를 계산

def find_q(dx, dt):
    assert dx > 0 and dt > 0 and dx <= vmax * dt
    tt = math.sqrt(2 * dx / amax)
    if tt * amax > vmax:
        tt = 0.5 * vmax / amax + dx / vmax
    if tt < dt:
        return tt - dt
    q = dx / dt - 0.5 * amax * dt
    if q + dt * amax > vmax:
        q = vmax - math.sqrt(2 * amax * (vmax * dt - dx))
    return q

# 현재 상태 (x, t)에서, 허용되는 행동 범위 [qmin, qmax]를 갖고
# 신호등 i (또는 i == nlight인 경우 목적지) 방향으로 전진,
# answer[0] (찾은 최적의 이동 시간)와 speed 테이블을 업데이트

def scan_forward_qrange(x, t, qmax, qmin, i, answer):
    global nlight, xdest, lights, speed
    if i == nlight:
        dt = find_dt(xdest - x, qmax)
        if t + dt < answer[0]:
            answer[0] = t + dt
    else:
        dx = lights[i].x - x
        tmin = t + find_dt(dx, qmax)
        tmax = t + find_dt(dx, qmin)
        cycle_time = lights[i].red + lights[i].green
        k = int(tmin // cycle_time)
        while k * cycle_time <= tmax and k * cycle_time <= answer[0] and k < MAX_CYCLE:
            green_start = k * cycle_time + lights[i].red
            green_end = (k + 1) * cycle_time
            # 만약 신호등 i에 정확히 빨간불로 바뀌는 순간 도착할 수 있다면...
            if green_end <= tmax:
                q_val = find_q(dx, green_end - t)
                v_val = q_val if q_val > 0 else 0.0
                v_val += amax * find_dt(dx, v_val)
                if v_val > vmax:
                    v_val = vmax
                if v_val > speed[i][k + 1]:
                    speed[i][k + 1] = v_val
            # [tmin, tmax] 구간에 부분적으로 포함되는 녹색 신호 기간에 대해
            # Q 범위를 제한하고, 더 전진
            if green_start <= tmax:
                qsub_max = qmax
                qsub_min = qmin
                if green_start > tmin:
                    qsub_max = find_q(dx, green_start - t)
                if green_end < tmax:
                    qsub_min = find_q(dx, green_end - t)
                scan_forward_qrange(x, t, qsub_max, qsub_min, i + 1, answer)
            k += 1


# 상태 (x, t, v)에서 [여기서 v는 해당 시점의 속도입니다],
# 허용되는 Q 범위를 설정하고 전진시킵니다.

def go_forward(x, t, v, i, answer):
    qmax = v
    qmin = -answer[0]  # qmin은 긴 대기 시간만큼 낮을 수 있습니다 (즉, -trip_time).
    scan_forward_qrange(x, t, qmax, qmin, i, answer)


# 모든 신호등에 대한 속도 테이블을 초기화
# 여행 소요 시간의 상한을 계산:
# 시작점에서 각 신호등까지 이동 (각 신호등에서 완전 정지를 강제)
# 빨간불 지속 시간을 더함
# 그 후 시작 상태와 신호등 상태에서 전진

def solve_case():
    global nlight, xdest, lights, speed
    # 모든 신호등에 대한 속도 테이블을 초기화
    speed = [[-1.0 for _ in range(MAX_CYCLE)] for _ in range(nlight)]
    
    # 여행 소요 시간의 상한을 계산
    # 시작점에서 각 신호등까지 이동하면서 (각 신호등에서 완전 정지를 강제하고)
    # 빨간불 지속 시간을 더함
    ans = 0.0
    x = 0.0
    for i in range(nlight):
        ans += find_dt(lights[i].x - x, 0)
        ans += lights[i].red
        x = lights[i].x
    ans += find_dt(xdest - x, 0)
    answer = [ans]  
    
    # 시작 상태 (x=0, t=0, v=0)와 신호등 상태에서 전진
    go_forward(0.0, 0.0, 0.0, 0, answer)
    
    # 각 신호등에 대해, 도달 가능한 각 사이클 시간마다 더 전진
    for i in range(nlight):
        cycle_time = lights[i].red + lights[i].green
        for k in range(MAX_CYCLE):
            if k * cycle_time > answer[0]:
                break
            if speed[i][k] >= 0:
                go_forward(lights[i].x, k * cycle_time, speed[i][k], i + 1, answer)
    return answer[0]


def main():
    global xdest, nlight, lights
    data = sys.stdin.read().split()
    pos = 0
    out_lines = []
    while pos < len(data):
        try:
            xdest = float(data[pos])
            pos += 1
            nlight = int(data[pos])
            pos += 1
        except:
            break
        lights = []
        for _ in range(nlight):
            x_val = float(data[pos]); pos += 1
            red_val = float(data[pos]); pos += 1
            green_val = float(data[pos]); pos += 1
            lights.append(Light(x_val, red_val, green_val))
        res = solve_case()
        out_lines.append(f"{res:.3f}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    main()
