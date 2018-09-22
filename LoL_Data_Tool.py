from typing import List


# caution, ugly code    |
#                       V

def read_store_transactions() -> List[List[str]]:
    fp = file_check("storeTransactions.json")
    lines = fp.readlines()
    amnt = int((len(lines) - 1) / 12)
    batches = [list(lines[i * 12 + 1:i * 12 + 13]) for i in range(amnt)]
    fp.close()
    return batches


def check_rp_spent():
    sum_spent = 0
    sum_bought = 0
    for i in range(len(batches_global)):
        txt = batches_global[i][5]
        val = int(txt[9:len(txt) - 2])
        if val < 0:
            sum_spent -= val
        if val > 0:
            sum_bought += val
    print("RP Bought: {:d}".format(sum_bought))
    print("RP Spent: {:d}\n".format(sum_spent))


def check_ip_spent():
    sum_ip = 0
    for i in range(len(batches_global)):
        txt = batches_global[i][4]
        val = int(txt[9:len(txt) - 2])
        sum_ip -= val
    print("IP Spent: {:d}\n".format(sum_ip))


def check_money_spent():
    sum_money = 0
    fp = file_check("rpPurchases.json")
    lines = fp.readlines()
    amnt = int((len(lines) - 1) / 12)
    batches = [list(lines[i * 12 + 1:i * 12 + 13]) for i in range(amnt)]
    fp.close()
    for i in range(len(batches)):
        txt = batches[i][8]
        sum_money += float(txt[13:len(txt) - 2])
    print("Money Spent: {:.0f} (of your currency)\n".format(sum_money))


def file_check(name: str):
    try:
        fn = open(name)
    except IOError:
        print(
            "Error: '{:s}' does not exist in the current directory.\n\nMove the executable/script into your Data Folder.\n".format(name))
        input("PRESS ENTER TO CONTINUE")
        raise SystemExit
    return fn


batches_global = read_store_transactions()
check_rp_spent()
check_ip_spent()
check_money_spent()
input("PRESS ENTER TO CONTINUE.")
