import tkinter as tk

def on_button_click(value):
    # 現在のエントリーテキストを取得
    current_text = entry.get()
    # エントリーをクリアして新しい値を挿入
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def clear_entry():
    # エントリーをクリア
    entry.delete(0, tk.END)

def calculate_result():
    try:
        # エントリーテキストから式を取得し計算
        expression = entry.get()
        result = eval(expression)
        # 計算結果を表示
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        # エラーが発生した場合は"Error"を表示
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# ウィンドウの作成
window = tk.Tk()
window.title("Simple Calculator")

# エントリー
entry = tk.Entry(window, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# ボタン配置
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

# ボタンの配置とイベントハンドラの設定
for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda b=button: on_button_click(b) if b != '=' else calculate_result()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# クリアボタン
tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 14), command=clear_entry).grid(row=row_val, column=col_val)

# ウィンドウのループ
window.mainloop()
