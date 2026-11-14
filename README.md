# 🗺️ 이형규 포트폴리오

---

## INTRODUCTION

### 개발자로서의 이형규.

<div align="center">

## 타협하지 않고 집요하게.

</div>

<br>

<div align="center">

### 🎮 게임 플레이

*" 머릿속 아이디어가 코드를 통해 실제로 작동 될 때 가장 재밌습니다 "*

<br>

### 🏗️ 아키텍처

*" 하나를 고칠 때 다른 곳을 건드리지 않아도 되는 구조 "*

<br>

### 🔥 도 전

*" 재밌을 것 같으면 일단 뛰어드는 사람 "*

</div>

---

> `Unity`, `DX11`, `C++`, `C#`, `Win32API` 기반 게임 클라이언트 프로그래머. <br>
>
> "동작하는 코드"를 넘어 **"성능과 구조가 아름다운 코드"** 를 지향합니다.
> 
> DirectX11 기반 자체 엔진부터 Unity 기반 서비스 수준의 아키텍처까지, 엔진 레벨의 이해를 바탕으로 구조와 성능을 함께 설계합니다.

---

# 💻 프로젝트

| 프로젝트 | 엔진 · 언어 | 기간 · 인원 | 대표 성과 |
|:---|:---:|:---:|:---|
| [🎮 블루아카이브 팬메이드 OperationKivotos](#project-bluearchive) | Unity · C# | 2026.01 ~ 진행 중 · 1인 | 느린 프레임 **▼47%** · Global 상주 메모리 **▼60%** |
| [🎮 이터널 리턴 모작](#project-eternal) | DirectX11 · C++ | 2025.07 ~ 2025.09 · 2인 | 코너 끼임 **93쌍 → 0** · 충돌 처리 **135.8배** 단축 |
| [🎮 Brotato 모작](#project-brotato) | Direct2D · C++ | 2025.02 ~ 2025.03 · 2인 | DrawCall **1,296 → 1** · 대규모 웨이브 **150 ~ 250 FPS** |

<br>

<a name="project-bluearchive"></a>
## 🎮 블루아카이브 팬메이드 OperationKivotos ([상세내용](DETAIL.md#bluearchive-main))

> ( 2026.01 ~ 진행 중 ) ( 1인 개인 프로젝트 )

<img width="700" height="400" alt="블루아카이브 프로젝트 스크린샷" src="https://github.com/user-attachments/assets/127ef1e4-c683-425a-a1f7-4bcc25107fc0" />

### 🔧 사용 기술 및 언어
- **Environment** : Unity
- **Language** : C#
- **Library / Package** : `Addressables`, `UniTask`, `Newtonsoft.Json`, `NPOI`
- **Tool** : Claude

### 📌 담당 범위
> **1인 개발 — 설계 · 구현 · 측정 전부 담당**

*   **System & Data**
    *   싱글톤(`Managers`) 기반 중앙 집중형 시스템 아키텍처
    *   Excel / JSON 이원화 데이터 주도 설계 · `DataManager` 통합 조회
    *   `Action` / `Delegate` 이벤트 구독으로 데이터 · UI 분리
*   **Optimization & Memory**
    *   7가지 활성화 방식 실측 비교 → **거리 기반 활성화 + 화면 밖 갱신 LOD** (가장 느린 1% 프레임 ▼47%)
    *   `Addressables` 위 수명 스코프 4종(Global / Scene / Party / Popup) → 해제 책임을 호출부에서 구조로 이전 (Global 상주 메모리 ▼60%)
    *   `UniTask` 비동기 로딩 · 오브젝트 풀 · 아틀라스 캐시 수명 통합
*   **Gameplay & Combat**
    *   흐름(Timeline) / 행동(Event) 분리 **SkillSystem** — 일반몹 · 보스가 같은 구조, 차이는 조립과 값
    *   다형성 계층형 `Behavior Tree` 몬스터 AI · Timeline 보스 패턴
    *   파티 4인 태그 전투 · 메인 / 서브 무작위 옵션 장비

### 🚀 Highlights & 목차
> **각 항목 클릭 시 상세 구현 내용(DETAIL.md)으로 이동합니다.**

**1. 🔨 주요 개발 기능** <br>
&nbsp;&nbsp; └ [필드 몬스터 관리 : 거리 기반 활성화와 갱신 LOD](DETAIL.md#optimization-bluearchive) <br>
&nbsp;&nbsp; └ [전투 행동 설계 : SkillSystem + 다형성 계층형 몬스터 AI](DETAIL.md#ability-bluearchive) <br>
&nbsp;&nbsp; └ [리소스 수명 관리 : 수명 스코프와 레지스트리](DETAIL.md#resource-lifetime-bluearchive) <br>
&nbsp;&nbsp; └ [데이터 주도 설계(Data-Driven) 및 에셋 베이킹 자동화](DETAIL.md#data-driven-bluearchive) <br>
&nbsp;&nbsp; └ [UI 렌더링 최적화 및 이벤트 분리](DETAIL.md#ui-optimization-bluearchive) <br>

<br>

**2. 🛠️ 문제 해결 (Troubleshooting)** <br>
&nbsp;&nbsp; └ **[필드 몬스터 관리 : 거리 기반 활성화와 갱신 LOD 도입](DETAIL.md#optimization-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 가까운 몬스터만 켜고, 화면 밖은 덜 갱신 → **가장 느린 1% 프레임 ▼47% (4.68 → 2.50ms)**

&nbsp;&nbsp; └ **[전투 행동 설계 : 흐름과 행동 분리를 통한 확장](DETAIL.md#ability-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 흐름은 데이터로, 새 코드는 행동만 → **4번 추가 · 흐름 코드 0줄**

&nbsp;&nbsp; └ **[리소스 수명 관리 : 2버킷 구조의 한계와 수명 스코프 도입](DETAIL.md#resource-lifetime-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Addressables 리소스를 수명 스코프 단위로 관리 → **Global 상주 메모리 ▼60% (513 → 205MB)**

<br>

### 🎥 [시연 영상 보러가기](https://youtu.be/yPBj7T_f7ds?si=zlXlAo7Us3Utixns) · 💾 [소스코드](https://github.com/vfly1189/OperationKivotos-Code)

<br>
<hr>
<br>

<a name="project-eternal"></a>
## 🎮 이터널 리턴 모작 ([상세내용](DETAIL.md#eternal-return-main))

> ( 2025.07 ~ 2025.09 ) ( 2개월 ) ( 2인 팀 · 프로그래머 )

<img width="700" height="400" alt="이터널 리턴 모작 스크린샷" src="https://github.com/user-attachments/assets/b5edd5af-9ce7-4f17-bc8a-84f8bb745edd" />

### 🔧 사용 기술 및 언어
- **Environment** : Visual Studio 2022
- **Language** : C++, HLSL
- **Library** : `DirectX11`, `Win32API`

### 📌 담당 범위
> **2인 팀 프로젝트 — 엔진 코어 · 렌더링 · 길찾기 · AI · 콘텐츠까지 클라이언트 전반 담당**

*   **System & Framework**
    *   게임 프레임워크 (씬 관리 · 오브젝트 생명주기)
    *   컴포넌트 시스템 (`Image`, `Text`, `Script` 등)
    *   UI 시스템 (계층 구조 · 스크롤러블 패널 · 텍스트 렌더링)
*   **Rendering & Optimization**
    *   `Forward` + `Deferred` Hybrid 렌더링 파이프라인 (G-Buffer / MRT)
    *   `GPU Instancing` 기반 대규모 환경 오브젝트 렌더링
    *   `Quad Tree` 공간 분할 Picking · 충돌 처리 최적화
*   **Gameplay & AI**
    *   `NavMesh` & `NavMeshAgent` 길찾기 · Funnel + Bezier 경로 스무딩 · Spatial Grid 검색 최적화
    *   몬스터 생성 · AI (FSM → Behavior Tree)
    *   플레이어 캐릭터(니키) 스킬 · 기본 공격
    *   아이템 시스템 (제작 · 등급 · 레시피 · 스탯 적용)

### 🚀 Highlights & 목차
> **각 항목 클릭 시 상세 구현 내용(DETAIL.md)으로 이동합니다.**

**1. 🔨 주요 개발 기능** <br>
&nbsp;&nbsp; └ [Deferred Rendering (Hybrid)](DETAIL.md#deferred-rendering) <br>
&nbsp;&nbsp; └ [GPU Instancing](DETAIL.md#gpu-instancing) <br>
&nbsp;&nbsp; └ [Quad Tree 공간 분할](DETAIL.md#quad-tree) <br>
&nbsp;&nbsp; └ [NavMesh 길찾기 · 검색 최적화 (Spatial Grid)](DETAIL.md#navmesh) <br>
&nbsp;&nbsp; └ [몬스터 AI 시스템 (FSM → Behavior Tree)](DETAIL.md#fsm-to-bt-feature) 

<br>

**2. 🛠️ 문제 해결 (Troubleshooting)** <br> 
&nbsp;&nbsp; └ **[Hybrid 렌더링 : Deferred와 Forward의 장점 결합](DETAIL.md#deferred-rendering-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 조명은 화면 픽셀에만, 반투명 UI만 Forward → **Forward + Deferred 혼합 파이프라인**

&nbsp;&nbsp; └ **[NavMesh 경로 스무딩](DETAIL.md#navmesh-smoothing)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `Funnel + Bezier`로 **코너 끼임 93쌍 → 0**

&nbsp;&nbsp; └ **[마우스 Picking + 충돌 처리 최적화 (Quad Tree)](DETAIL.md#quadtree-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 검사할 후보만 남겨 **충돌 처리 135.8배 단축 (53,922μs → 397μs)**

<br>

### 🎥 [시연 영상 보러가기](https://youtu.be/b6XVkd0xc-E?si=vMBVltpWKHP4UM11) · 💾 [소스코드](https://github.com/HyangRim/DirectX11-Engine-Client)

<br>
<hr>
<br>

<a name="project-brotato"></a>
## 🎮 Brotato 모작 ([상세내용](DETAIL.md#brotato-main))

> ( 2025.02 ~ 2025.03 ) ( 3주 ) ( 2인 팀 · 프로그래머 )

<img width="700" height="400" alt="Brotato 모작 스크린샷" src="https://github.com/user-attachments/assets/707d63de-187c-40e8-a571-43c336de358f" />

### 🔧 사용 기술 및 언어
- **Environment** : Visual Studio 2022
- **Language** : C++
- **Library** : `Win32API`, `Direct2D`, `DirectWrite`, `GDI+`, `FMOD`

### 📌 담당 범위
> **2인 팀 프로젝트 — 2D 엔진 코어 · 렌더링 최적화 · UI 담당**

*   **System & Framework**
    *   Manager – Scene – Object 3계층 프레임워크 (오브젝트 관리 · 씬 전환 · 생명주기)
    *   매니저 시스템 (`RenderManager`, `UIManager`, `EventManager` 등)
    *   이벤트 큐(`Event Queue`) 기반 지연 처리
    *   컴포넌트 시스템 (`Transform`, `Collider`, `Animator`, `Image`, `Text`)
*   **Rendering & Optimization**
    *   `GDI+` → `Direct2D` 하드웨어 가속 전환 · 더블 버퍼링
    *   타일맵 오프스크린 베이킹
*   **UI & Content**
    *   UI 시스템 (이미지 · 텍스트 · 계층 구조 · 콜백 이벤트)
    *   캐릭터 / 몬스터 애니메이션

### 🚀 Highlights & 목차
> **각 항목 클릭 시 상세 구현 내용(DETAIL.md)으로 이동합니다.**

**1. 🔨 주요 개발 기능** <br>
&nbsp;&nbsp; └ [Direct2D 렌더링 시스템](DETAIL.md#rendering-system-brotato)  <br>
&nbsp;&nbsp; └ [엔진 아키텍처 (Manager-Scene-Object)](DETAIL.md#engine-brotato)  <br>
&nbsp;&nbsp; └ [컴포넌트 기반 객체 설계](DETAIL.md#component-brotato)

<br>

**2. 🛠️ 문제 해결 (Troubleshooting)** <br>
&nbsp;&nbsp; └ **[Direct2D 하드웨어 가속 전환](DETAIL.md#direct2d-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - GPU 하드웨어 가속으로 **대규모 웨이브에서도 평균 150 ~ 250 FPS** (`GDI+`는 소수 객체에서도 20 ~ 40 FPS)

&nbsp;&nbsp; └ **[타일맵 렌더링 최적화](DETAIL.md#tilemap-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 오프스크린 베이킹으로 `DrawCall` **99.9% 절감 (1,296회 → 1회)**

&nbsp;&nbsp; └ **[이벤트 처리 안정성](DETAIL.md#event-queue-system)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 삭제 예약 목록 `vector` → `unordered_set` → 같은 객체는 한 번만 삭제, **`Double Free` 크래시 해결**

<br>

### 🎥 [시연 영상 보러가기](https://youtu.be/d-VZS1AdvtA?si=LsgWayJvOPfWndK6) · 💾 [소스코드](https://github.com/HyangRim/BrotatoClone)

<br>
<hr>
