import random
import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

play = False #bernilai true ketika dijalankan
tr = 500 

# player
player_X = 160 #start mobil 
player_y = 10
garis_tepi = [100,500] #Untuk collission dari tepi jalan dan box nya
# logic player 
y = 500
kecepatan = 10 #kecepatan buat jalannya
cek_point = 30
cek_y = 50
cek_kecepatan = 500
Point_colision = 0
#collison
colision = False # True ketika menabrak
# score & leve
fix_skor = 0
fix_skor_player = 0
cek_lev = 1
# rintangan
x_r_playerx = random.randrange(130,500,10)#10 ini dari inputan keyboard dari mobil harus sama
x_r_playerxx=random.randrange(130,400,10)
x_r_playerxxx=random.randrange(160,300,10)
level_next = 1 # for level counting
y_rintangan = 500 # digunakan untuk pergerakan rintangan ke bawah


#draw textnya
def drawText(ch,xpos,ypos,r,b,g):
    color = [r, b, g]
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))    
 
def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    color = [0,0,0]
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def bg_text(x,y):
    glColor3ub(0, 255, 255)     
    glBegin(GL_QUADS)
    glVertex2f(285+x,230+y)
    glVertex2f(495+x,230+y)
    glVertex2f(495+x,280+y)
    glVertex2f(285+x,280+y)
    glEnd()
       
def drawTextNum(skor,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in str(skor):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))



#obejeck jalan ()
def jalan (jln):
    glPushMatrix()
    glBegin(GL_POLYGON) 
    glColor3ub(0,0,0) #hitam
    glVertex2f(jln - 100, 500)
    glVertex2f(jln - 100, 0) #left
    glVertex2f(jln + 300, 0) #right
    glVertex2f(jln + 300, 500)
    glEnd()
    glPopMatrix()

def tepi(tp):
    glPushMatrix()
    glColor3ub(255, 255, 0) #kode warna pake color picker
    glLineWidth(10)
    glBegin(GL_LINES) #utk membuat objek garis
    glVertex2f(tp, 0) 
    glColor3ub(255, 0, 0)
    glVertex2f(tp, 500)
    glEnd()
    glPopMatrix()

def kotak_coll(kcx):
    glPushMatrix()
    glColor3ub(14,15,20)
    glLineWidth(30)
    glBegin(GL_LINES)
    glVertex2f(kcx, 0) 
    glVertex2f(kcx, 500)
    glEnd()
    glPopMatrix()

def garis_mid(gmx,gmy):
    glPushMatrix()
    glTranslated(0,y,0)
    glColor3ub(255, 255, 255) #kode warna pake color picker
    glLineWidth(10)
    glBegin(GL_LINES) #utk membuat objek garis
    glVertex2f(gmx+125, gmy) 
    glVertex2f(gmx+125, gmy+50)
    glEnd()
    glPopMatrix()


#Object Mobil
def Mobil(x,y):
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(255, 50, 100)
    glVertex2f(x, y)
    glVertex2f(x + 30, y + 0)
    glVertex2f(x + 30, y + 35)
    glVertex2f(x + 30-5, y + 50)
    glVertex2f(x + 5, y + 50)
    glVertex2f(x , y + 35)
    glEnd()
    

    #lampu kiri
    glPointSize(4)
    glColor3d(255,255,0)
    glBegin(GL_POINTS)
    glVertex2f(x+22, y+47)
    glEnd()

    #lampu kanan
    glPointSize(4)
    glColor3d(255,255,0)
    glBegin(GL_POINTS)
    glVertex2f(x+5, y+47)
    glEnd()

    #hiasan
    glColor3d(255,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(x+5, y+5) #a
    glVertex2f(x+5, y+10) #b
    glVertex2f(x+25, y+10) #c
    glVertex2f(x+25, y+5) #d
    glEnd()

    glColor3d(30,10,110)
    glBegin(GL_TRIANGLES)
    glVertex2f(x+5, y+20) #a
    glVertex2f(x+5, y+15) #b
    glVertex2f(x+25, y+20) #c
    glVertex2f(x+25, y+15) #d
    glEnd()
    glPopMatrix()


# Disain Hiasan
def papan(x,y) :
    glPushMatrix()
    glColor3d(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(x+50, 0) #a
    glVertex2f(x+50, 200) #b
    glVertex2f(x+40, 200) #c
    glVertex2f(x+40, 0) #d
    glEnd()
    glPopMatrix()

def papan2(x,y) :
    glPushMatrix()
    glColor3d(0,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(x+60, 0) #a
    glVertex2f(x+60, 200) #b
    glVertex2f(x+50, 200) #c
    glVertex2f(x+50, 0) #d
    glEnd()
    glPopMatrix()

def papan3(x,y):
    glPushMatrix()
    glColor3ub(42, 172,116)
    glBegin(GL_POLYGON)
    glVertex2f(x+30, 200) #a
    glVertex2f(x+30, 300) #b
    glVertex2f(x+200, 300) #c
    glVertex2f(x+200, 200) #d
    glEnd()
    glPopMatrix()

def wall_mobil():
    glScale(0.2,0.2,0)
    glTranslated(2150,1700,0)
    glRotate(270,0,0,270)
    glBegin(GL_POLYGON) #BADAN MOBIL 1
    glColor3ub(178,34,34)
    glVertex2f(20, 100) #E
    glVertex2f(40, 100) #F
    glVertex2f(80, 50) #D
    glVertex2f(80, -100) #C
    glVertex2f(-20, -100) #A
    glVertex2f(-20, 50) #B
    glEnd()

    glBegin(GL_LINES) #WHITE LINE BADAN MOBIL 1
    glColor3d(0,0,0)
    glVertex2f(80, 50) #D
    glVertex2f(50, 0)
    glVertex2f(50, 0)
    glVertex2f(50, -50)
    glVertex2f(-20, 50) #B
    glVertex2f(10, 0)
    glVertex2f(10, 0)
    glVertex2f(10, -50)
    glEnd()

    glBegin(GL_POLYGON) #BADAN MOBIL 2
    glColor3ub(178,34,34)
    glVertex2f(-20, -50) #A
    glVertex2f(80, -50) #C
    glVertex2f(130, -100) #l
    glVertex2f(130, -250) #M
    glVertex2f(80, -300) #N
    glVertex2f(-20, -300) #I
    glVertex2f(-70, -250) #H
    glVertex2f(-70, -100) #G
    glEnd()

    glBegin(GL_LINES) #WHITE LINE BADAN MOBIL 2
    glColor3d(0,0,0)
    glVertex2f(50, -50) #CABANG KANAN
    glVertex2f(100, -120)
    glVertex2f(100, -120)
    glVertex2f(100, -280)
    glVertex2f(10, -50) #CABANG KIRI
    glVertex2f(-40, -120)
    glVertex2f(-40, -120)
    glVertex2f(-40, -280)
    glEnd()

    glBegin(GL_LINES) #LINE BADAN MOBIL
    glColor3d(0,0,0)
    glVertex2f(20, 100) #E
    glVertex2f(40, 100) #F
    glVertex2f(40, 100) #F
    glVertex2f(80, 50) #D
    glVertex2f(80, 50) #D
    glVertex2f(80, -50) #C
    glVertex2f(80, -50) #C
    glVertex2f(130, -100) #l
    glVertex2f(130, -100) #l
    glVertex2f(130, -250) #M
    glVertex2f(130, -250) #M
    glVertex2f(80, -300) #N
    glVertex2f(80, -300) #N
    glVertex2f(80, -350) #Q
    glVertex2f(80, -350) #Q
    glVertex2f(-20, -350) #R
    glVertex2f(-20, -350) #R
    glVertex2f(-20, -300) #I
    glVertex2f(-20, -300) #I
    glVertex2f(-70, -250) #H
    glVertex2f(-70, -250) #H
    glVertex2f(-70, -100) #G
    glVertex2f(-70, -100) #G
    glVertex2f(-20, -50) #A
    glVertex2f(-20, -50) #A
    glVertex2f(-20, 50) #B
    glVertex2f(-20, 50) #B
    glVertex2f(20, 100) #E
    glEnd()
    
    glBegin(GL_POLYGON) #SAYAP KANAN
    glColor3ub(255,215,0)
    glVertex2f(130, -100) #l
    glVertex2f(180, -150) #P
    glVertex2f(180, -200) #O
    glVertex2f(130, -250) #M
    glEnd()

    glBegin(GL_LINES) #LINE SAYAP KANAN
    glColor3d(0,0,0)
    glVertex2f(130, -100) #l
    glVertex2f(180, -150) #P
    glVertex2f(180, -150) #P
    glVertex2f(180, -200) #O
    glVertex2f(180, -200) #O
    glVertex2f(130, -250) #M
    glVertex2f(130, -250) #M
    glVertex2f(130, -100) #l
    glEnd()

    glBegin(GL_POLYGON) #SAYAP KIRI
    glColor3ub(255,215,0)
    glVertex2f(-70, -100) #G
    glVertex2f(-120, -150) #J
    glVertex2f(-120, -200) #K
    glVertex2f(-70, -250) #H
    glEnd()

    glBegin(GL_LINES) #LINE SAYAP KIRI
    glColor3d(0,0,0)
    glVertex2f(-70, -100) #G
    glVertex2f(-120, -150) #J
    glVertex2f(-120, -150) #J
    glVertex2f(-120, -200) #K
    glVertex2f(-120, -200) #K
    glVertex2f(-70, -250) #H
    glVertex2f(-70, -250) #H
    glVertex2f(-70, -100) #G
    glEnd()

    glBegin(GL_POLYGON) #PENGENDARA
    glColor3d(0,0,0)
    glVertex2f(10, -100) #V2
    glVertex2f(50, -100) #W2
    glVertex2f(80, -150) #U2
    glVertex2f(80, -320) #Q
    glVertex2f(-20, -320) #R
    glVertex2f(-20, -150) #T2
    glEnd()

    glBegin(GL_LINES) #WHITE LINE PENGENDARA
    glColor3d(255,255,255)
    glVertex2f(80, -150) #U2
    glVertex2f(30, -200)
    glVertex2f(-20, -150) #T2
    glVertex2f(30, -200)
    glVertex2f(-20, -320) #R
    glVertex2f(30, -260)
    glVertex2f(80, -320) #Q
    glVertex2f(30, -260)
    glVertex2f(30, -200) #GARIS PUTIH PEMOTONG
    glVertex2f(30, -260)
    glEnd()

    glBegin(GL_POLYGON) #JARAK RODA ATAS KANAN
    glColor3f(0.2, 0.2, 0.2)
    glVertex2f(80, 0) #D
    glVertex2f(130, 0) #S
    glVertex2f(130, -20) #A1
    glVertex2f(80, -20) #B1
    glEnd()

    glBegin(GL_LINES) #LINE JARAK RODA ATAS KANAN
    glColor3f(0, 0, 0)
    glVertex2f(80, 0) #D
    glVertex2f(130, 0) #S
    glVertex2f(130, 0) #S
    glVertex2f(130, -20) #A1
    glVertex2f(130, -20) #A1
    glVertex2f(80, -20) #B1
    glVertex2f(80, -20) #B1
    glVertex2f(80, 0) #D
    glEnd()

    glBegin(GL_POLYGON) #RODA ATAS KANAN
    glColor3d(0,0,0)
    glVertex2f(130, 60) #J1
    glVertex2f(190, 60) #I1
    glVertex2f(190, -80) #H1
    glVertex2f(130, -80) #G1
    glEnd()

    glBegin(GL_POLYGON) #JARAK ATAS RODA KIRI
    glColor3d(0.2, 0.2, 0.2)
    glVertex2f(-20, 0) #V
    glVertex2f(-70, 0) #U
    glVertex2f(-70, -20) #W
    glVertex2f(-20, -20) #Z
    glEnd()

    glBegin(GL_LINES) #LINE JARAK ATAS RODA KIRI
    glColor3d(0, 0, 0)
    glVertex2f(-20, 0) #V
    glVertex2f(-70, 0) #U
    glVertex2f(-70, 0) #U
    glVertex2f(-70, -20) #W
    glVertex2f(-70, -20) #W
    glVertex2f(-20, -20) #Z
    glVertex2f(-20, -20) #Z
    glVertex2f(-20, 0) #V
    glEnd()

    glBegin(GL_POLYGON) #RODA ATAS KIRI
    glColor3d(0, 0, 0)
    glVertex2f(-70, 60) #J1
    glVertex2f(-130, 60) #I1
    glVertex2f(-130, -80) #H1
    glVertex2f(-70, -80) #G1
    glEnd()

    glBegin(GL_POLYGON) #JARAK RODA BAWAH TENGAH
    glColor3d(0.2, 0.2, 0.2)
    glVertex2f(-20, -320) #R
    glVertex2f(80, -320) #Q
    glVertex2f(90, -340) #L1
    glVertex2f(90, -400) #S1
    glVertex2f(80, -410) #R1
    glVertex2f(-20, -410) #Q1
    glVertex2f(-30, -400) #P1
    glVertex2f(-30, -340) #K1
    glEnd()

    glBegin(GL_LINES) #WHITE LINE JARAK RODA BAWAH TENGAH
    glColor3d(0, 0, 0)
    glVertex2f(90, -340) #L1
    glVertex2f(70, -370)
    glVertex2f(-30, -340) #K1
    glVertex2f(-10, -370)
    glVertex2f(90, -400) #S1
    glVertex2f(70, -370)
    glVertex2f(-30, -400) #P1
    glVertex2f(-10, -370)
    glVertex2f(-30, -370) #GARIS PUTIH PEMOTONG
    glVertex2f(90, -370)
    glEnd()

    glBegin(GL_POLYGON) #JARAK RODA BAWAH KANAN
    glColor3d(0.2, 0.2, 0.2)
    glVertex2f(90, -340) #L1
    glVertex2f(130, -340) #N1
    glVertex2f(130, -400) #T1
    glVertex2f(90, -400) #S1
    glEnd()

    glBegin(GL_LINES) #WHITE LINE JARAK RODA BAWAH KANAN
    glColor3d(0, 0, 0)
    glVertex2f(90, -370)
    glVertex2f(130, -370)
    glEnd()

    glBegin(GL_POLYGON) #JARAK RODA BAWAH KIRI
    glColor3d(0.2, 0.2, 0.2)
    glVertex2f(-30, -340) #K1
    glVertex2f(-70, -340) #M1
    glVertex2f(-70, -400) #O1
    glVertex2f(-30, -400) #P1
    glEnd()

    glBegin(GL_LINES) #WHITE LINE JARAK RODA BAWAH KIRI
    glColor3d(0, 0, 0)
    glVertex2f(-30, -370)
    glVertex2f(-70, -370)
    glEnd()

    glBegin(GL_LINES) #LINE JARAK RODA BAWAH
    glColor3d(0, 0, 0)
    glVertex2f(-20, -320) #R
    glVertex2f(80, -320) #Q
    glVertex2f(80, -320) #Q
    glVertex2f(90, -340) #L1
    glVertex2f(90, -340) #L1
    glVertex2f(130, -340) #N1
    glVertex2f(130, -340) #N1
    glVertex2f(130, -400) #T1
    glVertex2f(130, -400) #T1
    glVertex2f(90, -400) #S1
    glVertex2f(90, -400) #S1
    glVertex2f(80, -410) #R1
    glVertex2f(80, -410) #R1
    glVertex2f(-20, -410) #Q1
    glVertex2f(-20, -410) #Q1
    glVertex2f(-30, -400) #P1
    glVertex2f(-30, -400) #P1
    glVertex2f(-70, -400) #O1
    glVertex2f(-70, -400) #O1
    glVertex2f(-70, -340) #M1
    glVertex2f(-70, -340) #M1
    glVertex2f(-30, -340) #K1
    glVertex2f(-30, -340) #K1
    glVertex2f(-20, -320) #R
    glEnd()

    glBegin(GL_POLYGON) #RODA BAWAH KANAN
    glColor3d(0,0,0)
    glVertex2f(130, -300) #A1
    glVertex2f(190, -300) #B1
    glVertex2f(190, -440) #E1
    glVertex2f(130, -440) #D1
    glEnd()

    glBegin(GL_POLYGON) #RODA BAWAH KIRI
    glColor3d(0,0,0)
    glVertex2f(-70, -300) #U1
    glVertex2f(-130, -300) #Z1
    glVertex2f(-130, -440) #W1
    glVertex2f(-70, -440) #V1
    glEnd()

    glBegin(GL_POLYGON) #sAYAP BELAKANG 1
    glColor3d(0,0,0)
    glVertex2f(-20, -410) #Q1
    glVertex2f(80, -410) #R1
    glVertex2f(80, -460) #G2
    glVertex2f(-20, -460) #F2
    glEnd()

    glBegin(GL_POLYGON) #sAYAP BELAKANG 2
    glColor3d(0,0,0)
    glVertex2f(80, -430) #G2
    glVertex2f(190, -500) #J2
    glVertex2f(190, -550) #Q2
    glVertex2f(170, -530) #R2
    glVertex2f(-110, -530) #K2
    glVertex2f(-130, -550) #I2
    glVertex2f(-130, -500) #H2
    glVertex2f(-20, -430) #Q1
    glEnd()

    glBegin(GL_POLYGON) #sAYAP BELAKANG 3
    glColor3ub(178,34,34)
    glVertex2f(-80, -530) #S2
    glVertex2f(-50, -510) #Z2
    glVertex2f(110, -510) #A3
    glVertex2f(140, -530) #L2
    glVertex2f(110, -550) #M2
    glVertex2f(-50, -550) #P2
    glEnd()

    glBegin(GL_LINES) #LINE sAYAP BELAKANG 3
    glColor3d(0,0,0)
    glVertex2f(-80, -530) #S2
    glVertex2f(-50, -510) #Z2
    glVertex2f(-50, -510) #Z2
    glVertex2f(110, -510) #A3
    glVertex2f(110, -510) #A3
    glVertex2f(140, -530) #L2
    glVertex2f(140, -530) #L2
    glVertex2f(110, -550) #M2
    glVertex2f(110, -550) #M2
    glVertex2f(-50, -550) #P2
    glVertex2f(-50, -550) #P2
    glVertex2f(-80, -530) #S2
    glVertex2f(-80, -530) #S2 (t3)
    glVertex2f(140, -530) #L2 (t3)
    glEnd()

    glBegin(GL_LINES) #WHITE LINE sAYAP BELAKANG
    glColor3d(255,255,255)
    glVertex2f(-50, -510) #Z2 (1)
    glVertex2f(10, -460)
    glVertex2f(10, -460)
    glVertex2f(10, -410)
    glVertex2f(-50, -510) #Z2 (2)
    glVertex2f(-80, -480)
    glVertex2f(110, -510) #A3 (1)
    glVertex2f(50, -460)
    glVertex2f(50, -460)
    glVertex2f(50, -410)
    glVertex2f(110, -510) #A3 (2)
    glVertex2f(140, -480)
    glEnd()

def background(x): #bg untuk berubah warna saat game over (tampilan skor akhir)
    glPushMatrix()
    glColor3ub(0,0,255)
    glBegin(GL_POLYGON)
    glVertex2f(100+x, 0) 
    glVertex2f(300+x, 0)
    glVertex2f(300+x, 500)
    glVertex2f(100+x, 500) 
    glEnd()
    glPopMatrix()


#Object Rintangannya
def rintangan_object1(x):
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(37, 188, 143) 
    glVertex2f(x, y_rintangan)
    glVertex2f(x,y_rintangan+40)
    glVertex2f(x+38,y_rintangan+40)
    glVertex2f(x+38,y_rintangan)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(255,0,0) 
    glVertex2f(x,y_rintangan+40)
    glVertex2f(x+10, y_rintangan+50)
    glVertex2f(x+35,y_rintangan+50)
    glVertex2f(x+40,y_rintangan+40)
    glEnd()
    glPointSize(4)
    glBegin(GL_POINTS)
    glColor3ub(0,255,255) 
    glVertex2f(x+10, y_rintangan+48)
    glEnd()
    glPointSize(4)
    glBegin(GL_POINTS)
    glColor3ub(0,255,255) 
    glVertex2f(x+30, y_rintangan+48)
    glEnd()
    glPopMatrix()

def rintangan_object2(x):
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(37, 188, 143) 
    glVertex2f(x, y_rintangan)
    glVertex2f(x,y_rintangan+40)
    glVertex2f(x+38,y_rintangan+40)
    glVertex2f(x+38,y_rintangan)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(255,0,0) 
    glVertex2f(x,y_rintangan+40)
    glVertex2f(x+10, y_rintangan+50)
    glVertex2f(x+35,y_rintangan+50)
    glVertex2f(x+40,y_rintangan+40)
    glEnd()
    glPointSize(4)
    glBegin(GL_POINTS)
    glColor3ub(0,255,255) 
    glVertex2f(x+10, y_rintangan+48)
    glEnd()
    glPointSize(4)
    glBegin(GL_POINTS)
    glColor3ub(0,255,255) 
    glVertex2f(x+30, y_rintangan+48)
    glEnd()
    glPopMatrix()

def rintangan_object3(x):
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(37, 188, 143) 
    glVertex2f(x, y_rintangan)
    glVertex2f(x,y_rintangan+40)
    glVertex2f(x+38,y_rintangan+40)
    glVertex2f(x+38,y_rintangan)
    glEnd()
    glBegin(GL_POLYGON)
    glColor3ub(255,0,0) 
    glVertex2f(x,y_rintangan+40)
    glVertex2f(x+10, y_rintangan+50)
    glVertex2f(x+35,y_rintangan+50)
    glVertex2f(x+40,y_rintangan+40)
    glEnd()
    glPointSize(4)
    glBegin(GL_POINTS)
    glColor3ub(0,255,255) 
    glVertex2f(x+10, y_rintangan+48)
    glEnd()
    glPointSize(4)
    glBegin(GL_POINTS)
    glColor3ub(0,255,255) 
    glVertex2f(x+30, y_rintangan+48)
    glEnd()
    glPopMatrix()


#logika 
def gerak(key,x,y):
    global colision,play,player_X,player_y
    if key == GLUT_KEY_UP :
        if colision == False :
            if player_y+50 < 500:
                player_y += 10
            else:
                player_y += 0
        # if player_y+10 < 500 :
    elif key == GLUT_KEY_DOWN : 
            if colision == False :
                 if player_y+50 > 50:
                    player_y -= 10
                 else:
                    player_y += 0
    elif key == GLUT_KEY_RIGHT:
        if colision == False:
            if player_X+50 > garis_tepi[1]:
                colision = True
            else:
                player_X += 10
        else:
            player_X += 0
    elif key == GLUT_KEY_LEFT:
        if colision == False:
            if player_X-20 < garis_tepi[0]:
                colision = True
            else:
                player_X -= 10    
    elif ord(key) == ord(b'\r'): #buat saat terjadi game over
        play = True
        colision = False #kenapa ini kok dibuat false, karena supaya tidak terjadi tubrukan terus menerus

def mouse_play_game(button, state, x, y):
    global play 
    if button == GLUT_LEFT_BUTTON:
        if (x >= 280 and x <= 480) and (y >= 220 and y <=280):
            play = True

def key_start(key,x,y):
    global play
    if ord (key) == ord (b'\r') : 
        play = True

def game_play():
    jalan(200)
    tepi(100) #kiri
    tepi(500) #kanan
    kotak_coll(305) #ditengah
    papan(480, 0)
    papan2(580,0)
    papan3(480,0)
    gmy = 20 # y pertama dari garis mid
    for i in range(7): #garis mid dibentuk sebanyak 7 menggunakan perulangan for
        garis_mid(180,gmy)
        gmy += 70 #memberikan jarak setiap garis_mid
        Mobil(player_X,player_y)

    drawText('SCORE : ',15,460,0,0,0) #player 1
    drawTextNum(fix_skor,25,440,0,0,0) # player 1
    drawText('LEVEL : ',15,420,0,0,0)
    drawTextNum(level_next,25,400,0,0,0)
    drawTextBold('Kata Tulus', 525, 275)
    drawTextBold('Hati-Hati', 530, 245)
    drawTextBold('Di Jalan!!!', 530,215)

def game_over():
    if colision == False:
        game_play()
        rintangan_object1(x_r_playerx)  
        rintangan_object2(x_r_playerxx) 
        rintangan_object3(x_r_playerxxx)
    else:
        
        background(0) #tampilannnya akan berada di tengah jalan
        drawText('YOUR FINAL SCORE: ',110,450,255,255,255) #player 1
        drawTextNum(fix_skor_player,180,430,255,0,0) # player 1
        drawText('HIGHEST LEVEL : ',110,400,255,255,255) #player 1
        drawTextNum(level_next,180,380,255,0,0) # player 1

    if colision==True:
            glPushMatrix()
            glColor3b(255,0,100 )
            glBegin(GL_QUADS)
            glVertex2f(270, 270)
            glVertex2f(480, 270)
            glVertex2f(480, 340)
            glVertex2f(270, 340)
            glEnd()
            glColor3ub(255,0,0)
            glLineWidth(3)
            glBegin(GL_LINE_LOOP)
            glVertex2f(270, 270)
            glVertex2f(480, 270)
            glVertex2f(480, 340)
            glVertex2f(270, 340)
            glEnd()
            glPopMatrix()
            drawTextBold("GAME OVER",290,310)
            drawText("Enter play",320,290,200, 100, 100) 

def start_game():
    glPushMatrix()
    glColor3b(36, 200, 127)
    glBegin(GL_QUADS)
    glVertex2f(280, 220)
    glVertex2f(480, 220)
    glVertex2f(480, 280)
    glVertex2f(280, 280)
    glEnd()
    glColor3ub(0,0,0)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(280, 220)
    glVertex2f(480, 220)
    glVertex2f(480, 280)
    glVertex2f(280, 280)
    glEnd()
    glScale(1,1,0)
    drawTextBold("P L A Y G A M E",295,250)
    drawTextBold('"GRAND CARS RACING"',250,400)
    drawText("DEVELOPMENT (KELOMPOK M) ",260,200,255,0,0)
    drawText("1. REZA OCTA FAHLEVI (3007) ",240,180,255,0,0)
    drawText("2. ANANDA SALSABILA (3009) ",240,160,255,0,0)
    drawText("3. IKBAR SAIF FADILAH (3061) ",240,140,255,0,0)
    wall_mobil()
    glPopMatrix()

def timer_rintangan(value):
    global y_rintangan, tr, x_r_playerx, cek_lev,colision,x_r_playerxx,Point_colision,player_y,x_r_playerxxx
    if play == True:
        y_rintangan -= 20
        if colision==False:
            print('sumbu x : ',x_r_playerx,x_r_playerxx,x_r_playerxxx,player_X) 
            print('sumbu y : ',player_y,y_rintangan) 
        if y_rintangan < -500:
                cek_lev += 1
                y_rintangan = 550
                x_r_player,x_r_playerxx,x_r_playerxxx = random.randrange (130,500,10), random.randrange(130,400,10),random.randrange(160,300,10)
        if (cek_lev %2) == 0:
                tr-=100
        if tr <100:
                tr = 100 
        if (player_X in range(x_r_playerx-50, x_r_playerx+20)) and player_y in range(y_rintangan-50, y_rintangan+50):
                print('aduh tubrukan : ',x_r_playerx,y_rintangan)
                colision = True
        if (player_X in range(x_r_playerxx-30, x_r_playerxx+30)) and player_y in range(y_rintangan-50, y_rintangan+40):
                print('aduh tubrukan : ',x_r_playerxx,y_rintangan)
                colision = True
        if (player_X in range(x_r_playerxxx-20, x_r_playerxx+20)) and player_y in range(y_rintangan-30, y_rintangan+30):
                print('aduh tubrukan : ',x_r_playerxxx,y_rintangan)
                colision=True
    #timer rintangan_object awal = 500, berkurang hingga mencapai 100
    glutTimerFunc(tr,timer_rintangan,0)

def timer(value):
    global y, kecepatan, fix_skor, cek_point, cek_y, cek_kecepatan, level_next, fix_skor_player
    if play==True:
        if colision == False:
            y -= kecepatan  
            if y < value :
                # 50 adalah tingkatan awal.... berkurang 5 hingga tingkatan akhir menjadi 20
                y = cek_y
            fix_skor += kecepatan 
            if fix_skor % cek_kecepatan == 0 :
                level_next += 1
                cek_y -= 5
                cek_point -= 5
                cek_kecepatan += 10000
            if cek_y < 20:
                cek_y = 20
                
            if cek_point < 10:
                cek_point = 10
        else:
            fix_skor_player = fix_skor
    #timer awal = 30, berkurang sebanyak 5 hingga mencapai 10
    glutTimerFunc(cek_point,timer,0)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    if play == True:
        game_over()
    else:
        start_game()
    glutSwapBuffers() #utk membersihkan layar, double buffering

def init():
     glClearColor(0, 128, 128, 2.0)
     gluOrtho2D(0, 500.0, -500.0, 500.0)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 650,0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def Main():
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGBA)
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 500)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("Ayo Kita Main Gamee")
    glutDisplayFunc(showScreen)
    glutSpecialFunc(gerak)
    glutMouseFunc(mouse_play_game)
    glutKeyboardFunc(key_start)
    glutKeyboardFunc(gerak)
    timer_rintangan(0)
    timer(0)
    init()
    glutIdleFunc(showScreen)
    glutMainLoop()

Main()