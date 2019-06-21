import glob
import os

print('Начало выполнения программы\n\n')
for unit in glob.glob("/Users/yaroslav/**/*", recursive=True):
    if unit.startswith('КЛЮЧЕВАЯ ФРАЗА КОТОРУЮ НАДО УДАЛИТЬ '):
        print(unit)
    os.rename(unit, unit.replace('КЛЮЧЕВАЯ ФРАЗА КОТОРУЮ НАДО УДАЛИТЬ ', ''))
print('\n\nВыполнение переименования закончено. Программа завершена.')
