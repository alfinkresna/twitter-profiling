#!/usr/bin/env python3
import requests, json, sys, os

headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,bn;q=0.8",
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        "content-type": "application/json",
        "dnt": "1",
        'origin': 'https://twitter.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'en'
        }

def m_1():
    os.system("clear")
    b = """
    \033[31m
     /$$$$$$$$            /$$   /$$    
    |__  $$__/           |__/  | $$    
       | $$ /$$  /$$  /$$ /$$ /$$$$$$  
       | $$| $$ | $$ | $$| $$|_  $$_/  
       | $$| $$ | $$ | $$| $$  | $$    
       | $$| $$ | $$ | $$| $$  | $$ /$$
       | $$|  $$$$$/$$$$/| $$  |  $$$$/
       |__/ \_____/\___/ |__/   \___/  \033[0m  
                                   
         \033[36m    Twitter Profiling

             Created by Alfin \033[0m                                                                  
         """
    print(b)
    us = input("\033[37m>\033[0m \033[31mMasukan Username \033[37m: \033[0m")
    url = "https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables={\"screen_name\":\"" + us + "\",\"withHighlightedLabel\":true}"
    res  = requests.get(url, headers=headers)
    resp = json.loads(res.text)

    bio = resp["data"]["user"]["legacy"]["description"]
    id = resp["data"]["user"]["rest_id"]
    followers = resp["data"]["user"]["legacy"]["followers_count"]
    location = resp["data"]["user"]["legacy"]["location"]
    name = resp["data"]["user"]["legacy"]["name"]
    created = resp["data"]["user"]["legacy"]["created_at"]
    following = resp["data"]["user"]["legacy"]["friends_count"]
    favc = resp["data"]["user"]["legacy"]["favourites_count"]
    cust = resp["data"]["user"]["legacy"]["has_custom_timelines"]
    listc = resp["data"]["user"]["legacy"]["listed_count"]
    mediac = resp["data"]["user"]["legacy"]["media_count"]
    protected = resp["data"]["user"]["legacy"]["protected"]
    statc = resp["data"]["user"]["legacy"]["statuses_count"]
    verified = resp["data"]["user"]["legacy"]["verified"]
    at = resp["data"]["user"]["legacy"]["is_translator"]
    td = resp["data"]["user"]["legacy"]["pinned_tweet_ids_str"]
    bn = resp["data"]["user"]["legacy"]["withheld_in_countries"]

    if location == '':
            location = 'Tidak Diketahui'
    if bio == '':
            bio = 'Tidak Ada Bio'

    if verified == True:
            verified = 'Terverifikasi'
    if verified == False:
            verified = 'Tidak Terverifikasi'        

    if at == True:
            at = 'Menggunakan Penerjemah'
    if at == False:
            at = 'Tidak'

    if cust == True:
            cust = 'Menggunakan Custom Timelines'
    if cust == False:
            cust = 'Tidak'

    if td == []:
         td = 'Tidak Diketahui'

    if bn == []:
         bn = 'Tidak Diblokir'

    if protected == True:
            protected = 'Dilindungi'
    if protected == False:
            protected = 'Tidak Dilindungi'

    if res.status_code == 200:
            print(f"""
\033[37m>\033[0m \033[36mNama \033[37m: {name} \033[0m
            
\033[37m>\033[0m \033[36mLink Photo \033[37m: https://twitter.com/{us}/photo \033[0m

\033[37m>\033[0m \033[36mLink Banner \033[37m: https://twitter.com/{us}/header_photo \033[0m

\033[37m>\033[0m \033[36mTwitter ID \033[37m: {id} \033[0m

\033[37m>\033[0m \033[36mBio \033[37m: {bio} \033[0m

\033[37m>\033[0m \033[36mVerifikasi \033[37m: {verified} \033[0m

\033[37m>\033[0m \033[36mDilindungi \033[37m: {protected} \033[0m

\033[37m>\033[0m \033[36mCustom Timelines \033[37m: {cust} \033[0m

\033[37m>\033[0m \033[36mDiblokir Di Beberapa Negara \033[37m: {bn} \033[0m

\033[37m>\033[0m \033[36mMenggunakan Penerjemah \033[37m: {at} \033[0m
            
\033[37m>\033[0m \033[36mFollowers \033[37m: {followers} \033[0m

\033[37m>\033[0m \033[36mFollowing \033[37m: {following} \033[0m

\033[37m>\033[0m \033[36mID Tweet Yang Disematkan \033[37m: {td} \033[0m

\033[37m>\033[0m \033[36mJumlah Tweet Favorit \033[37m: {favc} \033[0m

\033[37m>\033[0m \033[36mJumlah Status \033[37m: {statc} \033[0m

\033[37m>\033[0m \033[36mJumlah Media \033[37m: {mediac} \033[0m

\033[37m>\033[0m \033[36mJumlah Yang Terdaftar \033[37m: {listc} \033[0m

\033[37m>\033[0m \033[36mLokasi \033[37m: {location} \033[0m
            
\033[37m>\033[0m \033[36mTanggal Pembuatan Akun \033[37m: {created} \033[0m""")
    
    elif res.status_code == 404:
            print("Akun tidak ditemukan")

def m_2():
     print()
     i = input("\033[37m>\033[0m \033[31mUlang Lagi ? \033[37m:\033[37m ")
     try:
          while True:
               if i == "tidak" or i == "t":
                    print()
                    sys.exit("\033[37m>\033[0m \033[36mKeluar\033[0m\n")
               elif i == "iya" or i == "ya" or i == "y":
                    m_1()
                    m_2()
               else:
                    print()
                    print("\033[37m>\033[0m \033[36mPilihan Salah\033[0m")
                    m_2()
     except KeyboardInterrupt:
          sys.exit("\n\033[0m")

m_1()
m_2()