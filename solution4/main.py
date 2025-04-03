import math

data = {
    "재질": "",
    "지름": 0,
    "두께": 1,
    "면적": 0.0,
    "무게": 0.0
}

metarial = {
    "유리": 2.4,
    "알루미늄": 2.7,
    "탄소강": 7.85
}

GRAVITY_FACTOR = 0.376

def sphere_area(diameter, material="유리", thickness=1):
    radius = diameter / 2
    area = 2 * math.pi * (radius ** 2)
    if material in metarial:
        volume = area * (thickness / 100)
        weight = volume * metarial[material] * 1000
        weight /= 1000
        weight *= GRAVITY_FACTOR
    else:
        print("잘못된 재질입니다. '유리', '알루미늄', '탄소강' 중 선택하세요.")
        return None, None
    
    return round(area, 3), round(weight, 3)

while True:
    try:
        # 사용자 입력 받기
        diameter = float(input("돔의 지름을 입력하세요(m) : "))
        if diameter == 0:
            print("프로그램을 종료합니다.")
            break
        if diameter < 0:
            print("지름은 0보다 커야 합니다.")
            continue
        
        material = input("재질을 선택하세요 (유리, 알루미늄, 탄소강): ")
        if material not in metarial:
            print("잘못된 재질입니다. 다시 입력하세요.")
            continue
        
        thickness = input("두께를 입력하세요(cm): ")
        thickness = float(thickness) if thickness.strip() else 1
        if thickness <= 0:
            print("두께는 0보다 커야 합니다.")
            continue
        
        # 계산 수행
        area, weight = sphere_area(diameter, material, thickness)
        if area is None:
            continue
        
        # 전역 변수 업데이트
        data["재질"] = material
        data["지름"] = diameter
        data["두께"] = thickness
        data["면적"] = area
        data["무게"] = weight
        
        # 결과 출력
        print(f"재질 ⇒ {data['재질']}, 지름 ⇒ {data['지름']}m, 두께 ⇒ {data['두께']}cm, 면적 ⇒ {data['면적']}m², 무게 ⇒ {data['무게']}kg")
    
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력하세요.")
