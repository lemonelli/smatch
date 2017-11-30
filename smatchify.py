import sys,io


#initialize files
linear_amr = io.open('%s' % sys.argv[1], mode="w", encoding="utf-8")
amr_data = io.open('%s.smatched' % sys.argv[1], mode='r', encoding="utf-8")


while True:
    next = amr_data.read(1)
    if next == ')':
        next = amr_data.read(1)
    elif next == '':
        break
    else:
        continue

linear_amr.close()
amr_data.close()
