import binascii

def custom_format_to_bytes(hex_string):
    # '0x' 접두사 제거 후 문자열을 바이트로 변환
    byte_data = bytes.fromhex(hex_string[2:])[::-1]
    return byte_data

# 사용자로부터 입력 받기
hex_string = input("Enter little-endian hex string (e.g., 0x67616c662f706d742f): ")

# 입력받은 리틀 엔디언 형식의 16진수(hex) 문자열을 바이트로 변환하여 원래 문자열로 디코딩
try:
    byte_data = custom_format_to_bytes(hex_string)
    original_string = byte_data.decode('utf-8')
    print("Original string:", original_string)
except (ValueError, binascii.Error) as e:
    print("Error:", e)
