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
|:---:|:---|
| 🎯 **장르** | 쿼터뷰, 배틀로얄, MOBA |
| ⏱️ **개발 기간** | 2개월 |
| 👥 **개발 인원** | 2인 (프로그래머로 참여) |
| 🛠️ **개발 환경** | C++, DirectX11, FMOD |
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

**Hybrid 렌더링 파이프라인 구축 (Deferred + Forward)**  
- 불투명(Geometry)은 **Deferred Rendering**으로 처리하여 다중 광원 환경에서 성능을 확보  
- 투명/반투명(예: UI, 알파 블렌딩 오브젝트)은 **Forward Rendering**으로 별도 처리하여 블렌딩 문제 해결  
- 결과적으로 **불투명은 MRT 기반 G-Buffer**, **투명은 Forward Pass**로 렌더링하는 Hybrid 구조로 구성 [file:44]

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


</details>

<br>
<hr>
<br>


<details open>
<summary><h3>🎭 인스턴싱 기반 렌더링</h3></summary>

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

<br>
<hr>
<br>

<details open>
<summary><h3>🌑 쿼드 트리</h3></summary>

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

**쿼드트리 기반 충돌 처리**
- AABB(Axis-Aligned Bounding Box) 충돌 검사 [[📄AABB 충돌 검사]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L421-L492)
- Sphere Collider 구현 [[📄Sphere Collider 충돌 검사]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/QuadTree.cpp#L494-L580)
- 계층적 충돌 그룹 관리

</details>

<br>
<hr>
<br>

<details open>
<summary><h3>🧭 NavMesh 기반 길찾기 시스템</h3></summary>

<br>

**3D 공간 길찾기 구현**
- NavMesh 구축
  - 맵 데이터를 로드하여 다각형(Triangle) 그래프로 구성된 네비게이션 메쉬 구축
- A* 알고리즘
  - 출발지와 목적지가 속한 삼각형을 찾아 최단 경로(Triangle Path)를 산출하고, String Pulling(경로 단축) 기법을 적용하여, 지그재그 형태의 A* 경로를 **직선화(Smoothing)** 하고 자연스러운 이동 구현
  - ![NavMesh](https://github.com/user-attachments/assets/5c0fb898-07a2-4029-986e-475e1bb2e61a)
- NavMeshAgent
  - 상태 패턴(Idle, Moving)을 적용하여 이동 로직 분리
  - 매 프레임 UpdateMovement에서 GetNearestPointOnNavMesh를 호출
  - Spatial Grid로 최적화된 검색을 통해 캐릭터를 NavMesh 표면 위로 투영하고 이동 경로 보정


</details> 

<br>
<hr>
<br>

<details open>
<summary><h3>🎬 애니메이션 시스템</h3></summary>

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

<br>

<div align="right">
  <a href="#table-of-contents">⬆️ 목차로 돌아가기</a>
</div>

---

## 🛠️ 문제 해결

### 1️⃣ Forward에서 Deferred Rendering으로 전환

> **🚨 문제 상황**
> 
> 다수의 동적 광원 사용 시 Forward Rendering 방식에서 성능 저하 발생 (광원 수 × 오브젝트 수의 연산)

**💡 해결 과정**
- Deferred Rendering 파이프라인 설계 및 구현 [[📄Deferred Rendering 구현]](https://github.com/HyangRim/DirectX11-Engine-Client/blob/d0b9114a5d95640c568cfa5f0bffa8fb9e8c036b/Engine/RenderManager.cpp#L75-L113)
- G-Buffer 4개 생성 (Albedo, Normal, Position, Material)
  - ![디퍼드렌더링](https://github.com/user-attachments/assets/16f34e58-f14a-44b4-ac76-c26db09755ca)
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

### 2️⃣ NavMesh 검색 속도 최적화 (Spatial Grid)

> **🚨 문제 상황**
> 
> 캐릭터가 이동할 때마다 지형의 높낮이를 반영하고 경로 이탈을 방지하기 위해 현재 위치가 "어떤 삼각형 위에 있는지" 판별해야 합니다.
> 
> 맵이 넓어 NavMesh의 삼각형 개수가 수천 개로 늘어나자, 매 프레임 GetNearestPointOnNavMesh에서 전체 삼각형을 순회(Linear Search, O(N))하는 방식이 심각한 CPU 병목을 유발했습니다.

**💡 해결 과정**​

- 공간 해싱(Spatial Grid) 도입
  - 맵 전체를 일정 크기(CellSize: 25.0f)의 그리드로 분할
  - unordered_map<uint64, vector<int>>를 사용하여 각 그리드 셀에 포함된 삼각형 인덱스를 미리 매핑 (InitializeSpatialGrid)
  - <img width="1122" height="357" alt="image" src="https://github.com/user-attachments/assets/a3135a41-b5e9-46ca-b498-18f5b455663d" />
- 검색 로직 최적화
  - GetNearestPointOnNavMesh 호출 시, 캐릭터의 월드 좌표를 그리드 키(Key)로 변환
  - 전체 삼각형을 뒤지는 대신, 해당 셀에 속한 소수의 삼각형만 검사하도록 변경하여 연산량 최소화
  - m_lastFoundTriangle 변수를 통한 캐싱으로 연속적인 프레임에서의 검색 비용 추가 절감

**✅ 결과**
- 삼각형 검색 복잡도를 O(N) → O(1) (평균) 수준으로 단축
- 다수의 NPC가 동시에 길찾기와 이동 보정을 수행해도 프레임 저하 없는 안정적인 퍼포먼스 확보
- | case 1 | case 2 |
    | :---: | :---: |
    | <img width="360" height="149" alt="image" src="https://github.com/user-attachments/assets/43d4a9ba-5cbd-43da-bc92-ab82ded95206" /> | <img width="355" height="140" alt="image" src="https://github.com/user-attachments/assets/efd1d8ff-4feb-42f0-aa3f-bbb6bb7b4d56" /> |

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
- 객체 500개에서의 성능비교
  - <img width="1048" height="656" alt="객체 500개 성능비교" src="https://github.com/user-attachments/assets/956a6342-f9a2-494a-b33a-128847239bc0" />

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

Brotato는 로그라이크 요소가 결합된 탑다운 슈팅 게임으로, 플레이어는 감자 캐릭터를 조작하여 웨이브 방식으로 몰려오는 적들을 물리치며 생존하는 것이 목표입니다. 각 웨이브 사이 상점에서 무기와 아이템을 구매하여 캐릭터를 강화하고, 다양한 빌드 조합을 통해 전략적인 플레이가 가능합니다.

## 📌 학습 목표 및 내용

**게임 엔진의 기본 아키텍처와 렌더링 파이프라인 학습**

1. GDI+ → Direct2D 전환으로 FPS를 20~40 → 60+로 개선
2. 타일맵 렌더링을 1,296회 DrawCall에서 1회로 최적화.

이 과정에서 게임 엔진의 기본 아키텍처 설계와 성능 최적화의 중요성을 깨닫게 되었습니다.

<br>

---

## 🔨 주요 개발

<details open>
<summary><b>🏗️ 아키텍처 설계</b></summary>

<br>

**Manager-Scene-Object 3계층 구조** 기반 엔진 설계 (싱글톤 패턴)
- CCore를 중심으로 10개 Manager (Time, Key, Camera, Scene 등)를 싱글톤으로 초기화
  [[📄매니저 초기화]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCore.cpp#L88-L100) 
- 메인 루프에서 매 프레임 각 Manager의 update()를 순차 호출하여 게임 로직 처리
  [[📄프레임 처리 흐름]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CCore.cpp#L106-L173) 
- Scene 추상 클래스 기반 상속으로 Main/Shop/Run_End 등 6개 씬 제작 및 관리
  [[📄씬 구조]](https://github.com/HyangRim/BrotatoClone/blob/master/Client/CSceneMgr.cpp) 
- 각 씬 내 GROUP_TYPE별로 객체들을 벡터로 관리하고 update/finalupdate/render 순서 보장

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

</details>

<details open>
<summary><b>🏗️ 아키텍처 및 이벤트 시스템</b></summary>

<br>

**지연 처리(Delayed Processing) 기반 이벤트 시스템**
- 이벤트 큐(vector): 게임 로직 도중 발생하는 객체 생성/삭제, 씬 전환 요청을 즉시 수행하지 않고 순차적으로 큐에 저장하여 프레임 동기화 유지
  - [[📄이벤트 처리]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/CEventMgr.cpp#L44-L92)
- 일괄 처리(Execute): 모든 로직 업데이트가 끝난 후 이벤트를 일괄 실행. 특히 객체 삭제 요청은 **중복 방지 컨테이너(unordered_set)** 를 통해 안전하게 처리
- 생명주기 관리: 전역 함수(Create/DeleteObject)를 제공하여 어디서든 안전하게 객체 생명주기 제어
  - [[📄이벤트 등록]](https://github.com/HyangRim/BrotatoClone/blob/7c887b61fc9d09e10d9a9f0866541d067a76d7e2/Client/func.cpp#L7-L43)

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

</details>

<details open>
<summary><b>🖼️ UI 및 사운드 시스템</b></summary>

<br>

- 계층적 UI 컴포넌트 (Panel, Button, Slider, Text)와 콜백 기반 이벤트 처리
- FMOD 기반 멀티채널 오디오 (BGM/SFX 분리 관리)

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
| ![몬스터 많을때 플레이-1](https://github.com/user-attachments/assets/276c08d4-d76a-4fa5-a3a7-a5933ff0b6d1) | ![몬스터 많을때 플레이-2](https://github.com/user-attachments/assets/09890ffb-9d42-46b5-814c-603897c64c91) |

<br><br>

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
| ![타일최적화(Before)](https://github.com/user-attachments/assets/b5534d3c-3910-4649-914d-8c13902e7670) | ![타일최적화(After)](https://github.com/user-attachments/assets/08e592ca-8a7e-4ad2-9cb7-264ab596d6be) |
| **DrawCall: 1,296회 / FPS: ~650** | **DrawCall: 1회 / FPS: ~1,400** |

<br>
<br>

### 3️⃣ 이벤트 처리 시 중복 삭제로 인한 메모리 오염 방지
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


