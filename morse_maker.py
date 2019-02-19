def mkstr(text):
	wav_header="52 49 46 46 A3 BB 00 00 57 41 56 45 66 6D 74 20 10 00 00 00 01 00 01 00 40 1F 00 00 40 1F 00 00 01 00 08 00 64 61 74 61 7F BB 00 00"
	wav_header=wav_header.replace(" ","")
	dot="27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 27 01 27 80 D9 FF D9 80 "
	dot=dot.replace(" ","")
	blank="80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 80 "
	blank=blank.replace(" ","")
	long_dot=dot+dot+dot
	long_blank=blank+blank+blank
	morse_signal=''

	A=dot+blank+long_dot
	B=long_dot+blank+dot+blank+dot+blank+dot
	C=long_dot+blank+dot+blank+long_dot+blank+dot
	D=long_dot+blank+dot+blank+dot
	E=dot
	F=dot+blank+dot+blank+long_dot+blank+dot
	G=long_dot+blank+long_dot+blank+dot
	H=dot+blank+dot+blank+dot+blank+dot
	I=dot+blank+dot
	J=dot+blank+long_dot+blank+long_dot+blank+long_dot
	K=long_dot+blank+dot+blank+long_dot
	L=dot+blank+long_dot+blank+dot+blank+dot
	M=long_dot+blank+long_dot
	N=long_dot+blank+dot
	O=long_dot+blank+long_dot+blank+long_dot
	P=dot+blank+long_dot+blank+long_dot+blank+dot
	Q=long_dot+blank+long_dot+blank+dot+blank+long_dot
	R=dot+blank+long_dot+blank+dot
	S=dot+blank+dot+blank+dot
	T=long_dot
	U=dot+blank+dot+blank+long_dot
	V=dot+blank+dot+blank+dot+blank+long_dot
	W=dot+blank+long_dot+blank+long_dot
	X=long_dot+blank+dot+blank+dot+blank+long_dot
	Y=long_dot+blank+dot+blank+long_dot+blank+long_dot
	Z=long_dot+blank+long_dot+blank+dot+blank+dot
	one=dot+blank+long_dot+blank+long_dot+blank+long_dot+blank+long_dot
	two=dot+blank+dot+blank+long_dot+blank+long_dot+blank+long_dot
	three=dot+blank+dot+blank+dot+blank+long_dot+blank+long_dot
	four=dot+blank+dot+blank+dot+blank+dot+blank+long_dot
	five=dot+blank+dot+blank+dot+blank+dot+blank+dot
	six=long_dot+blank+dot+blank+dot+blank+dot+blank+dot
	seven=long_dot+blank+long_dot+blank+dot+blank+dot+blank+dot
	eight=long_dot+blank+long_dot+blank+long_dot+blank+dot+blank+dot
	nine=long_dot+blank+long_dot+blank+long_dot+blank+long_dot+blank+dot
	zero=long_dot+blank+long_dot+blank+long_dot+blank+long_dot+blank+long_dot

	morse_full='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	morse_list=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,one,two,three,four,five,six,seven,eight,nine,zero]
	for i in text:
		idx=morse_full.find(i)
		if idx==-1:
			print("대문자 및 숫자만 입력 가능합니다.")
		else:
			morse_signal+=morse_list[idx]+long_blank

	hexstring=wav_header+morse_signal

	return hexstring


import binascii
text=input("모스부호로 변환할 문자열을 입력하세요(only ENG) : ")
hexstring=mkstr(text)

morse_byte=''
morse_byte=binascii.unhexlify(hexstring)

f = open("result.wav","wb")
f.write(morse_byte)
f.close()
