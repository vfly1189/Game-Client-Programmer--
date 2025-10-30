# 📑 이형규 포트폴리오
>   <b>C++, Win32API, DX11</b>을 이용한 게임 개발의 경험이 있습니다. <br>

## <b> 주요 기술 - C++, DirectX11, UE5(공부중) </b>

## 목차

<table>
  <tbody>
    <tr>
      <td valign="top">
       <a>
        
 🎮 [Brotato 모작](#-brotato-모작) <br>
 > 📖 [게임 개요](#-게임-개요) <br>
   🔨 [주요 개발](#-주요-개발) <br>
   🛠️ [문제 해결](#%EF%B8%8F-문제-해결) <br>
   💻 [코드 샘플](#-코드-샘플)
       </a>
      </td>
      <td valign="top">
      <a>
 🎮 [TBI 모작](#-tbi-모작) <br>
 
 > 📖 [게임 개요](#-게임-개요-1) <br>
   🔨 [주요 개발](#-주요-개발-1) <br>
   🛠️ [문제 해결](#%EF%B8%8F-문제-해결-1) <br>
   💻 [코드 샘플](#-코드-샘플-1)
      </a>
      </td>
      <td valign="top">
      <a>
 🎮 [이터널리턴 모작](#-이터널-리턴-모작) <br>
 
 > 📖 [게임 개요](#-게임-개요-2) <br>
   🔨 [주요 개발](#-주요-개발-2) <br>
   🛠️ [문제 해결](#%EF%B8%8F-문제-해결-2) <br>
   💻 [코드 샘플](#-코드-샘플-2)
      </a>
      </td>
    </tr>
  </tbody>
</table>


---

# 🎮 Brotato 모작

<p align="left">
  <img src="https://github.com/user-attachments/assets/0fa0932b-be02-4008-a29b-4711adab14db" width="800"/>
</p>

<div align="left">

### 📌 프로젝트 정보

| 항목 | 내용 |
|:---:|:---|
| 🎯 **장르** | 탑다운 슈팅, 로그라이크 |
| ⏱️ **개발 기간** | 3주 |
| 👥 **개발 인원** | 2인 (프로그래머로 참여) |
| 🛠️ **개발 환경** | C++, Win32 API, Direct2D, FMOD |
| 🎬 **시연 영상** | [YouTube 바로가기](https://www.youtube.com/watch?v=d-VZS1AdvtA&list=LL&index=3) |

</div>

<br>

## 📖 게임 개요

Brotato는 로그라이크 요소가 결합된 탑다운 슈팅 게임으로, 플레이어는 감자 캐릭터를 조작하여 웨이브 방식으로 몰려오는 적들을 물리치며 생존하는 것이 목표입니다. 각 웨이브 사이 상점에서 무기와 아이템을 구매하여 캐릭터를 강화하고, 다양한 빌드 조합을 통해 전략적인 플레이가 가능합니다. 본 프로젝트는 C++과 Win32 API, Direct2D를 활용하여 원작의 핵심 게임플레이 메커니즘을 구현한 모작 프로젝트입니다.

<br>

---

## 🔨 주요 개발

<details open>
<summary><b>🏗️ 아키텍처 설계</b></summary>

<br>

**싱글톤 패턴 기반 매니저 시스템 구현**
- CCore, CTimeMgr, CKeyMgr, CCamera, CSceneMgr 등 핵심 시스템을 싱글톤으로 설계
- 게임 전반에 걸쳐 일관된 접근 방식 제공 및 메모리 관리 효율화

</details>

<details open>
<summary><b>🎨 렌더링 시스템</b></summary>

<br>

**Direct2D 기반 렌더링 파이프라인 구축**
- GDI/GDI+에서 Direct2D로 전환하여 FPS 20~40에서 60+ FPS로 성능 대폭 개선
- 자동 더블 버퍼링을 통한 깜박임 없는 부드러운 화면 전환
- WIC(Windows Imaging Component) 팩토리를 활용한 다양한 이미지 포맷 지원

**비트맵 관리 시스템**
- `unordered_map`을 활용한 비트맵 캐싱 시스템 구현
- 타일 분할 기능: 큰 이미지를 32x32 픽셀 단위로 자동 분할하여 타일맵 생성
- 초기 로딩 시 모든 리소스를 메모리에 적재하여 런타임 성능 최적화

</details>

<details open>
<summary><b>🎬 씬 관리 시스템</b></summary>

<br>

**유연한 씬 전환 구조**
- CScene 추상 클래스 기반 상속 구조 (Main, Select_Character, Select_Weapon, Start, Shop, Run_End)
- Enter()/Exit() 가상 함수를 통한 씬 진입/탈출 시 리소스 관리
- 이벤트 지연 처리 시스템으로 안전한 씬 전환 보장

</details>

<details open>
<summary><b>🧩 게임 오브젝트 시스템</b></summary>

<br>

**컴포넌트 기반 오브젝트 설계**
- CObject 추상 클래스를 기반으로 Player, Monster, Weapon, UI 등 다양한 객체 구현
- Collider, Animator, Rigidbody, Gravity 등 필요에 따라 동적으로 추가 가능한 컴포넌트
- Clone() 가상 함수를 통한 프로토타입 패턴 구현

</details>

<details>
<summary><b>✍️ 폰트 시스템</b></summary>

<br>

**커스텀 폰트 로더 구현**
- DirectWrite API를 활용한 .ttf 폰트 파일 동적 로딩
- CFontCollectionLoader와 CFontFileEnumerator를 통한 커스텀 폰트 컬렉션 관리
- 다국어 지원 (영문: Anybody-Medium, 한글: NotoSansKR-Medium)

</details>

<details>
<summary><b>📦 리소스 관리</b></summary>

<br>

**자동 리소스 로더**
- 게임 시작 시 content 폴더를 재귀적으로 탐색하여 모든 png, mp3, wav 파일 자동 로딩
- 파일명을 태그로 사용하여 간편한 리소스 접근
- 경로 관리자(CPathMgr)를 통한 상대 경로 처리

</details>

<details>
<summary><b>🖼️ UI 시스템</b></summary>

<br>

**계층적 UI 구조**
- PanelUI, BtnUI, SliderUI 등 다양한 UI 컴포넌트
- 콜백 함수 시스템을 통한 이벤트 처리 (전역 함수 및 멤버 함수 모두 지원)
- TextUI 컴포넌트로 텍스트 렌더링 및 외곽선 효과 지원

</details>

<details>
<summary><b>🔊 사운드 시스템</b></summary>

<br>

**FMOD 기반 오디오 엔진**
- BGM과 SFX 채널 분리 관리
- 마스터 볼륨, BGM 볼륨, SFX 볼륨 개별 조절 기능
- 슬라이더 UI를 통한 실시간 볼륨 조정

</details>

<br>

---

## 🛠️ 문제 해결

### 1️⃣ GDI에서 Direct2D로 전환을 통한 성능 개선

> **🚨 문제 상황**
> 
> GDI/GDI+를 사용한 초기 렌더링에서 타일맵만 그려도 FPS가 20~40대로 저조한 성능

**💡 해결 과정**
- Direct2D API 학습 및 렌더링 파이프라인 전면 재구축
- `ID2D1HwndRenderTarget`을 통한 하드웨어 가속 렌더링 적용
- `CreateCompatibleRenderTarget()`을 활용한 오프스크린 렌더링 구현
- WIC 팩토리를 통한 효율적인 이미지 로딩

**✅ 결과**
- FPS 60+ 안정적 유지, 깜박임 현상 완전 제거
- 게임 전체의 부드러운 플레이 경험 제공

<br>

### 2️⃣ 타일맵 렌더링 최적화

> **🚨 문제 상황**
> 
> 36x36 그리드의 타일맵을 렌더링할 때 매 프레임마다 1,296개의 개별 타일 객체를 각각 그리는 방식으로 인한 성능 저하

**💡 해결 과정**
- `CreateCompositeMapBitmap()` 함수를 구현하여 타일 합성 시스템 개발
- 오프스크린 렌더 타겟(`ID2D1BitmapRenderTarget`)을 생성하여 거대한 캔버스(1,168x1,168 픽셀) 준비
- 게임 시작 시 모든 32x32 픽셀 타일들을 하나의 거대한 비트맵으로 미리 합성
- 테두리 타일은 규칙적으로, 내부 타일은 랜덤하게 배치하여 자연스러운 맵 생성
- 런타임에는 합성된 단일 비트맵만 렌더링하도록 변경

**✅ 결과**
- 매 프레임 DrawBitmap() 호출 횟수가 **1,296회 → 1회**로 대폭 감소
- 타일맵 렌더링 성능 향상 및 안정적인 60 FPS 유지
- 메모리 사용량은 증가했으나 CPU 부하 크게 감소

<br>

### 3️⃣ 리소스 로딩 시스템 자동화

> **🚨 문제 상황**
> 
> 각 Scene마다 필요한 리소스를 수동으로 로드하여 코드 중복 및 관리 어려움

**💡 해결 과정**
- CFileMgr 클래스 구현으로 폴더 재귀 탐색 기능 추가
- `WIN32_FIND_DATA`를 활용한 파일 시스템 탐색
- 파일 확장자별 자동 분류 및 적절한 매니저에 등록
  - `.png` → Direct2DMgr
  - `.mp3/.wav` → CSoundMgr (BGM은 main_title_bgm 키워드로 자동 구분)

**✅ 결과**
- 리소스 로드 코드 대폭 간소화
- 새로운 리소스 추가 시 파일만 추가하면 자동 인식

<br>

### 4️⃣ 메모리 관리 및 씬 전환 안정성

> **🚨 문제 상황**
> 
> 씬 전환 시 객체 소멸 타이밍 문제로 인한 댕글링 포인터 발생 가능성

**💡 해결 과정**
- 이벤트 지연 처리 시스템(CEventMgr) 구현
- 프레임 단위 작업이 모두 완료된 후 이벤트 처리
- Scene의 Enter()/Exit() 가상 함수로 명확한 초기화/정리 시점 제공
- `Safe_Delete_Vec` 템플릿 함수로 안전한 벡터 삭제

**✅ 결과**
- 씬 전환 시 크래시 발생 없음
- 안정적인 메모리 관리

<br>

---

## 💻 코드 샘플

### 📌 핵심 시스템

| 시스템 | 링크 |
|:---:|:---|
| 🎮 **SingleTon 매니저 시스템** | [코드 보기](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCore.cpp#L58-L103) |
| 🔄 **Core 게임 루프** | [코드 보기](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCore.cpp#L106-L173) |

### 🗺️ 타일맵 시스템

| 기능 | 링크 |
|:---:|:---|
| ✂️ **비트맵 분할 시스템** | [코드 보기](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/Direct2DMgr.cpp#L210-L265) |
| 🚀 **타일맵 생성 최적화** | [코드 보기](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CScene.cpp#L431-L547) |

### ⚡ 이벤트 시스템

| 기능 | 링크 |
|:---:|:---|
| 📝 **이벤트 등록** | [코드 보기](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/func.cpp#L7-L43) |
| 🔄 **이벤트 처리** | [코드 보기](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L22-L42) |

### 💥 충돌 시스템

| 기능 | 링크 |
|:---:|:---|
| 🎯 **충돌 감지** | [코드 보기](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCollisionMgr.cpp#L22-L129) |

---





# 🎮 TBI 모작

<p align="left">
  <img src="https://github.com/user-attachments/assets/68e566af-bb56-4afb-9842-1002208e6540" width="800"/>
</p>

<div align="left">

### 📌 프로젝트 정보

| 항목 | 내용 |
|:---:|:---|
| 🎯 **장르** | 로그라이크, 던전 크롤러, 탑다운 슈팅 |
| ⏱️ **개발 기간** | 2개월 |
| 👥 **개발 인원** | 1인 (개인 프로젝트) |
| 🛠️ **개발 환경** | C++, Win32 API, Direct2D, FMOD |
| 🎬 **시연 영상** | [바로가기](https://tobrother.tistory.com/144) |
| 📝 **개발 블로그** | [상세 개발 과정](https://tobrother.tistory.com/category/WinApi/TBI%28%EB%8D%94%20%EB%B0%94%EC%9D%B8%EB%94%A9%20%EC%98%A4%EB%B8%8C%20%EC%95%84%EC%9D%B4%EC%9E%91%29%20%EB%AA%A8%EC%9E%91) |
| 💾 **GitHub** | [소스코드](https://github.com/vfly1189/TBI) |

</div>

<br>

## 📖 게임 개요

The Binding of Isaac(TBI)는 로그라이크 던전 크롤러 게임으로, 플레이어는 아이작이 되어 무작위로 생성되는 던전을 탐험하며 다양한 몬스터와 보스를 상대합니다. 눈물(탄환)을 발사하여 적을 처치하고, 방마다 등장하는 아이템을 수집하여 능력을 강화하는 것이 핵심입니다. 본 프로젝트는 C++과 Win32 API, Direct2D를 활용하여 원작의 독특한 게임플레이와 아이템 시너지 시스템을 재현한 개인 프로젝트입니다.

<br>

---

## 🔨 주요 개발

<details open>
<summary><b>🏗️ 상속 기반 객체 시스템</b></summary>

<br>

**계층적 오브젝트 구조**
- CObject 최상위 클래스를 기반으로 Player, Monster, Item, Projectile 등 구현
- 각 객체 타입별 특화된 기능을 가진 추상 클래스 설계
- Clone() 패턴을 통한 효율적인 객체 복제 시스템

**아이템 계층 구조**
- CItem 추상 기본 클래스에서 CPickUpItem, CCollectiblesItem, CBomb으로 분화
- 타입별 독립적인 동작 방식과 상호작용 로직 구현
- enum 기반 타입 관리로 확장성 확보

</details>

<details open>
<summary><b>🎮 State 패턴 기반 몬스터 AI</b></summary>

<br>

**유연한 AI 상태 관리**
- State 패턴을 활용한 몬스터 행동 시스템 구현
- IDLE, TRACE, ATTACK, DEAD 등 상태별 독립적인 로직
- 상태 전환 조건을 명확히 정의하여 예측 가능한 AI 동작

**다양한 몬스터 타입**
- 기본 추적형, 원거리 공격형, 돌진형 등 다양한 패턴 구현
- 각 몬스터별 고유한 상태 머신과 애니메이션 적용

</details>

<details open>
<summary><b>🗺️ 절차적 던전 생성 시스템</b></summary>

<br>

**랜덤 던전 생성 알고리즘**
- 방 배치 알고리즘을 통한 무작위 던전 구조 생성
- 시작방, 보물방, 보스방 등 특수 방 배치 로직
- 방 간 연결 통로 자동 생성

**타일 기반 맵 시스템**
- 벽, 바닥, 문 등 타일 타입별 충돌 처리
- 방 입장 시 문 개폐 애니메이션 및 몬스터 스폰

</details>

<details open>
<summary><b>💥 물리 기반 전투 시스템</b></summary>

<br>

**CRigidBody 컴포넌트**
- 중력, 속도, 마찰력을 고려한 물리 시뮬레이션
- 넉백, 발사체 궤적 등 물리 기반 전투 효과
- 벽 충돌 시 반사 처리

**충돌 감지 시스템**
- CCollider 컴포넌트를 통한 AABB 충돌 검사
- 충돌 진입/유지/탈출 이벤트 처리
- 레이어별 충돌 매트릭스 관리

</details>

<details>
<summary><b>🎨 애니메이션 시스템</b></summary>

<br>

**CAnimator 컴포넌트**
- 프레임 기반 스프라이트 애니메이션 시스템
- 애니메이션 재생, 일시정지, 반복 제어 기능
- 애니메이션 종료 이벤트 콜백 지원

**동적 애니메이션 생성**
- 런타임에 이미지 분할 및 애니메이션 생성
- 캐릭터, 몬스터, 아이템별 다양한 애니메이션 적용

</details>

<details>
<summary><b>🎁 아이템 시스템</b></summary>

<br>

**수집형 아이템 (PickUpItem)**
- 동전, 하트, 열쇠, 폭탄 등 소모성 아이템
- 충돌 시 자동 수집 및 효과 적용
- 타입별 개별 사운드 효과

**장식형 아이템 (CollectiblesItem)**
- 영구 능력치 상승 아이템
- 받침대, 그림자를 포함한 계층적 UI 구조
- 동적 이미지 로딩 시스템

**폭탄 아이템**
- 점화 → 폭발 → 소멸의 상태 머신 구현
- 시간 기반 상태 전환 로직
- 폭발 시 충돌 영역 동적 확장

</details>

<details>
<summary><b>🎬 씬 관리 시스템</b></summary>

<br>

**씬 전환 구조**
- 메인 메뉴, 캐릭터 선택, 던전, 보스방 씬 구현
- 페이드 인/아웃 효과를 통한 부드러운 전환
- 씬별 리소스 로드/언로드 관리

**UI 시스템**
- 체력, 아이템 개수 등 게임 HUD 표시
- 계층적 UI 구조로 복잡한 UI 구성 가능
- 버튼, 패널 등 상호작용 가능한 UI 컴포넌트

</details>

<br>

---

## 🛠️ 문제 해결

### 1️⃣ State 패턴을 통한 몬스터 AI 관리

> **🚨 문제 상황**
> 
> if-else 중첩으로 구현된 몬스터 AI 로직이 복잡해지고 유지보수가 어려움

**💡 해결 과정**
- State 패턴을 도입하여 각 상태를 독립적인 클래스로 분리
- CState 추상 클래스를 기반으로 IdleState, TraceState, AttackState 구현
- 상태 전환 조건을 명확히 정의하고 FSM(Finite State Machine) 구조 적용
- 각 몬스터 타입별 상태 클래스를 상속하여 특화된 행동 구현

**✅ 결과**
- 코드 가독성 및 유지보수성 대폭 향상
- 새로운 몬스터 타입 추가 시 기존 코드 수정 최소화
- 상태별 독립적인 디버깅 가능

<br>

### 2️⃣ BFS 기반 절차적 던전 생성 시스템

> **🚨 문제 상황**
> 
> 고정된 맵 구조로 인한 반복 플레이 시 지루함 발생

**💡 해결 과정**
- **BFS(Breadth-First Search) 알고리즘**을 활용한 방 배치 시스템 구현
- 시작 방에서 큐(queue)를 사용하여 인접한 4방향으로 순차적으로 방 확장
- `countNeighbors()` 함수로 각 방이 **단일 연결**만 가지도록 제약 조건 적용
- 방향을 랜덤으로 섞어(`std::shuffle`) 매번 다른 던전 구조 생성
- 최소 방 개수(10개)와 최대 방 개수(레벨에 따라 동적 조정) 조건 만족 시까지 재생성
- 맨해튼 거리(Manhattan Distance) 계산을 통한 특수 방 배치
  - **보스방**: 시작 방에서 가장 먼 막다른 방에 배치
  - **보물방**: 시작 방에서 가장 가까운 막다른 방에 배치
- JSON 파일 기반 방 레이아웃 로딩 시스템

**✅ 결과**
- 매 플레이마다 연결성이 보장된 유기적인 던전 구조 생성
- 레벨에 따라 방 개수가 증가하여 점진적인 난이도 조절
- 특수 방의 전략적 배치로 탐험 요소 강화
- 막다른 방 조건으로 보상/도전 방 자연스럽게 배치

<br>

### 3️⃣ 물리 기반 넉백 및 투사체 시스템

> **🚨 문제 상황**
> 
> 단순 좌표 이동 방식의 전투가 밋밋하고 타격감 부족

**💡 해결 과정**
- CRigidBody 컴포넌트에 힘(Force), 가속도, 속도 개념 도입
- `AddForce()` 함수로 즉각적인 힘 적용 시스템 구현
- 매 프레임 속도에 마찰력을 적용하여 자연스러운 감속
- 벽 충돌 시 속도 벡터 반사 처리

**✅ 결과**
- 피격 시 넉백 효과로 타격감 향상
- 포물선을 그리는 눈물 발사로 원작 느낌 재현

<br>

### 4️⃣ 아이템 계층 구조 설계 및 동적 효과 적용

> **🚨 문제 상황**
> 
> 다양한 아이템 타입(소모성, 영구, 폭탄 등)을 하나의 클래스로 관리하기 어려움

**💡 해결 과정**
- CItem 추상 기본 클래스 설계
- 타입별 특화 클래스 분리: CPickUpItem, CCollectiblesItem, CBomb
- 각 클래스에서 고유한 상호작용 로직 구현
- CollectiblesItem은 복합 UI 구조(받침대, 그림자, 아이템)로 구성
- 폭탄은 상태 머신 패턴으로 점화/폭발 단계 관리

**✅ 결과**
- 아이템 타입별 독립적인 로직으로 확장성 향상
- 새로운 아이템 추가 시 기존 코드 영향 최소화
- 아이템별 고유한 효과와 애니메이션 적용 가능

<br>

---

## 💻 코드 샘플

### 📌 State 패턴

| 기능 | 링크 |
|:---:|:---|
| 🤖 **State 기본 구조** | [코드 보기](https://github.com/vfly1189/TBI/blob/main/Client/CState.h) |
| 🏃 **TraceState 구현** | [코드 보기](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CFlyTraceState.cpp#L24-L63) |

### 🎁 아이템 시스템

| 기능 | 링크 |
|:---:|:---|
| 🎨 **아이템 기본 클래스** | [코드 보기](https://github.com/vfly1189/TBI/blob/main/Client/CItem.h) |
| 💎 **PickUpItem 구현** | [코드 보기](https://github.com/vfly1189/TBI/blob/main/Client/CPickUpItem.cpp) |
| 💣 **폭탄 시스템** | [코드 보기](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CBomb.cpp#L33-L66) |

### ⚙️ 컴포넌트 시스템

| 기능 | 링크 |
|:---:|:---|
| 💥 **RigidBody 물리** | [코드 보기](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CRigidBody.cpp#L23-L82) |
| 🎯 **Collider 충돌** | [코드 보기](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CCollisionMgr.cpp#L22-L129) |
| 🎬 **Animator 애니메이션** | [코드 보기](https://github.com/vfly1189/TBI/blob/main/Client/CAnimator.cpp) |

### 🗺️ 던전 생성

| 기능 | 링크 |
|:---:|:---|
| 🏰 **던전 생성 알고리즘** | [코드 보기](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/MapMgr.cpp#L27-L135) |
| 🚪 **방 관리 시스템** | [코드 보기](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/MapMgr.cpp#L395-L455) |
---


---


---

# 🎮 이터널 리턴 모작

<p align="left">
  <img src="https://github.com/user-attachments/assets/1d959a57-f3e9-4a0a-86ab-3b0b7e336d19" width="800"/>
</p>

<div align="left">

### 📌 프로젝트 정보

| 항목 | 내용 |
|:---:|:---|
| 🎯 **장르** | 쿼터뷰, 배틀로얄, MOBA |
| ⏱️ **개발 기간** | 2개월 |
| 👥 **개발 인원** | 2인 (프로그래머로 참여) |
| 🛠️ **개발 환경** | C++, DirectX11, FMOD, ImGui |
| 🎬 **시연 영상** | [YouTube 바로가기](https://www.youtube.com/watch?v=b6XVkd0xc-E&list=LL&index=19&t=1s) |
| 📝 **개발 블로그** | [상세 개발 과정](https://tobrother.tistory.com/category/DirectX11/Eternal%20Return%20%EB%AA%A8%EC%9E%91) |
| 💾 **GitHub** | [소스코드](https://github.com/HyangRim/DirectX11-Engine-Client) |

</div>

<br>

## 📖 게임 개요

이터널 리턴은 배틀로얄과 MOBA 장르가 결합된 쿼터뷰 서바이벌 게임입니다. 플레이어는 특정 캐릭터를 선택하여 맵을 탐색하며 재료를 수집하고, 제작 시스템을 통해 장비를 강화하여 최후의 1인(또는 1팀)이 되는 것을 목표로 합니다. 전략적인 동선 계획과 실시간 전투가 결합된 독특한 게임플레이가 특징입니다. 본 프로젝트는 C++과 DirectX11을 사용하여 핵심 메커니즘을 구현한 2인 협업 프로젝트입니다.

<br>

---

## 🔨 주요 개발

<details open>
<summary><b>🎨 Deferred Rendering 파이프라인</b></summary>

<br>

**디퍼드 렌더링 시스템 구축**
- Forward Rendering에서 Deferred Rendering으로 전환하여 다중 광원 처리 최적화
- G-Buffer 4개 구성 (Albedo, Normal, Position, Material)
- 멀티 렌더 타겟(MRT)을 활용한 지오메트리 정보 저장
- 풀스크린 쿼드를 통한 라이팅 패스 구현

**렌더링 파이프라인 구조**
- Shadow Pass: 4096x4096 그림자맵 생성
- Geometry Pass: 불투명 객체의 지오메트리 정보 G-Buffer에 저장
- Lighting Pass: G-Buffer 데이터 기반 조명 계산
- Forward Pass: 투명 객체 처리 (알파 블렌딩)

</details>

<details open>
<summary><b>🎭 인스턴싱 기반 렌더링</b></summary>

<br>

**GPU 인스턴싱 시스템**
- 동일 메시의 다수 객체를 한 번의 DrawCall로 처리
- 인스턴스 버퍼를 통한 Transform 데이터 전달
- MeshRenderer, ModelRenderer, AnimRenderer별 인스턴싱 지원
- DrawIndexedInstanced를 활용한 배치 렌더링

**성능 최적화**
- DrawCall 수 대폭 감소
- CPU-GPU 병목 현상 해소
- 대규모 오브젝트 렌더링 안정화

</details>

<details open>
<summary><b>🌑 쿼드 트리</b></summary>

<br>

**쿼드 트리(Quad Tree) 구현**
- 2D 공간을 4분할하는 트리 자료구조 설계 및 적용
- 각 노드에 해당 영역 내 오브젝트 정보 저장
- 탐색/삽입/삭제 연산에 따라 노드 분할과 병합 자동 관리
- 카메라 시야(Frustum)와 노드 영역의 교차 검사로 렌더링 대상을 신속하게 필터링

**최적화 기법**
- 오브젝트 수가 많아질수록 전체 탐색(O(n)) 대신 부분 공간 탐색(O(log n))으로 성능 대폭 향상
- 충돌 검사/렌더링 등 많은 반복 연산이 필요한 곳에서 연산량 감소
- 넓은 맵, 많은 오브젝트가 배치되는 상황에서도 프레임 드랍 없이 효율적 처리

</details>

<details open>
<summary><b>🌫️ Fog of War (전장의 안개) 시스템</b></summary>

<br>

**FOW 메커니즘**
- 플레이어 시야 범위 기반 가시성 계산
- 실시간 탐색 영역 업데이트
- 셰이더에서 픽셀별 가시성 판정
- 그라데이션 효과로 자연스러운 시야 전환

**구현 세부사항**
- 월드 좌표 기반 거리 계산
- 동적 시야 범위 조절 가능
- 팀 플레이 시 시야 공유 로직

</details>

<details>
<summary><b>🎬 애니메이션 시스템</b></summary>

<br>

**스켈레탈 애니메이션**
- FBX 기반 본 애니메이션 구현
- Compute Shader를 활용한 스키닝 연산
- 애니메이션 블렌딩 및 전환
- 루트 모션(Root Motion) 지원

**애니메이션 최적화**
- GPU 스키닝으로 CPU 부하 감소
- 애니메이션 인스턴싱 지원
- LOD에 따른 애니메이션 품질 조절

</details>

<details>
<summary><b>🏗️ 컴포넌트 기반 아키텍처</b></summary>

<br>

**유연한 게임 오브젝트 시스템**
- GameObject 기반 계층 구조
- Transform, MeshRenderer, Collider 등 다양한 컴포넌트
- Component 추가/제거/검색 시스템
- 부모-자식 관계를 통한 Transform 계층

**매니저 시스템**
- SceneManager: 씬 전환 및 오브젝트 관리
- ResourceManager: 메시, 텍스처, 셰이더 리소스 관리
- InputManager: 키보드/마우스 입력 처리
- TimeManager: 델타타임 및 FPS 관리

</details>

<details>
<summary><b>🎯 충돌 감지 시스템</b></summary>

<br>

**물리 기반 충돌 처리**
- AABB(Axis-Aligned Bounding Box) 충돌 검사
- OBB(Oriented Bounding Box) 지원
- Sphere Collider 구현
- 계층적 충돌 그룹 관리

**충돌 이벤트 시스템**
- OnCollisionEnter/Stay/Exit 콜백
- 레이어 기반 충돌 필터링
- 물리 재질별 반응 처리

</details>

<details>
<summary><b>🎮 카메라 시스템</b></summary>

<br>

**쿼터뷰 카메라**
- 플레이어 추적 카메라
- 부드러운 카메라 이동 (Lerp)
- 맵 경계 제한

**뷰/프로젝션 행렬 관리**
- View Matrix: 카메라 위치 및 방향
- Projection Matrix: 원근/직교 투영 전환
- Frustum Culling 지원

</details>

<br>

---

## 🛠️ 문제 해결

### 1️⃣ Forward에서 Deferred Rendering으로 전환

> **🚨 문제 상황**
> 
> 다수의 동적 광원 사용 시 Forward Rendering 방식에서 성능 저하 발생 (광원 수 × 오브젝트 수의 연산)

**💡 해결 과정**
- Deferred Rendering 파이프라인 설계 및 구현
- G-Buffer 4개 생성 (Albedo, Normal, Position, Material)
- 지오메트리 패스와 라이팅 패스 분리
- 멀티 렌더 타겟(MRT)을 통한 동시 렌더링
- 풀스크린 쿼드로 화면 전체에 조명 계산
- 투명 객체는 Forward Rendering으로 별도 처리

**✅ 결과**
- 다중 광원 사용 시 성능 대폭 향상
- 광원 수에 비례하지 않는 안정적인 프레임
- 복잡한 조명 효과 구현 가능

<br>

### 2️⃣ 인스턴싱을 통한 DrawCall 최적화

> **🚨 문제 상황**
> 
> 동일한 메시를 가진 다수의 오브젝트 렌더링 시 DrawCall이 과도하게 증가하여 CPU 병목 발생

**💡 해결 과정**
- GPU 인스턴싱 시스템 도입
- 인스턴스 버퍼 생성 및 Transform 데이터 전송
- `DrawIndexedInstanced()` API 활용
- 같은 메시/머티리얼을 가진 객체들을 배치로 묶어 처리
- Structured Buffer를 통한 인스턴스별 데이터 전달

**✅ 결과**
- DrawCall 수 **수천 회 → 수십 회**로 대폭 감소
- CPU 사용률 감소 및 프레임 안정화
- 대규모 오브젝트 배치 가능

<br>

### 3️⃣ 쿼드 트리 기반 공간 분할 최적화

> **🚨 문제 상황**
> 
> 넓은 맵에서 모든 오브젝트에 대해 충돌/렌더링 검사를 수행하여 불필요한 연산 발생

**💡 해결 과정**
- 쿼드 트리(Quad Tree) 자료구조 도입으로 공간 분할
- 맵을 4개의 사분면으로 재귀적으로 분할하는 트리 구조 구현
- 각 노드에 해당 영역 내 오브젝트 정보 저장
- 카메라 절두체(Frustum) 내 노드만 탐색하여 렌더링 대상 선별
- 충돌 검사 시 인접 영역의 오브젝트만 체크

**✅ 결과**
- 렌더링/충돌 검사 대상 오브젝트 수 대폭 감소
- 넓은 맵에서도 안정적인 프레임 유지
- 공간 쿼리 성능 향상 (O(n) → O(log n))

<br>

### 4️⃣ Fog of War 시스템 구현

> **🚨 문제 상황**
> 
> 전략 요소가 중요한 게임에서 플레이어 시야 제한 및 탐색 영역 표시 필요

**💡 해결 과정**
- 플레이어 위치 기반 시야 범위 계산
- 픽셀 셰이더에서 월드 좌표와 플레이어 위치 간 거리 계산
- 거리에 따른 가시성 계수 적용
- 그라데이션 효과로 시야 경계 자연스럽게 처리
- 라이팅 패스에서 FOW 효과 적용

**✅ 결과**
- 전략적 게임플레이 요소 강화
- 탐색의 재미 추가
- 시야 공유를 통한 팀 플레이 지원

<br>

---

## 💻 코드 샘플

### 📌 Deferred Rendering 파이프라인

| 시스템 | 링크 |
|:---:|:---|
| 🎨 **G-Buffer 생성** | [코드 보기](https://github.com/HyangRim/DirectX11-Engine-Client/blob/main/Engine/Graphics.cpp#L333-L390) |
| 💡 **Lighting Pass 셰이더** | [코드 보기](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Shaders/00.%20DeferredLighting.fx) |

### 🎭 인스턴싱 시스템

| 기능 | 링크 |
|:---:|:---|
| 🔄 **인스턴스 버퍼 관리** | [코드 보기](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Engine/InstancingBuffer.cpp) |
| 🎮 **MeshRenderer 인스턴싱** | [코드 보기](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/MeshRenderer.cpp#L91-L116) |

### 🌑 쿼드 트리

| 기능 | 링크 |
|:---:|:---|
| 🌓 **쿼드 트리 노드 삽입** | [코드 보기](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L218-L257) |
| ✨ **쿼드 트리 쿼리** | [코드 보기](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L75-L93) |

### 🌫️ Fog of War

| 기능 | 링크 |
|:---:|:---|
| 👁️ **FOW 계산 로직** | [코드 보기](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Shaders/FOW.fx) |

### 🎬 애니메이션 시스템

| 기능 | 링크 |
|:---:|:---|
| 🦴 **스켈레탈 애니메이션** | [코드 보기](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/ModelAnimator.cpp#L575-L611) |
| ⚡ **키프레임 보간** | [코드 보기](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/ModelAnimator.cpp#L749-L785) |

---


---


