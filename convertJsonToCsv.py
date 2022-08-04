import json
import csv
import os


def refactor_json_file(file_json):
    for item in file_json:
        file_json[file_json.index(item)] = item[:-2]
    return file_json


def correct_json_file(file_json):
    split_file_json = []
    correct_file_json = []
    for item in file_json:
        split_file_json = item.split(',')
        split_file_json[8] = split_file_json[8] + '"'
        split_file_json[16] = split_file_json[16] + '"'
        join_items = ','.join(split_file_json)
        correct_file_json.append(join_items)
    return correct_file_json


def output_json_file(correct_file_json):
    output_file_json = []
    for item in correct_file_json:
        json_load = json.loads(item)
        output_file_json.append(
            [json_load.get('uuid'), json_load.get('start_stamp'), json_load.get('end_stamp'),
             json_load.get('start_epoch'),
             json_load.get('hangup_cause'), json_load.get('duration'), json_load.get('xml_cdr_uuid'),
             json_load.get('bridge_uuid'), json_load.get('caller_id_name'),
             json_load.get('caller_id_number'), json_load.get('destination_number'),
             json_load.get('rtp_audio_in_mos'), json_load.get('billmsec'), json_load.get('leg'),
             json_load.get('answer_stamp'), json_load.get('record_sequence_number'),
             json_load.get('ott_id'), json_load.get('booking_id'),
             json_load.get('A_B_unique_tracker')])

    return output_file_json


if __name__ == '__main__':
    all_json_files = []
    write_json_files = []
    readFiles = []

    f = open(f'/etlstar/users/etladminuser/star_etl/axb/READ-LOG-FILES.csv', 'r')
    with f:
        reader = csv.reader(f)
        for row in reader:
            readFiles.append(row[0])

    for file in os.listdir("/etlstar/users/etlaxb"):
        if file.endswith(".json"):
            if file not in readFiles:
                all_json_files.append(file)
                write_json_files.append([file])

    for all_json_file in all_json_files:
        read_file = open(f'/etlstar/users/etlaxb/{all_json_file}', "r")
        file_json = read_file.readlines()

        file_json = refactor_json_file(file_json)

        correct_file_json = correct_json_file(file_json)

        outputFileJson = output_json_file(correct_file_json)

        file_name = all_json_file.split('.json')[0] + '.csv'
        f = open(f'/etlstar/users/etlaxb/axb/{file_name}', 'w')
        with f:
            writer = csv.writer(f)
            for row in outputFileJson:
                writer.writerow(row)

    d = open(f'/etlstar/users/etladminuser/star_etl/axb/READ-LOG-FILES.csv', 'a')
    with d:
        writer = csv.writer(d)
        for row in write_json_files:
            writer.writerow(row)
