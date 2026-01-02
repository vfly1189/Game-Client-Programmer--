# 🗺️ 이형규 포트폴리오
> "프레임의 낭만, 끝까지 쫓다."
> 
> <b> DX11, C++, Win32API 기반 게임 클라이언트 프로그래머. <br>
>
> 1 프레임의 성능 최적화를 위해 끝까지 파고드는 개발자 이형규입니다. "동작하는 코드"를 넘어 "성능과 구조가 아름다운 코드"를 지향하며, 엔진 레벨의 깊이 있는 이해를 바탕으로 문제를 해결합니다.

---

# 💻 프로젝트

<br>

## 🎮 Eternal Return ( 이터널리턴 )  ([상세내용](DETAIL.md#-이터널-리턴-모작))

> ( 2025.07 ~ 2025.09 ) ( 2개월 )

### 🔧사용 기술 및 언어
- Visual Studio 2022, C++ , DirectX11 , HLSL , Win32API
  
### 📌 담당 업무 및 경험
  - 2인 개발
  - UI 시스템 개발 ( 이미지, 텍스트, 계층 구조, 스크롤러블 패널 )
  - 게임 프레임 워크 구현(오브젝트 관리, 충돌, 몬스터 생성 및 AI 패턴)
  - GPU Instancing
  - 렌더링 파이프라인 구축 ( Forward + Deferred )
  - 쿼드 트리(공간 분할)를 사용한 렌더링 및 피킹 최적화
  - NavMesh & NavMeshAgent 구현 및 최적화
  - 니키 캐릭터 구현 ( 스킬 및 기본 공격 )
  - 컴포넌트 기능(Image, Text) 구현
  - 아이템 기능 구현 ( 아이템 기본 클래스 , 아이템 제작, 아이템 등급, 아이템 레시피, 아이템 적용 )

### 🚀 Highlights
- Quad Tree 충돌 최적화: 53,992μs → 397μs (135.8배)
- NavMesh 검색 최적화(Spatial Grid): 301μs → 14μs (약 20배+)
- Mouse Picking 최적화(Quad Tree): 656μs → 142μs (4.6배)
- Deferred + Forward Hybrid Rendering 파이프라인 설계(반투명/UI 처리)

### [시연 영상](https://youtu.be/b6XVkd0xc-E?si=vMBVltpWKHP4UM11)





## 🎮 Brotato ([상세내용](DETAIL.md#-brotato-모작))

> ( 2025.02 ~ 2025.03 ) ( 3주 )


### 🔧사용 기술 및 언어
- Visual Studio 2022, Win32API, DirectWrite, Direct2D, GDI+, FMOD


### 📌 담당 업무 및 경험
  - 2인
  - UI 시스템 개발 ( 이미지, 텍스트, 계층 구조 )
  - 게임 프레임 워크 구현(오브젝트 관리, 이벤트 후처리 시스템, 오브젝트 렌더링, 충돌, 물리)
  - GDI / GDI+ -> Direct2D 마이그레이션
  - 매니저 시스템(Direct2D, 캐릭터, UI, 오브젝트 관리, 이벤트) 구현
  - 타일맵 작업
  - 컴포넌트 기능(Transform, Collider, Animator, Image, Text) 구현


### 🚀 Highlights
- 타일맵 DrawCall 최적화: 1,296회 DrawBitmap → 1회(오프스크린 렌더링으로 통합 비트맵 생성)
- 성능 개선: 평균 FPS 650 → 1400 (약 2.15배)
- 프레임 타임: 1.54ms → 0.71ms (약 0.83ms 단축)
- 이벤트 처리 안정화: 중복 삭제(Double Free) 이슈를 자료구조 변경으로 해결(vector → unordered_set)

### [시연 영상](https://youtu.be/d-VZS1AdvtA?si=LsgWayJvOPfWndK6)



<br>

## 🎮 TBI : The Binding Of Isaac ([상세내용](DETAIL.md#-tbi-모작))

> ( 2025.03 ~ 2025.05 ) ( 2개월 )

### 🔧사용 기술 및 언어
- Visual Studio 2022, Win32API, DirectWrite, Direct2D, GDI+, FMOD

### 📌 담당 업무 및 경험
  - 1인 개발
  - UI 시스템 개발 ( 이미지, 텍스트, 계층 구조 )
  - 게임 프레임 워크 구현(오브젝트 관리, 이벤트 후처리 시스템, 오브젝트 렌더링, 충돌, 물리, 몬스터 생성 및 AI 패턴)
  - 캐릭터 구현 ( 아이작 , 케인 , 막달레나 , 유다 )
  - 매니저 시스템(Direct2D, 캐릭터, UI, 오브젝트 관리, 이벤트) 구현
  - 절차적 맵 생성 ( BFS 알고리즘기반 던전 생성 )
  - 애니메이션 시스템 ( 프레임기반 스프라이트 애니메이션 )
  - 컴포넌트 기능(Transform, Collider, Animator, Image, Text) 구현

### 🚀 Highlights
- 절차적 맵 생성: DFS 기반 생성의 선형화 문제를 BFS 기반 생성으로 개선(방사형 구조 유도)
- 몬스터 AI 구조화: if-else 중첩 로직을 State Pattern으로 분리(Idle/Trace/Attack)

### [시연 영상](https://tobrother.tistory.com/144)
<br>
