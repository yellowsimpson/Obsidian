import cv2
import os

# 이미지 경로 설정
image_path = 'resource/plane.jpg'

# 이미지 로드
image = cv2.imread(image_path)

# 그레이스케일 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 'result' 폴더가 없다면 생성
result_folder = 'result'
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

# 파일 이름 설정 (소스 파일명과 동일)
file_name = os.path.basename(image_path)

# 확장자를 제외한 파일 이름과 'result' 폴더 경로를 합쳐서 저장 경로 생성
result_image_path = os.path.join(result_folder, f'grayscale_{file_name}')

# 그레이스케일 이미지 저장
cv2.imwrite(result_image_path, gray_image)

# 원본 이미지와 그레이스케일 이미지 나란히 표시
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)

# 사용자가 아무 키나 눌러 창을 닫을 때까지 대기
cv2.waitKey(0)

# 창 닫기
cv2.destroyAllWindows()

# 저장된 이미지 경로 출력
print(f"Grayscale image saved to: {result_image_path}")
