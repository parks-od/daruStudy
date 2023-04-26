import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail

# 메인 처리 --
def send_test_gmail():
    # 메일 데이터(MIME) 작성 --
    msg = make_mime_text(
        mail_to = gmail.account,
        subject = '메일 송신 테스트',
        body = '안녕하세요, 테스트 메일입니다.')
    # 메일 보내기
    send_gmail(msg)
# 메일 데이터(MIME) 생성 --
def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['To'] = mail_to
    msg['From'] = gmail.account
    return msg

# Gmail 보내기
def send_gmail(msg):
    # Gmail 서버에 접속
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # 해당 smtp 메일 서버에 Hello 메시지 전송 하여 통신 연결
    server.starttls() # 포트 587 TSL의 경우 smtp연결을 tls모드로 설정
    server.ehlo()
    # 로그 출력
    server.set_debuglevel(0)
    server.login(gmail.account, gmail.password)
    server.send_message(msg) # 리스트 형식으로 입력해도 받음
    server.quit()

if __name__ == '__main__': # 다른 라이브러리에서 실행되지 않고 인터프리터에서 직접 실행됬을때 실행되게 함
    send_test_gmail()
    print('ok..')