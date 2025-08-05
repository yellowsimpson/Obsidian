import cv2
import os

# 이미지 경로 설정
image_path = 'resource/plane.jpg'

# 이미지 로드
image = cv2.imread(image_path)

# 가우시안 블러링 (Gaussian Blurring)
gaussian_blur_image = cv2.GaussianBlur(image, (5, 5), 0)

# 미디언 필터링 (Median Filtering)
median_blur_image = cv2.medianBlur(image, 5)

# 'result' 폴더가 없다면 생성
result_folder = 'result'
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

# 파일 이름 설정 (소스 파일명과 동일)
file_name = os.path.basename(image_path)

# 결과 이미지 저장 경로 설정
gaussian_result_path = os.path.join(result_folder, f'gaussian_blur_{file_name}')
median_result_path = os.path.join(result_folder, f'median_blur_{file_name}')

# 이미지 저장
cv2.imwrite(gaussian_result_path, gaussian_blur_image)
cv2.imwrite(median_result_path, median_blur_image)

# 원본 이미지와 노이즈 저감 이미지 나란히 표시
cv2.imshow('Original Image', image)
cv2.imshow('Gaussian Blur', gaussian_blur_image)
cv2.imshow('Median Blur', median_blur_image)

# 사용자가 아무 키나 눌러 창을 닫을 때까지 대기
cv2.waitKey(0)

# 창 닫기
cv2.destroyAllWindows()

# 저장된 이미지 경로 출력
print(f"Gaussian Blur image saved to: {gaussian_result_path}")
print(f"Median Blur image saved to: {median_result_path}")
