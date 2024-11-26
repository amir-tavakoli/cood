from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
#import bc-project 



# وضعیت حالت دارک مود
is_dark_mode = False

def toggle_dark_mode():
    global is_dark_mode

    if not is_dark_mode:
        # فعال کردن حالت تاریک
        Pan.config(bg='black')
        lb.config(bg='black', fg='white')
        button_frame.config(bg='black')
        dark_mode_button.config(text="Light Mode", style="Dark.TButton")
        style.configure('Green.TButton', background='black', foreground='green')
        style.configure('Blue.TButton', background='black', foreground='blue')
        style.configure('red.TButton', background='black', foreground='red')
        is_dark_mode = True
    else:
        # بازگشت به حالت روشن
        Pan.config(bg='white')
        lb.config(bg='white', fg='green')
        button_frame.config(bg='white')
        dark_mode_button.config(text="Dark Mode", style="Light.TButton")
        style.configure('Green.TButton', background='white', foreground='green')
        style.configure('Blue.TButton', background='white', foreground='blue')
        style.configure('red.TButton', background='white', foreground='red')
        is_dark_mode = False

def open_signup_window():
    # ایجاد پنجره جدید
    signup_window = Toplevel(Pan)
    signup_window.title('Sign Up')
    signup_window.geometry('300x400')  # اندازه پنجره جدید

    # عنوان پنجره
    label_signup = Label(signup_window, text='Sign Up Form', font=('tahoma', 16, 'bold'), fg='blue')
    label_signup.grid(row=0, column=0, columnspan=2, pady=10)

    # نام
    name_label = Label(signup_window, text='Name:')
    name_label.grid(row=1, column=0, pady=5, sticky='e')
    name_entry = Entry(signup_window)
    name_entry.grid(row=1, column=1, pady=5)

    # فامیلی
    last_label = Label(signup_window, text='Last Name:')
    last_label.grid(row=2, column=0, pady=5, sticky='e')
    last_entry = Entry(signup_window)
    last_entry.grid(row=2, column=1, pady=5)

    # کد ملی
    kod_label = Label(signup_window, text='National Code:')
    kod_label.grid(row=3, column=0, pady=5, sticky='e')
    kod_entry = Entry(signup_window)
    kod_entry.grid(row=3, column=1, pady=5)

    # یوزرنیم
    username_label = Label(signup_window, text='Username:')
    username_label.grid(row=4, column=0, pady=5, sticky='e')
    username_entry = Entry(signup_window)
    username_entry.grid(row=4, column=1, pady=5)

    # پسورد
    password_label = Label(signup_window, text='Password:')
    password_label.grid(row=5, column=0, pady=5, sticky='e')
    password_entry = Entry(signup_window, show='*')
    password_entry.grid(row=5, column=1, pady=5)

    # نمایش سایز دوچرخه
    Bicycle_size = [12, 16, 20, 24, 26, 27.5, 29]
    bicycle_size_label = Label(signup_window, text='Bicycle Size:')
    bicycle_size_label.grid(row=6, column=0, pady=5, sticky='e')
    bicycle_combobox = ttk.Combobox(signup_window, state="readonly", values=Bicycle_size)
    bicycle_combobox.grid(row=6, column=1, pady=5)

    # دکمه ارسال
    submit_button = ttk.Button(signup_window, text='Submit', command=signup_window.destroy)
    submit_button.grid(row=7, column=0, columnspan=2, pady=20)

    # دکمه بازگشت
    back_button = ttk.Button(signup_window, text='Back', command=signup_window.destroy)
    back_button.grid(row=8, column=0, columnspan=2, pady=5)


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



def log_in():
    global bi
    global login_window
    login_window = Toplevel(Pan)
    login_window.title('Log In')
    login_window.geometry('400x300')

    # اضافه کردن تصویر به پنجره لاگین
    a = Image.open("aa.jpg").resize((50, 50))
    bi = ImageTk.PhotoImage(a)

    # عنوان لاگین
    label_login = Label(login_window, text='LOG IN', image=bi, compound="left", font=('tahoma', 16, 'bold'), foreground='green')
    label_login.grid(pady=10)

    # ایجاد یک Frame برای قرار دادن فیلدهای ورودی با متد grid
    login_frame = Frame(login_window)
    login_frame.grid(pady=20)

    # فیلد ورودی کد ملی
    username_label = Label(login_frame, text='Username:')
    username_label.grid(row=0, column=0, pady=5, sticky='e')
    username_log = Entry(login_frame)
    username_log.grid(row=0, column=1, pady=5)

    # فیلد ورودی رمز عبور
    password_label = Label(login_frame, text='Password:')
    password_label.grid(row=0, column=2, pady=5, sticky='e')
    password_login = Entry(login_frame, show='*')
    password_login.grid(row=0, column=3, pady=5)

    # دکمه Submit
    vrod = ttk.Button(login_window, text='Submit', command=in_to)
    vrod.grid(row=2, column=0, pady=0)

    Back = ttk.Button(login_window, text='Back', command=login_window.destroy)
    Back.grid(row=3, column=0, pady=30)
price = 1
time = 10
def in_to():
    login_in_window = Toplevel(login_window)
    login_in_window.title('Logged in')
    login_in_window.geometry('750x400')

    charg = ttk.Button(login_in_window, text='Recharge account', command=charging)
    charg.grid(row=7, column=4, pady=10)
    
    startt = ttk.Button(login_in_window,text="Start of rent")
    startt.grid(row=7, column=6, pady=10)

    finish = ttk.Button(login_in_window, text="finish of rent")
    finish.grid(row=7, column=10, pady=15)


    label = Label(login_in_window, text="Welcome!", font=("Arial", 20))
    label.grid(row=0, column=1, pady=20)

    Wallet_credit_label = Label(login_in_window, text=f"Wallet credit {price} :" , font=("Arial", 16))
    Wallet_credit_label.grid(row=2, column=5, pady=5)

    time_label = Label(login_in_window, text = f"time {time} :", font=("Arial", 16))
    time_label.grid(row=5, column=5, pady=5)


    Back = ttk.Button(login_in_window, text='Back', command=login_in_window.destroy)
    Back.grid(row=8, column=5, pady=5)

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
