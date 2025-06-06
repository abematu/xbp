import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# 1. NewsAPIを使用して10年前の今日のニュースを取得
def get_news():
    # NewsAPIのAPIキー
    api_key = '08998da2d3314bd4ae78f2b02bab572b'  # ご自身のAPIキーを設定

    # 10年前の日付を計算
    date_10_years_ago = (datetime.now() - timedelta(days=365*10)).strftime('%Y-%m-%d')
    
    url = f'https://newsapi.org/v2/everything?q=*&from={date_10_years_ago}&to={date_10_years_ago}&apiKey={api_key}'
    
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'ok' and data['totalResults'] > 0:
        # ニュース情報の要約を作成
        articles = data['articles']
        news_summary = "10年前の今日に起こった出来事:\n\n"
        
        for article in articles[:5]:  # 最初の5つの記事を取り上げる
            title = article['title']
            description = article['description']
            url = article['url']
            news_summary += f"タイトル: {title}\n説明: {description}\n詳細: {url}\n\n"
        
        return news_summary
    else:
        return "10年前の今日に関連するニュースが見つかりませんでした。"

# 2. Outlookのメール送信
def send_email(subject, body, to_email):
    from_email = 'r202402099re@jindai.jp'  # Outlookのメールアドレス
    from_password = 'KFDWdC2MXS'  # Outlookのアカウントパスワード

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # OutlookのSMTPサーバー設定
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# 3. メイン処理
def main():
    # 10年前の今日のニュースを取得
    news_summary = get_news()

    # メールの件名と本文
    subject = "10年前の今日の出来事"
    body = news_summary
    
    # 送信先メールアドレス
    to_email = 'recipient_email@example.com'  # 受信者のメールアドレス
    
    # メール送信
    send_email(subject, body, to_email)
    print("メールが送信されました。")

if __name__ == '__main__':
    main()


