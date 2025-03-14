print("Hello Mars")

# with > close 사용하지 않아도 됨
with open('mission_computer_main.log', encoding="UTF8") as data :
	# read함수는 전체 내용 전체를 문자열로 불러온다.
	contents = data.read()
	print(contents)