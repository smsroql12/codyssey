import os

# 로그 파일 읽기
lists = []
with open("mission_computer_main.log", "r") as file:
    for line in file:
        timestamp, event, message = line.strip().split(",", 2)
        lists.append({"timestamp": timestamp, "event": event, "message": message})

# 시간의 역순으로 정렬
lists.sort(key=lambda x: x["timestamp"], reverse=True)

print(lists)

# 사전 객체로 변환
data_dict = {"logs": lists}

def search_logs(keyword):
    # 입력한 키워드로 로그를 검색하여 결과 출력
    result = [log for log in data_dict if isinstance(log, dict) and 'message' in log and keyword.lower() in log['message'].lower()]
    
    # 결과 출력
    if result:
        for log in result:
            print(f"Timestamp: {log['timestamp']}, Event: {log['event']}, Message: {log['message']}")
    else:
        print("검색 결과 없음.")

# 사용자로부터 검색할 키워드 입력 받기
keyword = input("검색어 입력 : ")
search_logs(keyword)

# JSON 형식으로 문자열 생성
def dict_to_json_string(d):
    def value_to_json(val):
        if isinstance(val, str):
            return f'"{val}"'
        elif isinstance(val, bool):
            return "true" if val else "false"
        elif val is None:
            return "null"
        elif isinstance(val, (int, float)):
            return str(val)
        elif isinstance(val, dict):
            return dict_to_json_string(val)
        elif isinstance(val, list):
            return f'[{", ".join(value_to_json(v) for v in val)}]'
    
    items = [f'"{key}": {value_to_json(value)}' for key, value in d.items()]
    return "{" + ", ".join(items) + "}"

# JSON 문자열로 변환
json_data = dict_to_json_string(data_dict)

# JSON 파일로 저장
with open("mission_computer_main.json", "w") as json_file:
    json_file.write(json_data)
