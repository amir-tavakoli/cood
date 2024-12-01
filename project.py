from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import sqlite3

import time as t  # اضافه کردن ماژول time

# ایجاد یا اتصال به دیتابیس
conn = sqlite3.connect('pedal.db')
cursor = conn.cursor()
total_elapsed_time = 0  # ذخیره زمان سپری شده
running = False
# ایجاد جدول کاربران
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    national_code TEXT UNIQUE,
    username TEXT UNIQUE,
    password TEXT,
    bicycle_size TEXT,
    wallet REAL DEFAULT 0,
    time_used REAL DEFAULT 0
)
''')
conn.commit()

# وضعیت حالت دارک مود
is_dark_mode = False

def toggle_dark_mode():
    global is_dark_mode

    if not is_dark_mode:
        Pan.config(bg='black')
        lb.config(bg='black', fg='white')
        button_frame.config(bg='black')
        dark_mode_button.config(text="Light Mode", style="Dark.TButton")
        style.configure('Green.TButton', background='black', foreground='green')
        style.configure('Blue.TButton', background='black', foreground='blue')
        style.configure('red.TButton', background='black', foreground='red')
        is_dark_mode = True
    else:
        Pan.config(bg='white')
        lb.config(bg='white', fg='green')
        button_frame.config(bg='white')
        dark_mode_button.config(text="Dark Mode", style="Light.TButton")
        style.configure('Green.TButton', background='white', foreground='green')
        style.configure('Blue.TButton', background='white', foreground='blue')
        style.configure('red.TButton', background='white', foreground='red')
        is_dark_mode = False
#confirm_recharge
def open_signup_window():
    signup_window = Toplevel(Pan)
    signup_window.title('Sign Up')
    signup_window.geometry('300x400')

    Label(signup_window, text='Sign Up Form', font=('tahoma', 16, 'bold'), fg='blue').grid(row=0, column=0, columnspan=2, pady=10)

    def submit_signup():
        first_name = name_entry.get()
        last_name = last_entry.get()
        national_code = kod_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        bicycle_size = bicycle_combobox.get()

        # بررسی تکراری نبودن کد ملی و نام کاربری
        cursor.execute('SELECT * FROM users WHERE national_code = ? OR username = ?', (national_code, username))
        if cursor.fetchone():
            Label(signup_window, text='National Code or Username already exists!', fg='red').grid(row=9, column=0, columnspan=2)
        else:
            cursor.execute('INSERT INTO users (first_name, last_name, national_code, username, password, bicycle_size) VALUES (?, ?, ?, ?, ?, ?)',
                           (first_name, last_name, national_code, username, password, bicycle_size))
            conn.commit()
            Label(signup_window, text='Sign Up Successful!', fg='green').grid(row=9, column=0, columnspan=2)

    name_entry = Entry(signup_window)
    name_entry.grid(row=1, column=1, pady=5)
    Label(signup_window, text='Name:').grid(row=1, column=0, pady=5, sticky='e')

    last_entry = Entry(signup_window)
    last_entry.grid(row=2, column=1, pady=5)
    Label(signup_window, text='Last Name:').grid(row=2, column=0, pady=5, sticky='e')

    kod_entry = Entry(signup_window)
    kod_entry.grid(row=3, column=1, pady=5)
    Label(signup_window, text='National Code:').grid(row=3, column=0, pady=5, sticky='e')

    username_entry = Entry(signup_window)
    username_entry.grid(row=4, column=1, pady=5)
    Label(signup_window, text='Username:').grid(row=4, column=0, pady=5, sticky='e')

    password_entry = Entry(signup_window, show='*')
    password_entry.grid(row=5, column=1, pady=5)
    Label(signup_window, text='Password:').grid(row=5, column=0, pady=5, sticky='e')

    bicycle_combobox = ttk.Combobox(signup_window, state="readonly", values=[12, 16, 20, 24, 26, 27.5, 29])
    bicycle_combobox.grid(row=6, column=1, pady=5)
    Label(signup_window, text='Bicycle Size:').grid(row=6, column=0, pady=5, sticky='e')

    ttk.Button(signup_window, text='Submit', command=submit_signup).grid(row=7, column=0, columnspan=2, pady=20)
    ttk.Button(signup_window, text='Back', command=signup_window.destroy).grid(row=8, column=0, columnspan=2, pady=5)

# ادامه کد...

    def reveal_password():
        # به صورت عادی نمایش بده
        current_password = password_entry.get()
        password_entry.config(show='')
        password_entry.delete(0, END)  # پاک کردن ورودی
        password_entry.insert(0, current_password)  # وارد کردن مجدد به صورت عادی

        # بعد از 2 ثانیه به ستاره تغییر می‌کند
        password_entry.after(500, lambda: password_entry.config(show='*'))
    


    # با هر بار تغییر در ورودی پسورد، تابع reveal_password فراخوانی می‌شود
    password_entry.bind("<KeyRelease>", lambda event: reveal_password())


# ... بقیه کد‌ها ...

def log_in():
    global username_log, password_login, login_window
    login_window = Toplevel(Pan)
    login_window.title('Log In')
    login_window.geometry('400x300')

    # ایجاد فیلدهای ورود
    Label(login_window, text='Username:').grid(row=0, column=0, pady=5, sticky='e')
    username_log = Entry(login_window)
    username_log.grid(row=0, column=1, pady=5)

    Label(login_window, text='Password:').grid(row=1, column=0, pady=5, sticky='e')
    password_login = Entry(login_window, show='*')
    password_login.grid(row=1, column=1, pady=5)

    # دکمه ورود
    ttk.Button(login_window, text='Submit', command=in_to).grid(row=2, column=0, pady=10)
    ttk.Button(login_window, text='Back', command=login_window.destroy).grid(row=3, column=0, pady=30)

start_time = None
user_data = None

def in_to():
    global start_time , user_data
    username = username_log.get()
    password = password_login.get()

    # بررسی اطلاعات ورود
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    if user:
        user_data = user
        login_window.destroy()
#login_in_window 
        # پنجره ورود موفق
        login_in_window = Toplevel()
        login_in_window.title('Logged in')
        login_in_window.geometry('750x400')

        wallet_label = Label(login_in_window, text=f"Wallet Balance: ${user[7]:.2f}", font=("Arial", 12), fg="blue")
        wallet_label.grid(row=0, column=1, pady=10)

        def update_wallet_display(new_balance):
            wallet_label.config(text=f"Wallet Balance: ${new_balance:.2f}")

        

        # total_elapsed_time متغیرهای کرنومتر
        start_time = None
        running = False

        # لیبل نمایش کرنومتر
        timer_label = Label(login_in_window, text="Timer: 00:00:00", font=("Arial", 12), fg="green")
        timer_label.grid(row=1, column=1, pady=10)

        
#Start of rent

        #total_elapsed_time = 0  # ذخیره زمان سپری شده
        # متغیر global برای وضعیت تایمر
          # وضعیت تایمر
        def start_rent():
            #total_elapsed_time = 0  # ذخیره زمان سپری شده
            global start_time, running
            if not running:  # اگر تایمر از قبل در حال اجرا نیست
                start_time = t.time() #شروع از زمان فعلی
                running = True
                update_timer()  # شروع به‌روزرسانی کرنومتر
                
                Label(login_in_window, text="Rent started!", fg='green').grid(row=3, column=1, pady=10)

            else:
                 Label(login_in_window, text="Rent is already running!", fg='red').grid(row=3, column=1, pady=10)

#total_elapsed_time

        def update_timer():
            global start_time , running
            if running:
                elapsed_time = t.time() - start_time  # زمان سپری‌شده از زمان شروع
                total_time = elapsed_time  # زمان کل (زمان از قبل سپری‌شده + زمان جدید)
                minutes, seconds = divmod(int(total_time), 60)
                hours, minutes = divmod(minutes, 60)
                timer_label.config(text=f"Timer: {hours:02}:{minutes:02}:{seconds:02}")
                timer_label.after(1000, update_timer)  # هر 1 ثانیه به‌روزرسانی می‌شود



        def finish_rent():
            global running, start_time, user_data
            if running:
                running = False
                end_time = t.time()
                elapsed_time = end_time - start_time
                total_elapsed_time = elapsed_time

                # محاسبه هزینه اجاره
                cost = (total_elapsed_time // 2700) * 1  # 1 دلار برای هر 45 دقیقه
                new_wallet = user_data[7] - cost

                # به‌روزرسانی در دیتابیس
                cursor.execute('UPDATE users SET wallet = ?, time_used = time_used + ? WHERE id = ?', 
                            (new_wallet, total_elapsed_time / 60, user_data[0]))
                conn.commit()

                # به‌روزرسانی اطلاعات کاربر از دیتابیس
                cursor.execute('SELECT * FROM users WHERE id = ?', (user_data[0],))
                user_data = cursor.fetchone()

                # به‌روزرسانی نمایش ولت و تایمر
                update_wallet_display(user_data[7])
                timer_label.config(text="Timer: 00:00:00")
                Label(login_in_window, text=f"Rent finished! Total cost: ${cost:.2f}", fg='blue').grid(row=4, column=1, pady=10)
            else:
                Label(login_in_window, text="No rent in progress!", fg='red').grid(row=4, column=1, pady=10)

        #ttk.Button(login_in_window, text='Start of rent', command=start_rent).grid(row=6, column=0, pady=10)
        #ttk.Button(login_in_window, text='Finish of rent', command=finish_rent).grid(row=6, column=1, pady=10)



        def recharge_account():
            recharge_window = Toplevel(login_in_window)
            recharge_window.title('Recharge Account')
            recharge_window.geometry('300x200')

            Label(recharge_window, text='Enter amount to recharge:').grid(row=0, column=0, pady=10)
            amount_entry = Entry(recharge_window)
            amount_entry.grid(row=0, column=1, pady=10)

            def confirm_recharge():
                global user_data
                amount = float(amount_entry.get())
                new_wallet = user_data[7] + amount

                cursor.execute('UPDATE users SET wallet = ? WHERE id = ?', (new_wallet, user_data[0]))
                conn.commit()

                # به‌روزرسانی اطلاعات کاربر از دیتابیس
                cursor.execute('SELECT * FROM users WHERE id = ?', (user_data[0],))
                user_data = cursor.fetchone()

                update_wallet_display(user_data[7])  # به‌روزرسانی مقدار نمایش ولت
                recharge_window.destroy()
                Label(login_in_window, text=f"Wallet Balance: ${user_data[7]:.2f}", fg='green', font=("Arial", 12)).grid(row=7, column=1, pady=10)
                # نمایش مانده حساب جدید در صفحه اصلی
                update_wallet_display(new_wallet)  # به‌روزرسانی مقدار موجودی
                recharge_window.destroy()
                Label(login_in_window, text=f"Wallet Balance: ${new_wallet:.2f}", fg='green', font=("Arial", 12)).grid(row=7, column=1, pady=10)
                Label(recharge_window, text="Recharge successful!", fg='blue').grid(row=3, column=0, columnspan=2, pady=10)
                
                # بستن پنجره پس از 2 ثانیه
                recharge_window.after(2000, recharge_window.destroy)



            ttk.Button(recharge_window, text='Recharge', command=confirm_recharge).grid(row=1, column=0, columnspan=2, pady=10)

        ttk.Button(login_in_window, text='Start of rent', command=start_rent).grid(row=6, column=0, pady=10)
        ttk.Button(login_in_window, text='Finish of rent', command=finish_rent).grid(row=6, column=1, pady=10)
        ttk.Button(login_in_window, text='Recharge Account', command=recharge_account).grid(row=6, column=2, pady=10)
    else:
        Label(login_window, text='Invalid Username or Password', fg='red').grid(row=4, column=0, columnspan=2)

# ادامه کد...
#Wallet

def charging():
    charging_ta =  Toplevel()
    charging_ta.title('Recharge account')
    charging_ta.geometry('500x500')


    Back = ttk.Button(charging_ta, text='Back', command=charging_ta.destroy)
    Back.grid(row=7, column=3, pady=15)

    labelcharg = Label(charging_ta, text='Enter the amount you want to recharge $:', font=("Arial", 12))
    labelcharg.grid(row=3, column=2, pady=5)  
    

    charging = Entry(charging_ta)
    charging.grid(row=3, column=3, pady=5)  # قرار دادن در سمت چپ


    ok_charging = ttk.Button(charging_ta, text='OK', command=charging_ta.destroy)
    ok_charging.grid(row=5, column=3, pady=15)





Pan = Tk()
Pan.title('PEDAL')
Pan.geometry('400x300')

image = Image.open("image.png").resize((50, 50))
pic = ImageTk.PhotoImage(image)

# نمایش تصویر و متن "پدال" در کنار هم در یک Label
lb = Label(Pan, text='PEDAL', image=pic, compound="left", font=('tahoma', 20, 'bold'), foreground='green')
lb.pack(anchor='n', pady=10)

style = ttk.Style()
style.theme_use('clam')
style.configure('Green.TButton', background='white', foreground='green', padding=10)
style.configure('Blue.TButton', background='white', foreground='blue', padding=10)
style.configure('red.TButton', background='red', foreground='white', padding=10)

button_frame = Frame(Pan, bg='white')
button_frame.pack(expand=True)
button_frame.pack_propagate(False)

log = ttk.Button(button_frame, text="LOG IN", style='Green.TButton', command=log_in)
log.grid(row=0, column=0, padx=50, pady=20, sticky='w')

# اتصال دکمه SIGN UP به تابع open_signup_window
sin_up = ttk.Button(button_frame, text="SIGN UP", style='Blue.TButton', command=open_signup_window)
sin_up.grid(row=0, column=1, padx=50, pady=20, sticky='e')

# دکمه خروج
exit_button = ttk.Button(button_frame, text="Exit", style='red.TButton', command=Pan.quit)
exit_button.grid(row=1, columnspan=2, pady=20)  # قرار دادن دکمه در زیر دکمه‌های دیگر

# دکمه برای تغییر حالت دارک مود
dark_mode_button = ttk.Button(button_frame, text="Dark Mode", style='Light.TButton', command=toggle_dark_mode)
dark_mode_button.grid(row=2, columnspan=2, pady=10)

Pan.mainloop()
