import uuid


# models içerisindeki Sale-transation_id kısmını otomatik 12 basamaklı büyük harf ve rakamdan oluşan işlem id si tanımlamak amacıyla bu fonksiyon oluşturuldu.
def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code
    