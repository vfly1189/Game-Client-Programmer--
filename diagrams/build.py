# 깃헙 전용 도식 빌드 — python -B diagrams/build.py
#  figs/<id>.svg (손으로 그린 도식) + gen_*.py 가 만드는 SVG(실측 데이터 차트)
#  → images/<id>.png (README · DETAIL 이 참조) + 도식 모음 PDF(diagrams/GitHub_Diagrams.pdf)
#  렌더링은 Microsoft Edge headless (Noto Sans KR / 맑은 고딕).
import os, re, sys, subprocess, html

sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FIGS = os.path.join(HERE, 'figs')
OUT_IMG = os.path.join(ROOT, 'images')
TMP = os.path.join(HERE, '_tmp')
EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
SCALE = 2

# (id, 제목) — 도식 모음 PDF 순서
BOOK = [
    ('블루아카이브 · 필드 몬스터 관리', [
        ('ba-field-1-sector-problem', 'Sector 단위 활성화가 경계에서 부딪힌 문제'),
        ('ba-field-2-root-cause', '원인 분석 — 회수 규칙과 판정 단위'),
        ('ba-field-3-seven-policies', '켜 둘 범위를 정하는 7가지 방식 비교'),
        ('ba-field-4-hysteresis', '⑤ 거리 기반 활성화 — 켜기 20m / 끄기 25m'),
        ('ba-field-5-timeline', '5분 자동 주행 — 살아 있는 몬스터 수와 프레임 시간'),
        ('ba-field-6-update-lod', '갱신 LOD — 화면 밖에서 가만히 있는 몬스터는 덜 돌린다'),
    ]),
    ('블루아카이브 · 전투 행동 설계', [
        ('ba-skill-1-problem', '흐름까지 부품으로 만든 AbilitySystem의 한계'),
        ('ba-skill-2-layers', '흐름은 Timeline 위에, 행동은 그 순간에만'),
        ('ba-skill-3-selector', '고르는 곳과 실행하는 곳의 분리'),
        ('ba-skill-4-compose', '행동 하나 = 무엇을 + 횟수 · 간격 + 어디에'),
        ('ba-skill-5-same-structure', '일반몹과 보스가 같은 구조 위에서 돈다'),
    ]),
    ('블루아카이브 · 리소스 수명 관리', [
        ('ba-resource-1-buckets', '2버킷 구조 — 수명이 애매한 리소스는 전부 Global로'),
        ('ba-resource-2-scope-timeline', '수명 스코프 4종 — 수명 경계가 곧 해제 시점'),
        ('ba-resource-3-why-scope', 'Addressables가 이미 세는데, 왜 스코프 층을 두었나'),
        ('ba-resource-4-result', '결과 — 상주 메모리는 줄고, 씬을 오가도 쌓이지 않는다'),
    ]),
    ('이터널 리턴 · NavMesh 경로 스무딩', [
        ('er-navmesh-1-los-problem', 'LOS 스무딩이 코너에서 벽 안을 지나는 이유'),
        ('er-navmesh-2-strict-los', '판정만 엄격하게 — 끼임은 사라졌지만 급하게 꺾인다'),
        ('er-navmesh-3-funnel-bezier', 'Funnel + Bezier — 코너 꼭짓점 기준 곡선 만들기'),
        ('er-navmesh-4-compare', '같은 코너, 네 가지 경로 비교'),
    ]),
]


def viewbox(svg):
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    return float(m.group(1)), float(m.group(2))


def page(body, w):
    css = open(os.path.join(HERE, 'style.css'), encoding='utf-8').read()
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{css}\nbody{{width:{w}px}}</style></head><body>{body}</body></html>'


def edge(args):
    subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run',
                    '--run-all-compositor-stages-before-draw', '--virtual-time-budget=2000'] + args,
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def load_svg(fid):
    p = os.path.join(FIGS, fid + '.svg')
    return open(p, encoding='utf-8').read()


def render(fid):
    svg = load_svg(fid)
    w, h = viewbox(svg)
    svg = re.sub(r'<svg ', f'<svg width="{w:g}" height="{h:g}" ', svg, count=1)
    hp = os.path.join(TMP, fid + '.html')
    open(hp, 'w', encoding='utf-8').write(page(svg, w))
    out = os.path.join(OUT_IMG, fid + '.png')
    edge([f'--force-device-scale-factor={SCALE}', f'--window-size={int(w)},{int(h)}',
          f'--screenshot={out}', 'file:///' + hp.replace(os.sep, '/')])
    return out


def book():
    parts = ['<h1 class="cover">깃헙 전용 도식 모음</h1><p class="sub">OperationKivotos (Unity) · 이터널 리턴 모작 (DirectX11)</p>']
    for sec, figs in BOOK:
        for i, (fid, title) in enumerate(figs):
            svg = load_svg(fid)
            parts.append(f'<section><div class="sec">{html.escape(sec)} · {html.escape(title)}</div>{svg}</section>')
    css = ('@page{size:1300px 980px;margin:0} section{page-break-before:always;padding:28px 50px} '
           'section svg{width:1200px;height:auto;max-height:820px} .sec{color:#5b6270;font-size:15px;margin-bottom:14px} '
           'h2{margin:4px 0 18px;font-size:26px} .cover{margin:380px 50px 0;font-size:44px} .sub{margin:12px 50px;color:#5b6270;font-size:20px}')
    hp = os.path.join(TMP, '_book.html')
    open(hp, 'w', encoding='utf-8').write(page(f'<style>{css}</style>' + ''.join(parts), 1300))
    out = os.path.join(HERE, 'GitHub_Diagrams.pdf')
    edge(['--no-pdf-header-footer', f'--print-to-pdf={out}', 'file:///' + hp.replace(os.sep, '/')])
    return out


if __name__ == '__main__':
    os.makedirs(TMP, exist_ok=True)
    # 데이터 차트 SVG 생성
    import gen_charts
    gen_charts.main(FIGS)
    only = sys.argv[1:]
    ids = [fid for _, figs in BOOK for fid, _ in figs]
    for fid in ids:
        if only and fid not in only: continue
        if not os.path.exists(os.path.join(FIGS, fid + '.svg')):
            print('skip (없음)', fid); continue
        print('png', os.path.relpath(render(fid), ROOT))
    if not only:
        print('pdf', os.path.relpath(book(), ROOT))
