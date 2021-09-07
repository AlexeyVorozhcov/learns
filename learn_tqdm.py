from tqdm import tqdm
from time import sleep

print ("Идет загрузка")
for progress in tqdm(range(50), colour="green"):
    sleep(0.1)

print ("Загрузка завершена")    