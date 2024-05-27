import streamlit as st
import random

# Sample list of names with duplicates
names = ['wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'wnnn',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'TONG',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'ATQT_Maple豆腐',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'Rengar',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'LIN',
 'Pin',
 'Pin',
 'Pin',
 'Pin',
 'Pin',
 'Pin',
 'Pin',
 'Pin',
 'Pin',
 'Pin',
 'Pin',
 'Pin',
 'Pin',
 'Bchu118',
 'Bchu118',
 'Bchu118',
 'Bchu118',
 'Bchu118',
 'Bchu118',
 'Bchu118',
 'Bchu118',
 'Bchu118',
 'Bchu118',
 'Bchu118',
 'Bchu118',
 'Zack',
 'Zack',
 'Zack',
 'Zack',
 'Zack',
 'Zack',
 'Zack',
 'Zack',
 'Zack',
 'Zack',
 'Zack',
 'Tl3o',
 'Tl3o',
 'Tl3o',
 'Tl3o',
 'Tl3o',
 'Tl3o',
 'Tl3o',
 'hins',
 'hins',
 'hins',
 'hins',
 'hins',
 'hins',
 'iam_kk',
 'iam_kk',
 'iam_kk',
 'iam_kk',
 'iam_kk',
 'iam_kk',
 'ATQT_主教',
 'ATQT_主教',
 'ATQT_主教',
 'ATQT_主教',
 'ATQT_主教',
 'ATQT_主教',
 '蛋蛋',
 '蛋蛋',
 '蛋蛋',
 '蛋蛋',
 '蛋蛋',
 '蛋蛋',
 'Luke Fan',
 'Luke Fan',
 'Luke Fan',
 'Luke Fan',
 'Luke Fan',
 'Peter',
 'Peter',
 'Peter',
 'Peter',
 'ATQT_ycJames',
 'ATQT_ycJames',
 'ATQT_ycJames',
 'ATQT_ycJames',
 'Reasonal',
 'Reasonal',
 'Reasonal',
 'Reasonal',
 'Adem#5858',
 'Adem#5858',
 'Adem#5858',
 'ian',
 'ian',
 'ian',
 'qaa4237',
 'qaa4237',
 'qaa4237',
 '無為無我',
 '無為無我',
 '無為無我',
 '冰冰',
 '冰冰',
 '冰冰',
 'NIEN',
 'NIEN',
 'NIEN',
 'ATQT_3r3h',
 'ATQT_3r3h',
 'hf',
 'hf',
 'rrryyy777',
 'rrryyy777',
 'Jason KD',
 'Junior',
 'Lin9',
 'SNOW CHEN',
 'bx_0822',
 '酪梨胖胖',
 'Arles',
 '鶇',
 'ATQT_Dylan',
 '冰冰',
 'yen']

# 初始化 session 狀態中的名單和獎項，如果還未初始化
if 'names' not in st.session_state:
    st.session_state.names = names.copy()
    random.shuffle(st.session_state.names)
    st.session_state.winners = []
    st.session_state.show_winners = False

# 獎項設定
prizes = [
    ("10獎", 30),
    ("9獎", 30),
    ("8獎", 30),
    ("7獎", 30),
    ("6獎", 30),
    ("5獎", 30),
    ("4獎", 60),
    ("3獎", 100),
    ("2獎", 150),
    ("頭獎", 200),
]

def draw_lottery():
    if st.session_state.names:
        prize = prizes[len(st.session_state.winners)]
        winner = st.session_state.names.pop()
        st.session_state.winners.append((winner, prize[0], prize[1]))
        st.write(f"恭喜 {winner} 抽中了{prize[0]}，獎金為 {prize[1]} U！")
    else:
        st.write("抽獎名單中已無剩餘人名！")

st.title("ATQT合約大賽抽獎")

st.write("點擊下方按鈕抽取幸運兒。")

if st.button("抽獎"):
    if len(st.session_state.winners) < 10:
        draw_lottery()
    else:
        st.write("所有獎項已抽完。")

# # 顯示剩餘名單
# if st.session_state.names:
#     st.write(f"剩餘名單：{st.session_state.names}")
# else:
#     st.write("所有人名已抽完。")

# 顯示所有獎項得獎者
# 添加按鈕顯示所有獎項得獎者
if len(st.session_state.winners) == 10:
    if st.button("顯示所有得獎者"):
        st.session_state.show_winners = True

# 顯示所有獎項得獎者
if st.session_state.show_winners:
    st.write("所有獎項的得獎者如下：")
    for winner, prize_name, prize_amount in st.session_state.winners:
        st.write(f"{prize_name} - {winner}，獎金：{prize_amount} U")