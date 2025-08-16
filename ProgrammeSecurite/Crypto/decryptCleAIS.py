from pyais import decode
#from pyais.stream import decode_msg
from datetime import datetime




# Trames AIS complètes
trames = [
    b"!AIVDO,3,1,0,A,>9NSa>i<u>2n05A@55DFj0EQ0hu<Ttr060848u8Br10u<U@Ttr0s;2sOS;;B,0*0D",
    b"!AIVDO,3,2,0,A,0GKRs;O;;Nr08E<tTr0BL5=<U=@4p<F0TllD@T5@Fr0EH4=D5@Ttr1E8LDq@,0*28",
    b"!AIVDO,3,3,0,A,F18E5DU<Fr1eA?c7O3??;;?W9l,2*0F"
]
decoded = decode(*trames)
print(decoded)




# Trames AIS complètes
#trames = [
#    "!AIVDO,3,1,0,A,>9NSa>i<u>2n05A@55DFj0EQ0hu<Ttr060848u8Br10u<U@Ttr0s;2sOS;;B,0*0D",
#    "!AIVDO,3,2,0,A,0GKRs;O;;Nr08E<tTr0BL5=<U=@4p<F0TllD@T5@Fr0EH4=D5@Ttr1E8LDq@,0*28",
#    "!AIVDO,3,3,0,A,F18E5DU<Fr1eA?c7O3??;;?W9l,2*0F"
#]

# # On les assemble façon stream, comme si on lisait un fichier ou réseau
# raw = "\r\n".join(trames).encode()
#
# # Décodage stream
# msgs = list(decode_msg(raw))
#
# # Extraction du flag
# for msg in msgs:
#     decoded = msg.decode()
#     if decoded.msg_type == 14:
#         mmsi = decoded.mmsi
#         message = decoded.text.strip()
#         timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
#         flag = f"{mmsi}_{timestamp}{{{message}}}"
#         print("FLAG :", flag)
