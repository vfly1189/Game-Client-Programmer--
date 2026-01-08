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

<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/b5edd5af-9ce7-4f17-bc8a-84f8bb745edd" />

### 🔧 사용 기술 및 언어
- **Environment** : Visual Studio 2022
- **Language** : C++, HLSL
- **Library** : DirectX11, Win32API


### 📌 담당 업무 및 경험
> **게임의 핵심 코어 시스템부터 콘텐츠 구현까지 전반적인 클라이언트 개발을 담당했습니다.**

*   **System & Framework**
    *   게임 프레임워크 설계 (씬 관리, 오브젝트 생명주기 관리)
    *   컴포넌트 시스템 구현 (Image, Text, Script 등)
    *   UI 시스템 개발 (계층 구조, 스크롤러블 패널, 텍스트 렌더링)
*   **Rendering & Optimization**
    *   렌더링 파이프라인 구축 (Forward + Deferred Hybrid)
    *   GPU Instancing 기반 대규모 환경 오브젝트 렌더링
    *   Quad Tree 공간 분할을 이용한 렌더링(Culling) 및 피킹 최적화
*   **Gameplay & AI**
    *   NavMesh & NavMeshAgent 길찾기 시스템 구현 및 최적화
    *   몬스터 생성 및 AI 패턴 로직 구현
    *   플레이어 캐릭터(니키) 스킬 및 기본 공격 로직 구현
    *   아이템 시스템 (제작, 등급, 레시피, 스탯 적용) 구현

### 🚀 Highlights & 목차
> **각 항목 클릭 시 상세 구현 내용(DETAIL.md)으로 이동합니다.**

**1. 🔨 [주요 개발 기능](DETAIL.md#주요개발-eternal-return)** <br>
&nbsp;&nbsp; └ [Deferred Rendering (Hybrid)](DETAIL.md#deferred-rendering) <br>
&nbsp;&nbsp; └ [GPU Instancing](DETAIL.md#gpu-instancing) <br>
&nbsp;&nbsp; └ [Quad Tree 공간 분할](DETAIL.md#quad-tree) <br>
&nbsp;&nbsp; └ [NavMesh 길찾기](DETAIL.md#navmesh)

<br>

**2. 🛠️ [문제 해결 (Troubleshooting)](DETAIL.md#-문제-해결)** <br> 
&nbsp;&nbsp; └ **[Forward → Deferred 전환](DETAIL.md#1️⃣-forward에서-deferred-rendering으로-전환-hybrid)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🎨 다중 광원과 반투명 객체를 동시 처리하는 Hybrid 파이프라인 구축

&nbsp;&nbsp; └ **[NavMesh 검색 최적화](DETAIL.md#2️⃣-navmesh-검색-속도-최적화-spatial-grid)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚡ Spatial Grid 도입으로 탐색 속도 **21.5배 가속 (301μs → 14μs)**

&nbsp;&nbsp; └ **[Quad Tree 충돌 최적화](DETAIL.md#3️⃣-쿼드-트리-기반-공간-분할-최적화)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🚀 불필요한 연산을 제거하여 충돌 처리 **135.8배 최적화 (53ms → 0.3ms)**

&nbsp;&nbsp; └ **[AI 구조 개선 (FSM → BT)](DETAIL.md#4️⃣-몬스터-ai-아키텍처-개선-fsm--behavior-tree)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🧠 Behavior Tree 도입으로 복잡한 AI 로직의 유지보수성 확보

<br>

### [🎥 시연 영상 보러가기](https://youtu.be/b6XVkd0xc-E?si=vMBVltpWKHP4UM11)

<br>
<hr>
<br>

## 🎮 Brotato ([상세내용](DETAIL.md#-brotato-모작))

> ( 2025.02 ~ 2025.03 ) ( 3주 )

<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/707d63de-187c-40e8-a571-43c336de358f" />

### 🔧 사용 기술 및 언어
- **Environment**: Visual Studio 2022
- **Language**: C++
- **Library**: Win32API, Direct2D, DirectWrite, GDI+, FMOD


### 📌 담당 업무 및 경험
> **2D 게임 엔진의 핵심 시스템 구현 및 렌더링 최적화를 담당했습니다.**

*   **System & Framework**
    *   게임 프레임워크 설계 (오브젝트 관리, 씬 전환, 생명주기 관리)
    *   매니저 시스템 구현 (RenderManager, UIManager, EventManager ... )
    *   이벤트 기반 지연 처리(Event Queue) 시스템 구축
    *   컴포넌트 시스템 구현 (Transform, Collider, Animator, Image, Text)
*   **Rendering & Optimization**
    *   GDI+ → Direct2D 마이그레이션 (하드웨어 가속 전환)
    *   타일맵 시스템 및 오프스크린 렌더링 최적화
    *   충돌 처리 및 물리 시스템 구현
*   **UI & Content**
    *   UI 시스템 개발 (이미지, 텍스트, 계층 구조 관리)
    *   캐릭터/몬스터 애니메이션 시스템 구현

### 🚀 Highlights & 목차
> **각 항목 클릭 시 상세 구현 내용(DETAIL.md)으로 이동합니다.**

**1. 🔨 [주요 개발 기능](DETAIL.md#주요개발-brotato)** <br>
&nbsp;&nbsp; └ [Direct2D 렌더링 시스템](DETAIL.md#rendering-system-brotato)  <br>
&nbsp;&nbsp; └ [엔진 아키텍처 (Manager-Scene-Object)](DETAIL.md#engine-brotato)  <br>
&nbsp;&nbsp; └ [컴포넌트 기반 객체 설계](DETAIL.md#component-brotato)

<br>

**2. 🛠️ [문제 해결 (Troubleshooting)](DETAIL.md#-문제-해결-1)** <br>
&nbsp;&nbsp; └ **[Direct2D 하드웨어 가속 전환](DETAIL.md#direct2d-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🚀 GDI+ 대비 렌더링 성능 **10배 향상 (20 FPS → 200+ FPS, GPU 가속)**

&nbsp;&nbsp; └ **[타일맵 렌더링 최적화](DETAIL.md#2️⃣tilemap-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🎨 오프스크린 베이킹으로 DrawCall **99.9% 절감 (1,296회 → 1회)**

&nbsp;&nbsp; └ **[이벤트 큐 메모리 관리](DETAIL.md#3️⃣event-queue-system)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🛡️ 지연 삭제 도입으로 객체 중복 삭제(Double Free) 이슈 해결 및 안정성 확보

<br>

### [🎥 시연 영상 보러가기](https://youtu.be/d-VZS1AdvtA?si=LsgWayJvOPfWndK6)



<br>

## 🎮 TBI : The Binding Of Isaac ([상세내용](DETAIL.md#-tbi-모작))

> ( 2025.03 ~ 2025.05 ) ( 2개월 )

<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/cc18a536-58fd-4679-8d4b-b7c3e95af758" />


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
