
from midiutil import MIDIFile
import random
import sys
import math
import pygame.mixer

pygame.mixer.init()
random.seed()

width = 200
height = 200
pixels = width*height
tes = int(pixels ** 0.25)

while True:
    try:       
        nspan = input('expression range (integer) ? ')
        expressrange = int(nspan)
    except:
        continue
    else:
        break


while True:
    try:
        dodrumsplz = input('Drums (Yes or no?)')
    except:
        continue
    else:
        break


def intorfloat():
    if random.randrange(0,2) == 1:
        a = random.randrange(0,expressrange)
    else:
        a = random.random()
    if type(a) == 'int':
        if random.randrange(0,3) == 1:
            a += random.random()
    if random.randrange(0,2) == 1:
        return a
    else:
        return -a


def randq(depth):
    vs = ['Ra','Rb','Rc','Rd','Ga','Gb','Gc','Gd','Ba','Bb','Bc','Bd','C','math.pi','(x+1)','(y+1)','(z+1)','(w+1)','(X+1)','(Y+1)','phi','width','height','pixels']
    erange = random.randrange(1,11)
    equals = [' = ',' += ',' -= ',' /= ',' *= ']
    ops = ['+','-','/','%','*']
    mathfuncs = ['math.log10(','math.sqrt(','math.cos(','math.sin(','math.tan(']
    initv = str(vs[random.randrange(0,len(vs)-6)])
    initv += equals[random.randrange(0,len(equals))]
    for v in range(erange):
        switch = random.randrange(0,depth)
        if switch == 0:
            initv += vs[random.randrange(0,len(vs))]      
        elif switch == 1:
            initv += str(intorfloat())
        elif switch == 2:
            initv += mathfuncs[random.randrange(0,len(mathfuncs))] + vs[random.randrange(0,len(vs))] + ')'
        initv += ops[random.randrange(0,len(ops))]

    if initv[-1] in ops:
        initv = initv[:-1]
    return initv

imcount = 0
while True:
    try:
        sys.stdout.write('.')
        while True:
            mod = random.randrange(0,2)
            if random.randrange(0,100) == 1:
                mod += 1
            dime1 = random.randrange(1,tes)
            dime2 = random.randrange(1,tes)
            dime3 = random.randrange(1,tes)
            dime4 = random.randrange(1,tes)
            alldimes = [dime1,dime2,dime3,dime4]
            if sum(alldimes) > pixels:
                continue
            elif sum(alldimes) < pixels:
                alldimes[random.randrange(0,len(alldimes))] += pixels - sum(alldimes)
            if sum(alldimes) == pixels:
                break
        
        depth = random.randrange(0,3) + 1
        d1 = random.randrange(1,5)
        d2 = random.randrange(1,5)
        d3 = random.randrange(1,5)
        d4 = random.randrange(1,5)
        Ra = intorfloat()
        Rb = intorfloat()
        Rc = intorfloat()
        Rd = intorfloat()
        Ga = intorfloat()
        Gb = intorfloat()
        Gc = intorfloat()
        Gd = intorfloat()
        Ba = intorfloat()
        Bb = intorfloat()
        Bc = intorfloat()
        Bd = intorfloat()
        moda = random.randrange(1,10000000)
        modb = random.randrange(1,10000000)
        modc = random.randrange(1,10000000)
        C = 0
        cby = intorfloat()
        X = 0
        Y = 0
        y = 1
        z = 1
        w = 1
        phi = 1.618033988749895
        gcount = 0
        inst = random.randrange(1,127)
        if inst == 9:
            inst = 11

        Rdat = []
        Gdat = []
        Bdat = []

        L1 = 'for x in range('+str(dime1)+'):'
        L2 = ''
        for l in range(d1):
            L2 += '\n' + '    ' + str(randq(depth))
        L3 = '\n' + '    ' + 'for y in range('+str(dime2)+'):'
        L4 = ''
        for l in range(d2):
            L4 += '\n' + '        ' + str(randq(depth))
        L5 = '\n' + '        ' + 'for z in range('+str(dime3)+'):'
        L6 = ''
        for l in range(d3):
            L6 += '\n' + '            ' + str(randq(depth))
        L7 = '\n' + '            ' + 'for w in range('+str(dime4)+'):'
        L8 = ''
        for l in range(d4):
            L8 += '\n' + '                ' + str(randq(depth))
        L9 = '\n' + '                ' + 'Rdat += [int(Ra+Rb+Rc+Rd)%'+str(moda)+']'
        L10 = '\n' + '                ' + 'Gdat += [int(Ga+Gb+Gc+Gd)%'+str(modb)+']'
        L11 = '\n' + '                ' + 'Bdat += [int(Ba+Bb+Bc+Bd)%'+str(modc)+']'
        L12 = '\n' + '                ' + 'C += cby'
        L13 = '\n' + '                ' + 'X += 1'
        L14 = '\n' + '                ' + 'if X >= width:'
        L15 = '\n' + '                    ' + 'X = 0'
        L16 = '\n' + '                    ' + 'Y += 1'

        command = L1+L2+L3+L4+L5+L6+L7+L8+L9+L10+L11+L12+L13+L14+L15+L16
        exec(command)
    except:
        continue
    else:
##        print command
        track = 0
        channel = 0
        time = 9
        duration = 1
        tempo = random.randrange(200,2000)
        volume = 126
        
        mf = MIDIFile(2)
        mf.addTempo(track,time,tempo)
        mf.addTempo(1,time,tempo)
        mf.addProgramChange(1,1,time,inst)
        for p in range(len(Rdat)):
            if 'es' in dodrumsplz:
                mf.addNote(0,9,((Rdat[p]+Gdat[p])%60)+27,time+p,duration,volume)
            mf.addNote(1,1,((Gdat[p]+Bdat[p])%60)+27,time+p+1,duration,volume)
            

    with open('Temp.mid','wb') as outpf:
        mf.writeFile(outpf)
    pygame.mixer.music.load('Temp.mid')
    pygame.mixer.music.play()
    dosave = input('\nType "save" to save midi.\nPress enter to skip.')
    if 'save' in dosave:
        print('saving...')
    else:
        print('\nplease wait key press has been recognized')
    if 'save' in dosave:
        mf = MIDIFile(2)
        mf.addTempo(track,time,tempo)
        mf.addTempo(1,time,tempo)
        mf.addProgramChange(1,1,time,inst)
        for p in range(len(Rdat)):
            if 'es' in dodrumsplz:
                mf.addNote(0,9,((Rdat[p]+Gdat[p])%60)+27,time+p,duration,volume)
            mf.addNote(1,1,((Gdat[p]+Bdat[p])%60)+27,time+p+1,duration,volume)
        with open(str(imcount)+'.mid','wb') as outpf:
            mf.writeFile(outpf)
        imcount += 1

        input('\nMidi_Hell'+str(imcount)+'.mid has been saved in audio folder.\nMove this file to a new folder or it may be overridden.\n')
                    
                
                
                


        
    
    
    




