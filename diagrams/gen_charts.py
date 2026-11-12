# 실측 데이터 차트 → figs/*.svg (build.py 가 부른다)
#  data/field_timeline.json : 개발 빌드 자동 주행 5분, ① Sector(2026-10-10 04:01) vs ⑤ 거리(03:45) 각 1회분
#   - live   : 0.5초 구간별 최대 살아 있는 몬스터 수
#   - dt_max : 1초 구간별 최대 프레임 시간(ms)
#   원본 로그(MetricsLogs/field_*_frames.csv)에서 OperationKivotos-Code/docs/FieldEntity/tools 의 집계 코드로 뽑음
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ORANGE, BLUE, RED, MUTED, LINE, GRID = '#e8590c', '#3b5bdb', '#e03131', '#5b6270', '#d5d9e2', '#eef0f4'


def poly(xs, ys, fx, fy):
    return ' '.join(f'{fx(x):.1f},{fy(y):.1f}' for x, y in zip(xs, ys))


def seg_spans(segs, end):
    out = []
    for i, (t0, lab) in enumerate(segs):
        t1 = segs[i + 1][0] if i + 1 < len(segs) else end
        if lab == 'a_sweep': out.append((t0, t1, '#f1f3f5', 'sweep'))
        elif lab.startswith('c'): out.append((t0, t1, '#d3f9d8', 'edge'))
        elif lab.startswith('b'): out.append((t0, t1, '#e5dbff', 'drag'))
    return out


def timeline(d):
    S, D = d['sector'], d['distance']
    W, H = 1200, 640
    X0, X1, T1 = 90, 1160, 296.3
    fx = lambda t: X0 + (X1 - X0) * t / T1
    # 패널 A : 살아 있는 몬스터
    A0, A1, AMAX = 150, 360, 200
    fa = lambda v: A1 - (A1 - A0) * v / AMAX
    # 패널 B : 프레임 시간
    B0, B1, BMAX = 430, 580, 25
    fb = lambda v: B1 - (B1 - B0) * v / BMAX
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">',
         '<rect width="100%" height="100%" fill="#fff"/>',
         '<text x="40" y="44" class="h1">5분 자동 주행 — 같은 빌드 · 같은 경로에서 ① Sector vs ⑤ 거리</text>',
         '<text x="40" y="74" class="s m">개발 빌드 실측 로그(각 1회분) · 회색 = 맵 한 바퀴, 초록 = 구역 경계 1m 왕복, 보라 = 몬스터를 끌고 다른 구역으로 이동</text>']
    # 범례
    o += [f'<line x1="880" y1="108" x2="910" y2="108" stroke="{ORANGE}" stroke-width="3"/><text x="918" y="113" class="s">① Sector</text>',
          f'<line x1="1010" y1="108" x2="1040" y2="108" stroke="{BLUE}" stroke-width="3"/><text x="1048" y="113" class="s">⑤ 거리</text>']
    for top, bot, fy, mx, step, unit, title in ((A0, A1, fa, AMAX, 50, '마리', '살아 있는 몬스터 수 (0.5초 구간 최대)'),
                                                 (B0, B1, fb, BMAX, 5, 'ms', '프레임 시간 (1초 구간 최대)')):
        for t0, t1, c, _ in seg_spans(S['segments'], T1):
            o.append(f'<rect x="{fx(t0):.1f}" y="{top}" width="{fx(t1) - fx(t0):.1f}" height="{bot - top}" fill="{c}"/>')
        v = 0
        while v <= mx:
            y = fy(v)
            o.append(f'<line x1="{X0}" y1="{y:.1f}" x2="{X1}" y2="{y:.1f}" stroke="{GRID}" stroke-width="1"/>')
            o.append(f'<text x="{X0 - 10}" y="{y + 5:.1f}" class="xs m end">{v}</text>')
            v += step
        o.append(f'<text x="{X0}" y="{top - 14}" class="h3">{title}</text>')
        o.append(f'<text x="{X0 - 10}" y="{top - 14}" class="xs m end">{unit}</text>')
    # 패널 A 선
    o.append(f'<polyline points="{poly(S["t"], S["live"], fx, fa)}" fill="none" stroke="{ORANGE}" stroke-width="1.6"/>')
    o.append(f'<polyline points="{poly(D["t"], D["live"], fx, fa)}" fill="none" stroke="{BLUE}" stroke-width="1.6"/>')
    # 60fps 기준선
    y60 = fb(1000 / 60)
    o.append(f'<line x1="{X0}" y1="{y60:.1f}" x2="{X1}" y2="{y60:.1f}" stroke="{RED}" stroke-width="1.4" stroke-dasharray="6 5"/>')
    o.append(f'<text x="{X1}" y="{y60 - 6:.1f}" class="xs c-red end">16.7ms = 60fps</text>')
    o.append(f'<polyline points="{poly(S["t_dt"], S["dt_max"], fx, fb)}" fill="none" stroke="{ORANGE}" stroke-width="1.4"/>')
    o.append(f'<polyline points="{poly(D["t_dt"], D["dt_max"], fx, fb)}" fill="none" stroke="{BLUE}" stroke-width="1.4"/>')
    # x 축
    for t in range(0, 301, 30):
        if t > T1: break
        o.append(f'<text x="{fx(t):.1f}" y="{B1 + 22}" class="xs m mid">{t}</text>')
    o.append(f'<text x="{(X0 + X1) / 2}" y="{B1 + 46}" class="s m mid">시간 (초)</text>')
    # 주석
    o.append(f'<text x="{fx(65):.1f}" y="{A0 + 22}" class="s m mid">맵 한 바퀴</text>')
    o.append(f'<text x="{fx(173):.1f}" y="{A0 + 22}" class="s c-purple mid">끌고 가기</text>')
    o.append(f'<text x="{fx(234):.1f}" y="{A0 + 22}" class="s c-purple mid">끌고 가기</text>')
    o.append('</svg>')
    return '\n'.join(o)


def main(figs_dir):
    d = json.load(open(os.path.join(HERE, 'data', 'field_timeline.json'), encoding='utf-8'))
    open(os.path.join(figs_dir, 'ba-field-5-timeline.svg'), 'w', encoding='utf-8').write(timeline(d))


if __name__ == '__main__':
    main(os.path.join(HERE, 'figs'))
