# 📑 이형규 포트폴리오
>   <b>C++, Win32API, DX11</b>을 이용한 게임 개발의 경험이 있습니다. <br>

## <b> 주요 기술 - C++, DirectX11, UE5(공부중) </b>

## 목차

<table>
  <tbody>
    <tr>
      <td valign="top">
       <a>
        
 🍴 [Brotato 모작](#brotato-모작) <br>
 > 🧩 [게임 개요](#게임-개요) <br>
   ✏️ [주요 개발](#주요-개발) <br>
   ✅ [문제 해결](#문제-해결) <br>
   💻 [코드 샘플](#코드-샘플)
       </a>
      </td>
      <td valign="top">
      <a>
 🏭 [TBI 모작](#tbi-모작) <br>
 
 > 🧩 [게임 개요](#게임-개요-1) <br>
   ✏️ [주요 개발](#주요-개발-1) <br>
   ✅ [문제 해결](#문제-해결-1) <br>
   💻 [코드 샘플](#코드-샘플-1)
      </a>
      </td>
      <td valign="top">
      <a>
 🏭 [이터널리턴 모작](#이터널-리턴-모작) <br>
 
 > 🧩 [게임 개요](#게임-개요-2) <br>
   ✏️ [주요 개발](#주요-개발-2) <br>
   ✅ [문제 해결](#문제-해결-2) <br>
   💻 [코드 샘플](#코드-샘플-2)
      </a>
      </td>
    </tr>
  </tbody>
</table>


---

# Brotato 모작

## 게임 개요
**Brotato**는 로그라이크 요소가 결합된 탑다운 슈팅 게임으로, 플레이어는 감자 캐릭터를 조작하여 웨이브 방식으로 몰려오는 적들을 물리치며 생존하는 것이 목표입니다.<br>
각 웨이브 사이 상점에서 무기와 아이템을 구매하여 캐릭터를 강화하고, 다양한 빌드 조합을 통해 전략적인 플레이가 가능합니다.<br>
본 프로젝트는 C++과 DirectX11을 활용하여 원작의 핵심 게임플레이 메커니즘을 구현한 모작 프로젝트입니다.<br>

- 장르: 탑다운 슈팅, 로그라이크
- 개발 기간: 3주
- 개발 인원: 2인 (프로그래머로 참여)
- 개발 환경: C++, Win32 API, Direct2D, FMOD
- 시연 영상: [YouTube](https://www.youtube.com/watch?v=d-VZS1AdvtA&list=LL&index=3)

![screenshot](https://github.com/user-attachments/assets/0fa0932b-be02-4008-a29b-4711adab14db)

## 주요 개발
### 아키텍처 설계
- **싱글톤 패턴 기반 매니저 시스템** 구현
  - CCore, CTimeMgr, CKeyMgr, CCamera, CSceneMgr 등 핵심 시스템을 싱글톤으로 설계
  - 게임 전반에 걸쳐 일관된 접근 방식 제공 및 메모리 관리 효율화

### 렌더링 시스템
- **Direct2D 기반 렌더링 파이프라인** 구축
  - GDI/GDI+에서 Direct2D로 전환하여 FPS 20~40에서 60+ FPS로 성능 대폭 개선
  - 자동 더블 버퍼링을 통한 깜박임 없는 부드러운 화면 전환
  - WIC(Windows Imaging Component) 팩토리를 활용한 다양한 이미지 포맷 지원

- **비트맵 관리 시스템**
  - `unordered_map`을 활용한 비트맵 캐싱 시스템 구현
  - 타일 분할 기능: 큰 이미지를 32x32 픽셀 단위로 자동 분할하여 타일맵 생성
  - 초기 로딩 시 모든 리소스를 메모리에 적재하여 런타임 성능 최적화

### 씬 관리 시스템
- **유연한 씬 전환 구조**
  - CScene 추상 클래스 기반 상속 구조 (Main, Select_Character, Select_Weapon, Start, Shop, Run_End)
  - Enter()/Exit() 가상 함수를 통한 씬 진입/탈출 시 리소스 관리
  - 이벤트 지연 처리 시스템으로 안전한 씬 전환 보장

### 게임 오브젝트 시스템
- **컴포넌트 기반 오브젝트 설계**
  - CObject 추상 클래스를 기반으로 Player, Monster, Weapon, UI 등 다양한 객체 구현
  - Collider, Animator, Rigidbody, Gravity 등 필요에 따라 동적으로 추가 가능한 컴포넌트
  - Clone() 가상 함수를 통한 프로토타입 패턴 구현

### 폰트 시스템
- **커스텀 폰트 로더 구현**
  - DirectWrite API를 활용한 .ttf 폰트 파일 동적 로딩
  - CFontCollectionLoader와 CFontFileEnumerator를 통한 커스텀 폰트 컬렉션 관리
  - 다국어 지원 (영문: Anybody-Medium, 한글: NotoSansKR-Medium)

### 리소스 관리
- **자동 리소스 로더**
  - 게임 시작 시 content 폴더를 재귀적으로 탐색하여 모든 png, mp3, wav 파일 자동 로딩
  - 파일명을 태그로 사용하여 간편한 리소스 접근
  - 경로 관리자(CPathMgr)를 통한 상대 경로 처리

### UI 시스템
- **계층적 UI 구조**
  - PanelUI, BtnUI, SliderUI 등 다양한 UI 컴포넌트
  - 콜백 함수 시스템을 통한 이벤트 처리 (전역 함수 및 멤버 함수 모두 지원)
  - TextUI 컴포넌트로 텍스트 렌더링 및 외곽선 효과 지원

### 사운드 시스템
- **FMOD 기반 오디오 엔진**
  - BGM과 SFX 채널 분리 관리
  - 마스터 볼륨, BGM 볼륨, SFX 볼륨 개별 조절 기능
  - 슬라이더 UI를 통한 실시간 볼륨 조정

## 문제 해결
### 1. GDI에서 Direct2D로 전환을 통한 성능 개선
**문제 상황**
- GDI/GDI+를 사용한 초기 렌더링에서 타일맵만 그려도 FPS가 20~40대로 저조한 성능

**해결 과정**
- Direct2D API 학습 및 렌더링 파이프라인 전면 재구축
- `ID2D1HwndRenderTarget`을 통한 하드웨어 가속 렌더링 적용
- `CreateCompatibleRenderTarget()`을 활용한 오프스크린 렌더링 구현
- WIC 팩토리를 통한 효율적인 이미지 로딩

**결과**
- FPS 60+ 안정적 유지, 깜박임 현상 완전 제거
- 게임 전체의 부드러운 플레이 경험 제공

### 2. 타일맵 렌더링 최적화
**문제 상황**
- 카메라 좌표가 소수점을 가질 때 타일 간 흰색 줄(틈새)이 발생하는 시각적 버그

**해결 과정**
- 카메라의 `m_vLookAt` 좌표를 `floor()` 함수로 정수화하여 픽셀 정렬
- 플레이어 객체는 소수점 좌표를 유지하되, 카메라만 정수 좌표 사용
- 타일 렌더링 시 정확한 픽셀 단위 배치로 틈새 제거

**결과**
- 타일맵 렌더링 시 시각적 아티팩트 완전 제거
- 부드러운 플레이어 이동과 깔끔한 맵 표현 양립

### 3. 리소스 로딩 시스템 자동화
**문제 상황**
- 각 Scene마다 필요한 리소스를 수동으로 로드하여 코드 중복 및 관리 어려움

**해결 과정**
- CFileMgr 클래스 구현으로 폴더 재귀 탐색 기능 추가
- `WIN32_FIND_DATA`를 활용한 파일 시스템 탐색
- 파일 확장자별 자동 분류 및 적절한 매니저에 등록
  - .png → Direct2DMgr
  - .mp3/.wav → CSoundMgr (BGM은 main_title_bgm 키워드로 자동 구분)

**결과**
- 리소스 로드 코드 대폭 간소화
- 새로운 리소스 추가 시 파일만 추가하면 자동 인식

### 4. 메모리 관리 및 씬 전환 안정성
**문제 상황**
- 씬 전환 시 객체 소멸 타이밍 문제로 인한 댕글링 포인터 발생 가능성

**해결 과정**
- 이벤트 지연 처리 시스템(CEventMgr) 구현
- 프레임 단위 작업이 모두 완료된 후 이벤트 처리
- Scene의 Enter()/Exit() 가상 함수로 명확한 초기화/정리 시점 제공
- `Safe_Delete_Vec` 템플릿 함수로 안전한 벡터 삭제

**결과**
- 씬 전환 시 크래시 발생 없음
- 안정적인 메모리 관리


## 코드 샘플
**[SingleTon 매니저 시스템](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCore.cpp#L58-L103)**

**[Core 게임 루프](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCore.cpp#L106-L173)**

### 타일맵
**[비트맵 분할 시스템](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/Direct2DMgr.cpp#L210-L265)**
**[타일맵 생성 최적화](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CScene.cpp#L431-L547)**

### 이벤트 시스템
**[이벤트 등록](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/func.cpp#L7-L43)**
**[이벤트 처리](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L22-L42)**

### 충돌 시스템
**[충돌 감지](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCollisionMgr.cpp#L22-L129)**

---

---

# TBI 모작


## 게임 개요
**The Binding of Isaac(TBI)**는 로그라이크 던전 크롤러 게임으로, 플레이어는 아이작이 되어 무작위로 생성되는 던전을 탐험하며 다양한 몬스터와 보스를 상대합니다.<br>
눈물(탄환)을 발사하여 적을 처치하고, 방마다 등장하는 아이템을 수집하여 능력을 강화하는 것이 핵심입니다.<br>
본 프로젝트는 C++로 원작의 독특한 게임플레이와 아이템 시너지 시스템을 재현한 개인 프로젝트입니다.<br>

- 장르: 로그라이크, 던전 크롤러, 탑다운 슈팅
- 개발 기간: 2개월월
- 개발 인원: 1인 (개인 프로젝트)
- 개발 환경: C++, DirectX11
- 관련 자료: [블로그 링크]

![screenshot](https://github.com/user-attachments/assets/68e566af-bb56-4afb-9842-1002208e6540)

## 주요 개발
여기에 주요 개발 내용...

## 문제 해결
여기에 문제 해결 내용...

## 코드 샘플
여기에 코드 샘플...

---


---

# 이터널 리턴 모작

## 게임 개요
**이터널 리턴**은 배틀로얄과 MOBA 장르가 결합된 쿼터뷰 서바이벌 게임입니다.<br> 
플레이어는 특정 캐릭터를 선택하여 맵을 탐색하며 재료를 수집하고, 제작 시스템을 통해 장비를 강화하여 최후의 1인(또는 1팀)이 되는 것을 목표로 합니다.<br>
전략적인 동선 계획과 실시간 전투가 결합된 독특한 게임플레이가 특징입니다.<br> 
본 프로젝트는 C++과 DirectX11을 사용하여 핵심 메커니즘을 구현한 2인 협업 프로젝트입니다.

- 장르: 쿼터뷰, 배틀로얄, MOBA
- 개발 기간: 2개월
- 개발 인원: 2인 (프로그래머로 참여)
- 개발 환경: C++, DirectX11, FMOD, ImGui

![screenshot](https://github.com/user-attachments/assets/1d959a57-f3e9-4a0a-86ab-3b0b7e336d19)

## 주요 개발
여기에 주요 개발 내용...

## 문제 해결
여기에 문제 해결 내용...

## 코드 샘플
여기에 코드 샘플...

---


