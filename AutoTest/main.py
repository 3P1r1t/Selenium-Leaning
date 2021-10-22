import qjbl
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
from selenium.webdriver.common.by import By
import cv2
import time
def get_code():
    driver.save_screenshot("full_snap.png")
    left = r_image.location['x']
    top = r_image.location['y']
    right = r_image.location['x'] + r_image.size['width']
    bottom = r_image.location['y'] + r_image.size['height']
    im = Image.open("full_snap.png")
    img = im.crop((left,top,right,bottom))
    img.save("icode.png")

def imgtostring():
    while True:
        cv2.destroyAllWindows()
        ocr = PaddleOCR(use_angle_cls=True, lang="en")
        img_path = './icode.png'
        result = ocr.ocr(img_path, cls=True)
        if result==[]:
            hyz.click()
            get_code()
            continue
        for line in result:
            print(line)
        from PIL import Image
        image = Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
        im_show = Image.fromarray(im_show)
        im_show.save('result.jpg')
        qjbl.code = txts[0]
        qjbl.value= scores[0]
        break

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://221.2.52.44:82/")
    while True:
        username = driver.find_element(By.NAME, "TextBox1")
        pwd = driver.find_element(By.NAME, "TextBox2")
        yzm = driver.find_element(By.NAME, "TextBox3")
        r_image = driver.find_element(By.ID, "icode")
        login = driver.find_element(By.ID, "Button1")
        hyz = driver.find_element(By.XPATH, "/html/body/form/div/div[3]/dl/dd[3]/a")
        time.sleep(1)
        get_code()
        time.sleep(1)
        imgtostring()
        print(qjbl.value,qjbl.code)
        if qjbl.value<0.5 or len(qjbl.code)!=4:
            hyz.click()
            time.sleep(1)
            continue
        else:
            username.clear()
            username.send_keys("2020145335")
            pwd.send_keys("871540656")
            yzm.send_keys(qjbl.code)
            login.click()
            time.sleep(1)
            result = EC.alert_is_present()(driver)
            if result:
                result.accept()
            else:
                print("登录成功")
                break









'''
if len(a[0])==4 and a[1]>=0.2:
    username.send_keys("2020145335")
    pwd.send_keys("871540656")
    yzm.send_keys(a[1])
    login.click()
else:
    driver.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)
    '''




