# 📑 이형규 포트폴리오
>   <b>C++, Win32API, DX11</b>을 이용한 게임 개발의 경험이 있습니다. <br>

## <b> 주요 기술 - C++, DirectX11 </b>

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
       </a>
      </td>
      <td valign="top">
      <a>
 🎮 [TBI 모작](#-tbi-모작) <br>
 
 > 📖 [게임 개요](#-게임-개요-1) <br>
   🔨 [주요 개발](#-주요-개발-1) <br>
   🛠️ [문제 해결](#%EF%B8%8F-문제-해결-1) <br>
      </a>
      </td>
      <td valign="top">
      <a>
 🎮 [이터널리턴 모작](#-이터널-리턴-모작) <br>
 
 > 📖 [게임 개요](#-게임-개요-2) <br>
   🔨 [주요 개발](#-주요-개발-2) <br>
   🛠️ [문제 해결](#%EF%B8%8F-문제-해결-2) <br>
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

**싱글톤 패턴 기반 매니저 시스템 구현** [[📄매니저 시스템]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCore.cpp#L58-L103)
- CCore, CTimeMgr, CKeyMgr, CCamera, CSceneMgr 등 핵심 시스템을 싱글톤으로 설계
  - [[📄SceneMgr.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CSceneMgr.h)
  - [[📄Camera 구조]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCamera.cpp#L42-L70)
  - [[📄KeyMgr 구조]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CkeyMgr.cpp#L77-L133)
- 게임 전반에 걸쳐 일관된 접근 방식 제공 및 메모리 관리 효율화

</details>

<details open>
<summary><b>🎨 렌더링 시스템</b></summary>

<br>

**Direct2D 기반 렌더링 파이프라인 구축** [[📄Direct2D.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/Direct2DMgr.h)
- GDI/GDI+에서 Direct2D로 전환하여 FPS 20~40에서 60+ FPS로 성능 대폭 개선
- 자동 더블 버퍼링을 통한 깜박임 없는 부드러운 화면 전환

**비트맵 관리 시스템**
- `unordered_map`을 활용한 비트맵 캐싱 시스템 구현
- 타일 분할 기능: 큰 이미지를 32x32 픽셀 단위로 분할하여 타일맵 생성
  - [[📄비트맵 분할 함수]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/Direct2DMgr.cpp#L210-L265) 
- 초기 로딩 시 모든 리소스를 메모리에 적재하여 런타임 성능 최적화

</details>

<details open>
<summary><b>🎬 씬 관리 시스템</b></summary>

<br>

**씬 전환 구조**
- CScene 추상 클래스 기반 상속 구조 (Main, Select_Character, Select_Weapon, Start, Shop, Run_End)
  - [[📄Scene.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CScene.h)
- Enter()/Exit() 가상 함수를 통한 씬 진입/탈출 시 리소스 관리
- 이벤트 지연 처리 시스템으로 안전한 씬 전환
  - [[📄씬 전환 이벤트 등록]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/func.cpp#L26-L33)
  - [[📄이벤트 매니저 update]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L22-L42)
  - [[📄이벤트 실행]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L71-L80) 
- ![씬전환-1](https://github.com/user-attachments/assets/204ca5d7-a298-480b-add6-d2cc7059701a)![씬전환-2](https://github.com/user-attachments/assets/15368ea7-bc48-474b-a26a-6f6321f9d2cd)

</details>

<details open>
<summary><b>🧩 게임 오브젝트 시스템</b></summary>

<br>

**컴포넌트 기반 오브젝트 설계** [[📄CObject.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CObject.h)
- CObject 추상 클래스를 기반으로 Player, Monster, Weapon, UI 등 다양한 객체 구현
- Collider, Animator, Rigidbody 등 필요에 따라 동적으로 추가 가능한 컴포넌트
  - [[📄Collider.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CCollider.h)
  - [[📄Animator.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CAnimator.h)
  - [[📄Rigidbody.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CRigidbody.h)
- Clone() 가상 함수를 통한 프로토타입 패턴 구현

</details>

<details open>
<summary><b>📦 리소스 관리</b></summary>

<br>

**자동 리소스 로더** [[📄파일 로딩]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CFileMgr.cpp#L64-L100)
- 게임 시작 시 content 폴더를 재귀적으로 탐색하여 모든 png, mp3, wav 파일 자동 로딩
- 파일명을 태그로 사용하여 간편한 리소스 접근
- 경로 관리자(CPathMgr)를 통한 상대 경로 처리

</details>

<details open>
<summary><b>🖼️ UI 시스템</b></summary>

<br>

**계층적 UI 구조**
- PanelUI, BtnUI, SliderUI 등 다양한 UI 컴포넌트
  - [[📄CUI.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CUI.h)
  - [[📄CPanelUI.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CPanelUI.h)
  - [[📄CBtn.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CBtnUI.h)
- 콜백 함수 시스템을 통한 이벤트 처리 [[📄버튼UI 콜백 함수 시스템]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CBtnUI.h#L90-L109)
- TextUI 컴포넌트로 텍스트 렌더링 및 외곽선 효과 지원
- ![UI](https://github.com/user-attachments/assets/afb4b6f7-7733-4251-9294-30503a1073dd)


</details>

<details open>
<summary><b>🔊 사운드 시스템</b></summary>

<br>

**FMOD 기반 오디오 엔진** [[📄사운드 매니저]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CSoundMgr.h)
- BGM과 SFX 채널 분리 관리
- 마스터 볼륨, BGM 볼륨, SFX 볼륨 개별 조절 기능
- 슬라이더 UI를 통한 실시간 볼륨 조정
- ![음향 조절](https://github.com/user-attachments/assets/b3692234-9d25-4c7d-a87d-42c6076ef09f)


</details>

<br>

---

## 🛠️ 문제 해결

### 1️⃣ GDI에서 Direct2D로 전환을 통한 성능 개선

> **🚨 문제 상황**
> 
> GDI/GDI+를 사용한 초기 렌더링에서 타일맵만 그려도 FPS가 20~40대로 저조한 성능

**💡 해결 과정** [[📄Direct2D 초기화]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/Direct2DMgr.cpp#L15-L59)
- Direct2D API 학습 및 렌더링 파이프라인 재구축
- `ID2D1HwndRenderTarget`을 통한 하드웨어 가속 렌더링 적용
- `CreateCompatibleRenderTarget()`을 활용한 오프스크린 렌더링 구현

**✅ 결과**
- **안정적인 퍼포먼스**: GDI에서 Direct2D 전환 후, 대규모 웨이브에서도 **FPS 60+** 를 안정적으로 유지
- **시각적 개선**: 더블 버퍼링 적용으로 화면 깜박임(Flickering) 현상 제거
- **플레이 경험**: 수백 개의 투사체와 몬스터가 등장하는 상황에서도 끊김 없는 부드러운 조작감 구현

| **대규모 웨이브** | **FPS 변화** |
| :---: | :---: |
| ![몬스터 많을때 플레이-1](https://github.com/user-attachments/assets/326b4b49-d345-45b0-bc99-995a12504daf) | ![몬스터 많을때 플레이-2](https://github.com/user-attachments/assets/36cd55b9-d3a5-4cbe-bef0-1e822fc2d569) |

<br>

### 2️⃣ 타일맵 렌더링 최적화
> **🚨 문제 상황**
> 
> 36x36 크기의 타일맵을 구현하면서 매 프레임 1,296번의 DrawBitmap을 호출.
> 
> 초기에는 600 FPS 이상이 나와 문제가 없어 보였으나, 몬스터와 투사체가 늘어나는 후반부 웨이브에서는 렌더링 부하가 로직 처리에 영향을 줄 위험이 있었음.

**💡 해결 과정** [[📄타일맵 생성 함수]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CScene.cpp#L431-L547)
- 오프스크린 렌더 타겟(`ID2D1BitmapRenderTarget`)을 생성하여 거대한 캔버스(1,152x1,152 픽셀) 준비
- 게임 시작 시 모든 32x32 픽셀 타일들을 하나의 거대한 비트맵으로 미리 합성 
- 테두리 타일은 규칙적으로, 내부 타일은 랜덤하게 배치하여 자연스러운 맵 생성
- 런타임에는 합성된 단일 비트맵만 렌더링하도록 변경

**✅ 결과**
- 매 프레임 DrawBitmap() 호출 횟수가 **1,296회 → 1회**로 대폭 감소
- 타일맵 렌더링 성능 향상 및 안정적인 60 FPS 유지
- 메모리 사용량은 증가했으나 CPU 부하 크게 감소
- FPS: 평균 650 → 1,400 (약 2.15배 증가)
- Frame Time: 1.54ms → 0.71ms (약 0.8ms 단축)
- 이 최적화를 통해 확보된 연산 자원은 후반부 100마리 이상의 적과 충돌 처리를 안정적으로 수행하는 데 사용.
-
| **Before (최적화 전)** | **After (최적화 후)** |
| :---: | :---: |
| ![타일최적화(Before)](https://github.com/user-attachments/assets/e3b623a7-a8d7-4381-8404-7a0877b81e6d) | ![타일최적화(After)](https://github.com/user-attachments/assets/d997642b-122b-469d-aef6-ad89d118bd60) |
| **DrawCall: 1,296회 / FPS: ~650** | **DrawCall: 1회 / FPS: ~1,400** |

<br>

### 3️⃣ 리소스 로딩 시스템 자동화

> **🚨 문제 상황**
> 
> 각 Scene마다 필요한 리소스를 수동으로 로드하여 코드 중복 및 관리 어려움

**💡 해결 과정** [[📄파일 로딩]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CFileMgr.cpp#L64-L100)
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
  - [[📄이벤트 등록]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/func.cpp#L7-L43)
  - [[📄이벤트 처리]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L22-L42)
- 프레임 단위 작업이 모두 완료된 후 이벤트 처리
  - [[📄이벤트 매니저 업데이트 위치]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCore.cpp#L106-L173)
- Scene의 Enter()/Exit() 가상 함수로 명확한 초기화/정리 시점 제공
- unordered_set을 이용한 중복 이벤트 처리 방지

**✅ 결과**
- 안정적인 메모리 관리

<br>


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

**계층적 오브젝트 구조** [[📄CObject.h]](https://github.com/vfly1189/TBI/blob/master/TBI/CObject.h)
- CObject 최상위 클래스를 기반으로 Player, Monster, Item, Projectile 등 구현
- 각 객체 타입별 특화된 기능을 가진 추상 클래스 설계
</details>

<details open>
<summary><b>🎁 객체 지향적 아이템 설계 (계층 구조 및 시스템)</b></summary>

<br>

**추상화 및 확장성 설계**[[📄CItem.h]](https://github.com/vfly1189/TBI/blob/master/TBI/CItem.h)
- `CItem` 추상 클래스를 정의하고 `enum`으로 타입을 관리하여 확장성 확보
- 기능과 역할에 따라 3가지 핵심 파생 클래스로 분화하여 구현

**1. 수집형 아이템 (PickUpItem)**
- 동전, 하트, 열쇠, 폭탄 등 소모성 아이템 관리
- 충돌 시(`OnCollisionEnter`) 자동 수집 및 플레이어 스탯/인벤토리 반영
  - ![픽업아이템 획득](https://github.com/user-attachments/assets/95e0795a-3e6e-4039-82b0-c05b71865c45)

**2. 장식형 아이템 (CollectiblesItem)**
- 영구 능력치 상승 아이템 (패시브 효과) [[📄특수 아이템 초기화]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CCollectiblesItem.cpp#L29-L57)
- 받침대, 그림자, 아이템 본체를 포함하는 복합 렌더링 구조 및 동적 이미지 로딩
  - ![아이템 획득 및 적용](https://github.com/user-attachments/assets/09b499cf-fe3a-43c9-beb1-e17dd4fed194)

**3. 폭탄 아이템 (Bomb)** [[📄폭탄 동작 로직]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CBomb.cpp#L33-L66)
- 점화(Ignite) → 폭발(Explode) → 소멸(Dead)
- 폭발 시 충돌체(Collider) 크기를 동적으로 확장하여 광역 데미지 처리
  - ![폭탄](https://github.com/user-attachments/assets/75f1caeb-97e1-40b8-97fd-8ba791233793)

</details>


<details open>
<summary><b>🎮 State 패턴 기반 몬스터 AI</b></summary>

<br>

**AI 상태 관리**
- State 패턴을 활용한 몬스터 행동 시스템 구현 [[📄CState.h]](https://github.com/vfly1189/TBI/blob/main/Client/CState.h)
- IDLE, TRACE, ATTACK, DEAD 등 상태별 독립적인 로직 
  - [[📄파리 몬스터 TraceState]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CFlyTraceState.cpp#L24-L63)
  - [[📄보스 몬스터 AttackState]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CBabyPlumAttackState.cpp#L32-L118)  
  - [[📄원거리 공격형 몬스터 AttackState]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CBabyPlumAttackState.cpp#L32-L118)

- 상태 전환 조건을 정의하여 예측 가능한 AI 동작

**다양한 몬스터 타입**
- 기본 추적형, 원거리 공격형, 돌진형 등 다양한 패턴 구현
- 각 몬스터별 고유한 상태 머신과 애니메이션 적용
- | **파리 몬스터** | **원거리 몬스터** | **보스 몬스터** 
    | :---: | :---: | :---: |
    | ![파리 추적](https://github.com/user-attachments/assets/33cbe640-c99f-4651-bdd3-f058cb5a1db2) | ![Horf 몬스터](https://github.com/user-attachments/assets/6792ba1d-cc72-4054-9db4-8bcd0f158db9) | ![보스공격패턴](https://github.com/user-attachments/assets/a38557c8-7436-4120-83a2-5eb71f5fc734) |
</details>

<details open>
<summary><b>🗺️ 절차적 던전 생성 시스템</b></summary>

<br>

**랜덤 던전 생성 알고리즘**
- 방 배치 알고리즘을 통한 무작위 던전 구조 생성 [[📄방 생성 알고리즘]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/MapMgr.cpp#L27-L135)
- 시작방, 보물방, 보스방 등 특수 방 배치 로직 [[📄특수 방 배치]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/MapMgr.cpp#L395-L455)
- 방 간 연결 통로 자동 생성
<img width="507" height="128" alt="image" src="https://github.com/user-attachments/assets/872c7f53-d02c-4983-acfe-d897bcf4c3c9" />

**타일 기반 맵 시스템**
- 벽, 바닥, 문 등 타일 타입별 충돌 처리
- 방 입장 시 문 개폐 애니메이션 및 몬스터 스폰

</details>

<details open>
<summary><b>💥 물리 기반 전투 시스템</b></summary>

<br>

**CRigidBody 컴포넌트**
- 중력, 속도, 마찰력을 고려한 물리 시뮬레이션 [[📄물리 효과 적용]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CRigidBody.cpp#L23-L82)
- 넉백, 발사체 궤적 등 물리 기반 전투 효과
- 벽 충돌 시 반사 처리(보스 몬스터 한정)

**충돌 감지 시스템** [[📄충돌 감지]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CCollisionMgr.cpp#L40-L129)
- CCollider 컴포넌트를 통한 AABB 충돌 검사
- 충돌 진입/유지/탈출 이벤트 처리
- 레이어별 충돌 매트릭스 관리 [[📄충돌 그룹 지정]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CCollisionMgr.cpp#L148-L168)

</details>

<details open>
<summary><b>🎨 애니메이션 시스템</b></summary>

<br>

**CAnimator 컴포넌트**
- 프레임 기반 스프라이트 애니메이션 시스템
- 애니메이션 재생, 일시정지, 반복 제어 기능 [[📄애니메이션 기능]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CAnimator.cpp#L109-L154)

**동적 애니메이션 생성** [[📄플레이어 애니메이션 스프라이트 관리]](https://github.com/vfly1189/TBI/blob/master/TBI/CPlayerMgr.h)
- 런타임에 이미지 분할 및 애니메이션 생성
- 캐릭터, 몬스터, 아이템별 다양한 애니메이션 적용

</details>


</details>

<details open>
<summary><b>🎬 씬 관리 시스템</b></summary>

<br>

**씬 전환 구조**
- 메인 메뉴, 캐릭터 선택, 던전, 보스방 씬 구현
- 페이드 인/아웃 효과를 통한 부드러운 전환 [[📄화면 전환 페이트 인/아웃 효과]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CScene_Main.cpp#L166-L195)
- 씬별 리소스 로드/언로드 관리
  - ![씬전환](https://github.com/user-attachments/assets/507fe226-f282-47dc-8563-ec03adada943)


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

**💡 해결 과정** [[📄CState.h]](https://github.com/vfly1189/TBI/blob/master/TBI/CState.h)
- State 패턴을 도입하여 각 상태를 독립적인 클래스로 분리
- CState 추상 클래스를 기반으로 IdleState, TraceState, AttackState 구현
  - [[📄파리 몬스터 TraceState]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CFlyTraceState.cpp#L24-L63)
  - [[📄보스 몬스터 AttackState]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CBabyPlumAttackState.cpp#L32-L118)
- 상태 전환 조건을 정의하고 FSM(Finite State Machine) 구조 적용
  - [[📄보스 몬스터 TraceState -> AttackState 전환]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CBabyPlumTraceState.cpp#L43-L49)
  - [[📄보스 몬스터 IdleState -> TraceState 전환]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CBabyPlumIdleState.cpp#L67-L73)
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

**💡 해결 과정** [[📄방 생성 알고리즘]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/MapMgr.cpp#L27-L135)
- **BFS(Breadth-First Search) 알고리즘**을 활용한 방 배치 시스템 구현
- 시작 방에서 큐(queue)를 사용하여 인접한 4방향으로 순차적으로 방 확장
- `countNeighbors()` 함수로 각 방이 **단일 연결**만 가지도록 제약 조건 적용
- 방향을 랜덤으로 섞어(`std::shuffle`) 매번 다른 던전 구조 생성
- 최소 방 개수(10개)와 최대 방 개수(레벨에 따라 동적 조정) 조건 만족 시까지 재생성
  - | **1단계** | **2단계** | **3단계** |
    | :---: | :---: | :---: |
    | <img width="807" height="412" alt="image" src="https://github.com/user-attachments/assets/7d77cb29-e9e2-4caa-a34d-289e533a91af" /> | <img width="963" height="457" alt="image" src="https://github.com/user-attachments/assets/1f449f2d-f487-4053-b59b-203d965fd757" /> | <img width="1133" height="491" alt="image" src="https://github.com/user-attachments/assets/db3d42a8-f9ba-4fb6-8691-c53ae7fa475e" />|
- 맨해튼 거리(Manhattan Distance) 계산을 통한 특수 방 배치
  - **보스방**: 시작 방에서 가장 먼 막다른 방에 배치
  - **보물방**: 시작 방에서 가장 가까운 막다른 방에 배치
  - [[📄특수 방 배치]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/MapMgr.cpp#L395-L455)
- JSON 파일 기반 방 레이아웃 로딩 시스템

**💡왜 BFS 알고리즘인가?**
- 백트래킹(Backtracking) 피로도 최소화
  - DFS의 선형적 구조는 맵 이동 동선이 지나치게 길어지는 단점이 존재.
  - BFS를 통해 시작점 중심의 방사형 클러스터를 형성하여, 플레이어가 상점이나 보물방을 이용하기 위해 이동하는 불필요한 시간을 줄이고 전투 밀도를 높였습니다.

- 확장성을 고려한 공간 스캔
  - 순차적으로 인접 공간을 탐색하는 구조 덕분에, 추후 '2x2 대형 방'이나 '특수 모양 방'을 추가할 때 주변 빈 공간을 체크하고 할당하는 알고리즘으로 확장하기 유리하다고 판단.


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
  - [[📄CRigidBody 구현]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CRigidBody.cpp#L23-L82)
- `AddForce()` 함수로 즉각적인 힘 적용 시스템 구현
  - ![RigidBody](https://github.com/user-attachments/assets/ffaa5fc2-3c23-4de9-9a78-f540ad6e8cad)
- 매 프레임 속도에 마찰력을 적용하여 자연스러운 감속
- 벽 충돌 시 속도 벡터 반사 처리(보스 몬스터 한정)

**✅ 결과**
- 피격 시 넉백 효과로 타격감 향상
- 포물선을 그리는 눈물 발사로 원작 느낌 재현

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

**디퍼드 렌더링 시스템 구축** [[📄Deferred Rendering 구현]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L75-L113)
- Forward Rendering에서 Deferred Rendering으로 전환하여 다중 광원 처리 최적화 
- G-Buffer 4개 구성 (Albedo, Normal, Position, Material)
- 멀티 렌더 타겟(MRT)을 활용한 지오메트리 정보 저장
- 풀스크린 쿼드를 통한 라이팅 패스 구현

**렌더링 파이프라인 구조**
- Geometry Pass: 불투명 객체의 지오메트리 정보 G-Buffer에 저장 [[📄G-Buffer 셰이더]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Shaders/00.%20GBuffer.fx)
- Lighting Pass: G-Buffer 데이터 기반 조명 계산 [[📄Lighting 셰이더]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Shaders/00.%20DeferredLighting.fx#L121-L162)
- Forward Pass: 투명 객체 처리 (알파 블렌딩) [[📄UI 객체 셰이더]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Shaders/ImageShader.fx)

</details>

<details open>
<summary><b>🎭 인스턴싱 기반 렌더링</b></summary>

<br>

**GPU 인스턴싱 시스템**
- 동일 메시의 다수 객체를 한 번의 DrawCall로 처리
- 인스턴스 버퍼를 통한 Transform 데이터 전달
- MeshRenderer, ModelRenderer, AnimRenderer별 인스턴싱 지원
  - [[📄MeshRenderer]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L311-L348)
  - [[📄ModelRenderer]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L350-L386)
  - [[📄AnimRenderer]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L388-L435)

**성능 최적화**
- DrawCall 수 대폭 감소
- CPU-GPU 병목 현상 해소
- 대규모 오브젝트 렌더링 안정화

</details>

<details open>
<summary><b>🌑 쿼드 트리</b></summary>

<br>

**쿼드 트리(Quad Tree) 구현** [[📄QuadTree.h]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Engine/QuadTree.h)
- 2D 공간을 4분할하는 트리 자료구조 설계 및 적용
- 각 노드에 해당 영역 내 오브젝트 정보 저장 [[📄노드에 객체 삽입]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L218-L257)
- 탐색/삽입/삭제 연산에 따라 노드 분할과 병합 자동 관리
- 카메라 시야(Frustum)와 노드 영역의 교차 검사로 렌더링 대상을 신속하게 필터링 [[📄객체 필터링]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L587-L651)

**최적화 기법**
- 오브젝트 수가 많아질수록 전체 탐색(O(n)) 대신 부분 공간 탐색(O(log n))으로 성능 대폭 향상
- 충돌 검사/렌더링 등 많은 반복 연산이 필요한 곳에서 연산량 감소
- 넓은 맵, 많은 오브젝트가 배치되는 상황에서도 프레임 드랍 없이 효율적 처리

</details>

<details open>
<summary><b>🌫️ Fog of War (전장의 안개) 시스템</b></summary>

<br>

**FOW 메커니즘** [[📄FOW 계산]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Shaders/00.%20DeferredLighting.fx#L47-L72)
- 플레이어 시야 범위 기반 가시성 계산
- 실시간 탐색 영역 업데이트
- 셰이더에서 픽셀별 가시성 판정
- 그라데이션 효과로 자연스러운 시야 전환

**구현 세부사항**
- 월드 좌표 기반 거리 계산
- 동적 시야 범위 조절 가능

</details>

<details open>
<summary><b>🎬 애니메이션 시스템</b></summary>

<br>

**스켈레탈 애니메이션**
- FBX 기반 본 애니메이션 구현 [[📄애니메이션 정보 저장]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/ModelAnimator.cpp#L575-L608)
- Compute Shader를 활용한 스키닝 연산
- 애니메이션 블렌딩 및 전환
  - [[📄애니메이션 블렌딩]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/ModelAnimator.cpp#L57-L130)
  - [[📄애니메이션 블렌딩-셰이더]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Shaders/00.%20Render.fx#L118-L193)
- 루트 모션(Root Motion) 지원

**애니메이션 최적화**
- GPU 스키닝으로 CPU 부하 감소 [[📄인스턴싱 + GPU 스키닝]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L388-L435)
- 애니메이션 인스턴싱 지원
- LOD에 따른 애니메이션 품질 조절

</details>

<details open>
<summary><b>🏗️ 컴포넌트 기반 아키텍처</b></summary>

<br>

**유연한 게임 오브젝트 시스템**
- GameObject 기반 계층 구조 [[📄GameObject.h]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Engine/GameObject.h)
- Transform, MeshRenderer, Collider 등 다양한 컴포넌트
- 부모-자식 관계를 통한 Transform 계층

**매니저 시스템**
- SceneManager: 씬 전환 및 오브젝트 관리
- ResourceManager: 메시, 텍스처, 셰이더 리소스 관리
- InputManager: 키보드/마우스 입력 처리
- TimeManager: 델타타임 및 FPS 관리

</details>

<details open>
<summary><b>🎯 충돌 감지 시스템</b></summary>

<br>

**물리 기반 충돌 처리**
- AABB(Axis-Aligned Bounding Box) 충돌 검사 [[📄AABB 충돌 검사]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L421-L492)
- Sphere Collider 구현 [[📄Sphere Collider 충돌 검사]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L494-L580)
- 계층적 충돌 그룹 관리


</details>

<details open>
<summary><b>🎮 카메라 시스템</b></summary>

<br>

**쿼터뷰 카메라** [[📄메인 카메라]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Client/CameraScript.cpp#L10-L69)
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
- Deferred Rendering 파이프라인 설계 및 구현 [[📄Deferred Rendering 구현]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L75-L113)
- G-Buffer 4개 생성 (Albedo, Normal, Position, Material)
- 지오메트리 패스와 라이팅 패스 분리
  -  [[📄Geometry Pass]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L311-L435)
  -  [[📄Lighting Pass]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L454-L502)
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
  -  [[📄MeshRenderer Instancing]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/MeshRenderer.cpp#L91-L116)
  -  [[📄ModelAnimator Instancing]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/ModelAnimator.cpp#L421-L442)
  -  [[📄Model Instancing]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/ModelRenderer.cpp#L85-L127)
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
- 맵을 4개의 사분면으로 재귀적으로 분할하는 트리 구조 구현 [[📄QuadTree.h]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Engine/QuadTree.h)
- 각 노드에 해당 영역 내 오브젝트 정보 저장 [[📄노드에 객체 삽입]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L218-L257)
- 카메라 절두체(Frustum) 내 노드만 탐색하여 렌더링 대상 선별 [[📄객체 필터링]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L587-L651)
- 충돌 처리 [[📄쿼드 트리 충돌 로직]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L945-L1113)

**✅ 결과**
- 렌더링/충돌 검사 대상 오브젝트 수 대폭 감소
- 넓은 맵에서도 안정적인 프레임 유지
- 공간 쿼리 성능 향상 (O(n) → O(log n))

<br>

### 4️⃣ Fog of War 시스템 구현

> **🚨 문제 상황**
> 
> 전략 요소가 중요한 게임에서 플레이어 시야 제한 및 탐색 영역 표시 필요

**💡 해결 과정** [[📄FOW 계산]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Shaders/00.%20DeferredLighting.fx#L47-L72)
- 플레이어 위치 기반 시야 범위 계산 
- 픽셀 셰이더에서 월드 좌표와 플레이어 위치 간 거리 계산
- 거리에 따른 가시성 계수 적용
- 그라데이션 효과로 시야 경계 자연스럽게 처리
- 라이팅 패스에서 FOW 효과 적용

**✅ 결과**
- 전략적 게임플레이 요소 강화
- 탐색의 재미 추가

---


