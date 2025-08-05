import cv2
import os

# 이미지 경로 설정
image_path = 'resource/plane.jpg'
template_path = 'resource/template2.jpg'

# 이미지 로드
image = cv2.imread(image_path)
template = cv2.imread(template_path)

# 템플릿 이미지 크기
template_height, template_width = template.shape[:2]

# 템플릿 매칭
result = cv2.matchTemplate(image, template, cv2.TM_SQDIFF_NORMED)

# 결과 매칭 위치 찾기
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 템플릿이 일치하는 위치
top_left = max_loc
bottom_right = (top_left[0] + template_width, top_left[1] + template_height)

# 결과 이미지에 템플릿 영역을 사각형으로 표시
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# 'result' 폴더가 없다면 생성
result_folder = 'result'
if not os.path.exists(result_folder):
    os.makedirs(result_folder)

# 결과 이미지 저장 경로 설정
template_matching_result_path = os.path.join(result_folder, 'template_matching_result.jpg')

# 결과 이미지 저장
cv2.imwrite(template_matching_result_path, image)

# 원본 이미지와 템플릿 매칭된 이미지를 각각 다른 창에 표시
cv2.imshow('Original Image', image)
cv2.imshow('Template Image', template)

# 사용자가 아무 키나 눌러 창을 닫을 때까지 대기
cv2.waitKey(0)

# 창 닫기
cv2.destroyAllWindows()

# 저장된 이미지 경로 출력
print(f"Template matching result image saved to: {template_matching_result_path}")
