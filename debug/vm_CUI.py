import re
import sys
import os
import time
##import pandas as pd
import difflib
from multiprocessing import Process, Value, Array, Lock
aslist1=[]
aslist2=[]
comAS=[]
oprAS=[]
comAS11=[]
oprAS11=[]
pcAS1=[]
dir=[]
dir2=[]
dir22=[]
stackAS=[]
terminatePOS=[]
startlist=[]*2
endlist=[]*2
codes=[]
com=[]
opr=[]
stack=[]
rstack=[]
temp=[]
ldata=[]
rdata=[]
top=-1
topAS=-1
count_pc=0
parflag=0
args=sys.argv

#push:
def push(a,stack,top):
    stack.append(a)
    return top+1

#pop1:
def pop1(stack,top):
    #t=stack[top-1]
    t=stack.pop()
    return (t,top-1)

#variable tableを引数の変数名から検索し共有変数スタックの番地を返す 
def search_table(opr,process_path):
    with open("variable_table.txt",'r') as f:
            variable_table=f.read().split('\n')
    t=0
    address=0
    for i in range(0,len(variable_table)-1,1):
        s=re.search(r'\d+',variable_table[i])
        if s.group()==(str)(opr):
            s2=re.search(r'([a-z](\d+).)+E',variable_table[i])
            match_count=0
            temp_path=s2.group()
            if len(process_path)>=len(temp_path):
                for j in reversed(range(0,len(s2.group()),1)):
                    if process_path[j]==temp_path[j]:
                        match_count=match_count+1
                    else:
                        break
                if match_count>=t:
                    address=i
                    t=match_count
    return address

def executedcommandAS(stackAS,comAS,oprAS,process_path,value,pcAS,topAS):
    ##print(comAS[pcAS])
    ##print(oprAS[pcAS])
    if comAS[pcAS]==1:#push　演算スタックに即値を積む
        topAS=push(oprAS[pcAS],stackAS,topAS)
        ##pre=pcAS
        return (pcAS+1,stackAS,topAS,process_path)
    elif comAS[pcAS]==2:#load　共有変数スタックから値を読み出し演算スタックに積む
        value.acquire()
        c=value[search_table(oprAS[pcAS],process_path)]
        ##print(c)
        value.release()
        topAS=push(c,stackAS,topAS)
        ##pre=pcAS
        return (pcAS+1,stackAS,topAS,process_path)
    elif comAS[pcAS]==6:#op　被演算子の種類の演算を行う
        if (oprAS[pcAS])==0:#'+'
            (c,topAS)=pop1(stackAS,topAS)
            (d,topAS)=pop1(stackAS,topAS)
            topAS=push(c+d,stackAS,topAS)
        elif (oprAS[pcAS])==1:#'*'
            ##print('bbb')
            (c,topAS)=pop1(stackAS,topAS)
            (d,topAS)=pop1(stackAS,topAS)
            topAS=push(c*d,stackAS,topAS)
        elif oprAS[pcAS]==2:#'-'
            (c,topAS)=pop1(stackAS,topAS)
            (d,topAS)=pop1(stackAS,topAS)
            topAS=push(d-c,stackAS,topAS)
        elif oprAS[pcAS]==3:#'>'
            ##print('aaa')
            (c,topAS)=pop1(stackAS,topAS)
            (d,topAS)=pop1(stackAS,topAS)
            if d>c:
                topAS=push(1,stackAS,topAS)
            else:
                topAS=push(0,stackAS,topAS)
        elif oprAS[pcAS]==4:#'=='
            (c,topAS)=pop1(stackAS,topAS)
            (d,topAS)=pop1(stackAS,topAS)
            if d==c:
                top=push(1,stackAS,topAS)
            else:
                top=push(0,stackAS,topAS)
        ##pre=pcAS
        return (pcAS+1,stackAS,topAS,process_path)
    
def executionAS(comAS,oprAS,process_path,value):
    for pcAS in range(0,len(comAS),1):
        ##print(topAS)
        executedcommandAS(stackAS,comAS,oprAS,process_path,value,pcAS,topAS)
        print(stackAS)
    return stackAS[0]

#各命令の実行
def executedcommand(stack,rstack,lstack,com,opr,pc,pre,top,rtop,ltop,address,value,tablecount,variable_region,lock,process_number,process_path,count_pc,process_count,terminate_flag,flag_number):
    notterminate=0
    if com[pc]==1:#push　演算スタックに即値を積む
        top=push(opr[pc],stack,top)
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==2:#load　共有変数スタックから値を読み出し演算スタックに積む
        value.acquire()
        c=value[search_table(opr[pc],process_path)]
        value.release()
        top=push(c,stack,top)
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==3:#store 変数の値を更新し値スタックにそれまでの変数の値及びプロセス番号とパスを積む
        value.acquire()
        with open("value_stack.txt",'a') as f:
            f.write(str(value[search_table(opr[pc],process_path)])+' '+str(process_number)+'.'+process_path+'\n')
        f.close()
        rtop.value=rtop.value+2
        (value[search_table(opr[pc],process_path)],top)=pop1(stack,top)
        value.release()
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==4:#jpc スタックトップの値をポップしその値が1なら被演算子の番地にジャンプする
        (c,top)=pop1(stack,top)
        if c==1:
            pre=pc
            pc=opr[pc]-2
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==5:#jmp　無条件で被演算子の番地にジャンプする
        pre=pc
        pc=opr[pc]-2
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==6:#op　被演算子の種類の演算を行う
        if (opr[pc])==0:#'+'
            (c,top)=pop1(stack,top)
            (d,top)=pop1(stack,top)
            top=push(c+d,stack,top)
        elif (opr[pc])==1:#'*'
            (c,top)=pop1(stack,top)
            (d,top)=pop1(stack,top)
            top=push(c*d,stack,top)
        elif opr[pc]==2:#'-'
            (c,top)=pop1(stack,top)
            (d,top)=pop1(stack,top)
            top=push(d-c,stack,top)
        elif opr[pc]==3:#'>'
            (c,top)=pop1(stack,top)
            (d,top)=pop1(stack,top)
            if d>c:
                top=push(1,stack,top)
            else:
                top=push(0,stack,top)
        elif opr[pc]==4:#'=='
            (c,top)=pop1(stack,top)
            (d,top)=pop1(stack,top)
            if d==c:
                top=push(1,stack,top)
            else:
                top=push(0,stack,top)
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==7:#label　ラベルスタックにジャンプ前のPCの値とプロセス番号を積む
        if args[2]=='f':
            with open("label_stack.txt",'a') as f:
                f.write(str(pre+1)+' '+str(process_number)+'\n')
            f.close()
            ltop.value = ltop.value+2
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==21:#rjmp　ラベルスタックから値を取り出しそのPCにジャンプする
        a=count_pc-int(lstack[ltop.value])
        ltop.value=ltop.value-2
        pre=pc
        return (a,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==22:#restore　値スタックから値を取り出し共有変数スタックに保存する
        s2=re.search(r'([a-z]\d+\.)+',rstack[rtop.value+1])
        process_path=s2.group()+".E"
        value[search_table(opr[pc],process_path)]=int(rstack[rtop.value])
        rtop.value=rtop.value-2
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==19 or com[pc]==28:#nop　no operation
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==8 or com[pc]==23:#par　並列ブロックの開始と終了を示す
        #if opr[pc]==1:
        #    terminate_flag[flag_number]=1
        #    print(str(flag_number))
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==9:#alloc　新しい変数の番地を確保し初期値を0にする
        #top=push(0,stack,top)
        if args[2]=='f':
            value[tablecount.value] = 0    #############################################################
            variable_region.append(0)
            with open("variable_table.txt",'a') as f:
                f.write(str(opr[pc])+'.'+process_path+'      0\n')
            tablecount.value=tablecount.value+1
        elif args[2]=='b':
            variable_path=search_table(opr[pc],process_path)
            variable_region.append(0)
            with open("variable_table.txt",'r') as f:
                variable_table=f.read().split('\n')
            s=re.search(r'\s(-)?(\d+)',variable_table[variable_path])
            variable_value=int(s.group().strip(' '))
            value[search_table(opr[pc],process_path)]=variable_value
            tablecount.value=tablecount.value+1
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==10:#free　変数の番地の解放を示し値スタックにそれまでの値を保存する
        table_address=search_table(opr[pc],process_path)
        value.acquire()
        with open("value_stack.txt",'a') as f:
            f.write(str(value[search_table(opr[pc],process_path)])+' '+str(process_number)+'.'+process_path+'\n')
        f.close()
        value.release()
        value[table_address]=0
        pre=pc
        variable_region[opr[pc]] = value[opr[pc]]
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==11:#proc　手続きの開始　label命令とblock命令を行う　返り番地を演算スタックに積む
        if args[2]=='f':
            with open("label_stack.txt",'a') as f:
                f.write(str(pre+1)+' '+str(process_number)+'\n')
            f.close()
            push(pre+1,stack,top)
        pre=pc
        process_path='p'+str(opr[pc])+'.'+process_path
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==12:#ret　手続きの終了　演算スタックから返り番地を取り出しその番地にジャンプする
        (c,top) = pop1(stack,top)
        for i in range(0,len(process_path),1):
            if process_path[i] == '.':
                process_path=process_path[i+1:len(process_path)]
                break
        pre=pc
        return (c,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==13:#block　パスを追加
        if com[pc+3]==16 and (com[pc+1]==5 or com[pc+1]==8):
            process_path='c'+str(opr[pc])+'.'+process_path
        else:
            process_path='b'+str(opr[pc])+'.'+process_path
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==14:#end　パスの削除
        for i in range(0,len(process_path),1):
            if process_path[i] == '.':
                process_path=process_path[i+1:len(process_path)]
                break
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==15:#fork 並列プロセスの生成
        lock.release()
        process={}
        start_process_count = process_count.value
        already_terminate = {}
        f=open('a'+(str)(opr[pc])+'.txt',mode='r')
        tables=f.read()
        ##print(tables)
        ##print(len(tables))
        #並列ブロックを参照しそれぞれ開始番地と終了番地を取り出して各プロセスに与えプロセスを生成する
        #for i in range(0,len(tables),10):
        #    t1=tables[i:i+4]
        #    s1=re.search(r'\d+',t1)
        #    t2=tables[i+5:i+9]
        #    s2=re.search(r'\d+',t2)
        #    terminate_flag[process_count.value]=0                               ###start end list
        #    process[process_count.value]=Process(target=execution,args=(com,opr,(int)(s1.group()),(int)(s2.group()),count_pc,stack,address,value,tablecount,rstack,lstack,rtop,ltop,0,variable_region,lock,process_number + '.' + str(process_count.value-start_process_count+1),process_path,process_count,terminate_flag,process_count.value,0))
        #    process_count.value=process_count.value+1
        for i in range(0,len(tables),10):
            t1=tables[i:i+4]
            s1=re.search(r'\d+',t1)
            t2=tables[i+5:i+9]
            s2=re.search(r'\d+',t2)
            print(i)
            print(s1.group())
            print(s2.group())
            terminate_flag[process_count.value]=0                               ###start end list
            process[process_count.value]=Process(target=execution,args=(com,opr,comb,oprb,(int)(s1.group()),(int)(s2.group()),count_pc,stack,address,value,tablecount,rstack,lstack,rtop,ltop,0,variable_region,lock,process_number + '.' + str(process_count.value-start_process_count+1),process_path,process_count,terminate_flag,process_count.value,0,assertF,asl2,pcASSERT,dir,dir2,comAS,oprAS,terminatePOS))
            process_count.value=process_count.value+1
        end_process_count = process_count.value
        for i in range(start_process_count,process_count.value,1):
            process[i].start()
        terminate_count=0
        #自分が生成したプロセスが終了しているかどうかを監視する．終了している場合terminateでプロセスを完全終了させる
        for i in range(0,100,1):
            already_terminate[i]=0 ##親
        while True:
            for i in range(start_process_count,end_process_count,1):
                if terminate_flag[i]>=1 and already_terminate[i]==0:
                    process[i].terminate() ##
                    process[i].join()
                    already_terminate[i]=1
                    terminate_count=terminate_count+1
                    if not process[i].is_alive():
                        process[i].join()
                    if terminate_flag[i]==2:
                        notterminate+=1
            if terminate_count==end_process_count-start_process_count:
                pre=pc
                lock.acquire()
                return (int(s2.group()),pre,stack,top,rtop,tablecount,process_path,notterminate)
        pre=pc
        lock.acquire()
        return (a,pre,stack,top,rtop,tablecount,process_path)
    elif com[pc]==16:#merge 並列ブロックの終了を示す
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==17:#func 関数の開始 label命令とblock命令を行い演算スタックトップの一つ下に帰り番地を積む
        if args[2]=='f':
            with open("label_stack.txt",'a') as f:
                f.write(str(pre+1)+' '+str(process_number)+'\n')
            f.close()
            (c,top)=pop1(stack,top)
            push(pre+1,stack,top)
            push(c,stack,top)
        pre=pc
        process_path='f'+str(opr[pc])+'.'+process_path
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==18:#f_return 関数の終了 演算スタックの一つしたの値を取り出しその番地にジャンプする
        (d,top) = pop1(stack,top)
        (c,top) = pop1(stack,top)
        push(d,stack,top)
        for i in range(0,len(process_path),1):
            if process_path[i] == '.':
                process_path=process_path[i+1:len(process_path)]
                break
        pre=pc
        return (c,pre,stack,top,rtop,tablecount,process_path,notterminate)
        #elif com[pc]==19:#w_label whileの開始を示しlabel命令とblock命令を行う
        #with open("label_stack.txt",'a') as f:
        #    f.write(str(pre+1)+' '+str(process_number)+'\n')
        #f.close()
        #process_path='w'+str(opr[pc])+'.'+process_path
        #pre=pc
        #return (pc+1,pre,stack,top,rtop,tablecount,process_path)
        #elif com[pc]==20:#w_end whileの終了を示しlabel命令とend命令を行う
        #with open("label_stack.txt",'a') as f:
        #    f.write(str(pre+1)+' '+str(process_number)+'\n')
        #f.close()
        #process_path=process_path.replace('w'+str(opr[pc])+'.','')
        #return (pc+1,pre,stack,top,rtop,tablecount,process_path)
    elif com[pc]==24:#r_alloc 逆向きのalloc命令 値スタックから値を取り出し 確保した共有変数スタックの番地に保存する
        s2=re.search(r'([a-z]\d+\.)+',rstack[rtop.value+1])
        process_path=s2.group()
        with open("variable_table.txt",'a') as f:
                f.write(str(opr[pc])+'.'+process_path+'E      0\n')
        value[tablecount.value]=int(rstack[rtop.value])    ###############################################################
        tablecount.value=tablecount.value+1
        rtop.value=rtop.value-2
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==25:#r_free 逆向きのfree命令 変数の解放を示す
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
    elif com[pc]==26:#r_fork 逆向きのfork命令 前向きとは逆順に並列テーブルを参照する
        lock.release()
        process={}
        start_process_count = process_count.value
        f=open('a'+(str)(opr[pc])+'.txt',mode='r')
        already_terminate = {}
        tables=f.read()
        tables_process_number = int(len(tables)/10)
        print(str(tables_process_number))
        for i in range(0,len(tables),10):
            t1=tables[i:i+4]
            s1=re.search(r'\d+',t1)
            t2=tables[i+5:i+9]
            s2=re.search(r'\d+',t2)
            print(i)
            print(s1.group())
            print(s2.group())
            terminate_flag[process_count.value]=0                                                      ##
            process[process_count.value]=Process(target=execution,args=(com,opr,comb,oprb,count_pc-(int)(s2.group())+1,count_pc-(int)(s1.group())+1,count_pc,stack,address,value,tablecount,rstack,lstack,rtop,ltop,0,variable_region,lock,process_number + '.' + str(process_count.value-start_process_count+1),process_path,process_count,terminate_flag,process_count.value,1,assertF,asl2,pcASSERT,dir,dir2,comAS,oprAS,terminatePOS))
            process_count.value=process_count.value+1
        end_process_count = process_count.value
        for i in range(start_process_count,process_count.value,1):
            process[i].start()
        terminate_count=0
        for i in range(0,100,1):
            already_terminate[i]=0
        t3=tables[0:0+4]
        s3=re.search(r'\d+',t3)
        while True:
            for i in range(start_process_count,end_process_count,1):
                if terminate_flag[i]>=1 and already_terminate[i]==0:
                    process[i].terminate()
                    process[i].join()
                    already_terminate[i]=1
                    terminate_count=terminate_count+1
                    if not process[i].is_alive():
                        process[i].join()
                    if terminate_flag[i]==2:
                        notterminate+=1
            if terminate_count==end_process_count-start_process_count:
                pre=pc
                lock.acquire()
                return (count_pc-int(s3.group())+1,pre,stack,top,rtop,tablecount,process_path,notterminate)
        for i in range(start_process_count,process_count.value,1):
            process[i].join()
        a=count_pc-int(s3.group())

        pre=pc
        lock.acquire()
        return (a,pre,stack,top,rtop,tablecount,process_path)
    elif com[pc]==27:#r_merge 逆向きのmerge
        pre=pc
        return (pc+1,pre,stack,top,rtop,tablecount,process_path,notterminate)

#命令を実行していく関数 共有する変数を全て引数としていて返り値は変化する共有変数を返す
def execution(command,opr,comb,oprb,start,end,count_pc,stack,address,value,tablecount,rstack,lstack,rtop,ltop,endflag,variable_region,lock,process_number,process_path,process_count,terminate_flag,flag_number,direction,assertF,asl2,pcASSERT,dir,dir2,comAS,oprAS,terminatePOS):##開始アドレス終了アドレス方向
    pc=start
    pre=pc
    top=len(stack)
    ##global assertF
    global assertProcess
    num_variables = tablecount.value
    #順方向
    if direction==0:
        print('Process{0}が順方向実行開始'.format(process_number))
        print(pc)
        print(end)
        print(command[pre])
        while ((pc!=end or command[pre]==15) and assertF.value==1):
          if direction==1:
            break
          else:
            lock.acquire()
            if command[pc]==1:
                command1='   ipush'
            elif command[pc]==2:
                command1='    load'
            elif command[pc]==3:
                command1='   store'
            elif command[pc]==4:
                command1='     jpc'
            elif command[pc]==5:
                command1='     jmp'
            elif command[pc]==6:
                command1='      op'
            elif command[pc]==7:
                command1='   label'
            elif command[pc]==8:
                command1='     par'
            elif command[pc]==9:
                command1='   alloc'
            elif command[pc]==10:
                command1='    free'
            elif command[pc]==11:
                command1='    proc'
            elif command[pc]==12:
                command1='p_return'
            elif command[pc]==13:
                command1='   block'
            elif command[pc]==14:
                command1='     end'
            elif command[pc]==15:
                command1='    fork'
            elif command[pc]==16:
                command1='   merge'
            elif command[pc]==17:
                command1='    func'
            elif command[pc]==18:
                command1='f_return'
                #elif command[pc]==19:
                #command1=' w_label'
                #elif command[pc]==20:
                #command1='   w_end'
            elif command[pc]==19:
                command1='     nop'
            with open("output.txt",'a') as f:
                f.write("~~~~~~~~Process"+process_number+" execute~~~~~~~~\n")
                f.write("path : "+process_path+"\n")
                f.write("pc = "+str(pc+1)+"   command = "+command1+":"+(str)(command[pc])+"    operand = "+str(opr[pc])+"\n")
            print("~~~~~~~~Process"+process_number+" execute~~~~~~~~")
            print("path : "+process_path)
            print("pc = "+str(pc+1)+"   command = "+command1+":"+(str)(command[pc])+"    operand = "+str(opr[pc])+"")
            ##PCがassertにあるか　DIRが一致　assertの条件評価→stop停止フラグ
            for i in range(0,asl2,1):
                if pc == pcASSERT[i]:
                    if dir[i] == 'FWD':
                        assert_re=executionAS(comAS[i],oprAS[i],process_path,value)
                        if assert_re==1:
                            assertF.value=0
                            ##assertProcess.value=flag_number
                            ##print(i)
                            print("################################################################################################")
                            print("STOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOPSTOP")
                            print("################################################################################################")
                            print('Process{0}が停止しました'.format(process_number))
                            ########nyuryoku yameru- jun-noaction,assertF==C gyaku-live-gyaku or die-same(zettaiandsotai)
                            ##next=int(input("次の動作を入力(順方向実行=0, 逆方向実行=1, 終了=2): "))
                            ##next=sys.stdin.readline()
                            ##次の動作により場合分け
                            ##print(i)
                            ##print(dir)
                            ##print(dir2)
                            if dir2[i]==0:
                                assertF.value=1
                                direction=0
                                print('次の動作は順方向実行です')
                            elif dir2[i]==1:
                                assertF.value=1
                                direction=1
                                print('次の動作は逆方向実行です')
                            elif dir2[i]==2:
                                exit()
            ##print(flag_number)
            ##print(terminate_flag[flag_number])   ##
            ##print(process_number)   ##子プロセスの番号（0.1,0.2,0.3....）
            ##print(assertF.value)   ##実行か停止か（0→停止, 1→実行）
            if assertF.value==1 and direction==0:
                print('Process{0}が順方向実行中'.format(process_number))
            #各命令を実行する/////////////////////////////////////////////////////////////////////////
                (pc,pre,stack,top,rtop,tablecount,process_path,notterminate)=executedcommand(stack,rstack,lstack,command,opr,pc,pre,top,rtop,ltop,address,value,tablecount,variable_region,lock,process_number,process_path,count_pc,process_count,terminate_flag,flag_number)
                if command[pre]==15:
                    if notterminate>0:
                        direction=1
                    with open("output.txt",'a') as f:
                        f.write("---fork end--- (process "+process_number+")\n")
                    print("---fork end--- (process "+process_number+")")
                with open("output.txt",'a') as f:
                    f.write("executing stack:       "+str(stack[0:])+"\n")
                    f.write("shared variable stack: "+str(value[0:tablecount.value])+"\n")
                    f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
                print("executing stack:       "+str(stack[0:])+"")
                print("shared variable stack: "+str(value[0:tablecount.value])+"")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                #if command[pre] == 10:
                #    with open("variable_region.txt",'w') as f:
                #        for i in range(0,num_variables,1):
                #            f.write(""+str(variable_region[i])+" ")          
                lock.release()
            else:
                lock.release()
                ##print(process_number)
                ##terminate_flag[flag_number]=1 ##process_count
                ##exit() ######################################################################
        #プロセスが終了したらterminate_flagを1にする
        ##print(flag_number)   ##子プロセスの番号（0,1,2....）
        ##print(start)   ##子プロセスの開始PC
        ##print(end)   ##子プロセスの終了PC
        ##print(terminate_flag[flag_number])   ##その子プロセスが終了したか否か()
        if direction==0:   ##正常
            print('開始PCが{0}:終了PCが{1}の'.format(start,end))
            print('Process{0}が終了しました'.format(process_number))
            terminatePOS[flag_number]=[start,end]
            terminate_flag[flag_number]=1
        else:   ##assert
            ##pc=count_pc+1-pc
            ##pre=count_pc+1-pre
            terminatePOS[flag_number]=[start,pc]
            terminate_flag[flag_number]=2

    #逆方向
    if direction==1:
        print('Process{0}が順方向実行開始'.format(process_number))
        print(pc)
        print(end)
        print(command[pre])
        while (pc!=end or command[pre]==26) and assertF.value==1:
          if direction==0:
            break
          else:
            lock.acquire()
            if command[pc]==21:
                command1='    rjmp'
            elif command[pc]==22:
                command1='  restore'
            elif command[pc]==23:
                command1='     par'
            elif command[pc]==24:
                command1=' r_alloc'
            elif command[pc]==25:
                command1='  r_free'
            elif command[pc]==26:
                command1='  r_fork'
            elif command[pc]==27:
                command1=' r_merge'
            elif command[pc]==28:
                command1='     nop'
            s=re.search(r'\d(\.\d+)*',lstack[ltop.value+1])
            s2=re.search(r'\d(\.\d+)*',rstack[rtop.value+1])
            #restore,r_alloc,rjmp命令では各値スタック,ラベルスタックトップのプロセス番号と一致しているかどうかを確認する
            if (process_number==s2.group() and (command[pc]==22 or command[pc]==24)) or (process_number==s.group() and command[pc]==21) or (command[pc]!=21 and command[pc]!=22 and command[pc]!=24):
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                with open("reverse_output.txt",'a') as f:
                    f.write("~~~~~~~~Process"+process_number+" execute~~~~~~~~\n")
                    f.write("path : "+process_path+"\n")
                    f.write("pc = "+str(pc+1)+"("+str(count_pc-pc)+")   command = "+command1+":"+(str)(command[pc])+"    operand = "+str(opr[pc])+"\n")
                print("~~~~~~~~Process"+process_number+" execute~~~~~~~~")
                #print("path : "+process_path)
                print("pc = "+str(pc+1)+"("+str(count_pc-pc)+")   command = "+command1+":"+(str)(command[pc])+"    operand = "+str(opr[pc])+"")
                print('Process{0}が逆方向実行中'.format(process_number))
                #各命令を実行する
                (pc,pre,stack,top,rtop,tablecount,process_path)=executedcommand(stack,rstack,lstack,command,opr,pc,pre,top,rtop,ltop,address,value,tablecount,variable_region,lock,process_number,process_path,count_pc,process_count,terminate_flag,flag_number)
                if command[pre]==26:
                    with open("reverse_output.txt",'a') as f:
                        f.write("---fork end--- (process "+process_number+")\n")
                    print("---fork end--- (process "+process_number+")")
                with open("reverse_output.txt",'a') as f:
                    f.write("shared variable stack: "+str(value[0:tablecount.value])+"\n\n")
                print("shared variable stack: "+str(value[0:tablecount.value])+"\n")
            lock.release()
        terminate_flag[flag_number]=1
    return stack   ##None     

#pcの値を逆に
def pcCHANGE(pc,count_pc):
    pc=count_pc+1-pc
    return(pc)

#assert用のコードを読み取り各リストに格納する
def assertread():
    global comAS
    global oprAS
    global pcASSERT
    global dir
    global dir22
    global dir2
    global asl2
    f=open("assert.txt",mode='r')
    asserts=f.read()
    f.close()
    ##print(asserts)
    #先頭の空白除去
    asasas=asserts.strip()
    ##print(asasas)
    #\nを除去
    asasa=asasas.replace('\n','')
    ##print(asasa)
    #コンマで区切りリストへ
    asas=asasa.split(',')
    #''リストを除去
    asa=[i for i in asas if i!='']
    ##print(asa)
    #二重→aslist1
    for i in range(0,len(asa),9):
        asaslist1=asa[i:i+9]
        aslist1.append(asaslist1)
    ##print(asaslist1)
    ##print(aslist1)
    #pcASの値をaslist1から取り出しintに
    for i in range(0,len(aslist1),1): 
        pcAS1.append(aslist1[i][2])
    ##print(pcAS1)
    pcASSERT=[int(i) for i in pcAS1] 
    ##print('pcASSERT = {0}'.format(pcASSERT))
    #dirをaslist1から取り出す
    for i in range(0,len(aslist1),1): 
        dir.append(aslist1[i][0])
    ##print('dir = {0}'.format(dir))
    #dir2をaslist1から取り出す
    for i in range(0,len(aslist1),1): 
        dir22.append(aslist1[i][1])
    dir2=[int(i) for i in dir22]
    ##print('dir2 = {0}'.format(dir2))
    ##print(dir2[0])
    #aslist2
    for i in range(0,len(aslist1),1): 
        aslist2.append(aslist1[i][3:])
    asl2=len(aslist2)
    ##print(aslist2)
    #comAS
    for j in range(0,len(aslist1),1): 
        for i in range(0,len(aslist2[0]),2): 
            comAS11.append(aslist2[j][i])
    ##print(comAS11)
    comAS1=[int(i) for i in comAS11] 
    for i in range(0,len(comAS1),len(aslist2[0])//2):
        comAS2=comAS1[i:i+len(aslist2[0])//2]
        comAS.append(comAS2)
    ##print('comAS = {0}'.format(comAS))
    #oprAS
    for j in range(0,len(aslist1),1): 
        for i in range(1,len(aslist2[0]),2): 
            oprAS11.append(aslist2[j][i])
    ##print(oprAS11)
    oprAS1=[int(i) for i in oprAS11] 
    for i in range(0,len(oprAS1),len(aslist2[0])//2):
        oprAS2=oprAS1[i:i+len(aslist2[0])//2]
        oprAS.append(oprAS2)
    ##print('oprAS = {0}'.format(oprAS))



#実行用のコードを読み取り各リストに格納する
def coderead():
    global codes
    global com
    global comb
    global opr
    global oprb
    global count_pc
    global parflag
    f=open(args[1],mode='r')
    codes=f.read()
    f.close()
    for i in range(0,len(codes),9):
        t1=codes[i:i+2]
        s1=re.search(r'\d+',t1)
        t2=codes[i+2:i+8]
        s2=re.search(r'\d+',t2)
        com.append((int)(s1.group()))
        opr.append((int)(s2.group()))
        comb=oprb
        oprb=1
        #comb.append((int)(s1.group()))
        #oprb.append((int)(s2.group()))
        count_pc=count_pc+1
    ##print('com = {0}'.format(com))
    ##print('opr = {0}'.format(opr))
    

#順方向の各命令を逆方向の命令へ変換する
def forward(com,opr,count_pc,comb,oprb):
    f2=open("inv_code.txt",mode='w')
    for i in range(0,count_pc,1):
        if com[count_pc-i-1]==7:#label to rjmp
            ##comb.append((int)21)
            ##oprb.append(0)
            f2.write("21     0\n")
        elif com[count_pc-i-1]==3:#store to restore
            ##comb.append(22)
            ##oprb.append(0)
            f2.write("22 "+str(opr[count_pc-i-1]).rjust(5)+"\n")
        elif com[count_pc-i-1]==4:#jpc to nop
            ##comb.append(28)
            ##oprb.append(0)
            f2.write("28     0\n")
        elif com[count_pc-i-1]==5:
            ##comb.append(28)
            ##oprb.append(0)
            f2.write("28     0\n")#jmp to nop
        elif com[count_pc-i-1]==8:#par to par
            if opr[count_pc-i-1]==0:
                f2.write("23 "+str(1).rjust(5)+"\n")
            elif opr[count_pc-i-1]==1:
                f2.write("23 "+str(0).rjust(5)+"\n")
        elif com[count_pc-i-1]==9:#alloc to r_free
            f2.write("25 "+str(opr[count_pc-i-1]).rjust(5)+"\n")
        elif com[count_pc-i-1]==10:#free to r_alloc
            f2.write("24 "+str(opr[count_pc-i-1]).rjust(5)+"\n")
        elif com[count_pc-i-1]==11:#proc to rjmp
            pname="p"+str(opr[count_pc-i-1])
            f2.write("21 "+pname.rjust(5)+"\n")
        elif com[count_pc-i-1]==12:#p_return to nop
            pname="p"+str(opr[count_pc-i-1])
            f2.write("28 "+pname.rjust(5)+"\n")
        elif com[count_pc-i-1]==13:#block to nop
            if com[count_pc-i]==5 and com[count_pc-i+1]==7 and com[count_pc-i+2]==16:
                bname="c"+str(opr[count_pc-i-1])
            else:
                bname="b"+str(opr[count_pc-i-1])
            f2.write("28 "+bname.rjust(5)+"\n")
        elif com[count_pc-i-1]==14:#end to nop
            if com[count_pc-i-2]==7 and com[count_pc-i-3]==5 and com[count_pc-i-4]==15:
                bname="c"+str(opr[count_pc-i-1])
            else:
                bname="b"+str(opr[count_pc-i-1])
            f2.write("28 "+bname.rjust(5)+"\n")
        elif com[count_pc-i-1]==15:#fork to r_merge
            aname="a"+str(opr[count_pc-i-1])
            f2.write("27 "+aname.rjust(5)+"\n")
        elif com[count_pc-i-1]==16:#merge to r_fork
            aname="a"+str(opr[count_pc-i-1])
            f2.write("26 "+aname.rjust(5)+"\n")
        elif com[count_pc-i-1]==17:#func to rjmp
            fname="f"+str(opr[count_pc-i-1])
            f2.write("21 "+fname.rjust(5)+"\n")
        elif com[count_pc-i-1]==18:#f_return to nop
            fname="f"+str(opr[count_pc-i-1])
            f2.write("28 "+fname.rjust(5)+"\n")
            #elif com[count_pc-i-1]==19:#w_label to rjmp
            #wname="w"+str(opr[count_pc-i-1])
            #f2.write("31 "+wname.rjust(5)+"\n")
            #elif com[count_pc-i-1]==20:#w_end to rjmp
            #wname="w"+str(opr[count_pc-i-1])
            #f2.write("31 "+wname.rjust(5)+"\n")
        else:
            f2.write("28     0\n")
    f2.close()


#順方向実行の出力
#プロセス番号
#パス
#プログラムカウンタ 命令 被演算子
#演算スタック
#共有変数スタック

#逆方向の出力
#プロセス番号
#プログラムカウンタ(順方向のプログラムカウンタ) 命令 被演算子
#共有変数スタック

if __name__ == '__main__':
    start_time = time.time()
    start=[]
    end=[]
    tabledata=[]
    tablecount= Value('i',0)
    address = Array('i',10)
    value = Array('i',100000)   #100→1000:n<=10    #100→10000:n<=15
    rstack = Array('i',100000)
    lstack = Array('i',100000)
    rtop = Value('i',0)
    ltop = Value('i',0)
    endflag={}
    endflag0=Value('i',0)
    notlabelflag=0
    lock=Lock()
    variable_region = []
    process_number='0'
    process_path='E'
    process_count = Value('i',0)
    terminate_flag = Array('i',100)
    assertF = Value('i',1)
    assertProcess = Value('i',-1)
    import multiprocessing 
    multiprocessing.set_start_method('spawn', True)
    for i in range(0,100,1):
        terminate_flag[i]=0
    
    mlock = Lock()
    lockfree  = Lock()
    a='1'
    path='table.txt'
    f=open(path,mode='r')
    tabledata=f.read()
    f.close()
    #順方向では共有変数テーブル,値スタック,ラベルスタック,出力ファイルを開く
    if args[2]=='f':
        with open("variable_table.txt",'w') as f:
            f.write("")
        f.close()
        with open("value_stack.txt",'w') as f:
            f.write("")
        f.close()
        with open("label_stack.txt",'w') as f:
            f.write("")
        f.close()
        with open("output.txt",'w') as f:
            f.write("")
        f.close()
    elif args[2]=='b':#逆方向も同様に各ファイルを開き,ラベルスタック,値スタックの情報をリストに保存する
        with open("variable_table.txt",'w') as f:
            f.write("")
        f.close()
        with open("label_stack.txt",'r') as f:
            label_stack=f.read().split()
        ltop.value=len(label_stack)-2
        with open("value_stack.txt",'r') as f:
            value_stack=f.read().split()
        rtop.value=len(value_stack)-2
        with open("reverse_output.txt",'w') as f:
            f.write("")
        f.close()
    k=0
    #実行バイトコードの読み取り
    coderead()
    assertread()

    #順方向実行
    if args[2]=='f':
        execution(com,opr,comb,oprb,0,count_pc,count_pc,stack,address,value,tablecount,rstack,lstack,rtop,ltop,endflag0,variable_region,lock,process_number,process_path,process_count,terminate_flag,0,0,assertF,asl2,pcASSERT,dir,dir2,comAS,oprAS,terminatePOS)
        ##if terminate_flag[0]==1:

        ##elif terminate_flag[0]==2:
            ##input(next="再開方向：")
            ##execution(com,opr,comb,oprb,count_pc-terminatePOS[0][1]+1,count_pc,count_pc,stack,address,value,tablecount,rstack,lstack,rtop,ltop,endflag0,variable_region,lock,process_number,process_path,process_count,terminate_flag,0,1,assertF,asl2,pcASSERT,dir,dir2,comAS,oprAS,terminatePOS)
    elif args[2]=='c':#順方向バイトコードから逆方向バイトコードへ変換
        forward(com,opr,count_pc)
    elif args[2]=='b':#逆方向実行
        execution(com,opr,comb,oprb,0,count_pc,count_pc,stack,address,value,tablecount,value_stack,label_stack,rtop,ltop,endflag0,variable_region,lock,process_number,process_path,process_count,terminate_flag,0,1,assertF,asl2,pcASSERT,dir,dir2,comAS,oprAS,terminatePOS)

    elapsed_time = time.time()-start_time
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")