import xlrd

from hashlib import md5

import pandas as pd

import json

import redis

import logging


redisClient = redis.StrictRedis(
    host="127.0.0.1", port=6379, db=2, charset="utf-8", decode_responses=True
)


def find(i):
    try:
        return redisClient.get(i)
    except Exception as e:
        logger.exception(e)


def encrypt(data):
    data = md5(data.encode()).hexdigest()
    return data


@api_view(["GET", "POST"])
def manage_items(request, *args, **kwargs):

    if request.method == "GET":

        loc = "records.xlsx"
        payername = ""
        # Reading an excel file using Python
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)

        payer_id_ls = sheet.col_values(4, 1)
        payer_nm_ls = sheet.col_values(5, 1)
        concat_id_nm = []
        crypted = []
        decrypted = []

        for i in range(len(payer_id_ls)):
            payername = "HEALTHY TEXAS"
            if isinstance(payer_id_ls[i], float):
                tmp = int(payer_id_ls[i])
                concat_id_nm.append(str(tmp) + "+" + str(payer_nm_ls[i]))
            else:
                concat_id_nm.append(str(payer_id_ls[i]) + "+" + str(payer_nm_ls[i]))

        for i in concat_id_nm:
            crypted.append(encrypt(i))

        for i in concat_id_nm:
            redisClient.set(i, encrypt(i))

        resmd5 = []

        for i in concat_id_nm:
            resmd5.append(find(i))
            keys = redisClient.keys()
            vals = redisClient.mget(keys)
            kv = zip(keys, vals)
            for i, j in kv:
                if payername in i:
                    tmp = i.split("+")[0]
                    logger.exception(f"payer ID for {j} is {tmp}")

        result = [crypt == md5 for md5 in resmd5 for crypt in crypted if md5 == crypt]

        return Response(result, status=200)