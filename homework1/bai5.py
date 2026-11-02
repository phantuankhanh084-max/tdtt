a=input("nhap ki tu in hoa:")
if 'B' <= a <= 'Z':
    b=chr(ord(a.lower())-1)
    print("chu cai thuong lien truoc la:",b)
else:
    print(a,"la truong hop dac biet")
