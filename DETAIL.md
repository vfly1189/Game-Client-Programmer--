# 📑 이형규 포트폴리오
## INTRODUCTION

<div align="center">

저는 이런 개발자입니다.

</div>

<br>

---

### 🎮 재미 — "어차피 해야 한다면, 즐기면서 하는 게 결과도 다릅니다"
- 게임 개발이 좋아서 선택한 일입니다. 좋아하는 일은 어렵고 귀찮은 순간에도 계속하게 만드는 힘이 있고, 그게 열정이라고 생각합니다.
- 게임 개발을 선택한 이유도, 지금도 계속하는 이유도 결국 같습니다 — 재밌으니까요.
  
---

### 🏗️ 구조 — "잘 짜인 구조를 보면 괜히 뿌듯한 사람"
- 혼자 작성한 코드라도 타인이 읽고 수정할 것을 염두에 두고 설계합니다.
- 기능이 동작하는 것보다, **왜 이렇게 설계했는지 설명할 수 있는 코드**를 더 중요하게 생각합니다. [인터페이스 하나로 데미지 파이프라인을 일원화](#combat-bluearchive)하거나, [공격자-피격자 간 결합을 끊어낸 설계](#combat-bluearchive)가 그 결과입니다.

***

### 🚀 도전 — "재밌을 것 같으면 일단 뛰어드는 사람"
- 익숙한 방식이 동작하더라도, **더 나은 구조나 기술이 있다면 다시 짭니다.** 단일 JSON에서 시작해 [Excel/JSON 하이브리드 파이프라인으로 진화](#data-driven-trouble)시키거나, [C# Task의 레이스 컨디션을 UniTask 메인스레드 동기화로 해결](#async-unitask-trouble)한 것이 그 예입니다.
- 완벽한 준비보다 **어느 정도 각이 잡히면 바로 실행하는 쪽**이 더 많이 배운다고 생각합니다. [FSM의 유지보수 한계를 직접 겪고 Behavior Tree로 리팩토링](#fsm-to-bt)한 것도 그렇게 시작됐습니다.

---

<br>

## 목차<a name="table-of-contents"></a>

<table>
  <thead>
    <tr>
      <th>🎮 블루아카이브 팬메이드 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th>🎮 이터널 리턴 모작 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th>🎮 Brotato 모작&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td valign="top">
        <br>
        <b><a href="#bluearchive-main">🎮 프로젝트 메인</a></b><br>
        <b><a href="#overview-bluearchive">📖 게임 개요</a></b><br>
        <b><a href="#goals-bluearchive">📌 학습 목표 및 달성</a></b><br>
        <b><a href="#features-bluearchive">🔨 주요 개발</a></b><br>
        <b><a href="#troubleshooting-bluearchive">🛠️ 문제 해결</a></b><br>
        &nbsp;&nbsp; └ <a href="#optimization-trouble">공간 분할(Sector) 스포너 최적화</a><br>
        &nbsp;&nbsp; └ <a href="#async-unitask-trouble">UniTask 비동기 파이프라인</a><br>
        &nbsp;&nbsp; └ <a href="#data-driven-trouble">데이터 관리 한계 극복 및 자동화</a>
      </td>
      <td valign="top">
        <br>
        <b><a href="#eternal-return-main">🎮 프로젝트 메인</a></b><br>
        <b><a href="#overview-eternal">📖 게임 개요</a></b><br>
        <b><a href="#goals-eternal">📌 학습 목표 및 달성</a></b><br>
        <b><a href="#features-eternal">🔨 주요 개발</a></b><br>
        <b><a href="#troubleshooting-eternal-return">🛠️ 문제 해결</a></b><br>
        &nbsp;&nbsp; └ <a href="#deferred-rendering-trouble">Deferred Rendering 전환</a><br>
        &nbsp;&nbsp; └ <a href="#navmesh-optimization">NavMesh 검색 최적화</a><br>
        &nbsp;&nbsp; └ <a href="#quadtree-optimization">쿼드 트리 공간 분할</a><br>
        &nbsp;&nbsp; └ <a href="#fsm-to-bt">FSM → BT 리팩토링</a>
      </td>
      <td valign="top">
        <br>
        <b><a href="#brotato-main">🎮 프로젝트 메인</a></b><br>
        <b><a href="#overview-brotato">📖 게임 개요</a></b><br>
        <b><a href="#goals-brotato">📌 학습 목표 및 달성</a></b><br>
        <b><a href="#features-brotato">🔨 주요 개발</a></b><br>
        <b><a href="#troubleshooting-brotato">🛠️ 문제 해결</a></b><br>
        &nbsp;&nbsp; └ <a href="#direct2d-optimization">Direct2D 전환</a><br>
        &nbsp;&nbsp; └ <a href="#tilemap-optimization">타일맵 렌더링 최적화</a><br>
        &nbsp;&nbsp; └ <a href="#event-queue-system">이벤트 큐 시스템</a>
      </td>
    </tr>
  </tbody>
</table>

<br>
<br>

---

# 🎮 블루아카이브 팬 메이드 OperationKivotos<a name="bluearchive-main"></a>

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/75321802-c496-4e3b-9ab9-5a32846b287f" />

### 📌 프로젝트 정보

| 항목 | 내용 |
|:---:|:---:|
| 🎯 **장르** | 수집형 액션 RPG, 서브컬처 |
| ⏱️ **개발 기간** | 2026.01 ~ 2026.04 (4개월) |
| 👥 **개발 인원** | 1인 (개인 프로젝트) |
| 🛠️ **개발 환경** | Unity, C#, `Addressables`, `UniTask`, `NPOI` |
| 🎬 **시연 영상** | [YouTube 바로가기](https://youtu.be/yPBj7T_f7ds?si=zlXlAo7Us3Utixns) |
| 📝 **개발 블로그** | [Velog 바로가기](https://velog.io/@vfly1189/series/Unity-%EB%B8%94%EB%A3%A8%EC%95%84%EC%B9%B4%EC%9D%B4%EB%B8%8C-%EC%B0%BD%EC%9E%91-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8) |
| 💾 **GitHub** | [소스코드](https://github.com/vfly1189/OperationKivotos) |

## 📑 프로젝트 목차<a name="toc-bluearchive"></a>

**1. 📖 [게임 개요](#overview-bluearchive)**

**2. 📌 [학습 목표 및 달성](#goals-bluearchive)**

**3. 🔨 [주요 개발 기능](#features-bluearchive)** <br>
&nbsp;&nbsp; └ [Sector 기반 플레이어 위치 추적형 존 로딩 시스템](#optimization-bluearchive)<br>
&nbsp;&nbsp; └ [비동기 로딩 및 Addressables 최적화 파이프라인](#async-pipeline-bluearchive)<br>
&nbsp;&nbsp; └ [데이터 주도 설계(Data-Driven) 및 에셋 베이킹 자동화](#data-driven-bluearchive)<br>
&nbsp;&nbsp; └ [다형성과 Timeline을 활용한 객체지향적 몬스터 아키텍처 설계](#behavior-tree-ai)<br>
&nbsp;&nbsp; └ [인터페이스(Interface) 기반 공용 데미지 파이프라인](#combat-bluearchive)<br>
&nbsp;&nbsp; └ [UI 렌더링 최적화 및 이벤트 분리](#ui-optimization-bluearchive)

**4. 🛠️ [문제 해결 (Troubleshooting)](#troubleshooting-bluearchive)** <br>
&nbsp;&nbsp; └ **[기획 변경에 따른 AI·렌더링 연산 병목 해소: Sector 기반 존 로딩 시스템](#optimization-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - `Sector` 기반 시야 컬링과 비동기 생명주기 제어로 해결하여 **안정적인 프레임 방어 성공**

&nbsp;&nbsp; └ **[동기식 하드코딩 탈피 및 UniTask 비동기 파이프라인 구축](#async-unitask-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 씬 전환 시 발생하는 `Task` 스레드풀의 `AssetBundle.Unload` 충돌을 `UniTask` 메인 스레드 동기화로 해결

&nbsp;&nbsp; └ **[대규모 데이터 관리의 한계 극복 및 파이프라인 이원화 (Excel/JSON)](#data-driven-trouble)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - 런타임 엑셀 파싱의 오버헤드를 에디터 타임 `ScriptableObject` 베이킹으로 이전하고 `DataManager`로 통합하여 **데이터 관리 최적화**

<div align="right">
  <a href="#table-of-contents">⬆️ 전체 목차로 돌아가기</a>
</div>


## 📖 게임 개요<a name="overview-bluearchive"></a>

**장르** : 쿼터뷰 액션 RPG

OperationKivotos(가제)는 4명의 캐릭터를 태그하여 전투를 진행하는 액션 RPG입니다. 5,000개 이상의 게임 데이터를 효율적으로 관리하고 런타임 성능을 방어할 수 있는 아키텍처 구축에 집중한 프로젝트입니다.

**🔄 핵심 루프 (Core Loop)**
1. **탐험 & 전투** : 필드를 자유롭게 탐험하며 마주치는 적들을 처치
2. **수집 & 성장** : 획득한 재화로 캐릭터의 스탯을 강화하고 장비를 업그레이드
3. **보스 공략** : 고유의 패턴을 가진 보스를 공략하여 상위 난이도 던전으로 진입

**🎯 개발 초점**
1. **유지보수성** : 유니티 엔진과 C# 언어의 특성을 이해하고 결합도가 낮은 확장성 있는 구조 설계
2. **지속 가능한 퍼포먼스** : 맵의 크기나 유닛 수에 관계없이 안정적인 프레임을 유지할 수 있는 런타임 최적화 구조 연구
3. **워크플로우** : 기획자와 개발자의 업무 분리를 고려한 에디터 자동화 툴 제작

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

## 📌 학습 목표 및 달성<a name="goals-bluearchive"></a>

> **"이전 프로젝트들을 회고하며 느낀 구조적 아쉬움을 개선하고, 확장성 높은 아키텍처를 연구 및 적용"**

과거 프로젝트(이터널 리턴 모작, Brotato 모작)에서 겪었던 로딩 병목, 데이터 하드코딩 등 구조적 문제를 식별하고 이를 객체지향 패턴으로 리팩토링하는 과정을 학습했습니다.

### 1️⃣ 리소스 로드 방식의 현대화 (UniTask)
- **과거의 한계** : 소규모 시연 목적의 개발로 인해 프로그램 시작 시 모든 리소스를 동기식으로 일괄 로딩함. 데이터 규모가 커질 경우 발생하는 초기 로딩 지연과 메모리 점유 문제를 해결할 필요성 인지
- **달성 성과** : `Addressables`와 `UniTask`를 결합하여 필요한 시점에 필요한 에셋만 로드하는 비동기 점진적 로딩 구조 구축.

### 2️⃣ 하드코딩 탈피와 데이터 주도 설계 (JSON & Excel)
- **과거의 한계** : 10~15개 내외의 데이터를 코드 내에 직접 선언하여 관리. 데이터 수정 시마다 재컴파일이 필요하며, 기획 데이터가 늘어날수록 유지보수가 불가능해지는 구조적 취약점 확인
- **달성 성과** : 모든 수치 데이터를 외부 포맷(Excel/JSON)으로 완전히 분리. 특히 무거운 파싱 로직을 에디터 타임으로 이전하는 SO 베이킹 자동화 툴을 개발하여, 코드 수정 없이 데이터만으로 게임의 밸런스를 제어하는 환경 구축

### 3️⃣ 결합도 감소를 통한 연쇄 수정 방지 (Decoupling)
- **과거의 한계** : 객체 간 강한 참조로 인해 기능 하나를 수정하면 수십 개의 파일을 동시에 수정해야 하는 현상 발생. 설계의 부재가 개발 속도를 저해하는 악순환 경험
- **달성 성과** : **인터페이스(Interface)** 와 이벤트(Observer) 패턴을 적극 도입하여 시스템 간 의존성 최소화. 기능을 수정하거나 추가해도 다른 모듈에 영향을 주지 않는 독립적이고 확장성 있는 아키텍처 설계 역량 확보

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

---

<br>

## 🔨 주요 개발<a name="features-bluearchive"></a>

<a name="optimization-bluearchive"></a>
<details open>
<summary><h3>🗺️ Sector 기반 플레이어 위치 추적형 존 로딩 시스템</h3></summary>

<br>

**구현 목적**
- 포탈 없이 연결된 단일 필드 구조로 전환하면서 맵 전체에 배치된 약400마리 몬스터의 AI·렌더링 연산 병목을 구역 단위로 제거하기 위해 도입.

**주요 구현 내용**
- **Trigger 기반 공간 분할(Sector) 아키텍처**
  - 매 프레임 재귀적 갱신 비용이 드는 QuadTree/Octree 대신, 고정 크기의 Trigger Collider로 맵을 논리 구역(`Sector`)으로 분할하는 시스템 구축.
  - 레벨 디자이너가 Inspector에서 구역을 직접 편집 가능한 구조 선택.
  - <img width="436" height="347" alt="스크린샷 2026-04-29 232436" src="https://github.com/user-attachments/assets/b4baaad4-d175-43f6-9a7a-1474a4839919" />

- **플레이어 위치 기반 엔티티 컬링(Entity Culling)**
  - 플레이어 진입 시 `SectorManager`가 현재 Sector의 스포너만 활성화.
  - Unity Frustum Culling이 처리하지 못하는 **오프스크린 AI/Script 연산**을 구역 단위로 차단.
  - Profiler 실측: Script 연산 **▼57%**, Triangles **▼67%**

- **CancellationToken을 활용한 안전한 리스폰 제어**
  - 구역 이탈·씬 전환 시 `CancelAllSpawnTasks()`로 리스폰 대기 중인 `UniTask.Delay`를 즉시 폐기(Dispose).
  - GameObject 파괴 이후 비동기 컨텍스트가 남아 Missing Reference를 유발하는 문제를 토큰 생명주기 관리로 차단.

> **🚀 기술 도입 배경**:
> 기획 변경으로 AI·렌더링 연산 병목과, 공간 분할·비동기 제어로 이를 극복한 과정은
> 하단 **[🛠️ 문제 해결](#optimization-trouble)** 파트에서 상세히 다룹니다.

</details>

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="async-pipeline-bluearchive"></a>
<details open>
<summary><h3>⏳ 비동기 로딩 및 Addressables 최적화 파이프라인</h3></summary>

<br>

**구현 목적**
- `Resources.Load`의 동기 로딩으로 인한 메인 스레드 블로킹을 제거하고, 런타임 중 디스크 I/O 없이 에셋을 즉시 반환하는 캐시 기반 비동기 파이프라인 구축

**주요 구현 내용**
- **글로벌(Global) 에셋 영구 캐싱 및 종속성 분리**
  - 전역으로 사용되는 UI, 사운드 에셋(`Label: Global`)과 씬 종속적인 데이터(맵, 몬스터)를 별도의 번들로 분리하여 **메모리 중복 로드 차단**
  - 글로벌 에셋은 `LoadDependenciesAsync`(커스텀 프리로드 함수)를 통해 일괄 로드 후 `globalHandles`에 영구 캐싱하여 잦은 로드/언로드 오버헤드 방지
  - <img width="716" height="357" alt="image" src="https://github.com/user-attachments/assets/c83e3e54-fe5a-4df8-8ad1-5a14ebd339b5" />

- **동적 리소스 요청 및 $O(1)$ 캐시 히트(Cache Hit)**
  - 씬 진입 전 필요한 프리팹을 `sceneHandles` 딕셔너리에 비동기로 미리 로드
  - 런타임 에셋 요청 시 `globalHandles` ➔ `sceneHandles` 순으로 캐시를 탐색하여 **인게임 런타임 중 디스크 I/O 병목 제거**
  - 씬 이탈 시 sceneHandles만 선택적으로 해제.

> **🚀 기술 도입 배경**: 문자열 하드코딩, 인스펙터 직접 참조, `Task` 사용 과정에서 발생한 언로드 타이밍 문제와 이를 `UniTask`로 마이그레이션한 과정은 하단 **[🛠️ 문제 해결](#async-unitask-trouble)** 파트에서 다룹니다.

</details>

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="data-driven-bluearchive"></a>
<details open>
<summary><h3>📊 데이터 주도 설계(Data-Driven) 및 에셋 베이킹 자동화</h3></summary>

<br>

**구현 목적**
- **런타임 성능(조회 속도)** 과 **기획자의 작업 편의성(수식 연산)** 이라는 두 마리 토끼를 잡기 위해 데이터 포맷을 Excel과 JSON으로 이원화하고, 로딩 오버헤드를 에디터 타임으로 이전

**주요 구현 내용**
- **대규모 수치 데이터 베이킹 자동화 (Excel ➔ ScriptableObject)**
  - 캐릭터 스탯, 성장치 등 수식 연산이 필수적인 데이터는 기획 친화적인 **Excel**로 관리
  - 런타임 엑셀 파싱 시 발생하는 GC 할당을 막기 위해, 빌드 전 NPOI를 활용해 엑셀 데이터를 가벼운 **`ScriptableObject` 에셋으로 자동 변환(Baking)** 하는 에디터 툴 구축
  - <img width="380" height="147" alt="스크린샷 2026-04-29 232518" src="https://github.com/user-attachments/assets/4e9c2464-d570-4eca-b778-7d5929bdb959" />
  
- **계층적 구조 데이터 관리 (JSON)**
  - 구역별 스포너 위치 등 다단계 깊이(Depth)를 가지는 데이터는 Excel의 2차원 표로 관리하기 부적합하여 **JSON** 포맷 채택

- **DataManager를 통한 $O(1)$ 통합 조회 시스템**
  - 베이킹된 SO 에셋과 JSON 데이터를 `DataManager`가 메모리에 일괄 로드하여 캐싱
  - 인게임 로직에서는 원본 파일 형식에 구애받지 않고 **ID(Key) 기반 $O(1)$ 속도로 데이터를 즉시 조회**

> **🚀 기술 도입 배경**: 
> 단순 하드코딩 ➔ 개별 SO ➔ 전체 JSON ➔ Excel/JSON 하이브리드로 파이프라인이 진화하게 된 성능 병목과 최적화 과정은 하단 **[🛠️ 문제 해결](#data-driven-trouble)** 파트에서 다룹니다.

</details>

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="behavior-tree-ai"></a>
<details open>
<summary><h3>🧱 다형성과 Timeline을 활용한 객체지향적 몬스터 아키텍처 설계</h3></summary>

<br>

**구현 목적**
- 몬스터 타입이 추가될 때마다 컨트롤러에 `if-else`가 누적되는 **God Class 안티패턴 방지**
- 공통 로직은 재사용하고 고유 패턴만 하위 클래스로 위임하는 **OCP(개방-폐쇄 원칙)** 기반 아키텍처 구축

**주요 구현 내용**
- **다형성을 활용한 계층형 상속 구조 (`Base ➔ Ranged ➔ Concrete`)**
  - 공통 생명주기(스탯, HP, 사망)는 `BaseMonsterController`로 통합하여 중복 제거
  - 실제 공격 패턴은 **가상 메서드(`GetCombatNode`)**로 열어두어, `MonsterAR`, `MonsterRL` 등 하위 클래스가 각자 무기 특성에 맞는 로직을 반환하도록 위임
  
- **의사 결정(Logic)과 시각적 연출(Timeline)의 Signal 기반 동기화**
  - 복잡한 이펙트가 동반되는 보스 스킬을 코드로 하드코딩하는 비효율을 제거하기 위해, **상태 판단(Logic)은 컨트롤러가, 복합 연출(View)은 Unity `Timeline`이 전담**
  - 컨트롤러가 Timeline을 `Play`하고 대기하면, 연출 도중 **지정된 프레임에 `Signal`을 방출하여 실제 데미지/소환 로직(`UniTask`)을 비동기로 동기화**하는 데이터 주도적 보스 패턴 완성

- **AI 상태 판단의 캡슐화 (Behavior Tree)**
  - 거대한 `Update()` 스파게티 코드를 막기 위해 최상위 상태 판단(생존 ➔ 전투 ➔ 추적 ➔ 대기)을 `Selector`와 `Sequence` 기반의 트리 구조로 캡슐화

**관련 이미지**

<div align="center">

**1️⃣ 계층형 몬스터 상속 구조**<br>
<img width="800" alt="Monster Hierarchy" src="https://github.com/user-attachments/assets/e3fb2002-7de2-4ea3-abf4-e7c5f3f3c88e" />
<p><em>공통 로직 통합과 확장성을 고려한 상속 설계</em></p>

<br>

**2️⃣ 일반 몬스터 다형성 위임 구조**<br>
<img width="800" alt="Normal Monster BT" src="https://github.com/user-attachments/assets/f2b7462a-3b70-41e6-8ae1-02a64be4e9c0" />
<p><em>전투 로직을 하위 클래스에서 각자 구현하도록 위임 (붉은 박스)</em></p>

<br>

**3️⃣ 보스 몬스터 Timeline 연동 구조**<br>
<img width="800" alt="Boss Monster Flow" src="https://github.com/user-attachments/assets/1c9e12da-b91b-43bc-9451-ca1f14f1b670" />
<p><em>스킬 판단(Logic)과 스킬 연출(Timeline)을 분리한 보스 패턴</em></p>

</div>

</details>

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="combat-bluearchive"></a>
<details open>
<summary><h3>⚔️ 인터페이스(Interface) 기반 공용 데미지 파이프라인</h3></summary>

<br>

**구현 목적**
- 공격자와 피격자 간의 강한 결합을 끊고, 객체 타입(플레이어, 몬스터, 오브젝트)에 구애받지 않는 범용적인 데미지 교환 아키텍처 구축

**주요 구현 내용**
- **인터페이스(`IDamageable`) 기반의 결합도 분리**
  - 피격 가능한 모든 객체는 `IDamageable`을 구현하여 `TakeDamage` 메서드를 각자의 방식대로 구현
  - 투사체나 포격 로직은 충돌 대상이 `IDamageable` 타입인지 캐스팅(`TryGetComponent`)만 검사하여 데미지를 전달하도록 분리하여 하드코딩된 분기문(`if/else`, Tag 검사) 제거

- **`DamageInfo` 구조체를 통한 데이터 캡슐화**
  - 단순 수치뿐만 아니라 공격자 참조, 크리티컬 여부 등을 담은 `DamageInfo` 구조체 설계
  - 향후 데미지 연산 공식이 복잡해져도 파이프라인 수정 없이 데이터 형태만 확장할 수 있는 유연성 확보

**관련 이미지**
| **최적화 전 (Before)** | **최적화 후 (After)** |
| :---: | :---: |
| <img width="500" alt="Before Damage Pipeline" src="https://github.com/user-attachments/assets/71f34b3e-68c2-4b0b-9548-6cd37ae39516" /> | <img width="500" alt="After Damage Pipeline" src="https://github.com/user-attachments/assets/2f6d21f4-1cba-49fd-a4fa-0b19adf47896" /> |
| *타입/태그별로 얽힌 하드코딩 피격 분기문* | *`IDamageable` 인터페이스로 일원화된 데미지 파이프라인* |

</details>

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="ui-optimization-bluearchive"></a>
<details open>
<summary><h3>🖥️ UI 렌더링 최적화 및 이벤트 분리</h3></summary>

<br>

**구현 목적**
- 매 프레임 UI를 강제 갱신하며 발생하는 CPU 오버헤드와 **Canvas 전체 Rebuild로 인한 Draw Call 문제** 해결

**주요 구현 내용**
- **옵저버(Observer) 패턴 기반 데이터-UI 분리**
  - C# `Action/Delegate`를 활용하여 체력 변화, 아이템 획득 등 **데이터 변동이 발생한 순간에만 이벤트를 브로드캐스트**
  - UI는 이벤트 수신 시에만 화면을 갱신하도록 설계하여 불필요한 `Update()` 연산 제거

- **목적별 Canvas 분할 최적화**
  - 모든 요소를 단일 캔버스에 넣지 않고, 갱신 빈도에 따라 **4개의 Canvas**(`Scene`, `System`, `World`, `Popup`)로 격리
  - 체력바나 팝업 데미지(`World`)가 매 프레임 위치를 갱신하며 캔버스를 더럽히더라도, 정적인 기본 UI(`Scene`)는 **Rebuild 대상에서 제외되어 렌더링 부하 최소화 및 Draw Call 절약**
  <img width="478" height="428" alt="image" src="https://github.com/user-attachments/assets/4aeb505b-1aa2-4777-b176-2b99db994853" />

</details>

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>


---

<br>

## 🛠️ 문제 해결<a name="troubleshooting-bluearchive"></a>

### 1️⃣ 기획 변경에 따른 AI·렌더링 연산 병목 해소: Sector 기반 존 로딩 시스템<a name="optimization-trouble"></a>

> **🚨 문제 상황: 단일 필드 전환 후 전체 맵 스포너의 AI/렌더링 연산 병목**
>
> - **기획 전환 결정**: 제한된 필드 구역에서 포탈(일반/보스)을 통해 인스턴스 던전에 진입하는 기존 구조는 탐험 몰입감이 떨어진다고 판단.
> - 포탈 없이 필드를 직접 탐험하는 단일 연결 구조로 전환하고, 맵 전체에 약 400마리 규모의 몬스터 배치.
> - **연산 병목 발생**: 시야 밖 구역의 MonsterSpawner까지 AI Behavior Tree 틱과 렌더링 연산을 매 프레임 소모하면서 유의미한 오버헤드 발생.

**💡 해결 과정**

1. **왜 QuadTree가 아닌 Trigger 기반 Sector 분할인가?**
   - 몬스터 밀집도가 극단적으로 높지 않은 레벨 디자인 특성상, 트리 자료구조를 매 프레임 재귀 갱신하는 QuadTree/Octree 방식은 구조 유지 비용이 오히려 오버헤드가 될 수 있다고 판단.
   - 고정 크기의 Trigger Collider로 공간을 분할하는 `Sector` 시스템으로 설계.
   - 구역 크기·위치를 Inspector에서 조정 가능.
     
<!-- Sector 구역 분할 Gizmo 이미지 -->
<div align="center">
<img width="600" alt="Sector" src="https://github.com/user-attachments/assets/5e1ca242-1aca-4d77-8550-39abaee0dedc" /> 
</div>

2. **플레이어 위치 기반 엔티티 컬링 구현**
   - 플레이어가 구역 진입(`OnTriggerEnter`) 시 `SectorManager`가 해당 Sector의 스포너만 활성화.
   - 이전 구역은 스폰 즉시 중단하고 오브젝트를 풀로 반환하여 AI 틱 연산 자체를 제거.
   - Unity Frustum Culling은 렌더링만 생략할 뿐 Script·Physics 연산은 그대로 실행됨을 Profiler로 확인. Sector 시스템은 이를 엔티티 단위로 보완하는 역할.

3. **UniTask + CancellationToken 기반 안전한 비동기 리스폰 제어**
   - 리스폰 대기 구현 시, GameObject 파괴 시 강제 종료되어 예외 처리가 까다로운 `Coroutine` 대신 생명주기 제어가 명확한 `UniTask` 채택.
   - 구역 이탈로 스포너가 비활성화될 때 `CancelAllSpawnTasks()`로 `CancellationToken`을 즉시 폐기.
   - 파괴된 GameObject를 참조하는 비동기 컨텍스트가 남지 않도록 설계하여 Missing Reference 차단.

**✅ 결과 (Unity Profiler 실측)**

| 항목 | 전체 Sector 활성 | 단일 Sector 활성 | 절감률 |
|---|---|---|---|
| Script 연산 | 1.793ms | 0.763ms | **▼ 57%** |
| Triangles | 1.75M | 575k | **▼ 67%** |

<img width="1274" alt="Sector" src="https://github.com/user-attachments/assets/e129309e-227d-42e3-ab9c-b85a5e048980" />

> 374마리 배치 기준 측정. 활성 구역이 전체의 약 1/5임을 감안하면,
> **몬스터 밀도가 증가할수록 절감 효과가 선형적으로 확대되는 확장 가능한 구조.**

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>


### 2️⃣ 동기식 하드코딩 탈피 및 UniTask 비동기 파이프라인 구축<a name="async-unitask-trouble"></a>

> **🚨 문제 상황: C# Task의 구조적 한계와 씬 라이프사이클 충돌**
>
> - 초기 구현 시 비동기 에셋 로딩을 위해 C# 기본 `Task(async/await)` 활용.
> - 씬 전환 시 `AssetBundle.Unload could not complete...` 에러가 간헐적으로 발생하며
>   씬 이동이 멈추는 현상 발생.
> - **원인 분석**:
>   1. **Unity 라이프사이클과의 분리**: C# `Task`는 Unity 메인 스레드의 생명주기와 무관하게 동작
>   2. **비동기 타이밍 충돌 (레이스 컨디션)**: Load 완료 전 씬 전환이 시작되면 다음 씬의 `Unload`가 먼저 호출되어 에셋 번들 해제 타이밍 충돌 발생
>   3. **제어 불가**: 씬 전환 중 이전 씬의 비동기 작업을 중단할 수단이 없어, 파괴된 객체를 참조하는 예외로 이어짐
>
> <img width="283" height="54" alt="image" src="https://github.com/user-attachments/assets/7b1883f7-c131-4f8a-be43-c33d2a0f434e" />

**💡 해결 과정**

1. **왜 Task 대신 UniTask인가?**
   - `UniTask`는 Unity 메인 스레드(`PlayerLoop`) 기반으로 동작하여 `Unload` 호출 순서가 PlayerLoop 안에서 보장됨 → 레이스 컨디션 해소
   - `destroyCancellationToken`으로 오브젝트 파괴 시 진행 중인 비동기 작업을 자동 중단하여 파괴된 객체 참조 예외 원천 차단

2. **왜 코루틴 대신 UniTask인가?**
   - **반환값 문제**: 코루틴(`IEnumerator`)은 결과를 직접 반환할 수 없어, 에셋 핸들을 `globalHandles` / `sceneHandles`에 저장하는 현재 구조에서 멤버 변수 우회가 강제됨.
   - `UniTask<T>`는 로드 결과를 `await` 한 줄로 받아 딕셔너리에 직접 캐싱 가능
   - **병렬 처리**: 씬 진입 전 다수 에셋을 동시에 프리로드해야 하는 파이프라인에서 코루틴은 `WhenAll`을 직접 구현해야 하나, `UniTask.WhenAll()`로 병렬 로드와 완료 대기를 간결하게 처리하여 총 로딩 시간 단축

**✅ 결과**
- **레이스 컨디션 제거**: PlayerLoop 기반 UniTask로 씬 전환과 리소스 로드/해제 타이밍 보장
- **안전한 생명주기 제어**: `destroyCancellationToken`으로 파괴된 객체 참조 예외 원천 차단
- **효율적인 병렬 로딩**: `UniTask.WhenAll()`로 다수 에셋 동시 로드, 씬 진입 로딩 시간 단축

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

### 3️⃣ 대규모 데이터 관리의 한계 극복 및 파이프라인 이원화 (Excel/JSON)<a name="data-driven-trouble"></a>

> **🚨 배경 및 문제 상황**
>
> - 데이터가 늘어날수록 ScriptableObject(SO)를 인스펙터에 수동 할당하는 방식은 참조 누락 에러를 유발. 이를 피해 모든 데이터를 JSON으로 분리.
> - 그러나 '레벨별 스탯 성장치'나 '드랍 테이블' 등 기획자의 수식 연산과 밸런싱이 필수적인 데이터까지 JSON으로 수기 작성하는 것은 생산성 저하 유발.

**💡 해결 과정**

1. **왜 데이터 포맷을 이원화(Excel/JSON) 했는가?**
- 기획 편의성을 위해 모든 것을 Excel로 통합할 수도 있었으나, 구역별 스포너(배열 안에 배열이 있는 형태) 정보처럼 **계층적 깊이(Depth)가 깊은 데이터는 2차원 표 형태인 엑셀로 표현하기가 더 비효율적임**을 인지.
- 따라서 수식 연산과 교차 참조가 필요한 스탯/아이템은 **Excel**로, 계층적 구조화가 필요한 스포너 등은 **JSON** 포맷으로 유지하는 **데이터 특성 기반 이원화 전략** 채택.

2. **왜 런타임에 파싱하지 않고 Editor Time에 SO로 굽는가(Baking)?**
- 초기에는 NPOI 라이브러리를 활용해 런타임에 엑셀을 직접 파싱했으나, 방대한 셀을 순회하며 발생하는 막대한 GC 할당과 렉(Spike) 확인.
- 이를 해결하기 위해 무거운 파싱 로직을 런타임에서 에디터 타임으로 이전. 기획자가 Excel을 수정하면 클릭 한 번으로 모든 시트를 파싱하여 가벼운 **`ScriptableObject` 에셋으로 자동 변환(Baking)하는 커스텀 에디터 툴** 개발.
- | **약 5,600개 데이터 베이킹 후 캐싱** | **약 10,600개 데이터 베이킹 후 캐싱 (스트레스 테스트)** |
  | :---: | :---: |
  | <img width="600" height="260" alt="image" src="https://github.com/user-attachments/assets/456c463b-8de5-4106-825d-a78f3b0aaf19" /> | <img width="600" height="260" alt="image" src="https://github.com/user-attachments/assets/aac554af-1480-4cd6-9724-ff32afa6b318"/> |

3. **DataManager 통합 및 $O(1)$ 캐싱**
- 베이킹된 SO 에셋과 JSON 데이터들을 게임 초기화 시점에 `DataManager`가 일괄 로드하여 ID(Key) 기반 딕셔너리로 캐싱. 배열 순회 없이 $O(1)$ 속도로 데이터 조회 지원.

**✅ 결과**
- "기획자는 수식 기반의 엑셀로 편하게 밸런싱하고, 클라이언트는 가볍게 구워진 SO로 빠르게 읽어 들이는" **실무형 데이터 주도 설계(Data-Driven) 파이프라인** 구축 완료.

<div align="right">
  <a href="#toc-bluearchive">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

---

<br>

# 🎮 이터널 리턴 모작<a name="eternal-return-main"></a>

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ee737290-1c9e-47af-95b2-b62d47e51f0c" />

### 📌 프로젝트 정보

| 항목 | 내용 |
|:---:|:---:|
| 🎯 **장르** | 쿼터뷰, 배틀로얄, MOBA |
| ⏱️ **개발 기간** | 2025.07 ~ 2025.09 (2개월) |
| 👥 **개발 인원** | 2인 (프로그래머로 참여) |
| 🛠️ **개발 환경** | C++, DirectX11, HLSL |
| 🎬 **시연 영상** | [YouTube 바로가기](https://youtu.be/b6XVkd0xc-E?si=XHB1nkE6C2-JarC8) |
| 📝 **개발 블로그** | [상세 개발 과정](https://tobrother.tistory.com/category/DirectX11/Eternal%20Return%20%EB%AA%A8%EC%9E%91) |
| 💾 **GitHub** | [소스코드](https://github.com/HyangRim/DirectX11-Engine-Client) |

## 📑 프로젝트 목차<a name="toc-eternal"></a>

**1. 📖 [게임 개요](#overview-eternal)**

**2. 📌 [학습 목표 및 달성](#goals-eternal)**

**3. 🔨 [주요 개발 기능](#features-eternal)** <br>
&nbsp;&nbsp; └ [Deferred Rendering (Hybrid)](#deferred-rendering)<br>
&nbsp;&nbsp; └ [GPU Instancing](#gpu-instancing)<br>
&nbsp;&nbsp; └ [Quad Tree 공간 분할](#quad-tree)<br>
&nbsp;&nbsp; └ [NavMesh 길찾기](#navmesh)<br>
&nbsp;&nbsp; └ [몬스터 AI 시스템](#fsm-to-bt-feature)

**4. 🛠️ [문제 해결 (Troubleshooting)](#troubleshooting-eternal-return)** <br>
&nbsp;&nbsp; └ **[Forward → Deferred 전환](#deferred-rendering-trouble)**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  다중 광원 처리와 반투명 객체를 혼합한 **Hybrid 파이프라인 구축**

&nbsp;&nbsp; └ **[NavMesh 검색 최적화](#navmesh-optimization)**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Spatial Grid 도입으로 탐색 속도 **21.5배 가속 (301μs → 14μs)**

&nbsp;&nbsp; └ **[Quad Tree 충돌 최적화](#quadtree-optimization)**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  불필요한 연산을 제거하여 충돌 처리 **135.8배 최적화 (53ms → 0.3ms)**

&nbsp;&nbsp; └ **[AI 구조 개선 (FSM → BT)](#fsm-to-bt)**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Behavior Tree 도입으로 **복잡한 AI 로직의 유지보수성 확보**

<div align="right">
  <a href="#table-of-contents">⬆️ 전체 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

## 📖 게임 개요<a name="overview-eternal"></a>

**장르**: 쿼터뷰 배틀로얄 / MOBA (Multiplayer Online Battle Arena)

이터널 리턴은 전략적인 쿼터뷰 시점의 생존 게임입니다. 플레이어는 루미아 섬에서 재료 파밍하고 장비를 제작하여 캐릭터를 성장시키며, 최후의 1인이 될 때까지 생존해야 합니다.

**🔄 핵심 루프 (Core Loop)**
1. **파밍 및 제작**: 맵 곳곳의 재료 수집
2. **장비 강화**: 상위 등급 장비 제작으로 전투력 상승
3. **생존 경쟁**: 금지 구역 회피 및 다른 생존자와의 전투
4. **승리**: 최후의 1인 생존

**🎯 개발 초점**
- DirectX 11을 이용한 **3D 렌더링 파이프라인 구축**
- **엔진 레벨의 성능 최적화** 및 아키텍처 설계

<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

## 📌 학습 목표 및 달성<a name="goals-eternal"></a>

> **"게임 엔진 레벨의 고급 렌더링 최적화 기법 습득"**

이 프로젝트의 핵심 목표는 상용 엔진 없이 DirectX 11 API로 3D 게임 엔진을 직접 구현하며, 대규모 리소스를 효율적으로 처리하는 최적화 기술을 체화하는 것이었습니다.

### 1️⃣ 고급 렌더링 파이프라인 구축
- **Deferred Rendering 도입**: 다수의 동적 광원(Point Light 등) 처리를 위해 Forward 방식 대신 Deferred 방식을 적용하여 연산 효율성 확보
- **G-Buffer 및 MRT 활용**: Albedo, Normal, Position 등 지오메트리 정보를 MRT(Multi Render Target)에 저장하여 라이팅 연산 최적화

### 2️⃣ 대규모 오브젝트 처리 최적화
- **GPU Instancing**: 동일한 메시를 사용하는 수천 개의 오브젝트(풀, 나무 등) 렌더링 시 발생하는 DrawCall 병목 현상 해결 (DrawCall 90% 이상 감소)
- **Quad Tree 공간 분할**: 절두체 선별(Frustum Culling) 및 충돌 검사 비용을 획기적으로 줄이기 위해 공간 분할 알고리즘 적용

### 3️⃣ 3D 게임 엔진 기술 심화
- **NavMesh 길찾기**: 복잡한 지형에서의 NPC 이동을 위한 네비게이션 메쉬 및 경로 탐색 알고리즘 구현
- **GPU Skinning**: 캐릭터 애니메이션 연산을 CPU에서 GPU(Compute Shader)로 이관하여 퍼포먼스 향상
<br>

<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<br>

---

<br>

## 🔨 주요 개발<a name="features-eternal"></a>

<a name="deferred-rendering"></a>
<details open>
<summary><h3>🎨 Deferred Rendering 파이프라인 (Hybrid)</h3></summary>

<br>

**렌더링 파이프라인 구조**
- **Hybrid 구조 설계**: 불투명 객체(Deferred)와 투명 객체(Forward)를 분리하여 처리하는 혼합 파이프라인 구축
- **MRT(Multiple Render Targets)**: 4개의 G-Buffer(Albedo, Normal, Position, Material)에 지오메트리 정보를 동시 출력하도록 셰이더 및 RTV 설정
- **Lighting Pass**: G-Buffer 텍스처를 입력받아 화면 전체에 조명 연산 수행
- | **Deferred Render** | **Hybrid ( Forward + Deferred )** |
  | :---: | :---: |
  | <img width="681" height="381" alt="image" src="https://github.com/user-attachments/assets/9baddec0-184e-4fd2-b54c-27656f34afc3" /> | <img width="681" height="381" alt="image" src="https://github.com/user-attachments/assets/6dfe8d4e-7d5f-412d-902d-9b43237c1937"/> |

**G-Buffer 구성 (MRT)**
- G-Buffer 4개 구성 (Albedo, Normal, Position, Material)
- 멀티 렌더 타겟(MRT)을 활용한 지오메트리 정보 저장
- 풀스크린 쿼드를 통한 라이팅 패스 구현
- | **Albedo** | **Normal** |
  | :---: | :---: |
  | <img width="681" height="381" alt="G-Buffer(Albedo)" src="https://github.com/user-attachments/assets/b55b1742-6d50-49e5-af1f-00e7d8823fde" /> | <img width="681" height="381" alt="G-Buffer(Normal)"     src="https://github.com/user-attachments/assets/eef9bef2-0883-4869-951a-a93c071c2a4c" />|
  | **Position (World Space)** | **Material** |
  | <img width="681" height="381" alt="G-Buffer(Position)" src="https://github.com/user-attachments/assets/7a3b3ab6-ab94-4b35-ac57-51d08b5a7f8a" /> | <img width="681" height="381" alt="G-Buffer(Material)" src="https://github.com/user-attachments/assets/1b91a1e8-e6ca-4836-aa60-b2fbcb2cfcd8" /> |

**렌더링 파이프라인 구조**
- Geometry Pass (Deferred): 불투명 객체의 지오메트리 정보를 G-Buffer에 저장 [[📄G-Buffer 셰이더]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Shaders/00.%20GBuffer.fx)
- Lighting Pass (Deferred): G-Buffer 데이터를 기반으로 조명 계산  [[📄Lighting 셰이더]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Shaders/00.%20DeferredLighting.fx#L121-L169)
- Forward Pass (Transparent/UI): 투명/반투명 객체(알파 블렌딩, UI 등)를 Forward로 렌더링하여 최종 합성 [[📄UI 객체 셰이더]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Shaders/ImageShader.fx)

> **🚀 기술 도입 배경**: 다중 광원 처리를 위한 포워드 렌더링의 한계와 해결 과정은 하단 **[🛠️ 문제 해결](#deferred-rendering-trouble)** 파트에서 다룹니다.

</details>

<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="gpu-instancing"></a>
<details open>
<summary><h3>🧬 인스턴싱 기반 렌더링 (GPU Instancing)</h3></summary>

<br>

**구현 배경 및 목표**
- 넓은 필드에 배치된 수천 개의 나무, 풀, 환경 오브젝트로 인한 **DrawCall 병목 현상(CPU Overhead) 해결**
- 개별 DrawCall 발생을 억제하고, 동일한 메쉬를 사용하는 객체들을 한 번의 API 호출로 처리

**🛠️ 기술적 구현**
- **인스턴스 버퍼(Instance Buffer)**: `World Matrix` 및 색상 정보를 담은 버퍼를 별도로 생성하여 VS(Vertex Shader)에 전달
- **배칭(Batching) 시스템**: 매 프레임 렌더링 큐에 등록된 객체 중, 동일한 키(Mesh + Material)를 가진 객체를 자동으로 묶어서 처리
- **다양한 렌더러 지원**: 정적 메쉬뿐만 아니라 애니메이션이 포함된 객체도 인스턴싱 지원
  - [[📄MeshRenderer (정적 객체)]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L311-L348)
  - [[📄AnimRenderer (애니메이션 객체)]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L388-L435)

**📊 최적화 로직 비교**
| 구분 | 기존 방식 (Individual) | 개선 방식 (Instancing) | 효과 |
| :---: | :---: | :---: | :---: |
| **API 호출** | 객체 수(N)만큼 호출 | **1회 호출** (Batch 단위) | **CPU 오버헤드 최소화** |
| **데이터 전달** | 매번 상수 버퍼(CB) 갱신 | **인스턴스 버퍼**로 일괄 전달 | **버스 대역폭 효율화** |
| **확장성** | 오브젝트 증가 시 성능 급락 | 수천 개가 늘어도 **비용 일정** | **대규모 씬 처리 가능** |

</details>

<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="quad-tree"></a>
<details open>
<summary><h3>🧱 쿼드 트리 (공간 분할 자료구조)</h3></summary>

<br>

**자료구조 설계**
- **재귀적 노드 시스템**: `QuadTreeNode` 클래스가 4개의 자식 노드 포인터와 자신의 영역(BoundingBox) 정보를 가지는 트리 구조
- **동적 객체 관리**: 오브젝트의 위치가 변경될 때마다 트리의 노드를 갱신(Update)하거나 재삽입(Re-insert)하는 로직 구현

**핵심 기능**
- **공간 쿼리(Spatial Query)**: 특정 영역(절두체, 마우스 피킹 Ray)과 겹치는 노드만 빠르게 선별하는 인터페이스 제공
- **충돌 그룹 관리**: 노드 단위로 객체 리스트를 관리하여 인접한 객체끼리만 상호작용하도록 설계

**관련 이미지**
| **마우스 Picking 최적화** | **충돌 처리 최적화 (Collision)** |
| :---: | :---: |
| <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/7accc4dd-0591-4851-ad2a-5f9eeac8a0ad" /> | <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/63a9e9e8-4f4f-4292-bba7-6cd7235e22f3" /> |
| Ray와 교차하는 노드(Leaf Node)만 선별하여 정밀 검사 | 빨간색 영역의 객체는 초록색 영역에서만 검사 |

**관련 코드**
- [[📄QuadTree.h (헤더 설계)]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Engine/QuadTree.h)
- [[📄Node Insert (객체 삽입 로직)]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L218-L257)

> **🚀 성능 최적화 사례**: 쿼드트리를 활용한 획기적인 충돌 처리 성능 개선(135배) 결과는 하단 **[🛠️ 문제 해결](#quadtree-optimization)** 파트에서 상세히 다룹니다.

</details>

<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="navmesh"></a>
<details open>
<summary><h3>🧭 NavMesh 길찾기 시스템</h3></summary>

<br>

**시스템 아키텍처**
- **NavMesh 데이터**: 맵 데이터를 삼각형(Triangle) 그래프 형태로 변환하여 이동 가능 영역 정의
- **경로 탐색(Pathfinding)**: 시작점과 도착점이 포함된 삼각형을 찾고, A* 알고리즘으로 연결된 삼각형들의 최단 경로 리스트 산출

**보정 알고리즘**
- **String Pulling**: 삼각형 중심을 잇는 지그재그 경로를 `Line-of-Sight` 검사를 통해 최단 직선 경로로 변환 [[📄경로 스무딩]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/NavMesh.cpp#L307-L360)
- **Agent FSM**: AI 캐릭터의 이동 상태(Idle, Move)를 관리하고 NavMesh 위로 위치를 투영(Projection)하는 에이전트 클래스 구현

**관련 이미지**
| **NavMesh 스무딩 (Before)** | **NavMesh 스무딩 (After)** |
| :---: | :---: |
| ![NavMesh-스무딩x](https://github.com/user-attachments/assets/b9f093b3-bff1-434e-b170-fdee9c4e83df) | ![NavMesh-스무딩o](https://github.com/user-attachments/assets/456e6486-6547-4893-80c6-bba4817ac855) |

> **🚀 검색 속도 최적화**: 대규모 맵에서의 경로 탐색 병목을 해결한 'Spatial Grid' 기법은 하단 **[🛠️ 문제 해결](#navmesh-optimization)** 파트에서 상세히 다룹니다.

</details>

<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="fsm-to-bt-feature"></a>
<details open>
<summary><h3>🤖 몬스터 AI 시스템 (Behavior Tree)</h3></summary>

<br>

**시스템 개요**
- **Behavior Tree (BT) 아키텍처**: 몬스터의 행동을 계층적 트리 구조로 설계하여 복잡한 의사결정 로직을 체계화
- **노드 구성**:
    - **Composite**: `Selector`(우선순위 선택), `Sequence`(순차 실행)
    - **Decorator**: 조건 검사 (`CheckHP`, `CheckRange` 등)
    - **Leaf**: 실제 행동 수행 (`Move`, `Attack`, `Die` 등)

**AI 행동 패턴 (우선순위)**
- **Selector 노드**를 통해 왼쪽부터 실행 가능성을 판단하여 가장 높은 우선순위 행동을 수행하도록 설계
1.  **생존 본능 (최우선)**: HP가 0 이하일 경우 즉시 `Die` 상태로 전이
2.  **전투 (Combat)**: 공격 사거리 내에 타겟이 있으면 `Attack` 수행
3.  **추적 (Trace)**: 타겟이 감지 범위 내에 있으면 NavMesh 경로를 따라 이동
4.  **대기 (Idle)**: 위 조건이 모두 해당하지 않을 경우 대기 상태 유지

**관련 이미지**
| **AI 행동 트리 구조 (시각화)** | **인게임 AI 동작 (추적 → 공격 → 사망)** |
| :---: | :---: |
| <img width="500" height="300" alt="bt-structure" src="https://github.com/user-attachments/assets/b9cb3150-afb2-494a-b3ef-224d4cb2fd75" /> | ![늑대 모션들](https://github.com/user-attachments/assets/ffdf45cc-240b-4467-abb6-840257999799) |

**관련 코드**
- [[📄BehaviorTree.h (트리 노드 설계)]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Engine/BehaviorTree.h)
- [[📄WolfAI.cpp (몬스터 트리 구성)]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/5d9aa0d9b421b32bf8004703d286ba5dbfd8bac5/Client/Wolf.cpp#L281-L319)

> **🚀 아키텍처 개선 사례**: 기존 FSM 구조의 한계(유지보수성 저하)를 극복하기 위해 Behavior Tree로 전환한 과정과 기술적 의사결정 내용은 하단 **[🛠️ 문제 해결](#fsm-to-bt)** 파트에서 상세히 다룹니다.

</details>

<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

---

<br>

## 🛠️ 문제 해결<a name="troubleshooting-eternal-return"></a>

### 1️⃣ Forward에서 Deferred Rendering으로 전환 (Hybrid)<a name="deferred-rendering-trouble"></a>

> **🚨 문제 상황: Forward Rendering의 구조적 한계**
> 
> **성능 병목** : 다수의 동적 광원(Skill Effects, Lights)이 배치되자 $O(\text{객체 수} \times \text{광원 수})$의 연산량으로 인해 프레임이 급격히 저하됨
> 
> **픽셀 오버드로우** : 화면에 보이지 않는 픽셀까지 불필요하게 셰이딩 연산을 수행하여 GPU 자원을 낭비함

**💡 해결 과정**

1.  **Deferred Rendering (지연 렌더링) 구현**
    *   **G-Buffer (MRT) 구축** : 4개의 Render Target에 물체의 정보를 동시에 기록하도록 셰이더 및 RTV 설정
        *   `Albedo`(색상), `Normal`(법선), `Position`(좌표), `Material`(재질)
        *   | **G-Buffer 실시간 구성 (MRT Debug View)** | 
            | :---: |
            | ![디퍼드렌더링](https://github.com/user-attachments/assets/f576aec2-0b4f-43db-8a5a-bc6250ff3a01) |
    *   **Lighting Pass** : G-Buffer 데이터를 샘플링하여 화면 전체(Screen Space)에 조명 연산 수행. 연산량을 **$O(\text{화면 해상도} \times \text{광원 수})$** 로 고정하여 객체 수 증가에 따른 성능 저하 방지

2.  **Hybrid Rendering으로 파이프라인 완성**
    *   **문제** : Deferred 방식의 구조적 한계로 인해 투명/반투명 객체(Alpha Blending) 처리가 불가능
    *   **해결 (Hybrid)** : 렌더링 파이프라인을 이원화하여 각 패스의 장점 결합
        *   **불투명 객체 (Opaque)** : Deferred Pass로 처리하여 다중 광원 연산 최적화
        *   **반투명/UI 객체 (Transparent)** : Lighting Pass 이후 Forward Pass로 렌더링하여 알파 블렌딩 정상 처리
    * | **Deferred Only (반투명/UI 미적용)** | **Hybrid (Deferred + Forward)** |
      | :---: | :---: |
      | <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/532b1300-8d61-492d-895f-298bf2efb7bd" /> | <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/4d721451-2f37-4160-bb71-78030de7103c" /> |

**✅ 결과**
*   **다중 광원 최적화**: 수백 개의 광원이 배치되어도 안정적인 60 FPS 유지
*   **표현력 향상**: Deferred의 이점(많은 광원)과 Forward의 이점(반투명 처리)을 모두 확보하여 화려한 게임 씬 구성 가능
*   **G-Buffer 시각화**: 각 Render Target이 정상적으로 출력됨을 디버깅 모드로 확인
  
<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

### 2️⃣ NavMesh 검색 속도 최적화 (Spatial Grid)<a name="navmesh-optimization"></a>

> **🚨 문제 상황: 선형 탐색(Linear Search)으로 인한 병목**
> 
> *   **구조적 문제** : 캐릭터가 이동할 때마다 현재 위치를 NavMesh 위의 유효한 지점으로 보정하기 위해 `GetNearestPointOnNavMesh`를 호출.
> *   **성능 저하** : 별도의 공간 분할 없이 구현된 초기 로직은 맵 전체의 삼각형(20,000개+)을 순차적으로 검사하는 $O(N)$ 비용 발생 [file:48]
> *   **코드 병목** : `GetNearestPointOnNavMesh` 내부에서 모든 삼각형과의 거리를 계산하는 반복문이 매 프레임 실행됨. [[📄GetNearestPointOnNavMesh()]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/NavMesh.cpp#L93-L129)

**💡 해결 과정**

1.  **공간 분할(Spatial Partitioning) 도입**
    *   맵 전체를 일정 크기의 **그리드(Grid)** 형태로 분할하고, 각 셀에 포함된 삼각형을 HashMap에 저장
    *   [[📄NavMesh.h :: SpatialGrid]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/NavMesh.h#L31-L81)

2.  **검색 알고리즘 최적화 ( $O(N) \rightarrow O(k)$, $k \ll N$ )**
    *   **해시맵(HashMap) 활용** : 입력된 월드 좌표를 키(Key)로 변환하여 셀에 즉시 접근하고, 해당 셀에 등록된 소수의 삼각형(k개, $k \ll N$)만 검사하도록 로직 변경
    *   **탐색 범위 축소** : 전체 삼각형을 순회하는 대신, 해당 셀에 등록된 **소수의 삼각형만 검사** 하도록 로직 변경
      *   | **Grid** |
          | :---: |
          | <img width="800" height="300" alt="image" src="https://github.com/user-attachments/assets/23899d6e-6b8f-45d7-a73e-57481c95c8bc" /> |
    *   [[📄NavMesh.cpp :: FindTriangleContaining]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/NavMesh.cpp#L463-L500)

**✅ 결과**
*   **성능 검증** : 탐색 소요 시간 **301μs → 14μs** (약 **21.5배** 성능 향상)
*   **확장성 확보** : 맵 크기가 커지거나 삼각형이 늘어나도 탐색 비용이 일정하게 유지됨
*   | **Linear Search (최적화 전)** | **Spatial Grid (최적화 후)** |
    | :---: | :---: |
    | <img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/b59f744c-0db7-424f-aa5f-de1a4227bd46" /> | <img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/1b0dd8aa-b523-4060-91d2-6048b1c60e53" /> |
*   | **Case 1** | **Case 2** |
    | :---: | :---: |
    | <img width="600" height="300" alt="530234536-43d4a9ba-5cbd-43da-bc92-ab82ded95206" src="https://github.com/user-attachments/assets/30f19404-e250-4b92-a0b6-bbe8559085e1" /> | <img width="600" height="300" alt="530234561-efd1d8ff-4feb-42f0-aa3f-bbb6bb7b4d56" src="https://github.com/user-attachments/assets/ad405d09-a50a-4730-8f42-4312e70d70ca" /> |

<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

### 3️⃣ 쿼드 트리 기반 공간 분할 최적화<a name="quadtree-optimization"></a>

> **🚨 문제 상황: $O(N^2)$의 충돌 검사 및 렌더링 부하**
> 
> *   **비효율적 연산** : 1,000개 이상의 오브젝트가 존재하는 넓은 맵에서, 모든 객체 쌍에 대해 충돌 검사를 수행( $N \times N$ )하여 프레임 드랍 발생
> *   **불필요한 렌더링** : 카메라 시야(Frustum) 밖의 객체까지 렌더링 파이프라인에 포함되어 GPU 자원 낭비

**💡 해결 과정**

1.  **쿼드 트리(Quad Tree) 도입 이유 (Why?)**
    *   **2D 기반 최적화** : 게임 시점이 **쿼터뷰(Quarter View)** 고정형이므로, 높이(Y축)에 대한 복잡한 분할(Octree) 대신 평면 분할만으로 충분
    *   **게임 기획 특성** : 근접 전투 중심이며 원거리 투사체가 없어, 화면 내 로직 처리에 집중하는 것이 효율적

2.  **기능 구현 및 최적화 전략**
    *   **공간 분할**: 맵 전체를 4분면으로 재귀적으로 분할하여 객체를 노드(Node) 단위로 관리
    *   **계층적 충돌 검사 (Hierarchical Collision Check)**:
        *   **내부 검사 (Internal)**: 동일한 Leaf Node에 속한 객체끼리만 검사.
        *   **경계 검사 (Boundary)**: 노드의 경계선에 걸쳐있는 객체(Parent Node 소속)는 하위 노드(Child Node)의 객체들과 교차 검사 수행.
        *   [[📄QuadTree 충돌 로직]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L945-L1113)
        *   [[📄QuadTree 쿼리]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L259-L278)
    
    *   | **충돌 검사 시각화 (빨간색 객체는 초록색 영역만 검사)** |
        | :---: |
        | <img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/07e61fdf-1211-4b0c-89de-ed349e610ae9" /> |

**✅ 결과**
*   **마우스 Picking** : 전체 검사 대비 **4.6배** 속도 향상 (656μs → **142μs**)
*   **충돌 처리** : $O(N^2)$ 비용을  줄여 **135.8배** 속도 향상 (53,992μs → **397μs**)
*   | **Picking 최적화 (Ray-Node 검사)** | **결과** |
    | :---: | :---: |
    | <img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/78c17ec1-386d-40a0-a706-64658aa07e40" /> | <img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/de4cc346-71c3-42ee-a2b9-b4eb4560233f" />|
*   | **충돌 처리 최적화 (Node 내부 검사)** | **결과** |
    | :---: | :---: |
    | <img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/07e61fdf-1211-4b0c-89de-ed349e610ae9" /> | <img width="500" height="350" alt="image" src="https://github.com/user-attachments/assets/ad1519df-17e7-412a-a11f-657f5d8e04f8" /> |

<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

### 4️⃣ 몬스터 AI 아키텍처 개선: FSM → Behavior Tree<a name="fsm-to-bt"></a>

> **🚨 문제 상황**
>
> **"FSM에서 상태/전이 조건이 증가하면서 유지보수성 급격히 악화"**
>
> - **파일 폭증** : Wolf 몬스터 1종에 상태 8개(Appear/Attack/Death/Dying/Run/Trace/Wait)만 구현해도 **클래스 16개** (.cpp + .h)가 생성됨
> - **전이 로직 분산** : 각 상태 클래스 내부에 "다음 상태로 언제 전환할 것인가"를 결정하는 조건이 흩어져 있어, 전체 흐름을 파악하기 어려움
> - **확장 비용 증가** : 새로운 행동(예: Skill) 추가 시, 기존의 여러 상태 클래스를 수정해야 하므로 사이드 이펙트 발생 위험 증가

**💡 해결 과정** [[📄BehaviorTree]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Engine/BehaviorTree.h)

**"계층적 우선순위 구조의 Behavior Tree 도입"**

- **Selector 기반 우선순위 판단** :
  - 루트 노드를 `Selector`로 설정하여 왼쪽(상위)에서 오른쪽(하위)으로 조건을 검사하며, 가장 먼저 성공하는 행동만 수행하도록 설계
  - 우선순위: **생존(사망 체크) > 전투(공격) > 추적(이동) > 대기(Idle)**

- **Sequence 노드로 조건-행동 묶음 구성** :
  - 각 행동을 `Sequence`로 구성하여 "조건 체크 → 행동 실행"을 하나의 논리 단위로 캡슐화
  - 예: `[HP <= 0 체크] → [Die()]` / `[사거리 내 체크] → [Attack()]`

- **상태 간 결합도 제거** :
  - 기존 FSM에서는 `TraceState` 내부에 "거리가 가까우면 AttackState로 전환" 코드가 있었으나, BT에서는 각 노드가 독립적으로 조건만 체크
  - 전환 로직은 부모 노드(Selector)가 자동으로 처리하므로, 노드 간 의존성 사라짐

**🤔 기술적 의사결정: 왜 Behavior Tree인가?**

**1. 우선순위의 구조화**
  - FSM에서는 "어떤 상태가 우선인가?"를 코드 곳곳에 숨겨진 `if`문으로 결정했으나, BT는 **트리 구조 자체**가 우선순위를 명시함
  - 면접관이나 후임 개발자가 코드를 보지 않고도 다이어그램만으로 AI 로직의 우선순위를 직관적으로 파악 가능

**2. 모듈화와 재사용성**
  - `CheckHP`, `CheckAttackRange` 같은 조건 노드는 다른 몬스터에도 재사용 가능
  - 새로운 행동(예: Skill) 추가 시, 기존 노드를 수정할 필요 없이 새로운 Sequence 노드를 트리의 적절한 위치에 삽입만 하면 됨

**3. 디버깅 용이성**
  - 각 노드가 `SUCCESS`, `FAILURE`, `RUNNING` 상태를 명확히 반환하므로, 런타임에 어느 노드에서 실패했는지 추적 가능
  - FSM의 "상태 A에서 상태 B로 전환이 안 됨" 같은 모호한 디버깅 상황 감소

**✅ 결과**

| 비교 항목 | 기존 (FSM) | 개선 (Behavior Tree) |
| :---: | :---: | :---: |
| **핵심 구조** | 상태 (State) + 전이 (Transition) | 행동 (Action) + 우선순위 (Selector) |
| **흐름 제어** | 각 상태가 다음 상태를 직접 결정 | 부모 노드가 자식의 실행 여부 결정 |
| **결합도** | 상태끼리 서로 참조 (강한 결합) | 노드끼리 서로 모름 (독립적) |
| **확장성** | 상태 추가 시 기존 코드 수정 필수 | 노드만 추가하면 됨 (수정 불필요) |
| **우선순위** | 코드 로직에 숨겨져 파악 힘듦 | 트리 구조(왼쪽→오른쪽)로 직관적 |

**📊 구조 비교**

| **FSM 구조 (상태 전이 다이어그램)** | **Behavior Tree 구조** |
| :---: | :---: |
| <img width="795" height="808" alt="image" src="https://github.com/user-attachments/assets/a45edf80-a4be-4046-994f-9d9fc2b5d645" /> | <img width="1471" height="709" alt="image" src="https://github.com/user-attachments/assets/b9cb3150-afb2-494a-b3ef-224d4cb2fd75" /> |
| *복잡하게 얽힌 상태 간 화살표* | *계층적으로 정리된 우선순위 구조* |

<div align="right">
  <a href="#toc-eternal">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<br>

---

<br>

# 🎮 Brotato 모작<a name="brotato-main"></a>

<p align="left">
  <img src="https://github.com/user-attachments/assets/0fa0932b-be02-4008-a29b-4711adab14db" width="800"/>
</p>

<div align="left">

### 📌 프로젝트 정보

| 항목 | 내용 |
|:---:|:---:|
| 🎯 **장르** | 탑다운 슈팅, 로그라이크 서바이벌 |
| ⏱️ **개발 기간** | 2025.02 ~ 2025.03 (3주) |
| 👥 **개발 인원** | 2인 (프로그래머로 참여) |
| 🛠️ **개발 환경** | C++, Direct2D, Win32 API |
| 🎬 **시연 영상** | [YouTube 바로가기](https://youtu.be/d-VZS1AdvtA?si=zvILKb3qGncavOqS) |
| 💾 **GitHub** | [소스코드](https://github.com/HyangRim/BrotatoClone) |

</div>

## 📑 프로젝트 목차<a name="toc-brotato"></a>

**1. 📖 [게임 개요](#overview-brotato)**

**2. 📌 [학습 목표 및 달성](#goals-brotato)**

**3. 🔨 [주요 개발 기능](#features-brotato)** <br>
&nbsp;&nbsp; └ [렌더링 시스템](#rendering-system-brotato)<br>
&nbsp;&nbsp; └ [엔진 아키텍처 (Manager-Scene-Object)](#engine-brotato)<br>
&nbsp;&nbsp; └ [컴포넌트 기반 객체 설계](#component-brotato)<br>

**4. 🛠️ [문제 해결 (Troubleshooting)](#troubleshooting-brotato)** <br>
&nbsp;&nbsp; └ **[GDI+ → Direct2D 전환](#direct2d-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  하드웨어 가속 도입으로 대규모 웨이브 시 **FPS 10배 향상 (20 → 200+)**

&nbsp;&nbsp; └ **[타일맵 렌더링 최적화](#tilemap-optimization)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  비트맵 베이킹(Baking) 기법으로 **Draw Call 99.9% 감소 (1,296회 → 1회)**

&nbsp;&nbsp; └ **[이벤트 시스템 자료구조 개선](#event-queue-system)** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  `unordered_set` 도입으로 **삭제 중복 요청(Double Free) 및 순환 참조 해결**

<div align="right">
  <a href="#table-of-contents">⬆️ 전체 목차로 돌아가기</a>
</div>

<br>

## 📖 게임 개요<a name="overview-brotato"></a>

**장르** : 탑다운 슈팅 / 로그라이크 서바이벌

Brotato는 감자가 되어 외계 행성에서 밀려오는 수많은 외계인을 물리치는 탑다운 아레나 슈팅 게임입니다. 최대 6개의 무기를 동시에 사용하며, 다양한 아이템과 특성을 조합하여 자신만의 빌드를 구축하고 생존해야 합니다.

**🔄 핵심 루프 (Core Loop)**
1. **웨이브 생존** : 제한 시간 동안 몰려오는 적들로부터 생존
2. **재화 획득** : 적 처치 시 떨어지는 재료 수집
3. **상점/빌드 강화** : 웨이브 종료 후 상점에서 무기 및 아이템 구매
4. **다음 웨이브** : 더 강력해진 적들과 전투

**🎯 개발 초점**
- **수백 개의 몬스터와 투사체**가 난무하는 대규모 난전 상황 구현
- **프레임 방어 및 최적화**를 위한 렌더링 파이프라인 설계

<div align="right">
  <a href="#toc-brotato">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

## 📌 학습 목표 및 달성<a name="goals-brotato"></a>

> **"게임 엔진의 기본 아키텍처와 2D 렌더링 파이프라인 학습"**

이 프로젝트의 목표는 엔진 없이 Win32 API와 Direct2D를 활용하여 게임 엔진의 핵심 구조(Scene 관리, Object 관리)를 직접 설계하고, GDI+에서 Direct2D로의 마이그레이션을 통해 하드웨어 가속의 필요성과 원리를 체득하는 것이었습니다.

### 1️⃣ 계층적 엔진 아키텍처 설계
- **Manager - Scene - Object 구조** : 게임의 생명주기를 관리하는 `GameManager`, 씬 전환을 담당하는 `SceneManager`, 객체를 관리하는 `ObjectManager` 등 3계층 구조의 싱글톤 패턴 적용
- **확장성 있는 설계** : 상속과 다형성을 활용하여 유지보수가 용이한 객체 지향적 엔진 아키텍처 구축

### 2️⃣ 렌더링 시스템의 이해 및 고도화
- **GDI+ → Direct2D 전환** : 초기 GDI+로 구현 시 발생한 성능 저하를 해결하기 위해 Direct2D로 렌더링 파이프라인 전면 교체 (하드웨어 가속 적용)
- **더블 버퍼링 (Double Buffering)** : 화면 깜빡임(Flickering) 현상을 방지하기 위해 백 버퍼(Back Buffer)에 먼저 그리고 프론트 버퍼(Front Buffer)와 교체하는 기법 적용

### 3️⃣ 성능 중심의 개발 프로세스
- **병목 지점 식별** : 프로파일링을 통해 대량의 객체 렌더링 시 발생하는 CPU 오버헤드 식별
- **최적화 기법 적용** : 불필요한 연산을 줄이기 위한 공간 분할 및 렌더링 배칭(Batching) 기법 연구 및 적용

<div align="right">
  <a href="#toc-brotato">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<br>

---

<br>

## 🔨 주요 개발<a name="features-brotato"></a>

<a name="rendering-system-brotato"></a>
<details open>
<summary><h3>🎨 렌더링 시스템</h3></summary>

<br>

**Direct2D 기반 렌더링 파이프라인**
- **하드웨어 가속** : GDI+의 CPU 렌더링 방식이 가진 성능 한계를 극복하기 위해, GPU 가속을 지원하는 Direct2D로 렌더링 파이프라인 교체
- **더블 버퍼링 (Double Buffering)** : 렌더 타겟(Back Buffer)에 모든 오브젝트를 먼저 그린 후, 화면(Front Buffer)과 교체(Present)하여 깜빡임(Flickering) 현상 차단
- [[📄Direct2D.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/Direct2DMgr.h)

**대규모 리소스 관리 및 최적화**
- **리소스 매니저** : `unordered_map`을 활용한 텍스처(비트맵) 캐싱 시스템을 구축하여 중복 로딩 방지 및 빠른 리소스 접근 지원
- **타일맵 렌더링 최적화 (Batching)** : 
    - 32x32 타일 1,296개(36x36)를 매 프레임 개별 렌더링하던 방식을 개선
    - 1,296회의 개별 드로우 콜을 하나의 비트맵 렌더링으로 병합(Batching) **DrawCall을 1,296회 → 1회로 감소**
      - [[📄오프스크린 비트맵]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CScene.cpp#L431-L547)

> **🚀 성능 개선 사례**:
> 1. GDI+ 대비 20배 이상의 성능 향상을 이뤄낸 **[Direct2D 전환기]** 는 하단 **[🛠️ 문제 해결](#direct2d-optimization)**에서 다룹니다.
> 2. 타일맵 드로우 콜을 99.9% 줄인 **[타일맵 베이킹 기법]** 은 하단 **[🛠️ 문제 해결](#tilemap-optimization)**에서 상세히 설명합니다.

</details>

<div align="right">
  <a href="#toc-brotato">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="engine-brotato"></a>
<details open>
<summary><h3>🏗️ 엔진 아키텍처 및 코어 시스템</h3></summary>

<br>

**Manager-Scene-Object 3계층 구조**
- **싱글톤 매니저** : `CCore`를 중심으로 Time, Key, Camera, Scene 등 10여 개의 핵심 기능을 담당하는 Manager 클래스들을 싱글톤 패턴으로 초기화 및 관리
  - [[📄매니저 초기화]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCore.cpp#L88-L100)
- **프레임워크 흐름 제어** : 메인 루프에서 매 프레임 `Progress()`를 호출하여 `Update` → `Render` 순서로 게임 로직과 렌더링을 일괄 처리

**지연 처리(Delayed Processing) 이벤트 시스템**
- **이벤트 큐(Event Queue)** : 객체 생성/삭제, 씬 전환 등의 요청을 즉시 실행하지 않고 큐에 저장하여 프레임 동기화 유지
- **안전한 생명주기 관리** : 모든 로직 업데이트가 끝난 후 이벤트를 일괄 처리하여, 반복문 순회 중 객체 삭제로 인한 `Iterator Invalidated` 에러 방지
  - [[📄이벤트 처리 로직]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L44-L92)

> **🚀 구조적 문제 해결**: 반복문 순회 중 객체 삭제로 인한 런타임 에러를 해결한 **[이벤트 큐 시스템 도입]** 과정은 하단 **[🛠️ 문제 해결](#event-queue-system)**에서 자세히 다룹니다.

</details>

<div align="right">
  <a href="#toc-brotato">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<a name="component-brotato"></a>
<details open>
<summary><h3>🧩 컴포넌트 기반 객체 시스템</h3></summary>

<br>

**확장성 있는 오브젝트 설계**
- **CObject 추상 클래스** : 모든 게임 객체의 기본이 되는 클래스로, 컴포넌트 컨테이너 역할 수행
- **컴포넌트 패턴** : `Collider`(충돌), `Animator`(애니메이션), `Rigidbody`(물리) 등 기능 단위로 컴포넌트를 분리하여 조합형 객체 설계
  - [[📄Collider.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CCollider.h)
  - [[📄Animator.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CAnimator.h)

**계층적 UI 시스템**
- **UI 컴포넌트화** : `Panel`, `Button`, `Text` 등 UI 요소를 객체화하고, 부모-자식 관계(Parent-Child)를 통해 위치와 렌더링 순서를 계층적으로 관리
- **콜백(Callback) 이벤트** : 버튼 클릭 등의 상호작용을 함수 포인터 기반의 콜백으로 처리하여 로직 결합도 감소

</details>

<div align="right">
  <a href="#toc-brotato">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<br>

---

<br>

## 🛠️ 문제 해결<a name="troubleshooting-brotato"></a>

### 1️⃣ GDI+에서 Direct2D 전환을 통한 렌더링 최적화<a name="direct2d-optimization"></a>

> **🚨 문제 상황: CPU 기반 렌더링의 한계**
> 
> *   **GDI/GDI+의 구조적 문제** : 픽셀 연산을 CPU가 전담하여 처리함에 따라, 다수의 오브젝트(몬스터, 투사체)가 등장하면 FPS가 20~40대로 급락
> *   **화면 품질 저하** : 단일 버퍼 렌더링으로 인한 플리커링(Flickering)과 낮은 주사율로 시각적 품질 저하.

**💡 해결 과정** [[📄Direct2D 초기화]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/Direct2DMgr.cpp#L15-L59)
- **하드웨어 가속 파이프라인** : CPU 의존적인 GDI+를 버리고, GPU 가속을 활용하는 Direct2D(`ID2D1HwndRenderTarget`)로 엔진 코어 교체
- **렌더링 아키텍처 개선** : `CreateCompatibleRenderTarget()`을 이용한 **Back Buffer 기반의 더블 버퍼링 아키텍처**를 구축하여 프레임 안정성 확보.

**✅ 결과**
- **압도적인 성능 향상** : 대규모 웨이브 상황에서도 **FPS 200+** (평균 150~250) 유지하여 GDI+ 대비 **약 10배 이상의 성능 개선** 확인 
- **안정적인 플레이** : 수백 개의 투사체와 몬스터가 난무하는 상황에서도 끊김 없는 부드러운 조작감 확보.

| **대규모 웨이브** | **FPS 변화** |
| :---: | :---: |
| ![몬스터 많을때 플레이-1](https://github.com/user-attachments/assets/276c08d4-d76a-4fa5-a3a7-a5933ff0b6d1) | ![몬스터 많을때 플레이-2](https://github.com/user-attachments/assets/09890ffb-9d42-46b5-814c-603897c64c91) |


<div align="right">
  <a href="#toc-brotato">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

### 2️⃣ 타일맵 렌더링 최적화: Draw Call 병목 해결<a name="tilemap-optimization"></a>

> **🚨 문제 상황**
>
> **"매 프레임 1,296회의 그리기 명령으로 인한 CPU 오버헤드 발생"**
>
> - **상황** : 36x36 크기의 타일맵을 구현하기 위해 매 프레임 **1,296번의 `DrawBitmap`** 함수 호출.
> - **위험** : 초기에는 650 FPS로 문제가 없어 보였으나, 몬스터(100마리 이상)와 투사체가 급증하는 후반부 웨이브에서 프레임 드랍이 발생할 잠재적 위험 확인.
> - **기술적 원인 분석** :
>   - **Context Switching 비용 과다** : 1,296번의 렌더링 명령을 개별적으로 처리하면서 CPU가 GPU에 명령을 제출(Submit)하는 과정에 병목 발생.
>   - **GPU 유휴 상태(Idle)** : CPU가 명령을 보내느라 바빠서, 정작 GPU는 명령을 기다리는 대기 시간이 길어짐 (CPU 바운드 현상).

**💡 해결 과정** [[📄타일맵 생성 함수]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CScene.cpp#L431-L547)

**"오프스크린 렌더링을 통한 배칭(Batching) 처리"**
- **오프스크린 타겟 생성** : `ID2D1BitmapRenderTarget`을 사용하여 메모리 상에 거대한 캔버스(1,152x1,152 픽셀)를 생성.
- **프리 렌더링 (Pre-rendering)** : 게임 로딩 시점에 36x36개의 타일(32px)을 순회하며 오프스크린 타겟에 **단 1장의 거대 비트맵** 으로 미리 합성.
  - *테두리 타일은 규칙적으로, 내부 타일은 랜덤하게 배치하여 자연스러운 맵 생성.*
- **런타임 최적화** : 매 프레임 1,296번의 루프를 도는 대신, 합성된 **단일 비트맵만 1회 렌더링** 하도록 변경.

**✅ 결과**
- 이 최적화를 통해 CPU의 명령 제출 비용을 획기적으로 줄여, 후반부 대규모 교전 로직(충돌 처리 등)을 위한 연산 자원을 확보했습니다.

- | 성능 지표 | 최적화 전 (Before) | 최적화 후 (After) | 개선율 |
  | :--- | :---: | :---: | :---: |
  |  **Draw Calls** | 1,296 회 | **1 회** | **99.9% 감소** |
  | **FPS (Avg)** | ~650 | **~1,400** | **약 2.15배 증가** |
  | **Frame Time** | 1.54 ms | **0.71 ms** | **약 0.8ms 단축** |
- | **Before (최적화 전)** | **After (최적화 후)** |
  | :---: | :---: |
  | ![타일최적화(Before)](https://github.com/user-attachments/assets/b5534d3c-3910-4649-914d-8c13902e7670) | ![타일최적화(After)](https://github.com/user-attachments/assets/08e592ca-8a7e-4ad2-9cb7-264ab596d6be) |
  | **DrawCall: 1,296회 / FPS: ~650** | **DrawCall: 1회 / FPS: ~1,400** |

<div align="right">
  <a href="#toc-brotato">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

### 3️⃣ 이벤트 처리 시 중복 삭제로 인한 메모리 오염 방지<a name="event-queue-system"></a>

> **🚨 문제 상황**
>
> **"동일 프레임 내 중복된 삭제 요청으로 인한 Double Free 크래시 발생"**
>
> - **상황** : 안전한 객체 관리를 위해 `DELETE_OBJECT` 이벤트를 즉시 처리하지 않고 `vector` 컨테이너에 담아 지연 처리(Deferred Deletion) 수행.
> - **문제** : 다수의 투사체가 동시에 하나의 몬스터를 타격하는 난전 상황에서, **동일한 몬스터 객체 주소에 대한 삭제 요청**이 큐에 여러 번 중복 등록됨.
> - **결과** : 메모리 해제 시, 이미 해제된 주소를 다시 해제하려는 **Double Free 오류** 및 댕글링 포인터 접근으로 인한 프로그램 강제 종료(Crash) 발생.

**💡 해결 과정** [[📄객체 삭제 이벤트 처리]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L61-L69)

**"이벤트 큐와 실제 삭제 컨테이너의 분리 및 `unordered_set` 도입"**

- **이벤트 처리 파이프라인 분리:**
  - 기존의 이벤트 큐(`vector`)는 순차적 이벤트 처리를 위해 그대로 유지하되, **실제 삭제할 객체를 모아두는 전용 저장소**를 별도로 분리했습니다.

- **중복 제거 로직 적용 (`unordered_set`):**
  - `Execute` 함수에서 삭제 이벤트를 처리할 때, 객체를 즉시 `delete`하지 않고 **삭제 스케줄러(`unordered_set`)**에 주소를 삽입합니다.
  - **자료구조 선택 이유:**
      - **유일성 보장** : `set`의 특성을 활용해 동일 주소가 여러 번 들어와도 자동으로 1개만 유지.
      - **성능 ( $O(1)$ )** : `std::set` 대신 해시 기반의 `std::unordered_set`을 사용하여 삽입/검색 성능을 $O(1)$ 로 최적화, 정렬 오버헤드 제거.
        
- **지연 삭제 (Lazy Deletion) 수행:** [[📄최종 삭제 로직]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L24-L30)
  - 모든 프레임 로직이 끝난 후, `unordered_set`에 모인 '유니크한' 객체 주소들만 순회하며 최종적으로 `delete`를 수행합니다.

 
**✅ 결과**
| 개선 항목 | 설명 |
| :---: | :---: |
| **안정성 확보** | 동일 프레임 내 수십 개의 삭제 요청이 들어와도 **메모리 해제는 단 1회만 수행됨**을 보장하여 크래시 차단. |
| **성능 유지** | 해시 기반 컨테이너(`unordered_set`) 사용으로 다수의 오브젝트가 상호작용하는 난전 상황에서도 오버헤드 없는 이벤트 처리 구현. |
| **구조 개선** | 삭제 요청(Logic)과 실제 메모리 해제 시점을 명확히 분리하여 코드의 유지보수성 향상. |

<div align="right">
  <a href="#toc-brotato">⬆️ 프로젝트 목차로 돌아가기</a>
</div>

<br>
<br>

---
