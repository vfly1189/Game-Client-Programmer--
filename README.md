# 🗺️ 이형규 포트폴리오

---

## INTRODUCTION

### 개발자로서의 이형규.

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

> `Unity`,`DX11`, `C++`, `C#` , `Win32API` 기반 게임 클라이언트 프로그래머. <br>
>
> "동작하는 코드"를 넘어 **"성능과 구조가 아름다운 코드"** 를 지향합니다.
> 
> DirectX11 기반 자체 엔진부터 Unity 기반 서비스 수준의 아키텍처까지, 엔진 레벨의 이해를 바탕으로 구조와 성능을 함께 설계합니다.

---

# 💻 프로젝트

## 🎮 블루아카이브 팬메이드 프로젝트 - OperationKivotos ([상세내용](DETAIL.md#bluearchive-main))

> ( 2026.01 ~ 2026.04 ) ( 4개월 ) ( 1인 )

<img width="700" height="400" alt="블루아카이브 프로젝트 스크린샷" src="https://github.com/user-attachments/assets/127ef1e4-c683-425a-a1f7-4bcc25107fc0" />

### 🔧 사용 기술 및 언어
- **Environment**: Unity 
- **Language**: C#
- **Library/Package**: `Addressables`, `UniTask`, `Newtonsoft.Json`, `NPOI`

### 📌 담당 업무 및 경험
> **이전 프로젝트들을 회고하며 느낀 구조적 아쉬움을 개선하고, 확장성 높은 아키텍처를 연구 및 적용**

*   **System Architecture**
    *   싱글톤(`Managers`) 기반의 중앙 집중형 시스템 아키텍쳐 설계
    *   Excel/JSON 이원화 기반 데이터 주도 설계 및 `DataManager` 통합 조회 시스템 구축
    *   `Action`/`Delegate` 이벤트 구독 방식으로 데이터-UI 분리
*   **Optimization & Memory Management**
    *   `Addressables` 기반 글로벌/씬 단위 핸들 분리 및 명시적 Release 구조 설계
    *   `UniTask` 기반 비동기 파이프라인 구축
    *   오브젝트 풀링 시스템 구현
*   **Gameplay & Combat**
    *   파티 기반의 실시간 캐릭터 교체 전투 시스템
    *   인터페이스(`IDamageable`)와 다형성을 활용하여 결합도를 낮춘 공용 데미지 연산 파이프라인 설계
    *   메인/서브 옵션 무작위 부여 방식의 호요버스 스타일 장비 스탯 시스템 구현
    *   `Behavior Tree`와 Unity `Timeline`을 연동하여 보스 몬스터의 다양한 공격 패턴 제어

### 🚀 Highlights & 목차
> **각 항목 클릭 시 상세 구현 내용(DETAIL.md)으로 이동합니다.**

**1. 🔨 주요 개발 기능** <br>
&nbsp;&nbsp; └ [Sector 기반 플레이어 위치 추적형 존 로딩 시스템](DETAIL.md#optimization-bluearchive) <br>
&nbsp;&nbsp; └ [비동기 로딩 및 Addressables 파이프라인](DETAIL.md#async-pipeline-bluearchive) <br>
&nbsp;&nbsp; └ [데이터 주도 설계(Data-Driven) 및 에셋 베이킹 자동화](DETAIL.md#data-driven-bluearchive) <br>
&nbsp;&nbsp; └ [다형성과 Timeline을 활용한 객체지향적 몬스터 아키텍처 설계](DETAIL.md#behavior-tree-ai) <br>
&nbsp;&nbsp; └ [인터페이스(Interface) 기반 공용 데미지 파이프라인](DETAIL.md#combat-bluearchive) <br>
&nbsp;&nbsp; └ [UI 렌더링 최적화 및 이벤트 분리](DETAIL.md#ui-optimization-bluearchive) <br>

<br>

**2. 🛠️ 문제 해결 (Troubleshooting)** <br>
&nbsp;&nbsp; └ **[기획 변경에 따른 AI·렌더링 연산 병목 해소: Sector 기반 존 로딩 시스템](DETAIL.md#optimization-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `Sector` 기반 시야 컬링과 비동기 생명주기 제어로 해결하여 **안정적인 프레임 방어 성공**

&nbsp;&nbsp; └ **[동기식 하드코딩 탈피 및 UniTask 비동기 파이프라인 구축](DETAIL.md#async-unitask-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 씬 전환 시 발생하는 `Task` 스레드풀의 `AssetBundle.Unload` 충돌을 `UniTask` 메인 스레드 동기화로 해결

&nbsp;&nbsp; └ **[대규모 데이터 관리의 한계 극복 및 파이프라인 이원화 (Excel/JSON)](DETAIL.md#data-driven-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 런타임 엑셀 파싱의 오버헤드를 에디터 타임 `ScriptableObject` 베이킹으로 이전하고 `DataManager`로 통합하여 **데이터 관리 최적화**

<br>

### 🎥 [시연 영상 보러가기](https://youtu.be/yPBj7T_f7ds?si=zlXlAo7Us3Utixns)

<br>
<hr>
<br>

## 🎮 Eternal Return (이터널리턴) ([상세내용](DETAIL.md#-이터널-리턴-모작))

> ( 2025.07 ~ 2025.09 ) ( 2개월 ) ( 2인 )

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

> ( 2025.02 ~ 2025.03 ) ( 3주 ) ( 2인 )

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
