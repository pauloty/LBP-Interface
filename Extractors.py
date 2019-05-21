# Imports necessarios para execucao
import cv2
import csv
import glob
import numpy as np
from skimage import feature
import mahotas.features
import os
from scipy.stats import kurtosis, skew

# precisa adaptar
def statisticalMoments(files, images):
    # Codigo para momentos estatisticos

    csv.register_dialect('dial', delimiter=';')
    myFile = open('CSVs\\StatiscalMoments_High.csv', 'w', newline="") # High file
    writer = csv.writer(myFile, dialect='dial')
    myFile1 = open('CSVs\\StatiscalMoments_Low.csv', 'w', newline="") # Low file
    writer1 = csv.writer(myFile1, dialect='dial')
    myFile2 = open('CSVs\\StatiscalMoments_Severe.csv', 'w', newline="") # Lesao Grave file
    writer2 = csv.writer(myFile2, dialect='dial')
    myFile3 = open('CSVs\\StatiscalMoments_Normal.csv', 'w', newline="") # Lesao Normal file
    writer3 = csv.writer(myFile3, dialect='dial')

    row = []
    i = 0
    for img in images:
        row.append(files[i].rsplit('\\', 1)[1])  # Adiciona o nome da imagem no arquivo
        row.append(np.mean(img))
        row.append(np.var(img))
        row.append(kurtosis(img, axis=None, fisher=False))  # Nao usa a definicao de Fisher e calcula sobre a imagem inteira
        row.append(skew(img, axis=None))
        if 'high' in files[i]:
            writer.writerow(row)
        if 'low' in files[i]:
            writer1.writerow(row)
        if 'severe' in files[i]:
            writer2.writerow(row)
        if 'normal' in files[i]:
            writer3.writerow(row)
        row[:] = []
        i = i + 1

    myFile.close()
    myFile1.close()
    myFile2.close()
    myFile3.close()
# precisa adaptar
def huMoments(files, images):

    csv.register_dialect('dial', delimiter=';')
    myFile = open('CSVs\\HuMoments_High.csv', 'w', newline="") # High file
    writer = csv.writer(myFile, dialect='dial')
    myFile1 = open('CSVs\\HuMoments_Low.csv', 'w', newline="") # Low file
    writer1 = csv.writer(myFile1, dialect='dial')
    myFile2 = open('CSVs\\HuMoments_Severe.csv', 'w', newline="") # Lesao Grave file
    writer2 = csv.writer(myFile2, dialect='dial')
    myFile3 = open('CSVs\\HuMoments_Normal.csv', 'w', newline="") # Lesao Normal file
    writer3 = csv.writer(myFile3, dialect='dial')

    row = []
    i = 0
    for img in images:
        row.append(files[i].rsplit('\\', 1)[1])  # Adiciona o nome da imagem no arquivo
        ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        M = cv2.moments(th, True)
        row.extend(list(cv2.HuMoments(M).flatten()))
        if 'high' in files[i]:
            writer.writerow(row)
        if 'low' in files[i]:
            writer1.writerow(row)
        if 'severe' in files[i]:
            writer2.writerow(row)
        if 'normal' in files[i]:
            writer3.writerow(row)
        row[:] = []
        i = i + 1

    myFile.close()
    myFile1.close()
    myFile2.close()
    myFile3.close()
# precisa adaptar
def haralickMoments(files, images):
    # CODIGO PARA HARALICK

    csv.register_dialect('dial', delimiter=';')
    myFile = open('CSVs\\Haralick_High.csv', 'w', newline="")  # High file
    writer = csv.writer(myFile, dialect='dial')
    myFile1 = open('CSVs\\Haralick_Low.csv', 'w', newline="")  # Low file
    writer1 = csv.writer(myFile1, dialect='dial')
    myFile2 = open('CSVs\\Haralick_Severe.csv', 'w', newline="")  # Lesao Grave file
    writer2 = csv.writer(myFile2, dialect='dial')
    myFile3 = open('CSVs\\Haralick_Normal.csv', 'w', newline="")  # Lesao Normal file
    writer3 = csv.writer(myFile3, dialect='dial')

    row = []
    i = 0
    for img in images:
        row.append(files[i].rsplit('\\', 1)[1])  # Adiciona o nome da imagem no arquivo
        row.extend(list(mahotas.features.haralick(img).mean(0)))
        if 'high' in files[i]:
            writer.writerow(row)
        if 'low' in files[i]:
            writer1.writerow(row)
        if 'severe' in files[i]:
            writer2.writerow(row)
        if 'normal' in files[i]:
            writer3.writerow(row)
        row[:] = []
        i = i + 1

    myFile.close()
    myFile1.close()
    myFile2.close()
    myFile3.close()

def lbp(path, lbp_sampling_points, lbp_sampling_radius, method):
    # CODIGO PARA LBP
    images = []
    files = glob.glob(path+'/*/*.png')
    for myFiles in files:
        #print(myFiles)
        img = cv2.imread(myFiles, cv2.IMREAD_GRAYSCALE)
        images.append(img)

    eps = 1e-7

    csv.register_dialect('dial', delimiter=';')
    myFile = open('CSVs\\LBP_High.csv', 'w', newline="")  # High file
    writer = csv.writer(myFile, dialect='dial')
    myFile1 = open('CSVs\\LBP_Low.csv', 'w', newline="")  # Low file
    writer1 = csv.writer(myFile1, dialect='dial')
    myFile2 = open('CSVs\\LBP_Severe.csv', 'w', newline="")  # Lesao Grave file
    writer2 = csv.writer(myFile2, dialect='dial')
    myFile3 = open('CSVs\\LBP_Normal.csv', 'w', newline="")  # Lesao Normal file
    writer3 = csv.writer(myFile3, dialect='dial')

    row = []
    i = 0
    for img in images:
        row.append(files[i].rsplit('\\', 1)[1])  # Adiciona o nome da imagem no arquivo
        lbp = feature.local_binary_pattern(img, lbp_sampling_points, lbp_sampling_radius, method=method)
        (hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, lbp_sampling_points + 3), range=(0, lbp_sampling_points + 2))
        hist = hist.astype("float")
        hist /= (hist.sum() + eps)
        row = list(hist)
        if 'high' in files[i]:
            writer.writerow(row)
        if 'low' in files[i]:
            writer1.writerow(row)
        if 'severe' in files[i]:
            writer2.writerow(row)
        if 'normal' in files[i]:
            writer3.writerow(row)
        row[:] = []
        i = i + 1

    myFile.close()
    myFile1.close()
    myFile2.close()
    myFile3.close()
