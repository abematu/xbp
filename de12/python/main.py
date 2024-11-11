            import random

# じゃんけんの手のリスト
rock_paper_scissors = [‘グー’, ‘チョキ’, ‘パー’]

# ゲーム開始のメッセージ
print(‘じゃんけんしましょう’)
print(‘番号を入力してね’)
print(‘1番・グー　2番・チョキ　3番・パー’)

# ユーザーの手の入力
number = input(‘あなたの手は？ ‘)

# ユーザーの手の判定
if number == ‘1’:
user = ‘グー’
elif number == ‘2’:
user = ‘チョキ’
elif number == ‘3’:
user = ‘パー’

# コンピューターの手の選択
cpu = random.choice(rock_paper_scissors)

# ユーザーとコンピューターの手を表示
print(f’あなたは{user}。向こうは{cpu}。’)

# 勝敗の判定と結果の表示
if user == ‘グー’:
if cpu == ‘グー’:
print(‘あいこ！’)
elif cpu == ‘チョキ’:
print(‘あなたの勝ち！’)
elif cpu == ‘パー’:
print(‘あなたの負け！’)
# 他の手の組み合わせも同様に判定できます

                                                                              

