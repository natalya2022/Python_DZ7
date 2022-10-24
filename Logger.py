def log_line(str):
    with open('log.txt','a',encoding='utf-8') as f:
        f.write(f'{str} \n')
