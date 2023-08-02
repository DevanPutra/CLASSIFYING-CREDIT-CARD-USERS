# CLASSIFYING CREDIT CARD USERS

## Latar Belakang
    Dari data yang ada, terdapat berbagai  pengguna kartu kredit. Bank ingin melihat sebenarnya apa yang paling berpengaruh terhadap keputusan "dibekukan atau tidak". sehingga akan dilihat dan dicari apakah pengaruh terbesar terhadap pengambilan keputusan tersebut.

## Problem Statement
    Mengklasifikasikan tipe orang dan ratio dalam pembayaran tiap pengguna, menggunakan [LogisticRegression(), DecisionTreeClassifier(), SVC(), RandomForestClassifier(), GaussianNB(), KNeighborsClassifier(), AdaBoostClassifier()] agar melihat dan dibandingkan model mana yang terbaik dalam menentukan model dan melihat model mana yang dapat melihat hubungan /pengaruh-pengaruh dari feature-feature dalam menjelaskan dasar apa dilakukan keputusan "dibekukan atau tidak"

## Step
   ### Cleaning Data
       Langkah pertama dari clasifikasi ini adalah perlunya kita pastikan bahwa data yang kita miliki sudah bersih, tidak terdapat data missing atau data yang duplicate. Sejauh pengecekan dapat diperhatikan bahwa data yang dimiliki **tidak terdapat missing value** dan hanya **terdapat duplicate**, sehingga dapat di ambil salah satu saja dari data duplicate yang ada.
   ### EDA
       Setelah kita cleaning data, kita perlu untuk memahami data yang kita miliki. Yaitu yang pertama, kita bisa melakukan EDA dengan membuat berbagai macam group dan membuat berbagai plot untuk bisa memahami data yang kita miliki. 
       Hasil EDA: 
       - Data yang dimiliki mayoritas adalah data yang pengguna cradit baik, atau yang 0 (tidak akan dibekukan) "Walaupun mayoritas 0, namun kita perlu perhatikan yang 1 atau jenis2 pay yang tidak memiliki keterangan dari datasetnya."
       
       dari notebook terdapat pola pembayaran yang sudah dikategorikan menurut pay 0-6, namun tidak ada keterangan lebih labjutnya, sehingga berdasarkan analisis, pay yang ada dapat dikategorikan sebagai berikut:
      
       -2 = dilihat dari polanya dari bulan april sampai september, -2 merupakan mereka yang rutin membayar dan kemungkinan melakukan prepayment (bayar sebelum jatuh tempo) karena jumlah tagihan cenderung lebih kecil dibandingkan yang dibayar
       -1 = dilihat dari polanya dari bulan april sampai september, -1 merupakan mereka yang rutin membayar tepat waktu sesuai dengan tagihannya karena jumlah tagihan cenderung imbang dibandingkan yang dibayar
       0 = dilihat dari polanya dari bulan april sampai september, 0 merupakan mereka yang rutin membayar tepat waktu namun tidak sesuai dengan tagihannya, atau kurang dari yang seharusnya dibayarkan karena jumlah tagihan lebih banyak dibandingkan yang dibayar namun dari setiap bulan selalu ada pembayaran
       -8 = dilihat dari polanya dari bulan april sampai september, 1-8 merupakan mereka yang menunggak membayatr 1= nunggak 1 bulan, 2=nunggak 2bulan dan seterusnya. karena polanya yang lebih besar tagihan dan terkadang ada yang tidak membayar.
   ### Features Selection
      Pada tahap ini, akan dipili feature yang akan digunakan berdasarkan coorelation terhadap data target, dan akan dilakukan juga setelahnya dengan multikolinearitas agar tidak terdapat data dependent yang saling mempengaruhi agar tidak ada bias dallam prediksi.
      Sehingga feature yang dipili merupakan:
      1. credit_limit_category	
      2. total_pay	
      3. last_bill	
      4. pay_ratio	
      5. sex	
      6. education_level	
      7. marital_status	
      8. age
   ### Preprocessing
      Dalam proses ini, akan dilakukan train test split untuk membagi data yang akan di training dan data yang akan di tes atau akan di prediksi. Setelah itu, data yang akan di training akan dilakukan uji normality test atau akan dicek outliers yang ada.
   ### Model
      Setelah dilakukan semua step diatas, maka data dapat dilakukan prediksi dan hasilnya adalah:
      Model-model tersebut adalah:
      1. Logistic Regression dengan parameter terbaik {'classifier__C': 0.1, 'classifier__max_iter': 100, 'classifier__penalty': 'l1', 'classifier__solver': 'liblinear'} dan skor recall terbaik 0.0
      2. Decision Tree dengan parameter terbaik {'classifier__criterion': 'entropy', 'classifier__max_depth': None, 'classifier__min_samples_split': 2} dan skor recall terbaik 0.25405405405405407
      3. SVM dengan parameter terbaik {'classifier__C': 10, 'classifier__degree': 4, 'classifier__gamma': 'scale', 'classifier__kernel': 'poly'} dan skor recall terbaik 0.021621621621621623
      4. Random Forest dengan parameter terbaik {'classifier__max_depth': 20, 'classifier__max_features': 'log2', 'classifier__min_samples_leaf': 1, 'classifier__min_samples_split': 2, 'classifier__n_estimators': 300} dan skor recall terbaik 0.05405405405405406
      5. Gaussian Naive Bayes dengan parameter terbaik {'classifier__var_smoothing': 1e-09} dan skor recall terbaik 0.20000000000000004
      6. K-Nearest Neighbors dengan parameter terbaik {'classifier__algorithm': 'auto', 'classifier__n_neighbors': 5, 'classifier__weights': 'distance'} dan skor recall terbaik 0.14054054054054052
      7. AdaBoostClassifier dengan parameter terbaik {'classifier__learning_rate': 1, 'classifier__n_estimators': 150} dan skor recall terbaik 0.07027027027027027.
      
      Dari hasil ini, maka model terbaik yang akan dipilih adalah `DecisionTreeClassifier` karena memiliki performa terbaik dengan recall sebesar 0.25405405405405407 pada data pengujian. Model ini menggunakan klasifikasi pohon keputusan dengan kriteria pembagian 'entropy', maksimum kedalaman tak terbatas, dan jumlah sampel minimum untuk membagi simpul adalah 2. Model ini memiliki keunggulan karena mudah diinterpretasikan dan tidak memerlukan banyak penyesuaian hyperparameter.
