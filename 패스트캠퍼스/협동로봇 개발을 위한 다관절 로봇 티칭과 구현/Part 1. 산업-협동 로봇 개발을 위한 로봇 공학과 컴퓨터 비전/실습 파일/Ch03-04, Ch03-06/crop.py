import cv2
import os

# 이미지 경로 설정
image_path = 'resource/plane.jpg'

# 이미지 로드
image = cv2.imread(image_path)

# 크롭할 영역 정의 (좌측 상단 (x, y), 우측 하단 (x2, y2) 좌표)
x, y, w, h = 600, 400, 300, 300  # 예시로 (100, 100) 위치부터 가로 300px, 세로 300px 영역을 크롭

# 이미지 크롭
cropped_image = image[y:y+h, x:x+w]

# 'result' 폴더가 없다면 생성
result_folder = 'result'
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

# 파일 이름 설정 (소스 파일명과 동일)
file_name = os.path.basename(image_path)

# 확장자를 제외한 파일 이름과 'result' 폴더 경로를 합쳐서 저장 경로 생성
result_image_path = os.path.join(result_folder, f'cropped_{file_name}')

# 크롭된 이미지 저장
cv2.imwrite(result_image_path, cropped_image)

# 원본 이미지와 크롭된 이미지 나란히 표시
cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)

# 사용자가 아무 키나 눌러 창을 닫을 때까지 대기
cv2.waitKey(0)

# 창 닫기
cv2.destroyAllWindows()

# 저장된 이미지 경로 출력
print(f"Cropped image saved to: {result_image_path}")
