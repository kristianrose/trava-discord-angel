from time import sleep
import requests
import json
import time
import os
import sys

print(cyan + """

.                                       ,
)).               -===-               ,((
))).                                 ,(((
))))).            .:::.           ,((((((
))))))))).        :. .:        ,(((((((('
`))))))))))).     : - :    ,((((((((((((
 ))))))))))))))))_:' ':_((((((((((((((('
 `)))))))))))).-' \___/ '-._(((((((((((
  `))))_._.-' __)(     )(_  '-._._(((('
   `))'---)___)))'\_ _/'((((__(---'(('
     `))))))))))))|' '|(((((((((((('
       `)))))))))/'   '\((((((((('
         `)))))))|     |((((((('
          `))))))|     |(((((('   Angel Supreme 
                /'     '\         Feito por: Kristian
               /'       '\
              /'         '\
             /'           '\
             '---..___..---'


""")
sleep(5)
os.system(['clear', 'cls'][os.name == 'int'])
itoken = imput("Mande seu token --->")
sleep(2)
os.system(['clear', 'cls'][os.name == 'int'])
token = itoken # Adicione seu token
payload = {'content': '**🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐵🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒🍌🐵🍌🐒**'}
headers = {'Authorization':token,'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.12 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'}

print(white + ""
                      .-"""-.
   ,                 (_ _    \
  /|  ____     _      )= `)  ) ,"";,
 |(| ()___>===(()====(   (   (//``;\\
(|            ||~\__  `) (    )    ;||
              ||    `==\--`.-;     ;||
               \\      /   |`-._,  ;\\
        ,        `---;`    /     `._`\\   A tromba assim mais uma vez
      ,/|             >~~~~`._      `"`   Foi tocada, e assim o ataque surgiu.
      |(|            /   '    `""---.....___
     (|              | '.    '  _    .      ``\
                     \     '-.    '-   .   _  /
                      \ '.              -  ._`\
                       '.    '.     '-..     _/
              Kristian   '._   -  ._       _/
                            `-..__      .-'`
                                  `"'""`


""")
print(" ")
print("Coloque o id dos futuros expurgados")
channelId = input()
for _ in range(999999999);
       r = requests.post(f'https://discord.com/api/v8/channels/{channelId}/messages', headers=headers, json=payload')
       if r.status_code == 200;
       print('Os anjos da morte luar voltaram para castigar os usuarios, novamente.')
       elif r.status_code == 429;
       data = json.loads(r.text)
       print(f'Payload sendo enviado novamente em {data["retry_after"]) segundos')
       time.sleep(data['retry_after'])
       else:
           print("Verifique o id ou o token que foi adicionado. Kristian agradece!")
