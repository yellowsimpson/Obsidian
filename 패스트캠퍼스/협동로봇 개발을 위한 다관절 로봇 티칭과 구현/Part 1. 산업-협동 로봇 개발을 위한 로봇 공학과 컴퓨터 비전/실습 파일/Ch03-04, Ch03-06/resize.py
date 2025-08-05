import cv2
import os

# 이미지 경로 설정
image_path = 'resource/plane.jpg'

# 이미지 로드
image = cv2.imread(image_path)

# 이미지 크기 변경 (50%로 조정)
resized_image = cv2.resize(image, (int(image.shape[1] * 0.3), int(image.shape[0] * 0.2)))

# 'result' 폴더가 없다면 생성
result_folder = 'result'
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

# 파일 이름 설정 (소스 파일명과 동일)
file_name = os.path.basename(image_path)

# 확장자를 제외한 파일 이름과 'result' 폴더 경로를 합쳐서 저장 경로 생성
result_image_path = os.path.join(result_folder, f'resized_{file_name}')

# 결과 이미지 저장
cv2.imwrite(result_image_path, resized_image)

# 각 이미지를 다른 창에 표시
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)

# 사용자가 아무 키나 눌러 창을 닫을 때까지 대기
cv2.waitKey(0)

# 창 닫기
cv2.destroyAllWindows()

# 저장된 이미지 경로 출력
print(f"Resized image saved to: {result_image_path}")
