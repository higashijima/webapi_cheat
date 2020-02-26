import pickle

data = ['テストデータ', 2020, {'項目1': '文字列項目', '項目2': 12345}]
with open('data.binaryfile', 'wb') as datafile:
    pickle.dump(data, datafile)
datafile.close()

with open('data.binaryfile', 'rb') as datafile:
    pdata = pickle.load(datafile)
    print(pdata)
