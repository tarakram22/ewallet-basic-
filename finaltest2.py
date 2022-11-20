import datetime
from ssl import AlertDescription
import bcrypt
import pandas as pd
import prettytable
import pwinput
from pytz import timezone

class Auth:
    def __init__(self):
        self.data={'mom':{'mother':'mommy'},'dad':{'father':'daddy'},'ron':{'child':'ronny'},'harry':{'child':'har'},'mike':{'child':'mikey'},'wil':{'child':'wilson'},'rob':{'child':'robert'},'ray':{'child':'raymond'},'john':{'child':'johnathan'},'jen':{'child':'jenny'}}
    def login(self, username, password):
        if username not in self.data:
            return 'user not found',username,'notfound'
        else:
            user=list(self.data[username].keys())[0]
            if self.data[username][user]==password:
                x=True
            else:
                x=False
            return x,user,username
    def ulogin(self,user):
        if user=='mother':
            username=input('enter the username : ')
            password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
            if self.data[username]['mother']==password:
                x=True
            else:
                x=False
            return x
        elif user=='father':
            username=input('enter the username : ')
            password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
            if self.data[username]['father']==password:
                x=True
            else:
                x=False
            return x
        elif user=='child':
            username=input('enter the username : ')
            password = pwinput.pwinput(prompt='Enter your password: ', mask='*')
            if self.data[username]['child']==password:
                x=True
            else:
                x=False
            return x
    def block(self,user,username):
        # self.data=self.data.pop(username)
        k,v=username,self.data.pop(username)
        self.blockeduser.update({k:v})
        print(self.data)
        # print(self.data)

        

# a=Auth()
# status,user,username=a.login('mom','mommy')
# print(status,user,username)



class Parents(Auth):
    def __init__(self):
        super().__init__()
        self.balance=98.000
        self.bank_account=[]
        self.blockeduser={}
        tdf={'user': [],'username':[],'amount':[],'date&time':[],'type_of_transcation':[]}
        self.tdf=pd.DataFrame(tdf)
    def transactions(self,buser,username,amt,type_of_transcation):
        # tran = {'user': [],'username':[],'amount':[],'date&time':[],'type_of_transcation':[]}
        # tran["user"].append(buser)
        # tran["username"].append(username)
        # tran["amount"].append(amt)
        # tran['type_of_transcation'].append(type_of_transcation)
        # tran["date&time"].append(datetime.datetime.now())
        # tdf = pd.DataFrame(tran)
        # tdf['count']=tdf['username'].value_counts()
        # tdf['count'] = tdf['username'].map(tdf['username'].value_counts())
        # tdf=tdf[['username','date']].value_counts().reset_index()
        # tdf['date&time']=tdf['date&time']
        # tdf['dt']=pd.to_datetime(tdf['date&time']).dt.date
        # tdf.rename(columns={0: "count"}, inplace=True)
        # tdf['dt']=pd.to_datetime(tdf['dt']).dt.date
        self.tdf = self.tdf.concat({'user':buser, 'username': username, 'amount':amt,'date&time':datetime.datetime.now(),'type_of_transaction':type_of_transcation }, ignore_index=True)
        self.tdf['dt']=pd.to_datetime(self.tdf['date&time']).dt.date
        # self.tdf=self.tdf.update(tdf)
    def bal(self):
        if self.balance<100:
            return True 
        else:
            return False
    def his(self):
        print(self.tdf)
    def acc(self,user,username):
        if ((user =='mother' and username=='mom') or (user=='father' and username=='dad')):
            if not self.bank_account:
                ipba=int(input('please enter the bank account number(16digit)\n : '))
                if len(str(ipba))==16:
                    self.bank_account.append([ipba])
                    return True,'acc_update'
                else:
                    print('please enter a valid account number')
                    return False,'invalid_acc_no'
            else:
                if len(self.bank_account)==1:
                    op=int(input('select the following option\n 1-use the existing bank account ending with **** **** **** '+str(self.bank_account[0][0])[-4:]+'\n 2-add a second bank account \n 3-change the existing bank account\n : '))
                    if op==1:
                        print('using the bank account ending with **** **** **** '+str(self.bank_account[0][0])[-4:])
                        return True,'acc_used'
                    elif op==2:
                        ipba=int(input('please enter the second bank account number(16digit) \n : '))
                        if len(str(ipba))==16:
                            self.bank_account.append([ipba])
                            return True,'acc_update'
                        else:
                            print('please enter a valid account number')
                            return False,'invalid_acc_no'
                    elif op==3:
                        ipba=int(input('please enter the second bank account number(16digit) \n : '))
                        if len(str(ipba))==16:
                            self.bank_account[0][0]=ipba
                            return True,'acc_update'
                        else:
                            print('please enter a valid account number')
                            return False,'invalid_acc_no'
                    else:
                        print('invalid input')
                        return False,'invalid_ip'
                elif len(self.bank_account)==2:
                    op=int(input('select the following option \n 1-bank account ending with **** **** **** '+str(self.bank_account[0][0])[-4:]+'\n 2- a second bank account ending with **** **** **** '+str(self.bank_account[1][0])[-4:] +'\n 3-change the bank account'))
                    if op==1:
                        print('using self.bank_account ending with **** **** **** '+str(self.bank_account[0][0])[-4:])
                        return True,'acc_used'
                    elif op==2:
                        print('using self.bank_account ending with **** **** **** '+str(self.bank_account[1][0])[-4:])
                        return True,'acc_used'
                    elif op==3:
                        op=input('select option which acccount do u want to change \n 1- bank account ending with **** **** **** '+str(self.bank_account[0][0])[-4:] +'\n 2-bank account ending with **** **** **** '+str(self.bank_account[1][0])[-4:])
                        if op==1 or op==2:
                            ipba=int(input('please enter the bank account number(16digit) u wish to add \n : '))
                            if len(str(ipba))==16:
                                if op==1:
                                    self.bank_account[0][0]=ipba
                                    return True,'acc_updated'
                                else:
                                    self.bank_account[1][0]=ipba
                                    return True,'acc_update'       
                            else:
                                print('please enter a valid account number')
                                return False,'invalid_acc_no'
                        else:
                            return False,'invalid_ip'     
                    else:
                        return False,'invalid_ip'
                else:
                    return False,'asdfdsa'
        else:
            print('you are not authorized')
            return False,'not_authorized'
    def deposit(self,buser,username,d_amount):
        status,msg = self.acc(buser,username) 
        if status==True and msg=='acc_update':
            print('bank account updated')
            main() 
        elif status==True and msg=='acc_used':
            self.balance = self.balance+float(d_amount)
            self.transactions(buser,username,d_amount,'credit')
            print("\n Amount Deposited:",d_amount)
            main()
        else:
            print('deposit failed')
            main()
    def withdraw(self,buser,username,w_amount):
        print(buser,username,w_amount,self.balance)

        if w_amount>self.balance:
            print('\n Insufficient balance ')
            dn=input('would like to add money to your wallet \n y-yes \n n-no \n :')
            if dn=='y':
                at=input('enter the amount')
                self.deposit(buser,username,at)
            else:
                main()
        else:
            self.balance=self.balance-float(w_amount)
            self.transactions(buser,username,w_amount,'debit')
            print("\n You Withdrew:", w_amount)
    



class Wallet(Parents):
    def __init__(self):
        super().__init__()

    def bal(self):
        if self.balance<100:
            return True
        else:
            return False
    def payment(self,buser,username):
        # if self.balance<100:
        #     n.alerts(buser,username,'insufficient')
        if ((buser =='mother' and username=='mom') or (buser=='father' and username=='dad')):
            sname=input('please enter the name of the shop/org')
            inter=input('please enter the interact id')
            pamount=int(input('enter the amount'))
            if pamount<self.balance:
                print('insufficient balance')
                n.alerts(buser,username)
            else:
                self.balance=self.balance-pamount
                self.transactions(buser,username,pamount,'payment_debit')
                print('payment made sucessfully to'+sname+'id'+inter)
        elif buser=='child':
            sname=input('please enter the name of the shop/org')
            inter=input('please enter the interact id')
            pamount=int(input('enter the amount'))  
            if pamount >50:
                p=n.requests(buser,username,pamount)
                if p==True:
                    print('payment sucessfull')
                    self.transactions(buser,username,pamount,'debit-payment')

            if (not self.tdf['username']==username) and (pamount<50):
                self.balance=self.balance-pamount
                self.transactions(buser,username,pamount,'payment_debit')
            else:
                dl=self.tdf.loc[self.tdf['username']==username]
                if len(dl.index)<2:
                    bamt=int(dl.iloc[0]['amount'])
                    print('your daily balance quote is= '+str(50-bamt))
                    op=input('do you wish to use the daily balance amount to pay y-yes n-no')
                    if op=='y':
                        sname=input('please enter the name of the shop/org')
                        inter=input('please enter the interact id')
                        pamount=int(input('enter the amount'))
                        if pamount<=bamt:
                            self.balance=self.balance-pamount
                            self.transactions(buser,username,pamount,'payment_debit')
                        else:
                            print('entered amount is greater than the daily balance u have')
                            ip=input('do you wish to ask for the permission from mom y-yes n-no')
                            if ip =='y':
                                req= n.requests(buser,username,'hjgjg')
                                if req ==True:
                                    print('asfdasd')


                else:
                    re=input('would u like to request mom y-yes n-no')
                    if re =='y':
                        req= n.requests(buser,username,'123421')
                        if req ==True:
                            sname=input('please enter the name of the shop/org')
                            inter=input('please enter the interact id')
                            pamount=int(input('enter the amount'))
                            if self.balance>pamount:
                                self.balance=self.balance-pamount
                                self.transactions(buser,username,pamount,'payment_debit')
                            else:
                                print('insufficient balance')
                                dyn=input('request parents for wallet deposite y-yes n-no')
                                if dyn=='y':
                                    n.alerts(buser,username,bal,'request')
                                else:
                                    main()

    # def check_balance(self):
    #     if self.balance<100:
    #         return True
    #     else:
    #         return False


class Notifications(Parents):
    def __init__(self):
        super().__init__()
        pass
    def alerts(self,buser,username,msg=None):
        if msg == None:
            if self.balance<100:
                ipt=input('do you wish to add amount into wallet\n yes-y \n no-n \n :')
                if ipt=='y':
                    dmt=float(input('enter the amount u wish to deposit \n : '))
                    p.deposit(buser,username,dmt)
                else:
                    return False
            else:
                return False
        elif msg=='drequest':
            parent=input('whom do u want to request the deposit \n mom-m \n dad-d :')
            if parent=='m':
                x=a.ulogin('mother')
            elif parent=='d':
                x=a.ulogin('father')
            else:
                print('invalid input')
                main()
        elif msg =='insufficient':
            print('low balance less than 100 in wallet')
            ipt=input('do you wish to add amount into wallet\n yes-y \n no-n \n :')
            if ipt=='y':
                dmt=float(input('enter the amount u wish to deposit \n : '))
                p.deposit(buser,username,dmt)
            elif ipt=='n':
                print('exiting to the main menu')
                main()

    def requests(self,buser,username,amt):
        if len(self.tdf.loc[((self.tdf['username']==username) & (self.tdf['date']==datetime.date.today()))])>=1:
            parent=input('select whom would you like to get permission from mother-m father -f')
            if parent =='m':
                st=a.ulogin('mother')
                if st==True:
                    transfer=input('do you wish to transfer the request to father \n yes-y \n no-n \n :')
                    if transfer=='y':
                        st=a.ulogin('father')
                        if st== True:
                            pass
                    else:
                        print('do you authorized the transaction')
                        a=input('\n yes-y \n no-n \n :')
                        if a=='y':
                            pass

                    
                    
            elif parent =='f':       
                s=a.ulogin('mother')
                if s==True and usr=='mother':
                    print('please provide permission')
                    yn=input('y-yes ,n-no','transfer the request to father-t')
                    if yn=='y':
                        print('permission granted')
                        return True
                    elif yn=='n':
                        print('permission denied')
                        return False
                    elif yn=='t':
                        print('please enter fathers credentials')
                        usn=input('username')
                        pwd=input('password')
                        s,usr,u=a.login(usn,pwd)
                        if s==True and usr=='father':
                            print('please provide permission')
                            yn=input('y-yes ,n-no','transfer the request to father-t')
                            if yn=='y':
                                print('permission granted')
                                return True
                            elif yn=='n':
                                print('permission denied')
                                return False
                            else:
                                print('entered incorrect credentials')
                                main()
                else:
                    print('entered incorrect credentials')
                    main()



a = Auth()
p = Parents()
w = Wallet()
n = Notifications()
def main():
    usn=input('enter the username : ')
    pwd = pwinput.pwinput(prompt='Enter your password: ', mask='*')
    # pwd=input('enter the password : ')
    status,user,username=a.login(usn,pwd)
  # self.bank_account=[]
  # if wallet amount is equal to 0 should exit
    if ((status ==True) and (user=='father')) or ((status ==True) and (user=='mother')):
        lb=p.bal()
        if lb == True:
            print('low balance in the wallet less than 100$')
            r=input('do you wish to recharge the wallet \n yes-y \n no-n \n : ')
            if r=='y':
                d=float(input('enter the amount you wish deposit \n : $ '))
                p.deposit(user,username,d)
        choice=int(input('please select one of the following option \n 1:deposit \n 2-withdraw \n 3-pay/payment \n 4-block user \n 5-transaction statement \n 6-quit \n :  '))
        if choice==1:
            print(choice)
            amt=input('enter the amount you want to deposit \n : $ ')
            p.deposit(user,username,amt)
        elif choice==2:
            print(choice)
            wamount=float(input('enter the amount you want to withdraw'))
            withd=p.withdraw(user,username,wamount)
        elif choice==3:
            print(choice)
            w.payment
        elif choice==4:
            if status ==True and user=='father' and username=='dad':
                x = prettytable.PrettyTable()
                x.field_names = ["Sr.no.", "User", "username", "enter the option to select"]
                x.add_row(['i', 'Mother', 'mom', 1])
                x.add_row(['ii', 'Child','ron',2])
                x.add_row(['iii', 'Child','harry', 3])
                x.add_row(['iv', 'Child','mike',4])
                x.add_row(['v', 'Child','wilson', 5])
                x.add_row(['vi', 'Child','rob',6])
                x.add_row(['vii', 'Child','ray',7])
                x.add_row(['viii', 'Child','john',8])
                x.add_row(['ix', 'Child','jen',9])
                busr=int(input(str(x)+'-\n option : '))
                cnf=input('selected user:-'+str(x[busr-1])+'\n'+'do you wish to move ahead y-yes n-no : ')
                if cnf=='y':
                    if busr==1:
                        user='mother'
                        username='mom'
                        print(user,username)
                        p.block(user,username)
                        main()
                    elif busr==2:
                        user='child'
                        username='ron'
                        print(user,username)
                        p.block(user,username)
                        main()
                    elif busr==3:
                        user='child'
                        username='harry'
                        print(user,username)
                        p.block(user,username)
                        main()
                    elif busr==4:
                        user='child'
                        username='mike'
                        print(user,username)
                        p.block(user,username)
                        main()
                    elif busr==5:
                        user='child'
                        username='wilson'
                        print(user,username)
                        p.block(user,username)
                        main()
                    elif busr==6:
                        user='child'
                        username='rob'
                        print(user,username)
                        p.block(user,username)
                        main()
                    elif busr==7:
                        user='child'
                        username='ray'
                        print(user,username)
                        p.block(user,username)
                        main()
                    elif busr==8:
                        user='child'
                        username='john'
                        print(user,username)
                        p.block(user,username)
                        main()
                    elif busr==9:
                        user='child'
                        username='jen'
                        print(user,username)
                        p.block(user,username)
                        main()
                    else:
                        print('u have entered incorrect option')
                        main()
                else:
                    print('exiting')
                    main()
            else:
                print('you are not authorized')
                main()
        elif choice==5:
            p.his()
            main()
        elif choice==6:
            main()
    elif (status ==True) and (user=='child'):
        choice=int(input('please select one of the following option 1-pay/payment 2-request for over pay 6-quit: '))
        print(choice)
    elif status !=True:
        print('entered incorrect credentials ',username)
        main()
if __name__=='__main__':
    main()
    






        
