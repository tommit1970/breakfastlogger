import multiprocessing
from multiprocessing import Process, Manager, Value, Pool


def userProc(q, min, max):
    
    pstbinU1 = q.get()
    print(min, max, pstbinU1)

    try:
        r = requests.get(pstbinU1)
        
        sleep(10)
        content = r.text
        
        fp.writelines(content+'\n')
        fp.seek(0)
        links1 = fp.read()
        fp.close()

        
        sleep(random.randint(min, max))    
    except Exception:
        q.task_done()

def main(q, min, max):

    p1 = multiprocessing.Process(target=userProc, args=(q, min, max))
    
    
    p1.start()
    p1.join()
    q.join()

regex5 = (r'[a-zA-Z0-9\s_-]*')   
    
if __name__ == '__main__':
    
    min = str(input('please input minimum seconds: '))
    max = str(input('please input maximum seconds: '))

    q = multiprocessing.JoinableQueue()

    while True:
        text = str(input('Enter the pastebin raw URL(in http url form -> https://pastebin.com/raw/XXXXXXXX): '))

        if not text == '':
            q.put(text)
            main(q, min, max)
            break
        else:
            print('Please paste a proper Pastebin Raw Link...')
            continue
