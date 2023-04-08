import ddddocr
import requests
 

code_url="http://3xacg.com/wp-content/themes/modown/action/captcha2.php?0.39235232426298094"
r=requests.get(url=code_url,timeout=5)
with open('code.png','wb')as f:
    f.write(r.content)
    print("下载验证码成功！")
 
ocr = ddddocr.DdddOcr()
 
#with open(r'C:\Users\Administrator\Desktop\验证码识别\code.png', 'rb') as f:
    #img_bytes = f.read()
img_bytes=r.content
 
res = ocr.classification(img_bytes)
 
print(res)

