# import random
# import string
# from datetime import datetime, timedelta
import time


# # Генерация случайного хэша
# def generate_random_hash(length):
#     characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
#     return ''.join(random.choices(characters, k=length))
#
#
# # Генерация файла логов
# def generate_logs(file_path, num_logs, start_date, end_date):
#
#     delta = end_date - start_date
#     timedelta_step = delta / num_logs
#     date = start_date
#
#     with open(file_path, 'w') as f:
#         info = f'information {generate_random_hash(16)}'
#         f.write(f'[{start_date}] {info}\n')
#
#         for i in range(1, num_logs-1):
#             date = date + timedelta(seconds=random.uniform(0, timedelta_step.total_seconds()))
#             delta = end_date - date
#             timedelta_step = delta / (num_logs - i - 1)
#             info = f'information {generate_random_hash(16)}'
#             f.write(f'{date.strftime("[%Y-%m-%d %H:%M:%S]")} {info}\n')
#
#         info = f'information {generate_random_hash(16)}'
#         f.write(f'[{end_date}] {info}\n')


# Разбиение файла логов на несколько файлов по месяцам
def split_logs_by_month(log_file):
    files = {}
    with open(log_file, 'r') as f:
        for line in f:
            year = int(line[1:5])
            month = int(line[6:8])
            if (year, month) not in files:
                files[(year, month)] = open(f'logs_{year}_{month}.txt', 'a')
            files[(year, month)].write(line)
    for file in files.values():
        file.close()


def main():
    start = time.time()
    # start_date = datetime(2022, 1, 1, 10, 31, 53)
    # end_date = datetime(2022, 12, 31, 18, 45, 22)
    # generate_logs('logs.txt', 500000, start_date, end_date)
    split_logs_by_month('logs.txt')
    end = time.time()
    print("Execution time in seconds: ", (end - start))


if __name__ == '__main__':
    main()
