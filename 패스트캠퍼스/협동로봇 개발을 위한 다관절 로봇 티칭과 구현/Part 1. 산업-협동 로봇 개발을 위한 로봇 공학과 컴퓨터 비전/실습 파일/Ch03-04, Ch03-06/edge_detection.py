import cv2
import os

# 이미지 경로 설정
image_path = 'resource/plane.jpg'

# 이미지 로드
image = cv2.imread(image_path)

# 그레이스케일로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny 엣지 검출
edges = cv2.Canny(gray_image, 100, 300)  # 100과 200은 낮은/높은 임계값

# 'result' 폴더가 없다면 생성
result_folder = 'result'
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

# 파일 이름 설정 (소스 파일명과 동일)
file_name = os.path.basename(image_path)

# 결과 이미지 저장 경로 설정
edges_result_path = os.path.join(result_folder, f'edges_{file_name}')

# 엣지 이미지 저장
cv2.imwrite(edges_result_path, edges)

# 원본 이미지와 엣지 검출된 이미지 나란히 표시
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection (Canny)', edges)

# 사용자가 아무 키나 눌러 창을 닫을 때까지 대기
cv2.waitKey(0)

# 창 닫기
cv2.destroyAllWindows()

# 저장된 이미지 경로 출력
print(f"Edge detection image saved to: {edges_result_path}")
