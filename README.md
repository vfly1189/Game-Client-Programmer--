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
&nbsp;&nbsp; └ [NavMesh 길찾기](DETAIL.md#navmesh) <br>
&nbsp;&nbsp; └ [몬스터 AI 시스템](DETAIL.md#fsm-to-bt-feature) 

<br>

**2. 🛠️ [문제 해결 (Troubleshooting)](DETAIL.md#troubleshooting-eternal-return)** <br> 
&nbsp;&nbsp; └ **[Forward → Deferred 전환](DETAIL.md#deferred-rendering-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🎨 다중 광원과 반투명 객체를 동시 처리하는 Hybrid 파이프라인 구축

&nbsp;&nbsp; └ **[NavMesh 검색 최적화](DETAIL.md#navmesh-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚡ Spatial Grid 도입으로 탐색 속도 **21.5배 가속 (301μs → 14μs)**

&nbsp;&nbsp; └ **[Quad Tree 충돌 최적화](DETAIL.md#quadtree-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🚀 불필요한 연산을 제거하여 충돌 처리 
