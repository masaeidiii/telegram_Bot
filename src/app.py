import telebot
import base
import app_api


bot = telebot.TeleBot(base.TOKEN)
print('bot created...')






@bot.message_handler(commands= ['start']) # علامت کامند / بوده
def say_hello(message):
    bot.send_message(message.chat.id,text= 'به کانال من خوش اومدید')



@bot.message_handler(commands= ['help', 'support'])
def show_help_msg(message):
    bot.reply_to(message, text = 'در صورت نیاز با شماره 0916 تماس بگیرید')

@bot.message_handler(commands= ['news'])
def show_news(message):
    markup = telebot.types.InlineKeyboardMarkup()
    #markup = telebot.types.InlineKeyboardMarkup(row_width=2) put 2 option in  each line


    btn1 =telebot.types.InlineKeyboardButton(text='اخبار ورزشی ', url= 'https://www.varzesh3.com')
    btn2 =telebot.types.InlineKeyboardButton(text='اخبار عمومی ', url= 'https://www.shahrekhabar.com')
    btn3 =telebot.types.InlineKeyboardButton(text='اخبار اقتصادی ', url= 'https://www.tradingview.com')


    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id , text='یکی از گزینهارو انتخاب کن ', reply_markup= markup)

#================================================================
'''

@bot.message_handler(func=lambda message : True)
def handle_all_message(message):
        
    if message.text == 'تماس با ما':
        email = 'support@gmail.com'
        phone = '0936422813'
        post_box = '123456798'
        info = f"ایمیل  :{email},   شماره تماس :{phone} , صندوق پستی :{post_box}"


        bot.send_message(message.chat.id, text = info)
    
    elif message.text == 'درباره ما':
        bot.send_message(message.chat.id, text = "گروه اموزشی با ایده هایی روشن")

    
    elif message.text == "تعیین عضوییت":
        #membership_type= {'normal' : "3ماهه", 'vip': "یک ساله", 'firs_class':'محدود '}
        bot.send_message(message.chat.id, text= 'یکی از گزینه های 3 ماهه / یک ساله و نامحدود را انتخاب کنید')

    elif message.text == 'بازگشت':
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text = "به منوی اصلی باز گردید ", reply_markup= markup)


    else:
        bot.send_message(message.chat.id,"منظور شما را متوجه نشدم دوباره تلاش کنید")


بالای منو که باشه هرچی دستور زیرش باشه دیگه کار نمیکنه و میزنه متوجه نشدم  اونم به خاطر کد 40

'''
#===============================================


#فرقش با بالاییه:پایینی اینه که با کلیک به گزینه ها در صفحه چت نوشته میشه   نشون داده میشه, ولی بالاییه نشون داده نمیشه

@bot.message_handler(commands= ['menu'])
def show_menu(message):
    print(message)
    markup = telebot.types.ReplyKeyboardMarkup()

    btn1 = telebot.types.KeyboardButton(text = 'تماس با ما')
    btn2 = telebot.types.KeyboardButton(text = 'درباره ما')
    btn3 = telebot.types.KeyboardButton(text = 'تعیین عضوییت')
    btn4 = telebot.types.KeyboardButton(text = 'بازگشت')
    btn5 = telebot.types.KeyboardButton(text = 'اخبار ')
    
    markup.add(btn3,btn2,btn1,btn4,btn5)

    bot.send_message(message.chat.id , text= 'یکی از گزینهارو انتخاب کن', reply_markup= markup)


#============================================================
@bot.message_handler(commands=['movie'])
def show_movie(message):
    msg= bot.send_message(message.chat.id, 'آی دی فیلم مورد نظر را وارد نمایید')
    bot.register_next_step_handler(msg, get_movie_info)

def get_movie_info(message ):
    movie_id = message.text
    result = app_api.get_movie_info_by_id(movie_id)
    bot.send_message(message.chat.id, text=f"{result[0]} / {result[-1]}")

#=========================================================



@bot.message_handler(commands=['movie_name'])
def show_movie(message):
    msg= bot.send_message(message.chat.id, 'اسم فیلم مورد نظر را وارد نمایید')
    bot.register_next_step_handler(msg, get_movie_info_by_name)

def get_movie_info_by_name (message ):
    movie_name= message.text
    result = app_api.get_movie_info_by_name(movie_name)
    bot.send_message(message.chat.id, text=f"{result[0]} / {result[-1]}")





#===================================================



@bot.message_handler(func=lambda message : True)
def handle_all_message(message):
        
    if message.text == 'تماس با ما':
        email = 'support@gmail.com'
        phone = '0936422813'
        post_box = '123456798'
        info = f"ایمیل  :{email},   شماره تماس :{phone} , صندوق پستی :{post_box}"


        bot.send_message(message.chat.id, text = info)
    
    elif message.text == 'درباره ما':
        bot.send_message(message.chat.id, text = "گروه اموزشی با ایده هایی روشن")

    
    elif message.text == "تعیین عضوییت":
        #membership_type= {'normal' : "3ماهه", 'vip': "یک ساله", 'firs_class':'محدود '}
        bot.send_message(message.chat.id, text= 'یکی از گزینه های 3 ماهه / یک ساله و نامحدود را انتخاب کنید')

    elif message.text == 'بازگشت':
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text = "به منوی اصلی باز گردید ", reply_markup= markup)


    else:
        bot.send_message(message.chat.id,"منظور شما را متوجه نشدم دوباره تلاش کنید")




if __name__ == '__main__':
    bot.infinity_polling()