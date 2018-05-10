import getpass

class adjlist:

	def __init__(self,v,e):

		self.ver=v
		self.ed=e
		self.list=[listnode() for i in range(v)]
		for i in range(v):
			self.list[i].value=i
		self.news=[None for i in range(v)]

	def insertnews(self,r,str2):

		h=self.index(r)
		if (self.news[h]==None):
			self.news[h]="\nPost by:"+r+"\nPost:"+str2+"\n"
		else:
			self.news[h]="\nPost by:"+r+"\nPost:"+str2+"\n"+self.news[h]

	def viewpost(self):

		for i in range(self.ver):
			if (self.news[i]!=None):
				print(self.news[i])
				
	def insert(self,a,b):

		t=listnode()
		t.value=b
		temp=self.list[a].next
		self.list[a].next=t
		t.next=temp
		t=listnode()
		t.value=a
		temp=self.list[b].next
		self.list[b].next=t
		t.next=temp

	def insertnew(self,a,str):

		h=self.index(str)		
		self.insert(a,h)

	def printl(self):

		print("list")
		for i in range(self.ver):
			print(i,":",end=" ")
			t=self.list[i]
			while t.next:
				print(t.next.value,end=" ")
				t=t.next
		print()

	def index(self,name):

		for i in range(self.ver):
			if (name==self.list[i].id):
				return i
		return False

	def validity(self,name):

		h=self.index(name)
		if (h==False):
			print("invalid username")
			return False
		return True

	def passvalid(self,name,passname):

		h=self.index(name)
		if (self.list[h].pwd==passname):
			return True
		print("incorrect password")
		return False

	def lengthst(self,str1):

		return len(str1)

	def deleteacc(self,string5,leng):

		file=open('fb','r')
		s=list(file)
		file.close()
		c=''.join(s)
		x=c.replace("\n","#")
		d=x.find("endsq#"+string5)
		f = open("fb","w")
		for i in range(d):
			f.write(x[i])
		f.close()
		f=open("fb1","w")
		for i in range(d+leng+6,len(x),1):
			f.write(x[i])
		f.close()
		f=open("fb1","r")
		s1=list(f)
		c1=''.join(s1)
		d=c1.find("endsq")
		f.close()
		file=open("fb","a")
		for i in range(d,len(c1),1):
			file.write(c1[i])
		file.close()
		file=open('fb','r')
		s2=list(file)
		file.close()
		c2=''.join(s2)
		x2=c2.replace("#","\n")
		file=open('fb1','w')
		for line in x2:
			file.write(line)
		file.close()
		file=open('fb1','r')
		s3=file.readlines()
		file.close()
		file=open('fb','w')
		for line in s3:
			if line!=string5+"\n":
				file.write(line)
		file.close()

	def deletename(self,str4,lengt):

		file=open('fbn','r')
		ss=list(file)
		file.close()
		cs=''.join(ss)
		xs=cs.replace("\n","")
		ds=xs.find("endqq"+str4)
		f = open("fbn","w")
		for i in range(ds):		
			f.write(xs[i])
		f.close()
		f=open("fbn","a")
		for i in range(ds+lengt+5,len(xs),1):
			f.write(xs[i])
		f.close()
		file=open('fbn','r')
		ss2=list(file)
		file.close()
		cs2=''.join(ss2)
		xs2=cs2.replace("endqq","\nendqq\n")
		file=open('fbn','w')
		for line in xs2:
			file.write(line)
		file.close()

	def search(self,a,b):
		
		t=self.list[a]
		while (t.next):
			if (self.list[t.next.value].id==b):
				return True
			return False

	def printfriends(self,s):

		h=self.index(s)
		t=self.list[h]
		while (t.next):
			print(self.list[t.next.value].id)
			t=t.next
		print()

	def printdet(self,s):

		h=self.index(s)
		print("Userid:",self.list[h].id,"\nPassword::",self.list[h].pwd)

	def suggestions(self,s):

		print("-----------------")
		print("Friends of friends\n")
		q=queue()
		h=self.index(s)
		t=self.list[h]
		t.dist=0
		t.color='yellow'
		q.enqueue(t.value)
		while (not q.isEmpty()):
			u=q.dequeue()
			t=self.list[u].next
			while (t):
				i=t.value
				if (self.list[i].color=='white'):
					self.list[i].dist=self.list[u].dist+1
					if (self.list[i].dist==3):
						return
					if (self.list[i].dist==2):
						print(self.list[i].id,end="\n")
					self.list[i].pred=self.list[u]
					self.list[i].color='yellow'
					q.enqueue(t.value)
				t=t.next
			self.list[u].color='black'

	def prof(self,s,user,password):

		t=self.list[s]
		t.id=user
		t.pwd=password

	def sendmessage(self,name1,message1,r):

		h=self.index(r)
		h1=self.index(name1)
		if (self.list[h1].msg[h]==None):
			self.list[h1].msg[h]=message1
		else:
			self.list[h1].msg[h]=self.list[h1].msg[h]+"\n"+message1

	def inbox(self,name1):

		print("Messages")
		h=self.index(name1)
		for i in range(1000):
			if (self.list[h].msg[i]!=None):
				print("From :",self.list[i].id)
				print("Message :",self.list[h].msg[i])
				print()
		q=int(input("press 1 to clear all the messages"))
		if (q==1):
			f = open("message","r")
			lines = f.readlines()
			f.close()
			f = open("message","w")
			countline=0
			for line in lines:
				if line!=name1+"\n" or countline%3!=1:
					f.write(line)
				else:
					f.write("#\n")
				countline=countline+1
			f.close()
			for i in range(1000):
				self.list[h].msg[i]==None
			print("Messages")
	
	def isFriends(self,p,r,name):

            h=p.index(r)
            t=p.list[h]
            while (t.next):
                if (p.list[t.next.value].id==name):
                    return True
                t=t.next
            return False

class queue:

	def __init__(self):

		self.L=[None for i in range(2000)]
		self.front=0
		self.tail=0

	def enqueue(self,k):

		self.L[self.tail]=k
		self.tail=(self.tail+1)%2000

	def dequeue(self):

		self.front=(self.front+1)%2000
		return self.L[self.front-1]

	def isEmpty(self):

		if(self.front==self.tail):
			return True
		return False


class listnode:

	def __init__(self):
		self.value=0
		self.next=None
		self.dist=0
		self.color='white'
		self.pred=None
		self.id=None
		self.pwd=None
		self.msg=[None for i in range(2000)]



class List:

    def __init__(self):
        self.list1 = []

    def push(self,element):
        self.list1.append(element)

    def pop(self):
        return self.list1.pop()

class queuesearch:

	def __init__(self):

		self.head=listNode()
		self.tail=listNode()
		self.head=self.tail

	def pushtail(self,x):

		self.temp=listNode()
		self.temp.value=x
		self.tail.next=self.temp
		self.tail=self.temp

	def pushfront(self,x):

		self.temp=listNode()
		self.temp.value=x
		self.temp.next=self.head
		self.head=self.temp

	def printq(self):

		self.temp=listNode()
		self.temp=self.head
		while (self.temp.next):
			if (self.temp.value==0):
				self.temp=self.temp.next
				continue
			print(self.temp.value)
			self.temp=self.temp.next
		print(self.temp.value)

class listNode:

	def __init__(self):
		self.value=0
		self.next=None

class Tries:

    def __init__(self):

        self.root=TrieNode()
        self.s=List()
        self.qsearch=queuesearch()
                

    def Index(self,ch):

        return ord(ch)-ord('a')

    def Insert(self,key):

        t=self.root
        for c in key:
            i=self.Index(c)
            if not t.children[i]:
                t.children[i]=TrieNode()
            t=t.children[i]
        t.children[26]='*'
        t.isEnd=True

    def Search(self,key,origin,p):

        qsearch=queuesearch()
        t=self.root
        l=len(key)
        for c in key:
            i=self.Index(c)
            self.s.push(c)
            if not t.children[i]:
                return
            t=t.children[i]
        if t!=None :
            self.extras(t,origin,p)
            self.qsearch.printq()
            return
        else:
            return

    def extras(self,t,origin,p):

        pw=adjlist(2000,15000)
        if t.children[26]=='*':
            end=''.join(self.s.list1)
            if (end==origin):
            	return
            if (pw.isFriends(p,origin,end)):
        	    self.qsearch.pushfront(end)
            else:
            	self.qsearch.pushtail(end)
        if t!=None :
            for i in range(26) :
                if t.children[i]!=None:
                    al=ord('a')+i
                    self.s.push(chr(al))
                    self.extras(t.children[i],origin,p)
                    self.s.pop()
            return

class TrieNode:

        def __init__(self):

                self.children=[None]*27
                self.isEnd=False



def main():

	print("\033c")
	p=adjlist(2000,15000)
	q=1
	T=Tries()
	file=open('fb','r')
	s=list(file)
	file.close()
	f2=open('fbn','r')
	s1=list(f2)
	f2.close()
	f3=open('message','r')
	s3=list(f3)
	f3.close()
	f4=open('newsfeed','r')
	s4=list(f4)
	f4.close()
	counter=20000

	for i in range(len(s)):
		c=[None for w in range(len(s[i])-1)]
		for j in range(0,len(s[i])-1,1):
			c[j]=s[i][j]	
		r=''.join(c)
		if (i==0) or (i==counter+1):
			a=r
		elif (i==1) or (i==counter+2):
			b=r
			p.prof(q,a,b)
		else:	
			if (s[i]!='endsq\n'):
				p.insertnew(q,r)	
				if (i>=len(s)):
					return
			if (s[i]=='endsq\n'):
				q=q+1
				counter=i	

	for i in range(len(s1)):
		c=[None for w in range(len(s1[i])-1)]
		for j in range(0,len(s1[i])-1,1):
			c[j]=s1[i][j]
		r=''.join(c)
		T.Insert(r)

	messagecount=0
	for i in range(len(s3)):
		c1=[None for w in range(len(s3[i])-1)]
		for j in range(0,len(s3[i])-1,1):
			c1[j]=s3[i][j]
		r2=''.join(c1)
		if (messagecount%3==0):
			r=r2
		elif (messagecount%3==1):
			name1=r2
		else:
			message1=r2
			p.sendmessage(name1,message1,r)
		messagecount=messagecount+1

	newscount=0
	for i in range(len(s4)):
		c2=[None for w in range(len(s4[i])-1)]
		for j in range(0,len(s4[i])-1,1):
			c2[j]=s4[i][j]
		r3=''.join(c2)
		if (newscount%2==0):
			r=r3
		else:
			news=r3
			p.insertnews(r,news)
		newscount=newscount+1

	d=int(input("1-profile\n2-create account\n3-delete account\n"))
	print("\033c")

	if (d==3):
		uid=input("enter the name\n")
		if (p.validity(uid)):
			psd=getpass.getpass("enter the password\n")
			if (p.passvalid(uid,psd)):
				le=p.lengthst(uid)
				p.deleteacc(uid,le)
				p.deletename(uid,le)
	if (d==2):
		x=1
		q=q+1

		while (x==1):
			n=input("enter name\n")
			m = input('enter password\n')
			file=open('fb','a')
			file.write(n)
			file.write("\n")
			file.write(m)
			file.write("\n")
			p.prof(q,n,m)
			f2=open('fbn','a')
			f2.write(n)
			f2.write("\n")
			f2.write("endqq\n")
			f2.close()
			T.Insert(n)
			f=input("press y if there are any friends\n")

			while f=='y':
				g=input("enter your friends\n")
				valid1=p.validity(g)	
				if (valid1==True):
					p.insertnew(q,g)
					f=input("enter n if no friends are left\n")
					file.write(g)
					file.write("\n")

			x=int(input("enter 1 to create another account\n"))
			q=q+1
			file.write("endsq\n")
			file.close()
		print("\033c")

	def proceed(r):
		
		print("\033c")
		f=int(input("1-Personal Details\n2-Suggestions\n3-Friends\n4-Search for a friend\n5-Send Message\n6-Inbox\n7-Post\n8-newsfeed\n"))
		print("\033c")
		
		if (f==1):
			print("Details\n")
			p.printdet(r)
		
		elif (f==2):
			print("Friend Suggestions\n")
			p.suggestions(r)
		
		elif (f==3):
			print("Friends\n")
			p.printfriends(r)
		
		elif (f==4):
			strin=input("enter the key to search:\n")
			T.Search(strin,r,p)
		elif (f==5):
			v=1
			while v==1:
				name1=input("enter name\n")
				if (p.validity(name1)):
					message1=input("enter message\n")
					file=open('message','a')
					file.write(r+"\n"+name1+"\n"+message1+"\n")
					file.close()
					p.sendmessage(name1,message1,r)
					v=int(input("press 1 to send again"))
		elif (f==6):
			p.inbox(r)
		elif (f==7):
			news=input("enter the post\n")
			file=open('newsfeed','a')
			file.write(r+"\n"+news+"\n")
			file.close()
			p.insertnews(r,news)
		elif (f==8):
			p.viewpost()

		logout=int(input("enter 0 to logout"))
		return logout

	if (d==1) or (d==2):
		r=input("enter the person\n")
		valid=p.validity(r)	
		if (valid==True):
			secretcode = getpass.getpass('Password:')
			valid2=p.passvalid(r,secretcode)
			y=1
			if (valid2==True):
				y=proceed(r)
				while (y!=0):
					y=proceed(r)

if __name__=='__main__':
	main()
