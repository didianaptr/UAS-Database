import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="wfield1004",
  database="PERPUSTAKAAN_DAERAH_JAKARTA"
)
def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  cursor.execute("SELECT * FROM  BUKU_PERPUSTAKAAN WHERE Nama_buku LIKE %(keyword)s OR Tahun_penerbitan LIKE %(keyword)s OR Penulis_buku LIKE %(keyword)s OR nomor_ISBN LIKE %(keyword)s",{'keyword': keyword})
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)
      
def review_data(db):
    cursor = db.cursor()
    namaPemreview = input("masukan nama anda: ")
    keyword = input("Masukan judul buku: ")
    cursor.execute("SELECT Penulis_buku FROM  BUKU_PERPUSTAKAAN WHERE Nama_buku LIKE %(keyword)s",{'keyword': keyword})
    results = cursor.fetchall()
  
    if cursor.rowcount < 0:
      print("Tidak ada data")
    else:
      for data in results:
        print(data)
        buku = str(data)
        reviw = input("Masukkan 1-5 ")
        cursor.execute("insert into REVIEW_BINTANG(buku, penulis, review, namapemreview) VALUES(%s, %s, %s, %s)", (keyword, buku,reviw, namaPemreview ))
        db.commit()
        print("{} data berhasil disimpan".format(cursor.rowcount))
def show_menu(db):
  print("1. Cari Data")
  print("2. Review Bintang")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    search_data(db)
  elif menu == "2" :
        review_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)