#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apk_parse3.apk import APK
from gpapi.googleplay import GooglePlayAPI
from variable_app.var_app import gsfId, authSubToken, cloud_app, local_app


def GET_APP(gsfId, authSubToken, package):
    server = GooglePlayAPI("it_IT", "Europe/Rome")

    # LOGIN
    print("\nLogin with ac2dm token and gsfId saved\n")
    server.login(None, None, gsfId, authSubToken)

    # DOWNLOAD
    docid = package
    print("\nAttempting to download {}\n".format(docid))
    fl = server.download(docid)
    with open(docid + ".apk", "wb") as apk_file:
        for chunk in fl.get("file").get("data"):
            apk_file.write(chunk)
        print("\nDownload successful\n")

def DATA_APP(package):
    path = package + ".apk"
    apkf = APK(path)
    data_app = []
    data_app.append(apkf.file_size)
    data_app.append(apkf.file_md5)
    data_app.append(apkf.get_androidversion_name())
    return data_app

def CHECK_APP():
    data_android_cloud = DATA_APP(cloud_app)
    data_android_local = DATA_APP(local_app)
    count = len(data_android_local)
    check_data = []
    size_check = 0
    hash_check = 0
    version_check = 0
    for i in range(count):
        if i == 0:
            if data_android_cloud[i] == data_android_local[i]:
                size_check += 1
                check_data.append(size_check)
            else:
                check_data.append(size_check)
        elif i == 1:
            if data_android_cloud[i] == data_android_local[i]:
                hash_check += 1
                check_data.append(hash_check)
            else:
                check_data.append(hash_check)
        else:
            if data_android_cloud[i] == data_android_local[i]:
                version_check +=1
                check_data.append(version_check)
            else:
                check_data.append(version_check)
    return check_data

def REPORT_APP():
    report = CHECK_APP()
    count = len(report)
    for i in range(count):
        if i == 0:
            if report[i] == 0:
                print("\nРазмер файла из Google Play не совпадает с локальным файлом.\n")
            else:
                print("\nРазмер файла из Google Play совпадает с локальным файлом.\n")
        elif i == 1:
            if report[i] == 0:
                print("\nХэш-сумма файла из Google Play не совпадает с локальным файлом.\n")
            else:
                print("\nХэш-сумма файла из Google Play совпадает с локальным файлом.\n")
        else:
            if report[i] == 0:
                print("\nВерсия файла из Google Play не совпадает с локальным файлом.\n")
            else:
                print("\nВерсия файла из Google Play совпадает с локальным файлом.\n")



if __name__ == "__main__":
    GET_APP(gsfId, authSubToken, cloud_app)
    REPORT_APP()
