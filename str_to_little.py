import binascii

def bytes_to_custom_format(byte_data):
    # 바이트 배열을 리틀 엔디언 형식의 16진수(hex) 문자열로 변환하고 접두사 '0x'를 추가
    hex_string = '0x' + binascii.hexlify(byte_data[::-1]).decode('utf-8')
    return hex_string

# 예시: '/tmp/flag' 문자열을 바이트로 변환하여 원하는 형식으로 출력
data = input("Enter data: ")  # 사용자로부터 입력 받기

# 입력받은 문자열을 UTF-8로 인코딩하여 바이트로 변환
byte_data = data.encode('utf-8')

result = bytes_to_custom_format(byte_data)
print(result)
