from zipfile import ZipFile

zip = ZipFile('ClipsAndTacksF1ForModeler.zip')

zip.extract('ClipsAndTacksF1/RootExternalModel/Business service objects/Order/__FILE__ATTACHMENT/')

zip.extractall('files')
print(zip.namelist())

zip.close()

with ZipFile('ClipsAndTacksF1ForModeler.zip') as my_zip:
    zip.extractall()


