import cv2
import os

# 이미지 경로 설정
image_path = 'resource/plane.jpg'

# 이미지 로드
image = cv2.imread(image_path)

# 이미지의 중심을 기준으로 45도 회전
center = (image.shape[1] // 2, image.shape[0] // 2)  # 이미지의 중심 좌표
rotation_matrix = cv2.getRotationMatrix2D(center, -30, 0.5)  # 회전 행렬 생성 (45도, 1배 크기 유지)
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))  # 이미지 회전

# 'result' 폴더가 없다면 생성
result_folder = 'result'
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

# 파일 이름 설정 (소스 파일명과 동일)
file_name = os.path.basename(image_path)

# 확장자를 제외한 파일 이름과 'result' 폴더 경로를 합쳐서 저장 경로 생성
result_image_path = os.path.join(result_folder, f'rotated_{file_name}')

# 결과 이미지 저장
cv2.imwrite(result_image_path, rotated_image)

# 각 이미지를 다른 창에 표시
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)

# 사용자가 아무 키나 눌러 창을 닫을 때까지 대기
cv2.waitKey(0)

# 창 닫기
cv2.destroyAllWindows()

# 저장된 이미지 경로 출력
print(f"Rotated image saved to: {result_image_path}")
