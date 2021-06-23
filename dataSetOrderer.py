import csv
import shutil


def save_files(files, path):
    training_images_amount = int(round(len(files) * 0.8))
    count = 0

    for file_name in files:
        if count < training_images_amount:
            shutil.copy('Faces/img_align_celeba/img_align_celeba/' + file_name, 'Data/' + path + '/Training')
            count += 1
        else:
            shutil.copy('Faces/img_align_celeba/img_align_celeba/' + file_name, 'Data/' + path + '/Testing')
        print(count)


with open('list_attr_celeba.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    men = []
    women = []
    bold = []
    hairy = []
    people_with_head_wear = []
    people_without_head_wear = []

    for row in csv_reader:
        # Gender
        if (int(row[21]) == 1):
            men.append(row[0])
        else:
            women.append(row[0])
        # Bald
        if (int(row[5]) == 1):
            bold.append(row[0])
        else:
            hairy.append(row[0])
        # Hat
        if (int(row[36]) == 1):
            people_with_head_wear.append(row[0])
        else:
            people_without_head_wear.append(row[0])
#         files = ['file1.txt', 'file2.txt', 'file3.txt']
            # 0 image_id
            # 21 Male
            # 5 Bald
            # 36 hat
            # 32 smiling
            # line_count += 1
    # print(f'Processed {line_count} lines.')
    save_files(men, 'Male')
    save_files(women, 'Female')
    save_files(bold, 'Bald')
    save_files(hairy, 'WithHair')
    save_files(people_with_head_wear, 'WithHeadWear')
    save_files(people_without_head_wear, 'WithoutHeadWear')
