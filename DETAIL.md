# 📑 이형규 포트폴리오
## INTRODUCTION

### 개발자로서의 이형규

**🤝 함께 성장하는 팀 플레이어**

- 나의 코드가 팀원과 호환되는가를 항상 먼저 생각합니다.
- 짧은 주석, 코드 리뷰, 기술 문서화를 통해 팀원이 시간을 투자할 필요 없이 이해하고 사용할 수 있도록 돕습니다.

**🧠 끝까지 파고드는 문제 해결자**

- 겉으로 보이는 증상이 아닌 근본 원인을 찾습니다.
- "왜 느린가?" "어디가 병목인가?"를 어렴풋이 고민하는 것이 아니라,데이터로 직접 검증하고 해결합니다.

**🔧 완성도에 타협하지 않는 장인**

- 동작하는 코드 × 좋은 코드. 성능, 가독성 모두 확실하지 않으면 끝까지 고민합니다.
- 기술 부채를 쌓지 않고, 1프레임의 낭비도 없도록 깔끔하게 최적화를 추구합니다.

**📈 한계를 뛰어넘는 진취적 도전자**

- 치명적인 버그 앞에서도 당황하지 않고, 핵심 원인을 집중력으로 돌파합니다.
- 불가능 같던 성능 향상도 자료구조와 알고리즘 개선으로 기술적 난제를 해결할려고 노력합니다.

<br>
<br>


---

<br>
<br>

## 💡 관심사 & 가치관

- 일상에서도 항상 개발에 대한 아이디어를 떠올립니다. 게임 플레이 중에도 "이건 어떻게 구현했을까?"를 생각하며, 기술적 호기심을 놓지 않습니다.

- 팀 프로젝트를 진행할 때는 타인의 코드에 대한 이해가 빠른 편이며, 소통할 때 상대의 의도를 잘 파악합니다.
- 책임감이 있어, 한 번 시작한 일은 끝까지 몰두합니다.

- 플레이어가 게임을 즐기는 데 방해받지 않도록, 안정적인 프레임과 자연스러운 조작감을 중시합니다.
- 누구나 쉽게 즐길 수 있고, 기술적으로도 탄탄한 게임을 만드는 것이 목표입니다.

<br>
<br>

---

<br>

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
   🛠️ [문제 해결](#troubleshooting-eternal-return) <br>
       </a>
      </td>
      <td valign="top">
      <a>
 🎮 [Brotato 모작](#-brotato-모작) <br>
 
 > 📖 [게임 개요](#-게임-개요-1) <br>
   📌 [학습 목표 및 달성](#-학습-목표-및-달성-1) <br>
   🔨 [주요 개발](#-주요-개발-1) <br>
   🛠️ [문제 해결](#troubleshooting-brotato) <br>
      </a>
      </td>
      <td valign="top">
      <a>
 🎮  [TBI 모작](#-tbi-모작) <br>
 
 > 📖 [게임 개요](#-게임-개요-2) <br>
   📌 [학습 목표 및 달성](#-학습-목표-및-달성-2) <br>
   🔨 [주요 개발](#-주요-개발-2) <br>
   🛠️ [문제 해결](#troubleshooting-tbi) <br>
      </a>
      </td>
    </tr>
  </tbody>
</table>

<br>
<br>

---

<br>

# 🎮 이터널 리턴 모작

<img width="1000" height="800" alt="image" src="https://github.com/user-attachments/assets/ee737290-1c9e-47af-95b2-b62d47e51f0c" />

### 📌 프로젝트 정보

| 항목 | 내용 |
|:---:|:---:|
| 🎯 **장르** | 쿼터뷰, 배틀로얄, MOBA |
| ⏱️ **개발 기간** | 2개월 |
| 👥 **개발 인원** | 2인 (프로그래머로 참여) |
| 🛠️ **개발 환경** | C++, DirectX11, HLSL |
| 🎬 **시연 영상** | [YouTube 바로가기](https://youtu.be/b6XVkd0xc-E?si=XHB1nkE6C2-JarC8) |
| 📝 **개발 블로그** | [상세 개발 과정](https://tobrother.tistory.com/category/DirectX11/Eternal%20Return%20%EB%AA%A8%EC%9E%91) |
| 💾 **GitHub** | [소스코드](https://github.com/HyangRim/DirectX11-Engine-Client) |

</div>

<br>
<hr>
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
<hr>
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

<br>

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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

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
- **String Pulling**: 삼각형 중심을 잇는 지그재그 경로를 `Line-of-Sight` 검사를 통해 최단 직선 경로로 변환 [[📄경로 스무딩]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/NavMesh.cpp#L307-L360)
- **Agent FSM**: AI 캐릭터의 이동 상태(Idle, Move)를 관리하고 NavMesh 위로 위치를 투영(Projection)하는 에이전트 클래스 구현

**관련 이미지**
| **NavMesh 스무딩 (Before)** | **NavMesh 스무딩 (After)** |
| :---: | :---: |
| ![NavMesh-스무딩x](https://github.com/user-attachments/assets/b9f093b3-bff1-434e-b170-fdee9c4e83df) | ![NavMesh-스무딩o](https://github.com/user-attachments/assets/456e6486-6547-4893-80c6-bba4817ac855) |

> **🚀 검색 속도 최적화**: 대규모 맵에서의 경로 탐색 병목을 해결한 'Spatial Grid' 기법은 하단 **[🛠️ 문제 해결](#navmesh-optimization)** 파트에서 상세히 다룹니다.

</details>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<br>

---

<br>

## 🛠️ 문제 해결<a name="troubleshooting-eternal-return"></a>

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
      | <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/532b1300-8d61-492d-895f-298bf2efb7bd" /> | <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/4d721451-2f37-4160-bb71-78030de7103c" /> |


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
> *   **코드 병목** : `GetNearestPointOnNavMesh` 내부에서 모든 삼각형과의 거리를 계산하는 반복문이 매 프레임 실행됨. [[📄GetNearestPointOnNavMesh()]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/NavMesh.cpp#L93-L129)

**💡 해결 과정**

1.  **공간 분할(Spatial Partitioning) 도입**
    *   맵 전체를 일정 크기의 **그리드(Grid)** 형태로 분할하고, 각 셀에 포함된 삼각형을 HashMap에 저장
    *   [[📄NavMesh.h :: SpatialGrid]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/NavMesh.h#L31-L81)

2.  **검색 알고리즘 최적화 ( $O(N) \rightarrow O(1)$ )**
    *   **해시맵(HashMap) 활용** : 입력된 월드 좌표를 키(Key)로 변환하여 $O(1)$ 시간 복잡도로 현재 속한 셀에 즉시 접근
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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<br>

---

<br>

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

<br>

## 🔨 주요 개발

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
    - 1,296회의 개별 드로우 콜을 하나의 비트맵 렌더링으로 병합(Batching) **DrawCall을 1,296회 → 1회로 감소**
      - [[📄오프스크린 비트맵]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CScene.cpp#L431-L547)

> **🚀 성능 개선 사례**:
> 1. GDI+ 대비 20배 이상의 성능 향상을 이뤄낸 **[Direct2D 전환기]** 는 하단 **[🛠️ 문제 해결](#direct2d-optimization)**에서 다룹니다.
> 2. 타일맵 드로우 콜을 99.9% 줄인 **[타일맵 베이킹 기법]** 은 하단 **[🛠️ 문제 해결](#tilemap-optimization)**에서 상세히 설명합니다.

</details>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

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

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

### 2️⃣ 타일맵 렌더링 최적화: Draw Call 병목 해결<a name="tilemap-optimization"></a>

> **🚨 문제 상황**
>
> **"매 프레임 1,296회의 그리기 명령으로 인한 CPU 오버헤드 발생"**
>
> - **상황** : 36x36 크기의 타일맵을 구현하기 위해 매 프레임 **1,296번의 `DrawBitmap`** 함수를 호출.
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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
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
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<br>

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

**장르**: 탑다운 슈팅 / 로그라이크 던전 크롤러

TBI는 로그라이크 던전 크롤러 게임으로, 플레이어는 아이작이 되어 무작위로 생성되는 던전을 탐험하며 다양한 몬스터와 보스를 상대합니다. 눈물(탄환)을 발사하여 적을 처치하고, 방마다 등장하는 아이템을 수집하여 능력을 강화하는 것이 핵심입니다.

**🔄 핵심 루프 (Core Loop)**
1. **랜덤 던전 탐험** : 매 판 다르게 생성되는 방 구조 탐색
2. **전투 및 성장** : 몬스터/보스 처치 후 아이템 수집으로 능력치 강화
3. **다음 스테이지** : 보스 격파 후 더 깊은 던전으로 이동

**🎯 개발 초점**
- **절차적 맵 생성 알고리즘**과 FSM 기반의 다양한 몬스터 패턴 구현을 통한 게임성 강화
- **자료구조 기반 시스템 설계**를 통한 유기적인 게임 월드 구축

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

## 🤔 왜 TBI를 만들었는가?

이 프로젝트는 Brotato 모작을 통해 확립한 게임 엔진 아키텍처를 검증하고, 자료구조와 알고리즘을 실제 게임 로직에 심도 있게 적용해보기 위해 시작했습니다.

**1. 아키텍처의 재사용성과 확장성 검증**
- **질문** : "Brotato에서 설계한 엔진 구조가 다른 장르에도 통하는가?"
- **검증** : 동일한 Manager-Scene-Object 구조를 로그라이크 장르에 성공적으로 이식하며, 엔진 아키텍처의 범용성을 확인했습니다.

**2. 기술적 도전: 알고리즘의 실전 적용**
- **BFS 기반 맵 생성** : 단순 배치가 아닌, 맵 구조가 게임 난이도와 탐험 재미에 직접적인 영향을 미치도록 설계했습니다.
- **State 패턴의 고도화** : 복잡한 보스 몬스터 AI를 FSM으로 체계적으로 관리하며, 코드의 유지보수성을 높였습니다.

**3. 다음 단계로의 연결 고리**
- 이 프로젝트에서 익힌 **State 패턴**과 **컴포넌트 기반 설계** 경험은, 이후 **이터널 리턴 모작(DirectX 11)** 프로젝트에서 플레이어와 몬스터의 복잡한 상태를 관리하는 핵심 기반이 되었습니다.

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

## 📌 학습 목표 및 달성

> **"알고리즘과 설계 패턴을 활용한 게임 아키텍처 심화"**

단순한 기능 구현을 넘어, 자료구조(Queue, Set)와 디자인 패턴(State, Singleton)을 적재적소에 활용하여 견고한 시스템을 구축하는 것을 목표로 했습니다.

### 1️⃣ 자료구조 기반 시스템 설계
- **절차적 맵 생성 (Procedural Map Generation)** : BFS 알고리즘과 큐(Queue)를 활용하여 시작 방에서 보스 방까지의 거리를 계산하고, 유기적으로 연결된 던전 구조를 생성
- **FSM (Finite State Machine) 설계** : 몬스터의 다양한 행동(대기, 추적, 공격, 패턴 변화)을 상태(State) 클래스로 분리하여 관리, AI 로직의 복잡도 해소

### 2️⃣ 확장성 있는 오브젝트 구조
- **다형성 기반 오브젝트 관리** : 몬스터, 아이템, 발사체 등을 공통 부모 클래스로 추상화하여 일관된 인터페이스로 관리
- **컴포넌트 응용** : 각 오브젝트의 역할에 따라 필요한 기능(물리, 렌더링, 충돌)을 모듈화하여 재사용성 증대

### 3️⃣ 물리 엔진의 기초 구현
- **독자적인 RigidBody 구축** : 가속도, 마찰력, 충돌 반사 벡터 등을 직접 계산하여 발사체의 궤적이나 피격 시 넉백(Knock-back) 효과 등 물리적 상호작용 구현

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<br>

---

<br>


## 🔨 주요 개발

<details open>
<summary><h3>🗺️ 절차적 맵 생성 알고리즘 (BFS)</h3></summary>

<br>

**"단순 랜덤이 아닌, '플레이 가능한' 던전 구조 생성"**

- **BFS 기반 방 배치** : 큐(Queue) 자료구조를 활용해 시작 방을 기준으로 상하좌우로 뻗어나가는 **Breadth-First Search** 알고리즘을 구현하여, 끊김 없는 유기적인 맵 구조를 생성했습니다. [[📄방 생성 로직]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/MapMgr.cpp#L27-L135)
- **거리 기반 특수 방 배치** : 시작 지점으로부터의 '깊이(Depth)'를 계산하여, 가장 먼 방에 **보스방** 을 배치하고 적절한 거리에 **보물방** 을 배치하는 등 게임 밸런스를 고려한 로직을 적용했습니다.
- **자동 통로 연결** : 인접한 방의 유무를 비트마스크(Bitmask) 등으로 판별하여 문(Door)과 통로를 자동으로 생성하고 연결했습니다.
- <img width="700" height="350" alt="image" src="https://github.com/user-attachments/assets/e864f3c1-00dd-4c54-b5fb-3b30c0b1fcb3" />

> **🚀 알고리즘 이슈 해결**: 단순 랜덤 배치가 아닌, **[BFS 기반의 유기적인 던전 생성]** 과정과 맵 구조 밸런싱 최적화 내용은 하단 **[🛠️ 문제 해결](#bfs-map-gen)**에서 자세히 다룹니다.

</details>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<details open> 
<summary><h3>🧠 FSM 기반 몬스터 AI 시스템</h3></summary>

<br>
  
**"복잡한 패턴을 체계적으로 관리하는 상태(State) 패턴 도입"**

- **유한 상태 머신 (FSM) 설계** : 몬스터의 행동을 `Idle`, `Trace`, `Attack`, `Dead` 등의 상태 클래스로 분리하여 관리함으로써, 조건문(if-else) 도배를 방지하고 유지보수성을 높였습니다. [[📄CState.h]](https://github.com/vfly1189/TBI/blob/e32ef1e500817b39cec13dc5ce6077ed149d3487/TBI/CState.h#L1-L30)
- **다양한 패턴 구현** :
    - **Trace State** : 벡터 연산을 통해 플레이어를 자연스럽게 추적 [[📄추적 로직]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CFlyTraceState.cpp#L24-L63)
    - **Attack State** : 보스 몬스터의 탄막 발사, 돌진 등 복잡한 공격 패턴을 독립된 클래스로 구현 [[📄보스 공격]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CBabyPlumAttackState.cpp#L32-L118)
- | **보스 몬스터 패턴** |
  | :---: |
  | ![보스공격패턴](https://github.com/user-attachments/assets/a38557c8-7436-4120-83a2-5eb71f5fc734) |

> **🚀 구조적 문제 해결**: 복잡한 몬스터 패턴을 체계적으로 관리하기 위해 도입한 **[State 패턴(FSM) 설계]**와 이를 통한 AI 로직 개선 과정은 하단 **[🛠️ 문제 해결](#fsm-pattern)**에서 자세히 다룹니다.

</details>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<details open>
<summary><h3>💥 물리 엔진 및 인터랙션 구현</h3></summary>

<br>

**"직접 구현한 물리 연산으로 타격감과 상호작용 극대화"**

- **RigidBody 컴포넌트** : `가속도`, `속도`, `마찰력`을 직접 연산하여 미끄러지는 듯한 이동 구현. [[📄물리 연산]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CRigidBody.cpp#L23-L82)
- **반사 벡터 처리** : 투사체가 벽이나 장애물에 충돌할 때 입사각과 반사각을 계산하여 튕겨 나가는 물리적 상호작용을 적용. (보스 패턴 등 활용)
- **정밀한 충돌 처리** : `CCollisionMgr`를 통해 레이어(Layer)별 충돌 필터링을 적용, 아군/적군/지형 간의 불필요한 연산을 배제하고 정확한 충돌 이벤트를 처리.

</details>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<details open>
<summary><h3>🧱 확장성 있는 오브젝트 설계</h3></summary>

<br>

**"객체 지향적 설계를 통한 코드 재사용성 증대"**

- **계층적 상속 구조**: `CObject` → `CMonster` / `CProjectile` / `CItem` 으로 이어지는 상속 구조를 설계하여 렌더링, 충돌 처리 등 공통 기능을 부모 클래스에서 일괄 처리.
- **아이템 시스템 분리** : 
    - **수집형(PickUp)** : 획득 즉시 소모되는 아이템 (하트, 동전 등)
    - **장식형(Collectibles)** : 획득 시 플레이어의 스탯을 영구적으로 변경하거나 특수 효과를 부여하는 아이템 (받침대 + 본체 + 그림자 렌더링 구조 적용)

</details>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

<details open>
<summary><h3>🎨 스프라이트 애니메이션 시스템</h3></summary>

<br>

**"컴포넌트 기반 설계를 통한 유연한 애니메이션 제어"**

- **CAnimator 컴포넌트** : 모든 오브젝트(플레이어, 몬스터, 이펙트)에 부착 가능한 독립 컴포넌트로 설계하여, 애니메이션 로직과 객체 로직을 분리.
- **프레임 단위 정밀 제어** : `DeltaTime`을 누적하여 프레임 전환 속도를 조절하고, `Repeat`, `Stop`, `Reverse` 등 다양한 재생 모드를 지원하여 상황에 맞는 연출을 구현. [[📄애니메이션 로직]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/CAnimator.cpp#L109-L154)
- **상태 동기화** : FSM의 상태 변화(Idle → Run → Attack)에 따라 자동으로 적절한 애니메이션 클립을 교체(Switching)하도록 설계하여, 시각적 표현과 내부 로직의 일체감을 확보.

</details>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<br>

---

<br>

## 🛠️ 문제 해결<a name="troubleshooting-tbi"></a>

### 1️⃣ 절차적 맵 생성 이슈: DFS vs BFS 비교 분석<a name="bfs-map-gen"></a>

> **🚨 문제 상황**
>
> **"DFS 기반 생성 시, 맵이 지나치게 선형적(뱀 모양)으로 배치되는 현상 발생"**
>
> - **구조의 단순성** : Stack을 활용한 DFS(깊이 우선 탐색) 알고리즘 적용 시, 한 방향으로만 계속 뻗어나가는 '외길형' 맵이 자주 생성됨.
> - **플레이 경험 저하** : 갈래길이나 분기점이 부족하여 플레이어가 "탐험한다"는 느낌보다는 "정해진 길을 따라간다"는 강제된 느낌을 받음.
> - **개발 효율성 저하** : 방사형 구조를 만들기 위해 인위적인 백트래킹(Backtracking) 로직을 추가해야 했으나, 이는 코드 복잡도를 높이고 유지보수를 어렵게 만듦.


**💡 해결 과정** [[📄방 생성 알고리즘]](https://github.com/vfly1189/TBI/blob/6fbbe9197ad6d2709ceb42d302f4829158b9958d/TBI/MapMgr.cpp#L27-L135)

**"BFS(너비 우선 탐색) 도입을 통한 유기적인 던전 생성"**

- **Queue 기반의 방사형 확장** : 시작 방(Start Room)을 큐에 넣고 상하좌우 인접 방향으로 동시에 확장해 나가는 로직으로 변경했습니다.
- **연결성 보장 로직** : `std::shuffle`을 사용하여 확장 방향을 무작위로 섞되, `countNeighbors()` 함수로 인접 방의 개수를 제어하여 과도하게 뭉치거나 끊어지는 현상을 방지했습니다.
- **동적 난이도 조절** : 스테이지가 진행될수록 생성해야 할 최소/최대 방 개수를 증가시켜, 자연스러운 난이도 상승 곡선을 설계했습니다.


**🤔 기술적 의사결정: 왜 BFS 알고리즘인가?**

- **1. 백트래킹(Backtracking) 피로도 최소화**
  - DFS의 선형적 구조는 맵 이동 동선이 지나치게 길어지는 단점이 존재했습니다.
  - BFS를 통해 시작점 중심의 **방사형 클러스터**를 형성함으로써, 플레이어가 상점이나 보물방을 이용하기 위해 이동하는 불필요한 시간을 줄이고 전투 밀도를 높였습니다.

- **2. 확장성을 고려한 공간 스캔**
  - 순차적으로 인접 공간을 탐색하는 구조 덕분에, 추후 **'2x2 대형 방'** 이나 **'L자형 특수 방'** 을 추가할 때 주변 빈 공간을 체크하고 할당하는 알고리즘으로 확장하기 유리하다고 판단했습니다.


**✅ 결과**
- | 구분 | DFS (Before) | BFS (After) |
  | :---: | :---: | :---: |
  | **맵 구조** | **선형적 (Linear)** <br> 뱀처럼 길게 늘어진 형태 | **방사형 (Radial)** <br> 중앙 집중형 클러스터 형태 |
  | **탐험 경험** | 왔던 길을 되돌아가는 **백트래킹 빈번** | 분기점이 많아 **자유로운 탐험 가능** |
  | **특수 방 배치** | 끝점에 배치하기 모호함 | **거리(Depth) 계산**을 통해 보스/보물방 전략적 배치 용이 |

 **📉 생성 결과 비교**
 - | **DFS (선형적 구조)** | **BFS (방사형 구조)** |
   | :---: | :---: |
   | <img width="1323" height="356" alt="image" src="https://github.com/user-attachments/assets/1e306575-30a7-4e01-9ced-034f47b57052" />| <img width="1317" height="356" alt="image" src="https://github.com/user-attachments/assets/bae38606-a6ab-4b75-ae65-9d1da2673cd3" /> |
   | *한 줄로 길게 늘어짐* | *중심에서 고르게 퍼져나감* |


<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

<br>
<hr>
<br>

### 2️⃣ State 패턴을 통한 몬스터 AI 관리: 복잡도 해소 <a name="fsm-pattern"></a>

> **🚨 문제 상황**
>
> **"복잡한 조건문(Nested If-Else)으로 인한 '스파게티 코드' 발생"**
>
> - **상황** : 초기에는 `if (거리 < 100) 공격 else 추적` 형태의 단순한 로직으로 충분했으나, 보스 몬스터의 다양한 패턴(돌진, 탄막, 소환 등)이 추가되면서 `Update` 함수가 수백 줄로 비대해짐.
> - **문제**
>   - **가독성 저하** : 다중 중첩된 조건문으로 인해 로직의 흐름을 한눈에 파악하기 어려움.
>   - **확장성 부족** : 새로운 공격 패턴 하나를 추가하려면 기존 코드를 뜯어고쳐야 해서 사이드 이펙트(Side Effect) 발생 위험이 큼.
>   - **디버깅 난해** : 버그 발생 시 특정 상태에서의 문제인지 판별하기 어려움.

**💡 해결 과정** [[📄CState.h]](https://github.com/vfly1189/TBI/blob/master/TBI/CState.h)

**"상태(State) 패턴 도입을 통한 FSM(Finite State Machine) 설계"**

- **상태의 클래스화** :
  - 몬스터의 행동을 `CState` 추상 클래스를 상속받는 독립적인 클래스(`IdleState`, `TraceState`, `AttackState` 등)로 분리하여 캡슐화했습니다.
- **FSM 구조 적용** :
  - `Monster` 클래스는 현재 상태(`m_pCurrentState`) 포인터만 유지하며, 매 프레임 해당 상태의 `Update()`를 호출하도록 위임(Delegation)했습니다.
  - 상태 전환(Transition) 로직을 각 상태 내부의 `Enter` / `Exit` 함수에 정의하여, 상태 변경 시의 초기화 및 정리 작업을 명확히 했습니다.
- **상속을 통한 확장** :
  - `TraceState`를 상속받아 `CFlyTraceState`(비행형 추적), `CGroundTraceState`(지상형 추적) 등으로 세분화하여 코드 재사용성을 극대화했습니다.

**✅ 결과**
- | 개선 항목 | If-Else 방식 (Before) | State 패턴 (After) |
  | :---: | :---: | :---: |
  | **코드 구조** | 하나의 거대한 `Update` 함수 | 기능별로 분리된 **작은 클래스들** |
  | **확장성** | 코드 수정 시 기존 로직 영향 큼 | **새 클래스 추가**만으로 패턴 확장 가능 (OCP 준수) |
  | **유지보수** | 특정 조건문 찾기 어려움 | 해당 상태 클래스만 확인하면 됨 |

**🛠️ 구조 변화 비교**
- | **Before (스파게티 코드)** | **After (깔끔한 구조)** |
  | :---: | :---: |
  | <img width="1197" height="922" alt="image" src="https://github.com/user-attachments/assets/4b7b7f5b-d2bc-4f88-b9e7-2571be42e00f" /> | <img width="873" height="282" alt="image" src="https://github.com/user-attachments/assets/b22c68c9-2914-4d24-b141-5c85cd96898d" />|
  | *중첩된 조건문으로 읽기 힘든 로직* | *간단해진 구조* |

---


