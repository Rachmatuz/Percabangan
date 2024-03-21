#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Menentukan ganjil genap
nilai = int(input('Isikan Nilai:'))
sisa_bagi = nilai % 2
  
if sisa_bagi==0:
  print(f'{nilai} dalah bilangan genap')
else:
  print(f'{nilai} adalah bilangan gajil')
      
print('Program selesai')


# In[15]:


nilai_pemrogram = int(input('Isikan nilai pemrograman:'))
if nilai_pemrogram < 0 or nilai_pemrogram >100:
    print('Nilai Anda salah')
else:
    if nilai_pemrogram <50:
        print('E')
    elif nilai_pemrogram <60:
        print ('D')
    elif nilai_pemrogram <70:
        print ('C')
    elif nilai_pemrogram <80:
        print ('B')
    elif nilai_pemrogram <=100:
        print ('A')


# In[19]:


username = input('isikan username:')
password = input('isikan password:')

#jika username salah maka muncul "username anda salah"
#jika password salah maka muncul "password anda salah"
#jika keduanya salah maka muncul "username dan password anda salah"
#jika keduanya benar => "selamat datang (username)"
#username : admin
#password : admin

if username == 'admin':
    if password == 'admin':
        print(f'selamat datang {username}')
    else:
        print(f'password anda salah')
else:
    if password == 'admin':
        print("username anda salah")
    else:
        print("username dan password anda salah")


# In[15]:


nama = input('masukan nama:')
umur = int(input('masukan umur:'))
alamat = input('masukan alamat:')
tabungan = int(input('jumlah tabungan:'))


pangkat = ''
if umur > 40:
    if alamat == 'New york' or alamat == 'nevada' or alamat == 'havana':
        if tabungan > 10:
            pangkat = 'Don'

elif umur >25 and umur <40:
    if alamat == 'new jersey' or alamat == 'manhattan' or alamat == 'nevada':
        if tabungan >=1 and tabungan <=2:
            pangkat = 'Underboss'
                
elif umur >18 and umur <24:
    if alamat == 'california' or alamat == 'detroit' or  alamat == 'boston':
        if tabungan <= 1:
            pangkat = 'Capo'
            
if pangkat != '':
    print(f'{nama} kemungkinan seorang anggota mafia dengan pangkat {pangkat}')
else:
    print(f'{nama} tidak mencurigakan')
        


# In[ ]:




