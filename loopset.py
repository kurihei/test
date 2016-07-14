import datetime
import locale
import subprocess
import time

cmd = """curl -X POST http://localhost:8545 --data '{"jsonrpc":"2.0","method":"eth_sendTransaction","params":[{ "from": "0xb9a0c048e4a73014820cad918fbcc9dfc162b4e9","to": "0xb9a0c048e4a73014820cad918fbcc9dfc162b4e9","gas": "0x76c0","gasPrice": "0x9184e72a000","value": "0x9184e72a","data": "0x1ab06ee500000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000003"}],"id":1}'"""

cmdHead = """curl -X POST http://localhost:8545 --data '{"jsonrpc":"2.0","method":"eth_sendTransaction","params":[{ "from": "0xb9a0c048e4a73014820cad918fbcc9dfc162b4e9","to": "0x90f7a352ec030edf6dc7c79a290b3cccda6df4f2","gas": "0x76c0","gasPrice": "0x9184e72a000","value": "0x9184e72a","data": "0x1ab06ee5"""

cmdTail = """}],"id":1}'"""

def looping():
    datafile = open('mydata.txt')
    line = datafile.readline()

    while line:
 
        line = datafile.readline()

        rawline = line.replace('\n','')        
#        print(rawline) 
        synthCmd = cmdHead + rawline + '\"' + cmdTail
        print(synthCmd)
        print("\n")
        subprocess.call(synthCmd, shell=True)
        time.sleep(3)
    datafile.close

def show_datetime():
    d = datetime.datetime.today()
    print("%s年%s月%s日\n" % (d.year, d.month, d.day))
    print("%s時%s分%s.%s秒n" % (d.hour, d.minute, d.second, d.microsecond))
    print(d.strftime("%Y-%m-%d %H:%M:%S"), '\n')

if __name__ == '__main__':
    print("Start loopset!")
    show_datetime()
    looping()
