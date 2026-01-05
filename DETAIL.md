# 📑 이형규 포트폴리오
## INTRODUCTION

### 개발자로서의 이형규

**🤝 함께 성장하는 팀 플레이어**

- 나의 코드가 팀원과 호환되는가를 항상 먼저 생각합니다.
- 짧은 주석, 코드 리뷰, 기술 문서화를 통해 팀원이 시간을 투자할 필요 없이 바로 이해하고 사용할 수 있도록 돕습니다.

**🧠 끝까지 파고드는 문제 해결자**

- 겉으로 보이는 증상이 아닌 근본 원인을 찾습니다.
- "왜 느린가?" "어디가 병목인가?"를 어렴풋이 고민하는 것이 아니라, 프로파일러와 데이터로 직접 검증하고 해결합니다.

**🔧 완성도에 타협하지 않는 장인**

- 동작하는 코드 × 좋은 코드. 성능, 가독성 모두 확실하지 않으면 끝까지 고민합니다.
- 기술 부채를 쌓지 않고, 1프레임의 낭비도 없도록 깔끔하게 최적화를 추구합니다.

**📈 한계를 뛰어넘는 진취적 도전자**

- 치명적인 버그 앞에서도 당황하지 않고, 핵심 원인을 집중력으로 돌파합니다.
- 불가능 같던 성능 향상도 자료구조와 알고리즘 개선으로 기술적 난제를 해결한 경험이 있습니다.

<br>
<br>


---

## 💡 관심사 & 가치관

- 일상에서도 항상 개발에 대한 아이디어를 떠올립니다. 게임 플레이 중에도 "이건 어떻게 구현했을까?"를 생각하며, 기술적 호기심을 놓지 않습니다.

- 팀 프로젝트를 진행할 때는 타인의 코드에 대한 이해가 빠른 편이며, 소통할 때 상대의 의도를 잘 파악합니다.
- 책임감이 있어, 한 번 시작한 일은 끝까지 몰두합니다.

- 플레이어가 게임을 즐기는 데 방해받지 않도록, 안정적인 프레임과 자연스러운 조작감을 중시합니다.
- 누구나 쉽게 즐길 수 있고, 기술적으로도 탄탄한 게임을 만드는 것이 목표입니다.

<br>
<br>

---

## 목차<a name="table-of-contents"></a>

<table>
  <tbody>
    <tr>
      <td valign="top">
       <a>
        
 🎮 [이터널리턴 모작](#-이터널-리턴-모작) <br>
 
 > 📖 [게임 개요](#-게임-개요) <br>
   📌 [학습 목표 및 달성](#-학습-목표-및-달성) <br>
   🔨 [주요 개발](#-주요-개발) <br>
   🛠️ [문제 해결](#%EF%B8%8F-문제-해결) <br>
       </a>
      </td>
      <td valign="top">
      <a>
 🎮 [Brotato 모작](#-brotato-모작) <br>
 
 > 📖 [게임 개요](#-게임-개요-1) <br>
   📌 [학습 목표 및 달성](#-학습-목표-및-달성-1) <br>
   🔨 [주요 개발](#-주요-개발-1) <br>
   🛠️ [문제 해결](#%EF%B8%8F-문제-해결-1) <br>
      </a>
      </td>
      <td valign="top">
      <a>
 🎮  [TBI 모작](#-tbi-모작) <br>
 
 > 📖 [게임 개요](#-게임-개요-2) <br>
   📌 [학습 목표 및 달성](#-학습-목표-및-달성-2) <br>
   🔨 [주요 개발](#-주요-개발-2) <br>
   🛠️ [문제 해결](#%EF%B8%8F-문제-해결-2) <br>
      </a>
      </td>
    </tr>
  </tbody>
</table>

<br>
<br>

---

# 🎮 이터널 리턴 모작

<img width="1000" height="800" alt="image" src="https://github.com/user-attachments/assets/ee737290-1c9e-47af-95b2-b62d47e51f0c" />

### 📌 프로젝트 정보

| 항목 | 내용 |
|:---:|:---:|
| 🎯 **장르** | 쿼터뷰, 배틀로얄, MOBA |
| ⏱️ **개발 기간** | 2개월 |
| 👥 **개발 인원** | 2인 (프로그래머로 참여) |
| 🛠️ **개발 환경** | C++, DirectX11, HLSL |
| 🎬 **시연 영상** | [YouTube 바로가기](https://www.youtube.com/watch?v=b6XVkd0xc-E&list=LL&index=19&t=1s) |
| 📝 **개발 블로그** | [상세 개발 과정](https://tobrother.tistory.com/category/DirectX11/Eternal%20Return%20%EB%AA%A8%EC%9E%91) |
| 💾 **GitHub** | [소스코드](https://github.com/HyangRim/DirectX11-Engine-Client) |

</div>

<br>
<br>

## 📖 게임 개요

**장르**: 쿼터뷰 배틀로얄 / MOBA (Multiplayer Online Battle Arena)

이터널 리턴은 전략적인 쿼터뷰 시점의 생존 게임입니다. 플레이어는 루미아 섬에서 재료를 파밍하고 장비를 제작하여 캐릭터를 성장시키며, 최후의 1인이 될 때까지 생존해야 합니다.

**🔄 핵심 루프 (Core Loop)**
1. **파밍 및 제작**: 맵 곳곳의 재료 수집
2. **장비 강화**: 상위 등급 장비 제작으로 전투력 상승
3. **생존 경쟁**: 금지 구역 회피 및 다른 생존자와의 전투
4. **승리**: 최후의 1인 생존

**🎯 개발 초점**
- DirectX 11을 이용한 **3D 렌더링 파이프라인 구축**
- **엔진 레벨의 성능 최적화** 및 아키텍처 설계

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<br>

## 📌 학습 목표 및 달성

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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<br>

---

## 🔨 주요 개발

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

> **🚀 기술 도입 배경**: 다중 광원 처리를 위한 포워드 렌더링의 한계와 해결 과정은 하단 **[🛠️ 문제 해결](#deferred-rendering)** 파트에서 다룹니다.

</details>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>


<details open>
<summary><h3>🎭 인스턴싱 기반 렌더링 (GPU Instancing)</h3></summary>

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
| :---: | :--- | :--- | :--- |
| **API 호출** | 객체 수(N)만큼 호출 | **1회 호출** (Batch 단위) | **CPU 오버헤드 최소화** |
| **데이터 전달** | 매번 상수 버퍼(CB) 갱신 | **인스턴스 버퍼**로 일괄 전달 | **버스 대역폭 효율화** |
| **확장성** | 오브젝트 증가 시 성능 급락 | 수천 개가 늘어도 **비용 일정** | **대규모 씬 처리 가능** |

</details>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<details open>
<summary><h3>🌑 쿼드 트리 (공간 분할 자료구조)</h3></summary>

<br>

**자료구조 설계**
- **재귀적 노드 시스템**: `QuadTreeNode` 클래스가 4개의 자식 노드 포인터와 자신의 영역(BoundingBox) 정보를 가지는 트리 구조
- **동적 객체 관리**: 오브젝트의 위치가 변경될 때마다 트리의 노드를 갱신(Update)하거나 재삽입(Re-insert)하는 로직 구현

**핵심 기능**
- **공간 쿼리(Spatial Query)**: 특정 영역(절두체, 마우스 피킹 Ray)과 겹치는 노드만 빠르게 선별하는 인터페이스 제공
- **충돌 그룹 관리**: 노드 단위로 객체 리스트를 관리하여 인접한 객체끼리만 상호작용하도록 설계

**관련 이미지**
| **마우스 Picking** | **충돌 처리** |
| :---: | :---: |
| <img width="1267" height="708" alt="image" src="https://github.com/user-attachments/assets/7accc4dd-0591-4851-ad2a-5f9eeac8a0ad" /> | <img width="1267" height="709" alt="image" src="https://github.com/user-attachments/assets/63a9e9e8-4f4f-4292-bba7-6cd7235e22f3" /> |

**관련 코드**
- [[📄QuadTree.h (헤더 설계)]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Engine/QuadTree.h)
- [[📄Node Insert (객체 삽입 로직)]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L218-L257)

> **🚀 성능 최적화 사례**: 쿼드트리를 활용한 획기적인 충돌 처리 성능 개선(135배) 결과는 하단 **[🛠️ 문제 해결](#quadtree-optimization)** 파트에서 상세히 다룹니다.

</details>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<details open>
<summary><h3>🧭 NavMesh 길찾기 시스템</h3></summary>

<br>

**시스템 아키텍처**
- **NavMesh 데이터**: 맵 데이터를 삼각형(Triangle) 그래프 형태로 변환하여 이동 가능 영역 정의
- **경로 탐색(Pathfinding)**: 시작점과 도착점이 포함된 삼각형을 찾고, A* 알고리즘으로 연결된 삼각형들의 최단 경로 리스트 산출

**보정 알고리즘**
- **String Pulling**: 삼각형 중심을 잇는 지그재그 경로를 `Line-of-Sight` 검사를 통해 최단 직선 경로로 변환
- **Agent FSM**: AI 캐릭터의 이동 상태(Idle, Move)를 관리하고 NavMesh 위로 위치를 투영(Projection)하는 에이전트 클래스 구현

**관련 이미지**
| **NavMesh 스무딩 (Before)** | **NavMesh 스무딩 (After)** |
| :---: | :---: |
| ![NavMesh-스무딩x](https://github.com/user-attachments/assets/b9f093b3-bff1-434e-b170-fdee9c4e83df) | ![NavMesh-스무딩o](https://github.com/user-attachments/assets/456e6486-6547-4893-80c6-bba4817ac855) |

> **🚀 검색 속도 최적화**: 대규모 맵에서의 경로 탐색 병목을 해결한 'Spatial Grid' 기법은 하단 **[🛠️ 문제 해결](#navmesh-optimization)** 파트에서 상세히 다룹니다.

</details>

<br>
<br>
<br>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

---

## 🛠️ 문제 해결

### 1️⃣ Forward에서 Deferred Rendering으로 전환 (Hybrid)<a name="deferred-rendering"></a>

> **🚨 문제 상황: Forward Rendering의 구조적 한계**
> 
> **성능 병목** : 다수의 동적 광원(Skill Effects, Lights)이 배치되자 $O(\text{객체 수} \times \text{광원 수})$의 연산량으로 인해 프레임이 급격히 저하됨
> 
> **픽셀 오버드로우** : 화면에 보이지 않는 픽셀(Depth Test 실패)까지 불필요하게 셰이딩 연산을 수행하여 GPU 자원을 낭비함

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
      | <img width="1225" height="687" alt="image" src="https://github.com/user-attachments/assets/532b1300-8d61-492d-895f-298bf2efb7bd" /> | <img width="1462" height="820" alt="image" src="https://github.com/user-attachments/assets/4d721451-2f37-4160-bb71-78030de7103c" /> |


**✅ 결과**
*   **다중 광원 최적화**: 수백 개의 광원이 배치되어도 안정적인 60 FPS 유지
*   **표현력 향상**: Deferred의 이점(많은 광원)과 Forward의 이점(반투명 처리)을 모두 확보하여 화려한 게임 씬 구성 가능
*   **G-Buffer 시각화**: 각 Render Target이 정상적으로 출력됨을 디버깅 모드로 확인
  
<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

### 2️⃣ NavMesh 검색 속도 최적화 (Spatial Grid)<a name="navmesh-optimization"></a>

> **🚨 문제 상황: 선형 탐색(Linear Search)으로 인한 병목**
> 
> *   **구조적 문제** : 캐릭터가 이동할 때마다 현재 위치를 NavMesh 위의 유효한 지점으로 보정하기 위해 `GetNearestPointOnNavMesh`를 호출.
> *   **성능 저하** : 별도의 공간 분할 없이 구현된 초기 로직은 맵 전체의 삼각형(20,000개+)을 순차적으로 검사하는 $O(N)$ 비용 발생 [file:48]
> *   **코드 병목** : `GetNearestPointOnNavMesh` 내부에서 모든 삼각형과의 거리를 계산하는 반복문이 매 프레임 실행됨.

**💡 해결 과정**

1.  **공간 분할(Spatial Partitioning) 도입**
    *   맵 전체를 일정 크기의 **그리드(Grid)** 형태로 분할하고, 각 셀에 포함된 삼각형을 HashMap에 저장
    *   [[📄NavMesh.cpp :: InitializeSpatialGrid]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Engine/NavMesh.cpp#L440)

2.  **검색 알고리즘 최적화 ( $O(N) \rightarrow O(1)$ )**
    *   **해시맵(HashMap) 활용** : 입력된 월드 좌표를 키(Key)로 변환하여 $O(1)$ 시간 복잡도로 현재 속한 셀에 즉시 접근
    *   **탐색 범위 축소** : 전체 삼각형을 순회하는 대신, 해당 셀에 등록된 **소수의 삼각형만 검사** 하도록 로직 변경
      *   | **Grid** |
          | :---: |
          | <img width="800" height="300" alt="image" src="https://github.com/user-attachments/assets/23899d6e-6b8f-45d7-a73e-57481c95c8bc" /> |
    *   [[📄NavMesh.cpp :: GetNearestPointOnNavMesh (최적화 로직)]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/master/Engine/NavMesh.cpp#L93-L129)

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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

---

# 🎮 Brotato 모작

<p align="left">
  <img src="https://github.com/user-attachments/assets/0fa0932b-be02-4008-a29b-4711adab14db" width="800"/>
</p>

<div align="left">

### 📌 프로젝트 정보

| 항목 | 내용 |
|:---:|:---:|
| 🎯 **장르** | 탑다운 슈팅, 로그라이크 서바이벌 |
| ⏱️ **개발 기간** | 3주 |
| 👥 **개발 인원** | 2인 (프로그래머로 참여) |
| 🛠️ **개발 환경** | C++, Direct2D, Win32 API |
| 🎬 **시연 영상** | [YouTube 바로가기](https://youtu.be/d-VZS1AdvtA?si=zvILKb3qGncavOqS) |
| 💾 **GitHub** | [소스코드](https://github.com/HyangRim/BrotatoClone) |

</div>

<br>

## 📖 게임 개요

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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

## 📌 학습 목표 및 달성

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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<br>

---

<details open>
<summary><h3>🎨 렌더링 시스템 및 최적화</h3></summary>

<br>

**Direct2D 기반 렌더링 파이프라인**
- **하드웨어 가속** : GDI+의 CPU 렌더링 방식이 가진 성능 한계를 극복하기 위해, GPU 가속을 지원하는 Direct2D로 렌더링 파이프라인 교체
- **더블 버퍼링 (Double Buffering)** : 렌더 타겟(Back Buffer)에 모든 오브젝트를 먼저 그린 후, 화면(Front Buffer)과 교체(Present)하여 깜빡임(Flickering) 현상 차단
- [[📄Direct2D.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/Direct2DMgr.h)

**대규모 리소스 관리 및 최적화**
- **리소스 매니저** : `unordered_map`을 활용한 텍스처(비트맵) 캐싱 시스템을 구축하여 중복 로딩 방지 및 빠른 리소스 접근 지원
- **타일맵 렌더링 최적화 (Batching)** : 
    - 32x32 타일 1,296개(36x36)를 매 프레임 개별 렌더링하던 방식을 개선
    - 전체 타일을 하나의 오프스크린 비트맵(Off-screen Bitmap)에 미리 병합(Bake)하여 **DrawCall을 1,296회 → 1회로 감소**
  - [[📄비트맵 병합 및 렌더링]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/Direct2DMgr.cpp#L210-L265)

> **🚀 성능 개선 사례**:
> 1. GDI+ 대비 20배 이상의 성능 향상을 이뤄낸 **[Direct2D 전환기]**는 하단 **[🛠️ 문제 해결](#direct2d-optimization)**에서 다룹니다.
> 2. 타일맵 드로우 콜을 99.9% 줄인 **[타일맵 베이킹 기법]**은 하단 **[🛠️ 문제 해결](#tilemap-optimization)**에서 상세히 설명합니다.

</details>

<br>
<hr>
<br>

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

<br>
<hr>
<br>

<details open>
<summary><h3>🧩 컴포넌트 기반 객체 시스템</h3></summary>

<br>

**확장성 있는 오브젝트 설계**
- **CObject 추상 클래스** : 모든 게임 객체의 기본이 되는 클래스로, 컴포넌트 컨테이너 역할 수행
- **컴포넌트 패턴** : `Collider`(충돌), `Animator`(애니메이션), `Rigidbody`(물리), `AI`(인공지능) 등 기능 단위로 컴포넌트를 분리하여 조합형 객체 설계
  - [[📄Collider.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CCollider.h)
  - [[📄Animator.h]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CAnimator.h)

**계층적 UI 시스템**
- **UI 컴포넌트화** : `Panel`, `Button`, `Text` 등 UI 요소를 객체화하고, 부모-자식 관계(Parent-Child)를 통해 위치와 렌더링 순서를 계층적으로 관리
- **콜백(Callback) 이벤트** : 버튼 클릭 등의 상호작용을 함수 포인터 기반의 콜백으로 처리하여 로직 결합도 감소

</details>

<br>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

---

## 🛠️ 문제 해결

### 1️⃣ GDI에서 Direct2D로 전환을 통한 성능 개선<a name="direct2d-optimization"></a>

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
| ![몬스터 많을때 플레이-1](https://github.com/user-attachments/assets/276c08d4-d76a-4fa5-a3a7-a5933ff0b6d1) | ![몬스터 많을때 플레이-2](https://github.com/user-attachments/assets/09890ffb-9d42-46b5-814c-603897c64c91) |

<br><br>

### 2️⃣ 타일맵 렌더링 최적화<a name="tilemap-optimization"></a>
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
| ![타일최적화(Before)](https://github.com/user-attachments/assets/b5534d3c-3910-4649-914d-8c13902e7670) | ![타일최적화(After)](https://github.com/user-attachments/assets/08e592ca-8a7e-4ad2-9cb7-264ab596d6be) |
| **DrawCall: 1,296회 / FPS: ~650** | **DrawCall: 1회 / FPS: ~1,400** |

<br>
<br>

### 3️⃣ 이벤트 처리 시 중복 삭제로 인한 메모리 오염 방지<a name="event-queue-system"></a>
> **🚨 문제 상황**
>
> 객체 삭제 요청(DELETE_OBJECT)을 지연 처리하기 위해 vector에 담아 관리했습니다.
>
> 그러나 다수의 투사체가 동시에 하나의 몬스터를 타격하여 사망 처리가 중복 발생할 경우, 동일한 객체 주소에 대한 삭제 요청이 vector에 여러 번 적재되는 문제가 발생.
>
> 이로 인해 메모리 해제 시 Double Free 오류나 댕글링 포인터 접근으로 인한 크래시가 발생.

**💡 해결 과정**

- 이벤트 처리 구조 개선:
  - 이벤트 큐(vector)는 요청 순서 보장을 위해 유지하되, 실제 삭제할 객체를 모아두는 컨테이너를 별도로 분리

- 중복 제거 로직 적용 (unordered_set):
  - Execute 함수에서 삭제 이벤트를 처리할 때, 해당 객체를 즉시 지우지 않고 unordered_set (삭제 스케줄러) 에 삽입 [[📄객체 삭제 이벤트 처리]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L61-L69)
  - Set 자료구조의 특성을 이용해 동일 객체에 대한 중복 삭제 요청이 들어와도 자동으로 1회만 등록되도록 구현

- 지연 삭제 수행:
  - 모든 이벤트 처리가 끝난 후, unordered_set에 모인 객체들만 순회하며 최종적으로 delete 수행 [[📄객체 삭제]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L24-L30)
 
**✅ 결과**
- 동일 프레임 내 중복 삭제 요청이 들어와도 메모리 해제는 단 한 번만 수행됨을 보장
- 다수의 오브젝트가 상호작용하는 난전 상황에서도 안정적인 메모리 관리 구현

---

<br>

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

The Binding of Isaac(TBI)는 로그라이크 던전 크롤러 게임으로, 플레이어는 아이작이 되어 무작위로 생성되는 던전을 탐험하며 다양한 몬스터와 보스를 상대합니다. 눈물(탄환)을 발사하여 적을 처치하고, 방마다 등장하는 아이템을 수집하여 능력을 강화하는 것이 핵심입니다. 

## 📌 학습 목표 및 내용

**알고리즘과 설계 패턴을 활용한 게임 아키텍처 심화**

1. BFS를 이용한 던전 생성.
2. FSM으로 다양한 몬스터 AI를 관리.

이전에 배운 기술을 새로운 프로젝트에 적용하고, 그 과정에서 발견한 개선점을 다음 프로젝트에 역으로 반영하는 반복적 성장을 경험했습니다.

## 🤔 왜 TBI를 만들었는가?

1. **Brotato에서 학습한 기본 아키텍처를 다른 게임에 적용할 수 있는가?**
- YES. 같은 기본 구조로 다른 장르(로그라이크)를 구현

2. **새로운 기술적 도전이 있었는가?**
- BFS 던전 생성: 맵 구조가 게임 난이도에 미치는 영향 설계
- State 패턴: 복잡한 AI 로직을 체계적으로 관리

3. **배운 것이 다음 프로젝트(이터널 리턴)에 어떻게 활용되었는가?**
- State 패턴의 확장: 플레이어,몬스터 상태 관리에 활용

<br>

---

## 🔨 주요 개발

<details open>
<summary><b>🗺️ 절차적 던전 생성 시스템</b></summary>

<br>

**랜덤 던전 생성 알고리즘**
- 방 배치 알고리즘을 통한 무작위 던전 구조 생성 [[📄방 생성 알고리즘]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/MapMgr.cpp#L27-L135)
- 시작방, 보물방, 보스방 등 특수 방 배치 로직 [[📄특수 방 배치]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/MapMgr.cpp#L395-L455)
- 방 간 연결 통로 자동 생성
<img width="507" height="128" alt="image" src="https://github.com/user-attachments/assets/872c7f53-d02c-4983-acfe-d897bcf4c3c9" />

**타일 기반 맵 시스템**
- 벽, 문 등 타일 타입별 충돌 처리
- 방 입장 시 문 개폐 애니메이션 및 몬스터 스폰

</details>

<details open> 
<summary><b>🎁 확장성 있는 오브젝트 및 아이템 설계</b></summary>

<br>
  
**계층적 상속 구조 설계** [[📄CObject.h]](https://github.com/vfly1189/TBI/blob/master/TBI/CObject.h)
- CObject 추상 클래스를 기반으로 Monster, Projectile, Item 등으로 파생하여 다형성 구현
- 공통 기능(충돌, 렌더링)은 부모에서, 고유 기능(AI, 효과)은 자식에서 구현하여 코드 재사용성 증대

**전략적 아이템 시스템** [[📄CItem.h]](https://github.com/vfly1189/TBI/blob/master/TBI/CItem.h)
- 기능에 따라 수집형(PickUp), 장식형(Collectibles) 으로 클래스 분리
- 장식형 아이템: 받침대 + 본체 + 그림자의 복합 렌더링 구조와 획득 시 영구 스탯 반영 로직 구현
- 폭탄: 점화 → 폭발(Collider 확장) → 소멸의 상태 변화를 통해 광역 데미지 시스템 구현
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
- | **보스 몬스터** |
    | :---: |
    | ![보스공격패턴](https://github.com/user-attachments/assets/a38557c8-7436-4120-83a2-5eb71f5fc734) |
</details>

<details open>
<summary><b>💥 물리 기반 전투 시스템</b></summary>

<br>

**CRigidBody 컴포넌트**
- 중력, 속도, 마찰력을 고려한 물리 시뮬레이션 [[📄물리 효과 적용]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CRigidBody.cpp#L23-L82)
- 발사체 궤적 물리 기반 전투 효과
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
- 캐릭터, 몬스터, 아이템별 다양한 애니메이션 적용

</details>

<br>

---

## 🛠️ 문제 해결

### 1️⃣ BFS 기반 절차적 던전 생성 시스템

> **🚨 문제 상황**
> 
> DFS 알고리즘으로 던전을 생성했을 때 게임 플레이 중 문제 인식:
> 
> **플레이어 관점에서의 불편함:**
> - 게임 진행이 "탐험"이 아니라 "강제된 순회"처럼 느껴짐
> - 보스 앞에 도달했을 때 "여기까지 올 동안 너무 먼 길을 돌았다"는 피로감
>
> **알고리즘 관점에서의 분석:**
> - DFS의 선형적 특성이 게임의 선형적 흐름을 강제
> - "자유로운 탐험"이라는 로그라이크의 핵심 요소 훼손

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

### 2️⃣ State 패턴을 통한 몬스터 AI 관리

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


