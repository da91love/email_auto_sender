import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# 보내는 사람 정보
me = "보내는 사람 이메일아이디@gmail.com"
my_password = "비밀번호"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보 리스트로 작성
emails = ['yunju0514@naver.com', 'yunju0514@gmail.com']
# 여러 사람에게 보낼 for 반복문 작성
for you in emails:
    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "[공유]오늘의 주식 기사"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "따끈따끈 오늘자 기사가 도착했어요! '주식' 공부의 첫 걸음은 경제 기사 읽기부터! 오늘도 화이팅!"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 파일 첨부하기
    part = MIMEBase('application', "octet-stream")
    with open("네이버 기사 스크래핑.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="주식기사.xlsx")
    msg.attach(part)


    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())
s.quit()