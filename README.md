# 🗺️ 이형규 포트폴리오
> "프레임의 낭만, 끝까지 쫓다."
> 
> <b> `DX11`, `C++`, `Win32API` 기반 게임 클라이언트 프로그래머. <br>
>
> 1 프레임의 성능 최적화를 위해 끝까지 파고드는 개발자 이형규입니다. "동작하는 코드"를 넘어 "성능과 구조가 아름다운 코드"를 지향하며, 엔진 레벨의 깊이 있는 이해를 바탕으로 문제를 해결합니다.

---

# 💻 프로젝트

## 🎮 블루아카이브 팬메이드 프로젝트 - OperationKivotos ([상세내용](DETAIL.md#bluearchive-main))

> ( 2026.01 ~ 진행 중 )

<img width="700" height="400" alt="블루아카이브 프로젝트 스크린샷" src="https://github.com/user-attachments/assets/127ef1e4-c683-425a-a1f7-4bcc25107fc0" />

### 🔧 사용 기술 및 언어
- **Environment**: Unity 
- **Language**: C#
- **Library/Package**: `Addressables`, `UniTask`, `Newtonsoft.Json`, `NPOI`

### 📌 담당 업무 및 경험
> **확장성을 고려한 데이터 주도 설계(Data-Driven Design)와 비동기 로딩 파이프라인을 구축했습니다.**

*   **System Architecture**
    *   싱글톤(`Managers`) 기반의 중앙 집중형 시스템 구축으로 코어 매니저 13종의 결합도 최소화
    *   JSON 및 엑셀 기반의 데이터 주도 설계(`Data-Driven Design`)로 하드코딩을 배제하고 유지보수성 확보
    *   Observer 패턴(`Action Event`)을 활용해 프레임 낭비 없는 데이터-UI 동기화 파이프라인 구축
*   **Optimization & Memory Management**
    *   `Addressables` 에셋 시스템을 도입해 글로벌/씬 단위 핸들을 분리하고 명시적 메모리 해제(`Release`) 제어
    *   `UniTask`와 `CancellationToken`을 연계해 코루틴 누수를 방어하는 비동기 태스크 최적화 수행
    *   사전 로드(`Preload`) 기능을 지원하는 Addressables 전용 오브젝트 풀링 시스템을 직접 구현하여 **GC 스파이크 차단**
*   **Gameplay & Combat**
    *   파티 기반의 실시간 캐릭터 교체(Tag) 전투 시스템 및 경험치/레벨 공유 로직 구현
    *   인터페이스(`IDamageable`)와 다형성을 활용하여 결합도를 낮춘 공용 데미지 연산 파이프라인 설계
    *   메인 옵션과 서브 옵션이 무작위로 부여되는 호요버스(원신/스타레일) 스타일의 장비 아이템/스탯 구조 확립
    *   `Behavior Tree`와 Unity `Timeline`을 연동하여 보스 몬스터의 다양한 공격 패턴 제어

### 🚀 Highlights & 목차
> **각 항목 클릭 시 상세 구현 내용(DETAIL.md)으로 이동합니다.**

**1. 🔨 주요 개발 기능** <br>
&nbsp;&nbsp; └ [비동기 로딩 및 Addressables 파이프라인](DETAIL.md#async-pipeline-bluearchive) <br>
&nbsp;&nbsp; └ [NPOI 기반 데이터 주도 설계(Data-Driven) 자동화](DETAIL.md#data-driven-bluearchive) <br>
&nbsp;&nbsp; └ [Behavior Tree 기반 몬스터 AI 설계](DETAIL.md#behavior-tree-ai) <br>
&nbsp;&nbsp; └ [인터페이스와 다형성을 활용한 공용 데미지 파이프라인](DETAIL.md#combat-bluearchive) <br>
&nbsp;&nbsp; └ [UI 렌더링 최적화 및 이벤트 분리](DETAIL.md#ui-optimization-bluearchive) <br>

<br>

**2. 🛠️ 문제 해결 (Troubleshooting)** <br>
&nbsp;&nbsp; └ **[몬스터 God Class 리팩토링 및 상속 구조 세분화](DETAIL.md#ai-refactoring-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 방대한 `if-else`로 얽힌 코드를 계층형 상속 구조와 `Behavior Tree`로 분리하여 **OCP(개방-폐쇄 원칙) 준수 및 확장성 확보**

&nbsp;&nbsp; └ **[비동기 제어 한계 극복 및 UniTask 파이프라인 도입](DETAIL.md#async-unitask-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 코루틴의 콜백 지옥과 씬 전환 시 발생하는 고아 태스크(Orphan Task) 메모리 누수를 `CancellationToken`과 `UniTask`로 **완벽히 제어**

&nbsp;&nbsp; └ **[런타임 파싱 병목 해결을 위한 NPOI 데이터 베이킹](DETAIL.md#data-driven-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 기본 JSON의 딕셔너리 직렬화 한계를 극복하고 엑셀 데이터를 `ScriptableObject`로 베이킹하여 **데이터 조회 속도 최적화 (`O(N)` → `O(1)`)**

<br>

### 🎥 [시연 영상 보러가기](유튜브 링크를 여기에 넣어주세요)

<br>
<hr>
<br>

## 🎮 Eternal Return (이터널리턴) ([상세내용](DETAIL.md#-이터널-리턴-모작))

> ( 2025.07 ~ 2025.09 ) ( 2개월 )

<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/b5edd5af-9ce7-4f17-bc8a-84f8bb745edd" />

### 🔧 사용 기술 및 언어
- **Environment** : Visual Studio 2022
- **Language** : C++, HLSL
- **Library** : `DirectX11`, `Win32API`


### 📌 담당 업무 및 경험
> **게임의 핵심 코어 시스템부터 콘텐츠 구현까지 전반적인 클라이언트 개발을 담당했습니다.**

*   **System & Framework**
    *   게임 프레임워크 설계 (씬 관리, 오브젝트 생명주기 관리)
    *   컴포넌트 시스템 구현 (`Image`, `Text`, `Script` 등)
    *   UI 시스템 개발 (계층 구조, 스크롤러블 패널, 텍스트 렌더링)
*   **Rendering & Optimization**
    *   렌더링 파이프라인 구축 (`Forward` + `Deferred Hybrid`)
    *   `GPU Instancing` 기반 대규모 환경 오브젝트 렌더링
    *   `Quad Tree` 공간 분할을 이용한 렌더링(Culling) 및 피킹 최적화
*   **Gameplay & AI**
    *   `NavMesh` & `NavMeshAgent` 길찾기 시스템 구현 및 최적화
    *   몬스터 생성 및 AI 패턴 로직 구현
    *   플레이어 캐릭터(니키) 스킬 및 기본 공격 로직 구현
    *   아이템 시스템 (제작, 등급, 레시피, 스탯 적용) 구현

### 🚀 Highlights & 목차
> **각 항목 클릭 시 상세 구현 내용(DETAIL.md)으로 이동합니다.**

**1. 🔨 주요 개발 기능** <br>
&nbsp;&nbsp; └ [Deferred Rendering (Hybrid)](DETAIL.md#deferred-rendering) <br>
&nbsp;&nbsp; └ [GPU Instancing](DETAIL.md#gpu-instancing) <br>
&nbsp;&nbsp; └ [Quad Tree 공간 분할](DETAIL.md#quad-tree) <br>
&nbsp;&nbsp; └ [NavMesh 길찾기](DETAIL.md#navmesh) <br>
&nbsp;&nbsp; └ [몬스터 AI 시스템](DETAIL.md#fsm-to-bt-feature) 

<br>

**2. 🛠️ 문제 해결 (Troubleshooting)** <br> 
&nbsp;&nbsp; └ **[Forward → Deferred 전환](DETAIL.md#deferred-rendering-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 다중 광원과 반투명 객체를 동시 처리하는 **Hybrid 파이프라인 구축**

&nbsp;&nbsp; └ **[NavMesh 검색 최적화](DETAIL.md#navmesh-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `Spatial Grid` 도입으로 **탐색 속도 21.5배 가속 (301μs → 14μs)**

&nbsp;&nbsp; └ **[Quad Tree 충돌 최적화](DETAIL.md#quadtree-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 불필요한 연산을 제거하여 **충돌 처리 135.8배 최적화 (53ms → 0.3ms)**

&nbsp;&nbsp; └ **[AI 구조 개선 (FSM → BT)](DETAIL.md#fsm-to-bt)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `Behavior Tree` 도입으로 복잡한 AI 로직의 **유지보수성 확보**

<br>

### 🎥 [시연 영상 보러가기](https://youtu.be/b6XVkd0xc-E?si=vMBVltpWKHP4UM11)

<br>
<hr>
<br>

## 🎮 Brotato ([상세내용](DETAIL.md#-brotato-모작))

> ( 2025.02 ~ 2025.03 ) ( 3주 )

<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/707d63de-187c-40e8-a571-43c336de358f" />

### 🔧 사용 기술 및 언어
- **Environment**: Visual Studio 2022
- **Language**: C++
- **Library**: `Win32API`, `Direct2D`, `DirectWrite`, `GDI+`, `FMOD`


### 📌 담당 업무 및 경험
> **2D 게임 엔진의 핵심 시스템 구현 및 렌더링 최적화를 담당했습니다.**

*   **System & Framework**
    *   게임 프레임워크 설계 (오브젝트 관리, 씬 전환, 생명주기 관리)
    *   매니저 시스템 구현 (`RenderManager`, `UIManager`, `EventManager` 등)
    *   이벤트 기반 지연 처리(`Event Queue`) 시스템 구축
    *   컴포넌트 시스템 구현 (`Transform`, `Collider`, `Animator`, `Image`, `Text`)
*   **Rendering & Optimization**
    *   `GDI+` → `Direct2D` 마이그레이션 (하드웨어 가속 전환)
    *   타일맵 시스템 및 오프스크린 베이킹 최적화
    *   충돌 처리 및 물리 시스템 구현
*   **UI & Content**
    *   UI 시스템 개발 (이미지, 텍스트, 계층 구조 관리)
    *   캐릭터/몬스터 애니메이션 시스템 구현

### 🚀 Highlights & 목차
> **각 항목 클릭 시 상세 구현 내용(DETAIL.md)으로 이동합니다.**

**1. 🔨 주요 개발 기능** <br>
&nbsp;&nbsp; └ [Direct2D 렌더링 시스템](DETAIL.md#rendering-system-brotato)  <br>
&nbsp;&nbsp; └ [엔진 아키텍처 (Manager-Scene-Object)](DETAIL.md#engine-brotato)  <br>
&nbsp;&nbsp; └ [컴포넌트 기반 객체 설계](DETAIL.md#component-brotato)

<br>

**2. 🛠️ 문제 해결 (Troubleshooting)** <br>
&nbsp;&nbsp; └ **[Direct2D 하드웨어 가속 전환](DETAIL.md#direct2d-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `GDI+` 대비 렌더링 성능 **10배 향상 (20 FPS → 200+ FPS, GPU 가속)**

&nbsp;&nbsp; └ **[타일맵 렌더링 최적화](DETAIL.md#tilemap-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 오프스크린 베이킹으로 `DrawCall` **99.9% 절감 (1,296회 → 1회)**

&nbsp;&nbsp; └ **[이벤트 큐 메모리 관리](DETAIL.md#event-queue-system)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 지연 삭제(Lazy Deletion) 도입으로 객체 중복 삭제(`Double Free`) 이슈 해결 및 **안정성 확보**

<br>

### 🎥 [시연 영상 보러가기](https://youtu.be/d-VZS1AdvtA?si=LsgWayJvOPfWndK6)

<br>
<hr>
