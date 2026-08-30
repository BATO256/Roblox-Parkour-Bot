import requests
import time
import random

ROBLOSECURITY = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_CAEQAhoEEAQYASIbCgRkdWlkEhM2Mzg0NDY0OTQ2NDIxODM3OTA1IhMKBXVuYW1lEgozem96a2lsbGVyIhEKA3VpZBIKNDM4OTY4NTExMigD.S0GRtFFICM_cR4qLo5mDwB-Wx4a0jVyRNBbMTDLey61lgLmYz7-oykEbyoX-OobO39NArwnzSM1juWOzKKpcS2iSVubhS0tzUmr7zr2TMOQ2S3mlEGCcmyuswIKh0fi-M7rmW67S6XRI8_be8jiXwz0nRpFwsRwHZifrXVgaR_r8MjoehD7bubMuyX8caM5WSyQW9T3e9Q6C6PbB2WFpBcj9ul7Yl67nmtWZc0aFbOxWRffTbwKYlBM-WtZS6dENkZ0Z5Qvn3LSbjw_KC9zGwxiUiYUwuGmnD05_yTU3fL88un2Bn5DxA-ni4H6zepAXt-ewCsF7y_vS7EqNgmfFz5yUGaPTgq2IxPUToXayJJvNbT__AWL2xLuBa8Ql6Hu-K-f5hqZZBCYS_mwLSwqWs07ra3I1KI1TXwL_uWY7N0FTT1COBKd7a_hxi_N8RxBK8Y7muByoSNUVYWnL8pBytfqKX7eMI5jnIxajHIF734SvSTx7-YUT2MVoI4X9uMZPCUEi4ail6uMNHNxxRfs3xAV7eWklOvSAInyrM9WMLgUa_51wWq-NzgAWYZTtu8Era3YmTCC92URr307svQvkjr6gkPlbCrCCSeKbUsNYeiMnoXif8Oynrkh8CsBKC6SN8WvI_XDvHQ2PYP8a4MyWvl_7zXBKDwyyGk8ryMHUKQqJEbARkDJaHcyq9BiAznxkIInHTt99-HYZbURiZs2zAEiEULWI-y5v4F9HvtstlTEkDhrmToHo_zbEQt-Gkg1WBEc05gvCJJyNP-jh6_rueibtMUWuTkvvaHufCfEcZYYQjnRmOkU1Qp4R1y-nP876wWYxofKVMZEVRu8dwRjYM3zEm6bU7x9fIZYC2cAyLqmHDrgKE2XitEbwwOQgaVHh6qp8mDNnhZaAojnBi5BzrV3ePh9pPd1GS4oYDXpNffo.XNm4dYPALU3Tpm4EJmPmUvpjEE0"

headers = {
    "Cookie": f".ROBLOSECURITY={ROBLOSECURITY}",
    "Content-Type": "application/json"
}

def create_obstacle(position, size, color):
    return {
        "position": position,
        "size": size,
        "color": color,
        "type": random.choice(["قفز", "توقيت", "فخ", "لغز", "وهم"])
    }

def generate_map():
    traps = []
    for i in range(1, 81):
        x = random.uniform(-200, 200)
        z = i * 15
        y = 5 + (i % 5) * 3
        traps.append(create_obstacle([x, y, z], [4, 2, 4], f"RGB({i*3%255}, {i*7%255}, {i*11%255})"))
    return traps

print("بدء إنشاء خريطة الـ 80 خدعة...")
map_data = generate_map()
print(f"تم إنشاء {len(map_data)} خدعة بنجاح.")
