# Quiz master

from pathlib import Path
import random as ra
import sys

ap = Path.cwd()/'answ.txt'
qp = Path.cwd()/'ques.txt'
op = Path.cwd()/'opts.txt'
qes=[]
ans=[]
ops=[]
ls=[]
points=0
with qp.open(mode = 'r') as qf:
	qes=qf.readlines()

with ap.open(mode='r') as af:
	ans=af.readlines()

with op.open(mode='r') as of:
	ops=of.readlines()


def random_num():
	global ls
	if len(ls)==len(qes):
		sys.exit('End of Questions')
	rnum=ra.randint(0,len(qes))
	if rnum not in ls:
		ls.append(rnum)
		question(rnum)
		options(rnum)
	else:
		random_num()

def question(num):
	print(qes[num])
	print(len(qes))

def options(num):
	print(ops[num])

def answer(ch):
	global points
	ans_num=ls[-1]
	if ch.upper()==ans[ans_num].rstrip('\n'):
		print('Correct')
		points+=1
	else:
		print('Wrong')

print("Quiz Master")
print('Questions and Options are Given')
print('Enter your option as (A/B/C/D) or (Q) to quit')
print('Lets Start')

while True:
	print('continue (c) or quit (q) for points (p)')
	ch=input('\t>')
	if ch.upper()=='Q':
		print(f'You scored {points}')
		sys.exit('You Quit :(')
	elif ch.upper()=='P':
		print(f'current points: {points}')
	elif ch.upper()=='C':
		random_num()
		ans_ch=input('\t>')
		answer(ans_ch)

	else:
		print('Invalid choice')
