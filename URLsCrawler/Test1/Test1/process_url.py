#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Jasper
import csv,os,requests,sqlite3,multiprocessing

class Edit():
   domains = []
   cache0 = []
   transit = []
   buffer=[]
   cache = []
   store = []
   outcome=[]

   def editing(self):
      with open("input.csv", newline='') as f:
          reader = csv.reader(f)
          for row in reader:
              self.domains.append(row[0])

      with open("draft.csv", newline='') as f:
          reader = csv.reader(f)
          for row in reader:
              self.cache0.append(row[0])
          for c in self.cache0:
              c1 = c[10:-2]
              self.cache.append(c1)


      for dname in range(len(self.domains)):
          for ca in self.cache:
              if (self.domains[dname] in ca):
                  if ca.count('/') <= 5:
                      self.transit.append(ca)
                      self.cache.remove(ca)
              else:
                  continue
          self.buffer = self.transit[0:50]
          self.store.append(self.buffer)
          self.transit=[]
          self.buffer=[]



   def http_status(self,msg):
       r = requests.head(msg)
       code = r.status_code
       if code >= 200 and code < 400:
           return msg

   def multi(self,urls,bla):
       pool = multiprocessing.Pool(processes=4)
       results = []
       new = []
       for u in urls:
           for ui in u:
              results.append(pool.apply_async(self.http_status, (ui,)))
           for res in results:
              new.append(res.get())
           while None in new:
              new.remove(None)
           new.sort(key=lambda x: len(x))

           bla.append(new)
           new=[]
           results=[]

   def tworows(self,str1,str2):
        #dindex is the index of self.domains[]
        current_dir = os.path.abspath('.')
        file_name = os.path.join(current_dir, "output.csv")
        csvfile = open(file_name, 'w', encoding="UTF8",newline='')  #

        writer = csv.writer(csvfile, delimiter=",",dialect='excel')

        csvrow1 = []
        csvrow2 = []

        # str2=domains
        for i in range(len(str1)):
            for j in range(len(str1[i])):
               csvrow1.append(str2[i])
               csvrow2.append(str1[i][j])
        writer.writerows(zip(csvrow1, csvrow2))
        csvfile.close()


   def csv_to_db(self):
       conn = sqlite3.connect("Database01.db")
       curs = conn.cursor()
       curs.execute("CREATE TABLE crawled (Domain TEXT, URLs TEXT);")
       reader = csv.reader(open('output.csv', 'r'), delimiter=',')
       for row in reader:
           to_db = [row[0], row[1]]
           curs.execute("INSERT INTO crawled (Domain,URLs) VALUES (?, ?);", to_db)
       conn.commit()















