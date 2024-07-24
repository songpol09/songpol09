def cal_salary():
    
    n = str(input("ชื่อของพนักงาน : "))
    base_salary = float(input("เงินเดือนแบบปกติ (บาท/เดือน) : "))
    OT_h = int(input("จำนวนชั่วโมงที่เกินมา : "))
    
    H = 100
    Overtime_S = base_salary + (OT_h*H)
    
    if OT_h > 40:
        OVTP = (OT_h - 40) * H * 1.5
        Overtime_S += OVTP
        total_salary = Overtime_S + base_salary
        
    print(f"ชั่วโมงที่เกินมา : {OVTP:.2f} บาท")
    print(f"รวมทั้งสิ้น : {total_salary} บาท")
    
cal_salary()